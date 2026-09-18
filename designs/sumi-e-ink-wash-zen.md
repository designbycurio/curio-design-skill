---
version: 1

meta:
  id: sumi-e-ink-wash-zen
  name: Sumi-e Ink Wash
  description: Graded black sumi ink on weathered mulberry washi, breathing negative space, one vermilion seal.
  isDark: false
  tags: [minimal, historical, organic, handmade, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "pre-1900 (classical East Asian ink-wash tradition; Muromachi-period suiboku-ga onward)"
  region: "Japan (with Chinese ink-painting lineage)"
  regionZh: "日本（承中国水墨画脉络）"
  keyFigures: [Sesshū Tōyū, Hasegawa Tōhaku, Liang Kai, Mu Qi]
  movements: [Sumi-e suiboku-ga, Zen minimalism, brush calligraphy]

introduction: |
  Sumi-e is the Japanese art of ink-wash painting: graded black sumi diluted into
  tonal grays (notan), dry-brush strokes that leave "flying white" (kasure), and
  the vast emptiness of unpainted paper (ma). Nothing is added that the brush did
  not need. The ground is aged mulberry washi — a toned, weathered oatmeal — and
  the single point of color is the red of a carved seal pressed in cinnabar paste.
  This is a system built on restraint: most of the surface stays empty, and one
  small vermilion mark carries the whole composition.

introductionZh: |
  水墨画（墨絵）以一色之墨写万物。浓淡相破谓之「浓淡」（notan），干笔擦出
  飞白曰「枯れ」（kasure），而满幅最要紧处往往是那片不着一笔的留白——「间」（ma）。
  纸是经年泛黄的桑皮和纸，底色是被岁月染旧的燕麦灰，绝非雪白宣纸。通篇唯一的颜色，
  是钤在画角那一方朱砂印——印泥的赤红，是这套语言里唯一被允许的喧哗。一切删繁就简，
  以空养实，以墨见心。

colors:
  primary:    {"50": "#EDEBE7", "100": "#D7D3CC", "200": "#AEA89C", "300": "#857E70", "400": "#5C564A", "500": "#16130F", "600": "#13100C", "700": "#0F0D0A", "800": "#0B0907", "900": "#070605", "950": "#040303"}
  secondary:  {"50": "#ECEAE6", "100": "#D4D0C8", "200": "#A9A294", "300": "#7E7666", "400": "#564E40", "500": "#3A352D", "600": "#2F2B24", "700": "#23201B", "800": "#181512", "900": "#0D0B09", "950": "#070605"}
  accent:     {"50": "#FBE9E5", "100": "#F7CCC4", "200": "#F0A096", "300": "#EA7567", "400": "#E55A4A", "500": "#E2462F", "600": "#C23721", "700": "#962A19", "800": "#6B1E12", "900": "#40120A", "950": "#260A05"}
  neutral:    {"50": "#F2EEE6", "100": "#E5DFD2", "200": "#D8CFBE", "300": "#C2B8A4", "400": "#A39C8C", "500": "#857D6E", "600": "#6E675B", "700": "#524D44", "800": "#37332D", "900": "#1D1A16", "950": "#0F0D0B"}
  semantic:
    success: { bg: "#E5DFD2", text: "#3A4A2E", light: "#EDECDF", border: "#7C8A5E" }
    warning: { bg: "#F4E4C4", text: "#6B4A12", light: "#F8EED6", border: "#C39A45" }
    error:   { bg: "#FBE9E5", text: "#962A19", light: "#F7CCC4", border: "#E2462F" }
    info:    { bg: "#E2E0DC", text: "#3A352D", light: "#ECEAE6", border: "#6E675B" }
  background:
    page:    "#D8CFBE"
    surface: "#E0D8C9"
    subtle:  "#CEC4B1"
  text:
    primary:   "#16130F"
    secondary: "#3A352D"
    muted:     "#6E675B"
    inverse:   "#E5DFD2"

typography:
  families:
    heading: "'Zen Old Mincho', 'Shippori Mincho', 'Noto Serif JP', serif"
    body:    "'Shippori Mincho', 'Noto Serif JP', serif"
    mono:    "'Noto Serif JP', 'Shippori Mincho', serif"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600;700;800&family=Noto+Serif+JP:wght@300;400;500;600;700&family=Zen+Old+Mincho:wght@400;500;600;700;900&display=swap"
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
  radius: {none: "0", sm: "1px", md: "2px", lg: "3px", xl: "4px", full: "9999px"}
  color:  {default: "#A39C8C", subtle: "#C2B8A4", strong: "#3A352D", focus: "#E2462F"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(22,19,15,0.05)"
  sm: "0 1px 3px rgba(22,19,15,0.07)"
  md: "0 4px 12px rgba(22,19,15,0.08)"
  lg: "0 10px 28px rgba(22,19,15,0.10)"
  xl: "0 20px 48px rgba(22,19,15,0.12)"
  "2xl": "0 32px 72px rgba(22,19,15,0.14)"
  inner: "inset 0 1px 2px rgba(22,19,15,0.06)"
  focus: "0 0 0 3px rgba(226,70,47,0.28)"

motion:
  level: minimal
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.2, 0.64, 1)"
  hoverPatterns: [opacity, tint, underline]
  reducedMotion: true

composition:
  layout:        stack
  contentWidth:  narrow
  framing:       minimal
  gridIntensity: none
  rhythm:        8px

surfaceStyle: flat
blur:         none

iconography:
  treatment: linear
  set:       lucide
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#16130F", color: "#E5DFD2", border: "1px solid #16130F", shadow: "none", hoverBackground: "#3A352D", hoverShadow: "none", hoverColor: "#F2EEE6"}
    secondary: {background: "transparent", color: "#16130F", border: "1px solid #6E675B", shadow: "none", hoverBackground: "rgba(22,19,15,0.06)", hoverShadow: "none", hoverColor: "#16130F"}
    ghost:     {background: "transparent", color: "#3A352D", border: "1px solid transparent", shadow: "none", hoverBackground: "rgba(22,19,15,0.04)", hoverShadow: "none", hoverColor: "#16130F"}
    danger:    {background: "#E2462F", color: "#FBE9E5", border: "1px solid #E2462F", shadow: "none", hoverBackground: "#C23721", hoverShadow: "none", hoverColor: "#FBE9E5"}
    sizes:     {sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "2px"
    fontWeight: 500
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#E0D8C9"
    color: "#16130F"
    border: "1px solid #A39C8C"
    borderRadius: "2px"
    padding: "10px 14px"
    focusBorder: "1px solid #16130F"
    placeholderColor: "#857D6E"
  card:
    base:  {background: "#E0D8C9", border: "1px solid #C2B8A4", borderRadius: "2px", padding: "32px", shadow: "0 1px 3px rgba(22,19,15,0.07)"}
    hover: {shadow: "0 4px 12px rgba(22,19,15,0.08)", transform: "none"}
---

# Sumi-e Ink Wash

> Graded black ink on weathered washi, vast breathing emptiness, and a single vermilion seal.

## Origin
Sumi-e (墨絵, also suiboku-ga) is ink-wash painting carried from Song-dynasty China into Japan by Zen monks from the 14th century onward. Working in nothing but black sumi ink ground on an inkstone, masters such as Sesshū Tōyū and Hasegawa Tōhaku built entire landscapes from dilution alone — the gradient from saturated black to the palest gray standing in for distance, mist, and depth. The discipline is inseparable from Zen practice: the brush moves once, decisively, and cannot be corrected.

What defines the tradition is as much what is left out as what is put down. Vast areas of paper stay untouched (ma), a few dry strokes fracture into "flying white" (kasure) where the brush runs out of ink, and tonal massing (notan) organizes light and dark. The ground itself is handmade mulberry washi that has yellowed and grayed with age. A single carved seal, pressed in vermilion cinnabar paste (shuniku), signs and anchors the work — the lone note of color in an otherwise monochrome world.

## Overview
Composition cues:
- **Layout**: Single vertical column, asymmetric placement, content pushed off-center to leave generous void.
- **Content width**: Narrow measure; text and figures float in surrounding emptiness rather than filling the frame.
- **Framing**: Minimal — no boxes, no borders around content; the paper itself is the frame.
- **Grid intensity**: None. Composition is intuitive and breathing, never gridded.

## Colors
The palette is monochrome by doctrine: graded black sumi ink and the toned grays it produces when diluted, set against weathered mulberry-paper oatmeal. Color discipline is absolute — only one hue, the vermilion seal, is permitted, and it appears at most once per composition as a focal accent.

**Role usage**:
- Page background → `colors.background.page` (`#D8CFBE` weathered washi)
- Primary ink / headings / body text → `colors.text.primary` (`#16130F`)
- Secondary tonal text → `colors.text.secondary` (`#3A352D`)
- Muted gray (captions, fine strokes) → `colors.text.muted` (`#6E675B`)
- Mid-gray wash tone → `colors.neutral.400` (`#A39C8C`)
- Vermilion seal accent → `colors.accent.500` (`#E2462F`)
- Card / panel surface → `colors.background.surface` (`#E0D8C9`)

## Typography
Type is set in Mincho serifs — the printed descendants of brush calligraphy, with modulated strokes and triangular serifs (uroko) that echo the lift of a loaded brush. Display sizing is generous and airy, weights stay light to medium, and letter-spacing opens up to let each character breathe like a deliberate brushstroke.

**Text styles**:
- `display-xl` — Zen Old Mincho, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Zen Old Mincho, 64px, weight 600, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Shippori Mincho, 36px, weight 600, line-height 1.2, letter-spacing 0
- `body-lg` — Shippori Mincho, 18px, weight 400, line-height 1.8, letter-spacing 0.02em
- `body-md` — Noto Serif JP, 16px, weight 400, line-height 1.8, letter-spacing 0.02em
- `caption` — Noto Serif JP, 13px, weight 400, line-height 1.6, letter-spacing 0.05em
- `mono-md` — Noto Serif JP, 15px, weight 400, line-height 1.7, letter-spacing 0.05em

## Spacing & Layout
- Base unit 4px; rhythm on an 8px field for generous, calm spacing.
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container max-width holds a narrow measure (≤768px for text) so emptiness dominates the viewport.
- Section padding is large (96–128px) — silence between elements is structural, not decorative.

## Elevation & Depth
Depth comes from ink tonality, not from shadow or layering. The surface is flat matte paper; panels distinguish themselves only by the faintest tone shift, never by floating. Shadows, where used at all, are barely perceptible and warm-toned to read as ink soaking into fiber rather than UI elevation.

- Surface style: flat, matte, papery.
- Blur: none.
- Shadow ladder: near-invisible at rest (`xs`/`sm`), softening only slightly on the largest surfaces; no glassy or glossy elevation anywhere.

## Shapes
- Corner radii are essentially square (1–4px) — paper edges and seal impressions are crisp, not rounded.
- The one exception is the seal stamp itself and avatar marks, which may use the carved-square or full-round geometry of a hanko.
- No pill shapes, no large rounded cards.

## Motion
Motion is meditative and sparse — interactions resolve like ink settling into paper, never bouncing or sliding theatrically. Most state changes are pure opacity or a gentle ink-tint deepening. Nothing should feel mechanical or hurried.

- Level: minimal.
- Durations: 120–600ms; default transitions around 250ms.
- Easings: gentle ease-out for entrances; a soft spring reserved for the rare seal-stamp accent.
- Hover patterns: opacity shift, ink-tint deepening, calligraphic underline that draws in.

## Techniques
Three recipes characteristic of this brand: graded notan washes, dry-brush kasure edges, and the vermilion seal stamp.

### Notan ink-wash gradient
A graded tonal wash from saturated sumi black to pale gray, mimicking diluted ink bleeding across washi.
```css
.notan-wash {
  background: linear-gradient(
    160deg,
    #16130F 0%,
    #3A352D 28%,
    #6E675B 55%,
    #A39C8C 78%,
    rgba(216,207,190,0) 100%
  );
  filter: blur(0.5px);
}
```

### Kasure flying-white edge
Dry-brush texture where the stroke fractures and bare paper shows through, achieved by layering a streaked mask over an ink fill.
```css
.kasure-stroke {
  background-color: #16130F;
  -webkit-mask-image: repeating-linear-gradient(
    92deg,
    #000 0px,
    #000 6px,
    transparent 7px,
    #000 11px,
    rgba(0,0,0,0.4) 14px,
    #000 18px
  );
  mask-image: repeating-linear-gradient(
    92deg,
    #000 0px, #000 6px, transparent 7px,
    #000 11px, rgba(0,0,0,0.4) 14px, #000 18px
  );
  border-radius: 1px;
}
```

### Vermilion seal stamp
A small carved-square hanko impression in cinnabar red — the single focal accent, with slightly uneven edges to read as hand-pressed.
```css
.hanko-seal {
  display: inline-block;
  width: 56px;
  height: 56px;
  color: #E2462F;
  border: 3px solid currentColor;
  border-radius: 3px;
  font-family: 'Zen Old Mincho', serif;
  font-weight: 700;
  line-height: 50px;
  text-align: center;
  letter-spacing: 0;
  box-shadow: inset 0 0 0 2px rgba(226,70,47,0.25);
  filter: contrast(1.1) saturate(1.05);
  opacity: 0.92;
}
```

## Iconography
Icons are thin, even-weight line drawings that read like a single continuous brush gesture. Keep stroke weights light and consistent, prefer simple open forms over filled glyphs, and use icons sparingly — an icon should feel as deliberate as a placed brushstroke.

- Treatment: linear, single-weight.
- Set: lucide (or any minimal feather-style set).
- Stroke: 1.5px.

## Do's & Don'ts
### ✓ Do
- Let large areas of weathered washi stay empty — honor ma as a structural element.
- Build hierarchy from graded ink tone (notan), not from color or borders.
- Reserve the vermilion seal `#E2462F` for one focal accent per view.
- Keep edges brush-grade: soft notan washes and fractured kasure texture, never crisp vector lines.
- Set type in Mincho serifs with open letter-spacing so each character breathes.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — use weathered washi `#D8CFBE`.
- Do not fill the page; honor large ma negative space.
- No multi-color palette — only graded black ink plus the one vermilion seal.
- Avoid crisp digital vector edges; keep brush-grade tonality and kasure texture.

## Applications
Best suited to contemplative, premium contexts: gallery and museum sites, tea and ceramics brands, poetry and literary publishing, wellness and meditation products, and minimalist editorial layouts. The aesthetic rewards restraint, so it excels wherever silence and a single decisive mark carry more weight than density of information.
