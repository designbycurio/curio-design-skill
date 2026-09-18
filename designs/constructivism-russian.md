---
version: 1

meta:
  id: constructivism-russian
  name: Russian Constructivism
  description: Militant geometric design forged in revolutionary red, black diagonals, and bold sans-serif type
  isDark: false
  tags: [modernist, bold, historical, decorative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1917–early 1930s; suppressed by Socialist Realism ~1934"
  region: "Soviet Union (Moscow, Vitebsk)"
  regionZh: "苏联（莫斯科、维捷布斯克）"
  keyFigures: [Aleksandr Rodchenko, El Lissitzky, Vladimir Tatlin, Varvara Stepanova]
  movements: [Suprematism, Productivism, Bauhaus-adjacent]

introduction: |
  Russian Constructivism arose from the 1917 October Revolution as a radical rejection of "art for art's sake." Designers like Rodchenko, Lissitzky, and Stepanova demanded that visual form serve socialist construction — producing propaganda posters, book covers, and film advertisements with militant clarity.

  The movement's visual language is unmistakable: revolutionary red slashed across black and white, heavy geometric sans-serif type set at aggressive diagonals, photomontage collisions, and asymmetric compositions that feel perpetually in motion. Suppressed by Stalin's doctrine around 1934, its influence echoes through punk graphics, Bauhaus typography, and contemporary brutalist web design.

introductionZh: |
  俄国构成主义诞生于1917年十月革命的烈火之中，彻底否定了"为艺术而艺术"的旧观念。罗德琴科、利西茨基、斯捷潘诺娃等设计师坚持视觉形式必须为社会主义建设服务，创造出大量宣传海报、书籍封面和电影广告，以战斗般的清晰度传达革命信息。

  这一运动的视觉语言独树一帜：革命红色斜劈黑白画面，厚重的几何无衬线字体以30°或45°角倾斜排列，照片蒙太奇硬切拼贴，不对称构图始终充满动势。尽管在1934年前后被斯大林的社会主义现实主义教条所压制，其影响却深远地回响在朋克平面设计、包豪斯字体排印以及当代粗野主义网页设计之中。

colors:
  primary:
    "50": "#fef2f2"
    "100": "#fee2e2"
    "200": "#fca5a5"
    "300": "#f87171"
    "400": "#ef4444"
    "500": "#d40000"
    "600": "#b91c1c"
    "700": "#991b1b"
    "800": "#7f1d1d"
    "900": "#601010"
    "950": "#3b0808"
  secondary:
    "50": "#fafafa"
    "100": "#f5f5f5"
    "200": "#e5e5e5"
    "300": "#d4d4d4"
    "400": "#a3a3a3"
    "500": "#000000"
    "600": "#000000"
    "700": "#000000"
    "800": "#000000"
    "900": "#000000"
    "950": "#000000"
  accent:
    "50": "#fefce8"
    "100": "#fef9c3"
    "200": "#fef08a"
    "300": "#fde047"
    "400": "#facc15"
    "500": "#eab308"
    "600": "#ca8a04"
    "700": "#a16207"
    "800": "#854d0e"
    "900": "#713f12"
    "950": "#422006"
  neutral:
    "50": "#fafaf5"
    "100": "#f5f5ec"
    "200": "#e8e8dc"
    "300": "#d4d4c8"
    "400": "#a8a89c"
    "500": "#6b6b60"
    "600": "#52524a"
    "700": "#3d3d38"
    "800": "#292926"
    "900": "#1a1a18"
    "950": "#0d0d0c"
  semantic:
    success: { bg: "#166534", text: "#ffffff", light: "#dcfce7", border: "#16a34a" }
    warning: { bg: "#eab308", text: "#000000", light: "#fef9c3", border: "#ca8a04" }
    error:   { bg: "#d40000", text: "#ffffff", light: "#fee2e2", border: "#b91c1c" }
    info:    { bg: "#000000", text: "#ffffff", light: "#f5f5f5", border: "#525252" }
  background:
    page:    "#f5f5ec"
    surface: "#ffffff"
    subtle:  "#e8e8dc"
  text:
    primary:   "#000000"
    secondary: "#292926"
    muted:     "#6b6b60"
    inverse:   "#f5f5ec"

typography:
  families:
    heading: "'Archivo Black', 'Anton', Impact, sans-serif"
    body:    "'Barlow Condensed', 'Roboto Condensed', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Archivo+Black&family=Barlow+Condensed:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"
  scale:
    "2xs": "0.625rem"
    xs: "0.75rem"
    sm: "0.875rem"
    base: "1rem"
    lg: "1.125rem"
    xl: "1.25rem"
    "2xl": "1.5rem"
    "3xl": "1.875rem"
    "4xl": "2.25rem"
    "5xl": "3rem"
    "6xl": "4rem"
    "7xl": "6rem"
  weights: { light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800 }
  lineHeights: { tight: 1.1, snug: 1.2, normal: 1.4, relaxed: 1.5, loose: 1.7 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.08em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px",  md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "0", md: "0", lg: "2px", xl: "4px", full: "9999px" }
  color:  { default: "#000000", subtle: "#292926", strong: "#d40000", focus: "#d40000" }
  width:  { thin: "1px", default: "2px", thick: "4px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "2px 2px 0 rgba(0,0,0,1)"
  sm: "3px 3px 0 rgba(0,0,0,1)"
  md: "4px 4px 0 rgba(0,0,0,1)"
  lg: "6px 6px 0 rgba(0,0,0,1)"
  xl: "8px 8px 0 rgba(0,0,0,1)"
  "2xl": "12px 12px 0 rgba(0,0,0,1)"
  inner: "inset 2px 2px 0 rgba(0,0,0,0.15)"
  focus: "0 0 0 3px rgba(212,0,0,0.5)"

motion:
  level: "minimal"
  durations: { instant: "0ms", fast: "80ms", normal: "150ms", slow: "250ms", slower: "400ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.2, 0, 0, 1.4)"
  hoverPatterns: [opacity, tint]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "full-bleed"
  framing:       "bordered"
  gridIntensity: "strong"
  rhythm:        "4px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "2px"

components:
  button:
    primary:   { background: "#d40000", color: "#ffffff", border: "2px solid #000000", shadow: "3px 3px 0 #000000", hoverBackground: "#b91c1c", hoverShadow: "1px 1px 0 #000000", hoverColor: "#ffffff" }
    secondary: { background: "#000000", color: "#ffffff", border: "2px solid #000000", shadow: "3px 3px 0 #d40000", hoverBackground: "#292926", hoverShadow: "1px 1px 0 #d40000", hoverColor: "#ffffff" }
    ghost:     { background: "transparent", color: "#000000", border: "2px solid #000000", shadow: "none", hoverBackground: "#000000", hoverShadow: "none", hoverColor: "#ffffff" }
    danger:    { background: "#d40000", color: "#ffffff", border: "2px solid #7f1d1d", shadow: "3px 3px 0 #7f1d1d", hoverBackground: "#991b1b", hoverShadow: "1px 1px 0 #7f1d1d", hoverColor: "#ffffff" }
    sizes:
      sm: { height: "32px", padding: "0 12px", fontSize: "0.75rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "0.875rem" }
      lg: { height: "52px", padding: "0 32px", fontSize: "1rem" }
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "0.08em"
    textTransform: "uppercase"
  input:
    background: "#ffffff"
    color: "#000000"
    border: "2px solid #000000"
    borderRadius: "0"
    padding: "8px 12px"
    focusBorder: "2px solid #d40000"
    placeholderColor: "#6b6b60"
  card:
    base:  { background: "#ffffff", border: "3px solid #000000", borderRadius: "0", padding: "24px", shadow: "4px 4px 0 #000000" }
    hover: { shadow: "6px 6px 0 #d40000", transform: "translate(-2px, -2px)" }
---

# Russian Constructivism

> Militant geometric design forged in revolutionary red, black diagonals, and bold sans-serif type.

## Origin

Russian Constructivism erupted from the 1917 October Revolution, born in Moscow and Vitebsk art workshops where designers rejected bourgeois aesthetics. Aleksandr Rodchenko, El Lissitzky, Vladimir Tatlin, and Varvara Stepanova demanded that visual form serve socialist construction — producing propaganda posters, film advertisements, book covers, and the magazine LEF. Their work weaponized photomontage, geometric abstraction, and bold typography into instruments of mass communication.

The movement drew on Malevich's Suprematism and evolved into Productivism, insisting art must enter factories and streets. Lissitzky's "Beat the Whites with the Red Wedge" (1919), Rodchenko's photomontage posters for Mayakovsky's poems, and the Stenberg brothers' film posters defined a visual vocabulary that would influence Bauhaus typography, punk graphics, and contemporary brutalist web design. The movement was suppressed around 1934 under Stalin's Socialist Realism doctrine, but its confrontational energy endures.

## Overview
Composition cues:
- **Layout**: Asymmetric stacking — elements collide along strong horizontal, vertical, and diagonal axes rather than sitting in orderly grids.
- **Content width**: Full-bleed — imagery and color blocks push to the edge, maximizing confrontational impact.
- **Framing**: Bordered — thick black borders and split-color blocks define containers; no soft cards or floating panels.
- **Grid intensity**: Strong — visible structural lines and hard edges enforce hierarchy through collision, not spacing.

## Colors
The palette is ideological: revolutionary red (#d40000), absolute black, and absolute white. These three dominate every composition. Occasionally yellow enters as a tertiary accent — never pastels, never greys, never gradients. Color is applied in flat fills, used structurally to divide space and direct attention. Red commands action, black anchors structure, white provides the breath of the paper surface.

**Role usage**:
- Page background → `colors.background.page` (warm cream paper)
- Surface/card background → `colors.background.surface` (pure white)
- Primary actions and revolutionary accents → `colors.primary.500`
- Text and structural borders → `colors.secondary.500`
- Tertiary highlights and warnings → `colors.accent.500`
- Body text → `colors.text.primary`
- Secondary text → `colors.text.secondary`
- Muted labels → `colors.text.muted`

## Typography
Type is a weapon. Headings roar in Archivo Black — a heavy geometric sans-serif whose sharp-angled cuts evoke Cyrillic propaganda letterforms. Body text uses Barlow Condensed for efficient, tightly-packed information delivery. All headings are uppercase with wide tracking, reinforcing the movement's militancy. Diagonal and rotated text is the signature move: break the horizontal reading line to arrest attention.

**Text styles**:
- `display-xl` — Archivo Black, 96px, weight 400 (inherently bold), line-height 1.0, letter-spacing 0.08em, uppercase
- `display-lg` — Archivo Black, 64px, weight 400, line-height 1.05, letter-spacing 0.08em, uppercase
- `heading-1` — Archivo Black, 48px, weight 400, line-height 1.1, letter-spacing 0.05em, uppercase
- `body-lg` — Barlow Condensed, 20px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — Barlow Condensed, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Barlow Condensed, 12px, weight 600, line-height 1.4, letter-spacing 0.08em, uppercase
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px
- Scale: 2–4–6–8–12–16–24–32–48–64–96–128px
- Container: 1024px (lg) default; full-bleed for hero sections
- Section padding: 64px vertical (md), 96px for large sections
- Grid gap: 16px (md) between stacked blocks; 24px between major sections
- Rhythm: 4px increments throughout — no fractional spacing

## Elevation & Depth
Constructivism rejects soft depth. There are no blurred shadows, no ambient occlusion, no glassmorphism. Depth is achieved through hard offset shadows — solid black rectangles displaced 3–6px right and down, simulating ink blocks printed slightly out of register. This creates a mechanical, print-shop materiality.

- Surface style: flat — no gradients, no blur
- Shadow ladder: xs (2px offset), sm (3px), md (4px), lg (6px), xl (8px), 2xl (12px) — all solid black, no blur
- Focus ring: 3px red glow for interactive states
- Cards lift on hover by translating -2px along both axes while the shadow grows

## Shapes
- Corner radii: none — all elements are sharp rectangles (0px radius)
- Buttons: sharp-cornered rectangles; parallelogram variants via CSS skew for decorative treatments
- Cards: no rounded corners, thick borders only
- Tags/badges: sharp rectangles with 0 radius
- Accent: xl radius (4px) reserved for rare pill-shaped elements only

## Motion
Constructivism is static by ideology — the poster does not move. Motion in digital adaptation is minimal and mechanical: hard snaps, no elastic bounce, no organic ease. Transitions should feel like a letterpress stamp hitting paper.

- Level: minimal
- Fast transition: 80ms (hover states)
- Normal transition: 150ms (state changes)
- Slow transition: 250ms (panel reveals)
- Easing: linear or sharp ease-out — never springy
- Hover patterns: opacity shifts and flat color tint swaps
- Reduced motion: always respected

## Techniques

### Diagonal Red Wedge Accent
A signature Constructivist treatment: a sharp red diagonal element that slashes across a composition, inspired by Lissitzky's "Beat the Whites with the Red Wedge."
```css
.red-wedge {
  position: relative;
  overflow: hidden;
}
.red-wedge::after {
  content: '';
  position: absolute;
  top: -20%;
  right: -10%;
  width: 60%;
  height: 140%;
  background: #d40000;
  transform: rotate(-30deg);
  transform-origin: center;
  z-index: 0;
  pointer-events: none;
}
```

### Hard Offset Shadow Block
Mechanical offset shadows that evoke misregistered print blocks — a Constructivist signature replacing soft CSS box-shadow.
```css
.offset-block {
  position: relative;
  background: #ffffff;
  border: 3px solid #000000;
}
.offset-block::before {
  content: '';
  position: absolute;
  top: 6px;
  left: 6px;
  width: 100%;
  height: 100%;
  background: #000000;
  z-index: -1;
}
.offset-block:hover {
  transform: translate(-2px, -2px);
}
.offset-block:hover::before {
  top: 8px;
  left: 8px;
}
```

### Rotated Uppercase Label
Diagonal text placement — the Constructivist signature of breaking horizontal reading lines to arrest attention.
```css
.rotated-label {
  display: inline-block;
  font-family: 'Archivo Black', Impact, sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #ffffff;
  background: #d40000;
  padding: 4px 16px;
  transform: rotate(-5deg);
  transform-origin: left center;
  border: 2px solid #000000;
}
```

## Iconography
Icons follow the movement's geometric militancy: linear strokes at 2px weight, sharp terminals, no rounded caps. They should feel like they were cut from a linocut block — precise, angular, utilitarian. Decorative icon treatments are forbidden.

- Treatment: linear (sharp terminals)
- Set: Lucide
- Stroke: 2px

## Do's & Don'ts

### ✓ Do
- Use revolutionary red (#d40000) for all primary actions and attention-commanding elements
- Set headings in uppercase Archivo Black with wide letter-spacing
- Break compositions with aggressive diagonals (30° or 45° rotations)
- Apply hard offset shadows instead of blurred box-shadows
- Use asymmetric layouts that create dynamic tension between elements

### ✗ Don't
- Use pastels, muted tones, or earthy palettes
- Use decorative serif fonts
- Center or symmetrically balance layouts
- Introduce soft curves or organic shapes
- Apply gradients, glows, or glassmorphism effects

## Applications
Russian Constructivism is ideal for bold editorial sites, activist platforms, cultural institution pages, event landing pages, and any interface that demands confrontational visual authority. It works best at large scale — hero sections, poster-format layouts, full-bleed imagery — where the aggressive geometry and limited palette can dominate. It pairs naturally with photography-heavy content where photomontage-style compositions can create visual impact.
