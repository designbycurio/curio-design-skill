# Maintaining the bundled designs

The 105 styles in `designs/` are copied from Curio's canonical content bundles and
checked against the public catalog. `designs/manifest.json` records the source
revision and a hash for every file.

## Refresh the bundle

Use a freshly downloaded public catalog and the canonical Curio content
`bundles/` directory. Requires Python 3 and PyYAML.

```bash
curl -fsSL https://designbycurio.com/index.json -o /tmp/curio-catalog.json
python3 scripts/sync-designs.py --catalog /tmp/curio-catalog.json \
  --bundles /path/to/curio-content/bundles \
  --date YYYY-MM-DD --source-revision CONTENT_COMMIT_SHA
```

The script selects published `tier: free` entries, validates every source before
writing, and regenerates `designs/INDEX.md` and the checksum manifest. Source tier
metadata is normalized to the published catalog; design tokens and guidance are
preserved. If a bundled theme is no longer free, the script stops for review.

Since Curio 2.0 (October 2026) the website sells every style for one credit and
`tier` in the catalog is a legacy field, so a fresh sync can select more styles than
the 105 bundled here. Check with the maintainers before changing the set.

After a sync, update the counts in both READMEs, the README gallery and `SKILL.md`.
