#!/usr/bin/env python3
"""Sync bundled designs from an explicit published catalog and canonical bundles.
Requires Python 3 and PyYAML. Validates every source before writing files.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, required=True)
    parser.add_argument('--bundles', type=Path, required=True)
    parser.add_argument('--date', required=True, help='Catalog verification date (YYYY-MM-DD)')
    parser.add_argument('--source-revision', required=True)
    args = parser.parse_args()
    catalog = json.loads(args.catalog.read_text())
    assert isinstance(catalog, list) and catalog, 'Expected nonempty catalog list'
    ids = [theme['id'] for theme in catalog]
    assert len(ids) == len(set(ids)), 'Duplicate catalog IDs'
    free = sorted((t for t in catalog if t.get('tier') == 'free'), key=lambda t: t['id'])
    assert free, 'No free themes in catalog'
    root = Path(__file__).resolve().parents[1]
    prepared = []
    for theme in free:
        slug = theme['id']
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug), slug
        source = (args.bundles / slug / 'DESIGN.md').read_text()
        parts = source.split('---', 2)
        assert len(parts) == 3 and not parts[0].strip(), f'{slug}: missing frontmatter'
        meta = yaml.safe_load(parts[1])
        assert meta['meta']['id'] == slug, f'{slug}: wrong ID'
        for field in ('colors', 'typography', 'spacing', 'components'):
            assert meta.get(field), f'{slug}: missing {field}'
        assert '## ' in parts[2], f'{slug}: missing design guidance'
        # The published catalog determines current access; older source metadata
        # may predate a theme becoming free. Change only its tier field.
        front, count = re.subn(r'(?m)^  tier:.*$', '  tier: free', parts[1])
        assert count == 1, f'{slug}: ambiguous tier field'
        output = '---' + front + '---' + parts[2]
        prepared.append((theme, meta, source, output))
    expected = {t['id'] for t in free}
    existing = {p.stem for p in (root / 'designs').glob('*.md') if p.stem != 'INDEX'}
    assert not existing - expected, 'Previously bundled themes are no longer free; review before removing: ' + str(sorted(existing - expected))
    def cell(value):
        return ' '.join(str(value).split()).replace('|', r'\|')
    lines = ['# Designs Index', '', f'This skill bundles **{len(free)} free design systems** from the **{len(catalog):,}** themes in the published Curio catalog, verified {args.date}.', '',
             'Read the full linked design file, then apply `SKILL.md`. Examples are optional structural references.', '',
             '| ID | Name | Origin | Mood | Mode |', '|---|---|---|---|---|']
    manifest = {'verifiedAt': args.date, 'catalogUrl': 'https://designbycurio.com/index.json',
                'catalogSha256': hashlib.sha256(args.catalog.read_bytes()).hexdigest(),
                'sourceRevision': args.source_revision, 'totalThemes': len(catalog),
                'freeThemes': len(free), 'designs': []}
    for theme, meta, source, output in prepared:
        slug = theme['id']
        (root / 'designs' / f'{slug}.md').write_text(output)
        origin = meta.get('origin', {})
        lines.append('| ' + ' | '.join([f'[`{slug}`]({slug}.md)', cell(theme['name']),
            cell(str(origin.get('region', '')) + '; ' + str(origin.get('era', ''))),
            cell(theme.get('blurbShort') or meta['meta'].get('description', '')),
            'dark' if meta['meta'].get('isDark') else 'light']) + ' |')
        manifest['designs'].append({'id': slug, 'sourceSha256': hashlib.sha256(source.encode()).hexdigest(),
            'bundledSha256': hashlib.sha256(output.encode()).hexdigest(), 'sourceTier': meta['meta'].get('tier')})
    lines += ['', '## More designs', '',
        'Browse https://designbycurio.com for the current library. Check this index before sending the user to the website: the designs listed here are bundled free.', '',
        'For a design outside this bundle, use a user-provided Curio share link or the configured Curio MCP. Verify names and availability before recommending specific themes.', '']
    (root / 'designs' / 'INDEX.md').write_text('\n'.join(lines))
    (root / 'designs' / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(f'Synced {len(free)} free designs from {len(catalog)} published themes.')


if __name__ == '__main__':
    main()
