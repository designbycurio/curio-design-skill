---
version: 1

meta:
  id: islamic-girih-tile-geometry
  name: Islamic Girih Tiles
  description: Lustrous cobalt-and-turquoise glazed tilework laced with gold strapwork, a mathematized sacred geometry of endless star-and-polygon repeats.
  isDark: true
  tags: [historical, decorative, geometric, luxurious, ornate]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Medieval Islamic world; Persian Timurid (1370–1507) and Safavid Isfahan (1501–1736)"
  region: "Persia / Iran and the broader Islamic world"
  regionZh: "波斯 / 伊朗及更广阔的伊斯兰世界"
  keyFigures: [Master craftsmen and geometers of Islamic architectural ornament, Banna'i tilework artisans of Isfahan]
  movements: [Islamic geometric pattern, Girih-tile design, Persian tilework (kashi)]

introduction: |
  Girih are the interlaced geometric strapwork patterns of Islamic architectural
  decoration — star-and-polygon tessellations built from a small set of tiles
  that repeat without end. On a Persian mosque wall they read as lustrous
  cobalt-and-turquoise glazed ceramic, the interlacing drawn in gold over a
  white-line ground.

  This is mathematized sacred ornament: lapis-lazuli ultramarine and pyrite gold,
  exact and seamless. The tradition is aniconic — no figures, only the infinite
  repeat of decagons, pentagons and radiating stars, locked together with the
  precision of a geometer's compass.

introductionZh: |
  吉里赫（Girih）是伊斯兰建筑装饰中那种环环相扣的几何编带纹样——由极少数几种
  瓷砖拼出的星形与多边形镶嵌，可以无穷无尽地重复下去。在波斯伊斯法罕的清真寺
  墙面上，它呈现为光泽莹润的钴蓝与绿松石釉面陶瓷，金线在白底之上勾出交织的编带。

  这是一种被数学化的圣性装饰：取色于天青石的群青与黄铁矿的金黄，精确而无缝。
  这门传统是禁绝偶像的——没有人物形象，只有十边形、五边形与放射状星节点
  以圆规般的精度彼此咬合、永恒重复。

colors:
  primary:    {"50": "#E6EFF6", "100": "#C4DAEA", "200": "#9CC0D9", "300": "#6FA3C7", "400": "#4587B7", "500": "#1B6CA8", "600": "#175C90", "700": "#134B76", "800": "#0F3A5B", "900": "#0A2540", "950": "#06182B"}
  secondary:  {"50": "#E4F7F5", "100": "#BCEDE9", "200": "#8FE1DA", "300": "#5DD2C9", "400": "#3FC6BC", "500": "#2BB7B0", "600": "#239B95", "700": "#1B7C77", "800": "#145E5A", "900": "#0D403D", "950": "#072523"}
  accent:     {"50": "#FBF6E6", "100": "#F4E9C2", "200": "#EBD896", "300": "#E0C566", "400": "#D5B544", "500": "#C9A227", "600": "#AC8920", "700": "#8A6E1A", "800": "#675213", "900": "#45370D", "950": "#241D06"}
  neutral:    {"50": "#F2EFE6", "100": "#DDE5EC", "200": "#B9C8D6", "300": "#8FA6BB", "400": "#65809B", "500": "#46627E", "600": "#374E66", "700": "#2A3D52", "800": "#1B2C40", "900": "#0E3A5C", "950": "#0A2540"}
  semantic:
    success: { bg: "#0D403D", text: "#5DD2C9", light: "#145E5A", border: "#239B95" }
    warning: { bg: "#45370D", text: "#E0C566", light: "#675213", border: "#AC8920" }
    error:   { bg: "#4A1620", text: "#E58BA0", light: "#6B2230", border: "#A83B52" }
    info:    { bg: "#0F3A5B", text: "#6FA3C7", light: "#134B76", border: "#4587B7" }
  background:
    page:    "#0E3A5C"
    surface: "#103F63"
    subtle:  "#0A2540"
  text:
    primary:   "#F2EFE6"
    secondary: "#9CC0D9"
    muted:     "#65809B"
    inverse:   "#0A2540"

typography:
  families:
    heading: "'Reem Kufi', 'Noto Naskh Arabic', serif"
    body:    "'Noto Naskh Arabic', 'Amiri', serif"
    mono:    "'IBM Plex Mono', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Noto+Naskh+Arabic:wght@400;500;600;700&family=Reem+Kufi:wght@400;500;600;700&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "2px", md: "4px", lg: "8px", xl: "16px", full: "9999px"}
  color:  {default: "#C9A227", subtle: "#175C90", strong: "#E0C566", focus: "#2BB7B0"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(6,24,43,0.4)"
  sm: "0 1px 3px rgba(6,24,43,0.5), 0 1px 2px rgba(6,24,43,0.4)"
  md: "0 4px 8px rgba(6,24,43,0.5), 0 0 0 1px rgba(201,162,39,0.15)"
  lg: "0 10px 24px rgba(6,24,43,0.6), 0 0 0 1px rgba(201,162,39,0.2)"
  xl: "0 20px 48px rgba(6,24,43,0.65), 0 0 0 1px rgba(201,162,39,0.25)"
  "2xl": "0 32px 72px rgba(6,24,43,0.7), 0 0 0 1px rgba(201,162,39,0.3)"
  inner: "inset 0 1px 2px rgba(6,24,43,0.5)"
  focus: "0 0 0 3px rgba(43,183,176,0.45)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [glow, tint, stroke]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        "8px"

surfaceStyle: layered
blur:         none

iconography:
  treatment: linear
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#C9A227", color: "#0A2540", border: "1px solid #E0C566", shadow: "0 4px 8px rgba(6,24,43,0.5)", hoverBackground: "#D5B544", hoverShadow: "0 0 0 3px rgba(201,162,39,0.3)", hoverColor: "#06182B"}
    secondary: {background: "#1B6CA8", color: "#F2EFE6", border: "1px solid #2BB7B0", shadow: "0 2px 6px rgba(6,24,43,0.5)", hoverBackground: "#175C90", hoverShadow: "0 0 0 3px rgba(43,183,176,0.35)", hoverColor: "#F2EFE6"}
    ghost:     {background: "transparent", color: "#9CC0D9", border: "1px solid #175C90", shadow: "none", hoverBackground: "rgba(27,108,168,0.18)", hoverShadow: "none", hoverColor: "#F2EFE6"}
    danger:    {background: "#A83B52", color: "#F2EFE6", border: "1px solid #E58BA0", shadow: "0 2px 6px rgba(6,24,43,0.5)", hoverBackground: "#8A2E42", hoverShadow: "0 0 0 3px rgba(168,59,82,0.35)", hoverColor: "#F2EFE6"}
    sizes:     {sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "4px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#0A2540"
    color: "#F2EFE6"
    border: "1px solid #175C90"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "1px solid #2BB7B0"
    placeholderColor: "#65809B"
  card:
    base:  {background: "#103F63", border: "1px solid rgba(201,162,39,0.25)", borderRadius: "8px", padding: "24px", shadow: "0 10px 24px rgba(6,24,43,0.6)"}
    hover: {shadow: "0 20px 48px rgba(6,24,43,0.65), 0 0 0 1px rgba(201,162,39,0.4)", transform: "translateY(-2px)"}
---

# Islamic Girih Tiles

> Lapis ultramarine and pyrite gold, laced into an endless geometry of stars.

## Origin
Girih — Persian for "knot" — names the interlaced strapwork that covers the great
monuments of the medieval Islamic world. By the Timurid era (1370–1507), craftsmen
in Samarkand and Herat had reduced the bewildering complexity of these patterns to
a small kit of five tiles, each decorated with two lines, that could tile a wall
without seam or end. The Safavid capital of Isfahan (1501–1736) raised the craft to
its peak in the glazed faience of the Shah Mosque and Sheikh Lotfollah Mosque.

The palette came from the earth: ultramarine ground from Afghan lapis lazuli, gold
from pyrite, turquoise from copper glazes. There were no signed authors — the work
belonged to anonymous master geometers and *banna'i* tile-cutters whose names rarely
survive. What survives is the system itself: an aniconic, mathematically exact
ornament that, centuries later, was found to encode quasicrystalline symmetries
European mathematics did not describe until the 1970s.

## Overview
Composition cues:
- **Layout**: Strict symmetric grid; everything aligns to a radiating polygonal lattice.
- **Content width**: Container-bound, centered, never full-bleed chaos.
- **Framing**: Bordered surfaces with thin gold strapwork outlines.
- **Grid intensity**: Strong — the geometric scaffolding is visible and celebrated.

## Colors
The palette is mineral and luminous: a deep glazed-tile blue field over which gold
interlacing and turquoise stars read as light against dark. Cobalt/lapis carries the
structure, Persian turquoise animates the highlights, gold draws every contour, and a
warm white-line ground (`#F2EFE6`) provides the strapwork's bright edges. Nothing is
pale or washed out — every hue is saturated as fired glaze.

**Role usage**:
- Page background → `colors.background.page` (#0E3A5C deep glazed-tile blue)
- Primary actions / structural fills → `colors.primary.500` (#1B6CA8 cobalt/lapis)
- Highlights, stars, focus → `colors.secondary.500` (#2BB7B0 Persian turquoise)
- Strapwork outlines, borders, key accents → `colors.accent.500` (#C9A227 gold)
- Primary text / bright line ground → `colors.text.primary` (#F2EFE6)
- Deepest panels and recesses → `colors.background.subtle` (#0A2540)

## Typography
The voice is calligraphic, drawn from the Arabic faces that share the patterns' walls.
Reem Kufi gives headings an angular, monumental Kufic presence; Noto Naskh Arabic and
Amiri carry body text with the fluid grace of Naskh script. Type is set generously,
with open line-heights befitting sacred inscription, and never substituted with a
Latin serif or sans for display.

**Text styles**:
- `display-xl` — Reem Kufi, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Reem Kufi, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Reem Kufi, 36px, weight 600, line-height 1.2, letter-spacing 0
- `body-lg` — Noto Naskh Arabic, 18px, weight 400, line-height 1.8, letter-spacing 0
- `body-md` — Noto Naskh Arabic, 16px, weight 400, line-height 1.625, letter-spacing 0
- `caption` — Amiri, 12px, weight 400, line-height 1.5, letter-spacing 0.05em
- `mono-md` — IBM Plex Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px, rhythm anchored to an 8px lattice.
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container max-width: 1280px (xl), content centered.
- Section padding: 64px (md) to 128px (xl), generous to let patterns breathe.

## Elevation & Depth
Surfaces are layered glazed panels — solid tile-blue planes stacked with thin gold
hairline borders rather than soft diffusion. There is no blur; depth comes from
darkening recesses toward `#0A2540` and crowning raised surfaces with a faint gold
outline, like glaze catching light.

- Surface style: layered solid panels, no glass, no blur.
- Blur: none.
- Shadow ladder: tight blue-black drops (`rgba(6,24,43,…)`) paired with gold hairline rings, escalating from xs to 2xl.

## Shapes
- Corners: small and crisp — none/2px/4px/8px/16px; full (9999px) reserved for star-node dots and pills.
- Default radius for cards 8px, buttons/inputs 4px, echoing cut-tile edges.

## Motion
Motion is restrained and exact — patterns reveal rather than bounce. Hovers add a
soft turquoise or gold glow and tint; transitions are short and clean. The aesthetic
is precision, not exuberance, so nothing overshoots except the occasional gentle spring
on interactive nodes.

- Level: restrained.
- Durations: 120ms fast / 250ms normal / 400ms slow.
- Easings: standard ease-in-out default, spring reserved for node interactions.
- Hover patterns: glow, tint, stroke.

## Techniques
Brand-specific CSS recipes that carry the girih character.

### Gold strapwork border
A double-line interlacing frame: gold outer rule with an inset white-line ground, mimicking the strapwork outline.
```css
.girih-frame {
  border: 2px solid #C9A227;
  box-shadow:
    inset 0 0 0 1px #0E3A5C,
    inset 0 0 0 3px rgba(242,239,230,0.6),
    inset 0 0 0 4px #C9A227;
  background: #103F63;
}
```

### Tessellated star background
A seamless conic-and-radial decagon tile that repeats infinitely behind hero sections.
```css
.girih-tessellation {
  background-color: #0A2540;
  background-image:
    repeating-conic-gradient(from 18deg at 50% 50%,
      transparent 0deg 30deg,
      rgba(201,162,39,0.18) 30deg 31deg,
      transparent 31deg 36deg),
    radial-gradient(circle at 50% 50%, rgba(43,183,176,0.22) 0 6%, transparent 7%);
  background-size: 96px 96px, 96px 96px;
}
```

### Glazed-tile sheen
A fired-ceramic highlight applied to surfaces, suggesting wet glaze under raking light.
```css
.glazed {
  background:
    linear-gradient(135deg, rgba(242,239,230,0.10) 0%, transparent 35%),
    linear-gradient(180deg, #1B6CA8 0%, #0F3A5B 100%);
  border: 1px solid rgba(201,162,39,0.3);
}
```

## Iconography
Icons are thin linear glyphs that echo compass-and-straightedge construction, kept
geometric and outline-only. Use Phosphor (or a custom girih-derived set) at a 1.5px
stroke so they sit beside the gold strapwork without competing. Favor star, polygon,
and knot motifs over literal pictograms.

- Treatment: linear / outline.
- Set: phosphor.
- Stroke: 1.5px.

## Do's & Don'ts
### ✓ Do
- Use the deep glazed-tile blue `#0E3A5C` as the page field so gold and turquoise read luminous.
- Draw every contour and divider in gold `#C9A227` strapwork.
- Pair cobalt/lapis with Persian turquoise and gold as a three-color chord.
- Keep layouts exact, symmetric, and built on a radiating polygonal lattice.
- Set headings in Reem Kufi or Noto Naskh Arabic, never a Latin substitute.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds.
- Do not flatten to a single pale cyan; keep the cobalt–turquoise–gold trio.
- No figurative imagery — the tradition is aniconic, purely geometric.
- Avoid broken or asymmetric layouts; girih is exact, seamless, infinitely repeating.
- Do not substitute Latin serif/sans for headings; use Arabic Naskh/Kufi faces.

## Applications
Best suited to luxury, cultural, and heritage contexts: museum and exhibition sites,
premium product pages, conference identities, and editorial features on art, mathematics,
or architecture. The exact, ornamental geometry rewards generous, contemplative layouts
over dense dashboards.
