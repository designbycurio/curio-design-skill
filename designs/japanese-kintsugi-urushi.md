---
version: 1

meta:
  id: japanese-kintsugi-urushi
  name: Kintsugi & Urushi Lacquer
  description: Real gold seaming dark cured-lacquer surfaces — breakage made beautiful on deep urushi black-brown.
  isDark: true
  tags: [historical, luxurious, handmade, ornate, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Muromachi onward (15th c.); refined through Edo, still practiced today"
  region: "Japan, East Asia"
  regionZh: "日本"
  keyFigures: [Honami Koetsu, Ogata Korin, Shiomi Masanari]
  movements: [Kintsugi, Maki-e, Wabi-sabi]

introduction: |
  Kintsugi is the Japanese art of mending broken vessels with lacquer dusted in
  gold, refusing to hide the fracture and instead tracing it in light. The ground
  is urushi — sap of the lacquer tree, layered and polished to a deep chestnut
  black, with the final coat beneath the gold laid in iron-red so the seams sing.
  This system carries that craft into the interface: dark, glossy lacquer surfaces
  veined with hand-laid gold, asymmetric and breathing, every edge a repair worth
  showing.
introductionZh: |
  金继（kintsugi）是日本以漆和金粉修补破损器物的工艺：不掩裂痕，反以金线描其断处，
  让破碎本身成为器物最美的纹章。底色来自「漆」（urushi）——漆树之汁层层髹涂、研磨至
  栗色近黑的「roiro」漆面，金线之下垫一层弁柄红，使金愈发明亮。此设计系统将这门手艺
  移入界面：深沉莹润的漆色底，缀以手工描金的脉络，留白呼吸、构图不对称，每一道边缘都
  是一处值得袒露的修补。

colors:
  primary:    {"50": "#FBF3DC", "100": "#F4E3B0", "200": "#E8CB78", "300": "#D9B348", "400": "#C99B22", "500": "#B8860B", "600": "#9C7009", "700": "#7C5907", "800": "#5C4205", "900": "#3D2C03", "950": "#241A02"}
  secondary:  {"50": "#FBF0D8", "100": "#F5DFA8", "200": "#EBC86C", "300": "#DDB23D", "400": "#D2A92E", "500": "#C9A227", "600": "#AA871F", "700": "#876A18", "800": "#634E11", "900": "#40330B", "950": "#261E06"}
  accent:     {"50": "#FBE6E2", "100": "#F4C0B7", "200": "#E89486", "300": "#DB6755", "400": "#C5453A", "500": "#9E2A1B", "600": "#852316", "700": "#691B11", "800": "#4D140C", "900": "#310D08", "950": "#1D0704"}
  neutral:    {"50": "#F2E9E2", "100": "#DCC9BB", "200": "#BFA08B", "300": "#9C7A62", "400": "#7B5A45", "500": "#5C4232", "600": "#473023", "700": "#3A241A", "800": "#2A1A12", "900": "#1E140E", "950": "#130C08"}
  semantic:
    success: { bg: "#1F2A14", text: "#A9C46A", light: "#2C3A1C", border: "#475A2A" }
    warning: { bg: "#2E2407", text: "#D9B348", light: "#3D3009", border: "#6B5410" }
    error:   { bg: "#2E0F08", text: "#DB6755", light: "#3D1610", border: "#691B11" }
    info:    { bg: "#15211F", text: "#7BB0A4", light: "#1E2E2B", border: "#2F4A44" }
  background:
    page:    "#1E140E"
    surface: "#2A1A12"
    subtle:  "#3A241A"
  text:
    primary:   "#F2E9E2"
    secondary: "#C9A227"
    muted:     "#9C7A62"
    inverse:   "#1E140E"

typography:
  families:
    heading: "'Zen Old Mincho', 'Shippori Mincho', serif"
    body:    "'Noto Serif JP', 'EB Garamond', serif"
    mono:    "'EB Garamond', Georgia, serif"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Zen+Old+Mincho:wght@400;500;600;700&family=Shippori+Mincho:wght@400;500;600;700;800&family=Noto+Serif+JP:wght@300;400;500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap"
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
  color:  {default: "#473023", subtle: "#3A241A", strong: "#B8860B", focus: "#C9A227"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.35)"
  sm: "0 2px 6px rgba(0,0,0,0.45)"
  md: "0 6px 18px rgba(0,0,0,0.5), inset 0 1px 0 rgba(201,162,39,0.06)"
  lg: "0 14px 38px rgba(0,0,0,0.55), inset 0 1px 0 rgba(201,162,39,0.08)"
  xl: "0 26px 60px rgba(0,0,0,0.6), inset 0 1px 0 rgba(201,162,39,0.1)"
  "2xl": "0 40px 90px rgba(0,0,0,0.65)"
  inner: "inset 0 2px 6px rgba(0,0,0,0.5)"
  focus: "0 0 0 3px rgba(184,134,11,0.4)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [glow, tint, lift]
  reducedMotion: true

composition:
  layout:        stack
  contentWidth:  narrow
  framing:       solid
  gridIntensity: subtle
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
    primary:   {background: "linear-gradient(180deg, #C99B22 0%, #B8860B 60%, #9C7009 100%)", color: "#1E140E", border: "1px solid #9C7009", shadow: "0 2px 6px rgba(0,0,0,0.45), inset 0 1px 0 rgba(251,243,220,0.35)", hoverBackground: "linear-gradient(180deg, #D9B348 0%, #C99B22 60%, #B8860B 100%)", hoverShadow: "0 4px 14px rgba(184,134,11,0.4)", hoverColor: "#1E140E"}
    secondary: {background: "transparent", color: "#C9A227", border: "1px solid #B8860B", shadow: "none", hoverBackground: "rgba(184,134,11,0.12)", hoverShadow: "0 0 0 1px rgba(201,162,39,0.4)", hoverColor: "#F4E3B0"}
    ghost:     {background: "transparent", color: "#9C7A62", border: "1px solid transparent", shadow: "none", hoverBackground: "rgba(201,162,39,0.08)", hoverShadow: "none", hoverColor: "#C9A227"}
    danger:    {background: "#9E2A1B", color: "#F2E9E2", border: "1px solid #691B11", shadow: "0 2px 6px rgba(0,0,0,0.45)", hoverBackground: "#852316", hoverShadow: "0 4px 14px rgba(158,42,27,0.4)", hoverColor: "#F2E9E2"}
    sizes:     {sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "42px", padding: "0 22px", fontSize: "1rem"}, lg: {height: "52px", padding: "0 32px", fontSize: "1.125rem"}}
    borderRadius: "4px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#130C08"
    color: "#F2E9E2"
    border: "1px solid #473023"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "1px solid #B8860B"
    placeholderColor: "#7B5A45"
  card:
    base:  {background: "#2A1A12", border: "1px solid #3A241A", borderRadius: "8px", padding: "28px", shadow: "0 14px 38px rgba(0,0,0,0.55), inset 0 1px 0 rgba(201,162,39,0.08)"}
    hover: {shadow: "0 20px 50px rgba(0,0,0,0.6), inset 0 1px 0 rgba(201,162,39,0.12)", transform: "translateY(-2px)"}
---

# Kintsugi & Urushi Lacquer

> Breakage seamed in gold — dark cured lacquer veined with light, where the repair is the ornament.

## Origin
Kintsugi — "golden joinery" — emerged in Japan by the late Muromachi period, when a damaged tea bowl returned from China with crude metal staples is said to have prompted Japanese craftsmen to seek a mend worthy of the vessel. The answer was urushi: the sap of *Toxicodendron vernicifluum*, brushed in dozens of cured layers and polished to a chestnut-black sheen, with the broken seam filled and then dusted in real gold powder (maki-e). The final lacquer layer beneath the gold was laid in bengara iron-red so the metal would glow warm.

By the Edo era the technique was inseparable from wabi-sabi — the aesthetic that finds beauty in impermanence and imperfection. Lacquer masters such as the Shiomi maki-e lineage, and design-minded craftsmen around Honami Koetsu and Ogata Korin, elevated repair into an art that prized the history a fracture records rather than concealing it. A kintsugi vessel is not restored to its old self; it is made into something whose value lies precisely in having been broken.

## Overview
Composition cues:
- **Layout**: Vertical stacks with generous, asymmetric negative space; content drifts off-center like a vessel placed in a tokonoma alcove.
- **Content width**: Narrow, single-column reading measure — never edge-to-edge sprawl.
- **Framing**: Solid lacquer panels with soft inset sheen; no glass, no hard tech borders.
- **Grid intensity**: Subtle — alignment is felt, not drawn; the rhythm breathes rather than locks.

## Colors
The palette is the lacquerware itself: a cured chestnut-to-black urushi ground, makie gold for every seam and accent, a hot bengara iron-red glowing beneath the gold, and warm raw-lacquer browns for surfaces. Gold is the only "bright" — it must be earned, used for the lines of repair and the single most important action, never spread flat.
**Role usage**:
- Page background → `colors.background.page` (#1E140E)
- Panels & cards → `colors.background.surface` (#2A1A12)
- Recessed wells / inputs → `colors.neutral.950` (#130C08)
- Gold seams, primary action, key headings → `colors.primary.500` (#B8860B)
- Bright maki-e highlights, secondary text → `colors.secondary.500` (#C9A227)
- Iron-red glow / danger / emphasis → `colors.accent.500` (#9E2A1B)
- Body text on lacquer → `colors.text.primary` (#F2E9E2)
- Muted captions → `colors.text.muted` (#9C7A62)

## Typography
Mincho serifs carry the calligraphic, ceremonial register of the tea room; their tapered strokes and tiny triangular serifs (uroko) echo brush-laid lacquer. Display weight goes to Zen Old Mincho and Shippori Mincho, Japanese and Latin body to Noto Serif JP and EB Garamond. Type is set quiet and large, with airy line-height, like an inscription beside a treasured object.
**Text styles**:
- `display-xl` — Zen Old Mincho, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Shippori Mincho, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Zen Old Mincho, 36px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Noto Serif JP, 18px, weight 400, line-height 1.8, letter-spacing 0
- `body-md` — Noto Serif JP, 16px, weight 400, line-height 1.625, letter-spacing 0
- `caption` — EB Garamond, 14px, weight 400, line-height 1.5, letter-spacing 0.05em, italic
- `mono-md` — EB Garamond, 15px, weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit 4px; rhythm settles on an 8px cadence for calm vertical pacing.
- Scale: 2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128px.
- Container caps narrow (max ~768px reading width) so text feels like an inscription, not a feed.
- Section padding ample: 96–128px between major movements to let surfaces breathe.

## Elevation & Depth
Lacquer is layered, not floating — surfaces sit on the page with a deep matte shadow and a faint gold sheen along the top edge, never a glassy blur. Depth reads as polished wood-lacquer thickness, not as glass panes hovering in space.
- Surface style: layered solid lacquer panels with subtle inset top-light.
- Blur: none — lacquer is opaque and reflective, not frosted.
- Shadow ladder: soft, dark, diffuse (xs → 2xl), each with a hairline `inset 0 1px 0 rgba(201,162,39,…)` gold glint.

## Shapes
- Corner radii kept tight and restrained: sm 2px, md 4px, lg 8px, xl 16px.
- Pills (`full`) reserved for tags and small status seals.
- Prefer gently rounded rectangles and vessel-like silhouettes over sharp tech corners.

## Motion
Restrained and ceremonial — things settle into place the way lacquer cures, slow and certain. Gold reveals are the showpiece: a seam can draw itself along a path on entrance, and gold elements warm with a soft glow on hover rather than jumping.
- Level: restrained.
- Durations: fast 120ms, normal 250ms, slow 400ms, slower 600ms for seam draws.
- Easings: default ease-in-out; `out` for entrances; gentle `spring` only for the seam-trace reveal.
- Hover patterns: glow (warm gold halo), tint (red underglow), subtle lift on cards.

## Techniques
### Gold seam (kintsugi crack)
An irregular hand-laid gold seam dividing two lacquer surfaces, with a thin iron-red glow beneath the gold.
```css
.kintsugi-seam {
  position: relative;
  height: 3px;
  background: linear-gradient(90deg,
    #9C7009 0%, #C99B22 18%, #D4AF37 34%, #B8860B 52%,
    #D9B348 70%, #9C7009 88%, #C9A227 100%);
  /* organic, non-straight edge — never a ruler line */
  clip-path: polygon(
    0 40%, 8% 60%, 16% 30%, 27% 70%, 38% 35%, 50% 65%,
    61% 30%, 72% 68%, 83% 38%, 92% 62%, 100% 45%,
    100% 55%, 0 60%);
  filter: drop-shadow(0 0 4px rgba(212,175,55,0.5));
}
.kintsugi-seam::before { /* bengara iron-red underglow so the gold sings */
  content: "";
  position: absolute;
  inset: -2px 0;
  background: radial-gradient(ellipse at center, rgba(158,42,27,0.45), transparent 70%);
  z-index: -1;
}
```

### Maki-e gold powder (matte, not chrome)
Gold rendered as dusted powder — warm and soft-sheen — never a flat mirror gradient.
```css
.makie-gold {
  color: #1E140E;
  background:
    radial-gradient(circle at 30% 20%, rgba(251,243,220,0.5), transparent 40%),
    linear-gradient(135deg, #D4AF37 0%, #C9A227 45%, #B8860B 75%, #9C7009 100%);
  background-blend-mode: screen, normal;
  text-shadow: 0 1px 0 rgba(251,243,220,0.4);
}
```

### Nashiji lacquer ground
The cured urushi surface — chestnut-black with faint scattered gold flecks, like nashiji ("pear-skin") lacquer.
```css
.urushi-ground {
  background-color: #1E140E;
  background-image:
    radial-gradient(circle at 12% 24%, rgba(201,162,39,0.10) 0 1px, transparent 2px),
    radial-gradient(circle at 67% 58%, rgba(212,175,55,0.08) 0 1px, transparent 2px),
    radial-gradient(circle at 88% 82%, rgba(201,162,39,0.09) 0 1px, transparent 2px),
    radial-gradient(ellipse at 70% 0%, rgba(123,63,0,0.25), transparent 60%);
  background-size: 180px 180px, 220px 220px, 160px 160px, 100% 100%;
}
```

## Iconography
Use fine linear icons with a 1.5px stroke (Phosphor or similar), thin enough to read like brush lines rather than UI furniture. Where an icon marks something precious or a key action, tint it makie gold (#C9A227). Keep the set sparse — icons accent the ceremony, they don't crowd it.

## Do's & Don'ts
### ✓ Do
- Set everything on the deep urushi ground (#1E140E) — surfaces are lacquer, never paper.
- Use makie gold (#B8860B) for the lines of repair and the single most important action.
- Lay a thin bengara iron-red glow beneath gold seams so the gold sings.
- Embrace asymmetry and breathing negative space, like a vessel in an alcove.
- Render gold as soft-sheen powder with warm highlights, not a flat mirror.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds.
- No flat metallic-gold gradients that look like chrome — gold is powdered makie, warm and matte-to-soft-sheen.
- No symmetrical, gridded "perfect" layouts; embrace asymmetry and imperfection.
- No emoji-style cracks or comic fracture lines; seams are organic and hand-laid.

## Applications
Best for luxury and craft brands, gallery and museum sites, tea-ceremony and ceramics storefronts, premium editorial features, and any narrative that frames flaws and history as value. The dark, ceremonial register suits slow, considered reading over dense dashboards — show one precious thing at a time.
