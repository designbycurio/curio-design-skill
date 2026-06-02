---
version: 1

meta:
  id: de-stijl-mondrian
  name: De Stijl
  description: "Pure abstraction through primary colors, black lines, and rectangular grids inspired by Mondrian's Neoplasticism"
  isDark: false
  tags: [modernist, decorative, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1917–1931 (formally dissolved with Theo van Doesburg's death in 1931)"
  region: "Leiden, Netherlands (later Paris)"
  regionZh: "荷兰莱顿（后巴黎）"
  keyFigures: [Piet Mondrian, Theo van Doesburg, Gerrit Rietveld, Bart van der Leck]
  movements: [Neoplasticism, abstraction, modernism]

introduction: |
  De Stijl distills visual language to its absolute essence: vertical and horizontal black lines carving a white canvas into asymmetric rectangles filled with pure red, blue, or yellow. Founded in 1917 by Mondrian and van Doesburg, the movement sought universal harmony through radical reduction.

  This design system translates Neoplasticism into digital interfaces — thick black borders, zero border-radius, flat primary-color fills, and rigidly orthogonal layouts that echo Mondrian's iconic Compositions.
introductionZh: |
  "风格派"将视觉语言提炼至最纯粹的本质：黑色的水平与垂直线条将白色画布切割为不对称的矩形色块，仅以纯红、纯蓝、纯黄填充。1917年由蒙德里安与杜斯堡在荷兰莱顿创立，这场运动追求通过极致简化达到普遍和谐。

  本设计系统将新造型主义转化为数字界面——粗黑边框、零圆角、平面原色填充、严格正交的布局，忠实再现蒙德里安标志性"构成"系列画作的视觉精神。

colors:
  primary:
    "50": "#fde8e8"
    "100": "#fbc5c4"
    "200": "#f69a99"
    "300": "#f16e6c"
    "400": "#ec4744"
    "500": "#e6201c"
    "600": "#c81a17"
    "700": "#a91513"
    "800": "#8b100f"
    "900": "#6d0c0b"
    "950": "#4e0808"
  secondary:
    "50": "#e6eef8"
    "100": "#b3cceb"
    "200": "#80aade"
    "300": "#4d88d1"
    "400": "#2668ba"
    "500": "#0048a3"
    "600": "#003d8a"
    "700": "#003271"
    "800": "#002759"
    "900": "#001c40"
    "950": "#00112b"
  accent:
    "50": "#fffbe6"
    "100": "#fff3b3"
    "200": "#ffeb80"
    "300": "#ffe34d"
    "400": "#ffdc26"
    "500": "#ffd500"
    "600": "#d9b500"
    "700": "#b39500"
    "800": "#8c7500"
    "900": "#665500"
    "950": "#403600"
  neutral:
    "50": "#ffffff"
    "100": "#f5f5f5"
    "200": "#e5e5e5"
    "300": "#d4d4d4"
    "400": "#a3a3a3"
    "500": "#737373"
    "600": "#525252"
    "700": "#404040"
    "800": "#262626"
    "900": "#171717"
    "950": "#000000"
  semantic:
    success: { bg: "#e6201c", text: "#ffffff", light: "#fde8e8", border: "#e6201c" }
    warning: { bg: "#ffd500", text: "#000000", light: "#fffbe6", border: "#ffd500" }
    error: { bg: "#e6201c", text: "#ffffff", light: "#fde8e8", border: "#e6201c" }
    info: { bg: "#0048a3", text: "#ffffff", light: "#e6eef8", border: "#0048a3" }
  background:
    page: "#ffffff"
    surface: "#ffffff"
    subtle: "#f5f5f5"
  text:
    primary: "#000000"
    secondary: "#404040"
    muted: "#737373"
    inverse: "#ffffff"

typography:
  families:
    heading: "'Archivo Black', 'Work Sans', sans-serif"
    body: "'Work Sans', 'Archivo', sans-serif"
    mono: "'Space Mono', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Archivo+Black&family=Work+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap"
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
  weights:
    light: 300
    normal: 400
    medium: 500
    semibold: 600
    bold: 700
    extrabold: 800
  lineHeights:
    tight: 1.2
    snug: 1.375
    normal: 1.5
    relaxed: 1.625
    loose: 1.8
  letterSpacing:
    tighter: "-0.04em"
    tight: "-0.02em"
    normal: "0"
    wide: "0.05em"

spacing:
  base: "4px"
  scale: ["2px", "4px", "6px", "8px", "12px", "16px", "24px", "32px", "48px", "64px", "96px", "128px"]
  container:
    sm: "640px"
    md: "768px"
    lg: "1024px"
    xl: "1280px"
    full: "100%"
  gridGap:
    sm: "0px"
    md: "0px"
    lg: "0px"
    xl: "0px"
  sectionPadding:
    sm: "32px"
    md: "64px"
    lg: "96px"
    xl: "128px"

borders:
  radius:
    none: "0"
    sm: "0"
    md: "0"
    lg: "0"
    xl: "0"
    full: "0"
  color:
    default: "#000000"
    subtle: "#000000"
    strong: "#000000"
    focus: "#0048a3"
  width:
    thin: "2px"
    default: "3px"
    thick: "4px"
  style: "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  "2xl": "none"
  inner: "none"
  focus: "0 0 0 3px rgba(0, 72, 163, 0.4)"

motion:
  level: "minimal"
  durations:
    instant: "0ms"
    fast: "80ms"
    normal: "150ms"
    slow: "250ms"
    slower: "400ms"
  easings:
    default: "cubic-bezier(0, 0, 1, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.4, 0, 0.2, 1)"
  hoverPatterns: [tint, opacity]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "strong"
  rhythm: "4px"

surfaceStyle: "flat"
blur: "none"

iconography:
  treatment: "linear"
  set: "lucide"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "2px"

components:
  button:
    primary:
      background: "#e6201c"
      color: "#ffffff"
      border: "3px solid #000000"
      shadow: "none"
      hoverBackground: "#c81a17"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    secondary:
      background: "#0048a3"
      color: "#ffffff"
      border: "3px solid #000000"
      shadow: "none"
      hoverBackground: "#003d8a"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    ghost:
      background: "transparent"
      color: "#000000"
      border: "3px solid #000000"
      shadow: "none"
      hoverBackground: "#ffd500"
      hoverShadow: "none"
      hoverColor: "#000000"
    danger:
      background: "#e6201c"
      color: "#ffffff"
      border: "3px solid #000000"
      shadow: "none"
      hoverBackground: "#a91513"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    sizes:
      sm: { height: "36px", padding: "8px 16px", fontSize: "0.875rem" }
      md: { height: "44px", padding: "12px 24px", fontSize: "1rem" }
      lg: { height: "52px", padding: "16px 32px", fontSize: "1.125rem" }
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#ffffff"
    color: "#000000"
    border: "3px solid #000000"
    borderRadius: "0"
    padding: "12px 16px"
    focusBorder: "3px solid #0048a3"
    placeholderColor: "#737373"
  card:
    base:
      background: "#ffffff"
      border: "3px solid #000000"
      borderRadius: "0"
      padding: "24px"
      shadow: "none"
    hover:
      shadow: "none"
      transform: "none"
---

# De Stijl

> Pure abstraction through primary colors, black lines, and rectangular grids — Mondrian's Neoplasticism as a digital design system.

## Origin

De Stijl ("The Style") emerged in 1917 in the Netherlands, founded by painters Piet Mondrian and Theo van Doesburg alongside architect Gerrit Rietveld. The movement was a radical distillation of visual language: all form reduced to horizontal and vertical lines, all color reduced to red, blue, yellow, black, and white. Their journal *De Stijl* (1917–1932) served as the movement's manifesto, arguing that universal harmony could be achieved through pure abstraction and the elimination of individual expression.

Mondrian's iconic "Composition" paintings — asymmetric grids of black lines enclosing white rectangles punctuated by primary-color blocks — became the movement's visual shorthand. Rietveld translated these principles into three dimensions with the Red-Blue Chair (1918) and the Schröder House (1924) in Utrecht. The movement formally dissolved with van Doesburg's death in 1931 but profoundly shaped Bauhaus, the International Style, and modernist graphic design for the century that followed.

## Overview

Composition cues:
- **Layout**: Asymmetric rectangular grid — blocks of varying proportion divided by thick black lines, directly evoking Mondrian's paintings
- **Content width**: Container-bound with strong internal grid divisions
- **Framing**: Heavy black borders on all elements; no rounded corners, no shadows, no gradients
- **Grid intensity**: Strong — the grid IS the design; black lines are always visible structural elements

## Colors

De Stijl permits exactly five values: pure red (#e6201c), pure blue (#0048a3), pure yellow (#ffd500), black (#000000), and white (#ffffff). There are no greys, no mixed colors, no shades, no tints. Color is applied as flat, solid fills bounded by black lines. Most of the canvas remains white; color is used sparingly to create asymmetric visual weight — a large red block anchoring one corner, a small blue rectangle balancing it from across the composition.

**Role usage**:
- Page background → `colors.background.page` (always pure white)
- Primary actions and key highlights → `colors.primary.500` (Mondrian red)
- Secondary actions and informational elements → `colors.secondary.500` (Mondrian blue)
- Accent and active/selected states → `colors.accent.500` (Mondrian yellow)
- All text → `colors.text.primary` (pure black)
- All borders and dividers → `colors.neutral.950` (pure black)
- Inverse text on colored blocks → `colors.text.inverse` (pure white)

## Typography

De Stijl typography is geometric, constructed, and orthogonal. Theo van Doesburg designed a modular alphabet built entirely from horizontal and vertical strokes — no curves, no diagonals. The type voice is bold, declarative, and architectonic. Headings use Archivo Black for its squared, heavy geometry; body text uses Work Sans for its clean geometric proportions while remaining readable at paragraph lengths.

**Text styles**:
- `display-xl` — Archivo Black, 96px, weight 400 (Archivo Black has one weight), line-height 1.0, letter-spacing -0.04em
- `display-lg` — Archivo Black, 64px, weight 400, line-height 1.0, letter-spacing -0.02em
- `heading-1` — Archivo Black, 48px, weight 400, line-height 1.2, letter-spacing 0
- `body-lg` — Work Sans, 18px, weight 500, line-height 1.5, letter-spacing 0
- `body-md` — Work Sans, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Work Sans, 12px, weight 700, line-height 1.375, letter-spacing 0.05em, uppercase
- `mono-md` — Space Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px
- Grid gaps are 0px — blocks are separated by their black borders, not whitespace (borders serve as the grid lines, just like in a Mondrian painting)
- Section padding: 64px (md) to 128px (xl)

## Elevation & Depth

De Stijl is absolutely flat. There is no elevation, no depth, no shadows, no blur. All elements exist on a single plane, separated only by black lines. The visual hierarchy comes entirely from color weight, size proportion, and position within the grid — never from simulated depth.

- Surface style: flat — no layering, no stacking
- Blur: none
- Shadow ladder: all values are `none`

## Shapes

- All corner radii are **0** — zero exceptions. Neoplasticism forbids curves.
- All shapes are rectangles or squares
- No circles, no ellipses, no rounded corners, no pill shapes

## Motion

De Stijl's visual language is static and architectural. Motion, when present, is minimal and instantaneous — elements snap into position rather than flowing or easing.

- Level: minimal
- Durations: fast (80ms) to slow (250ms); nothing lingering
- Easings: linear preferred — no bouncing, no spring physics
- Hover patterns: flat tint swap (e.g., white block becomes yellow) or opacity change; no lifts, no scales, no glows

## Techniques

### Mondrian Grid Layout
A CSS Grid that divides the viewport into asymmetric rectangular regions separated by thick black lines, directly recreating a Mondrian composition.
```css
.mondrian-grid {
  display: grid;
  grid-template-columns: 2fr 3px 1fr 3px 1.5fr;
  grid-template-rows: 1.5fr 3px 1fr 3px 2fr;
  gap: 0;
  min-height: 100vh;
}
.mondrian-grid > .line-h,
.mondrian-grid > .line-v {
  background: #000000;
}
.mondrian-grid > .block-red { background: #e6201c; }
.mondrian-grid > .block-blue { background: #0048a3; }
.mondrian-grid > .block-yellow { background: #ffd500; }
.mondrian-grid > .block-white { background: #ffffff; }
```

### Primary-Color Block Accent
Applies a solid primary-color background to a content block, bounded by thick black borders — used for hero sections, callouts, and featured cards.
```css
.color-block-accent {
  background: #e6201c;
  color: #ffffff;
  border: 3px solid #000000;
  padding: 32px;
}
.color-block-accent--blue { background: #0048a3; }
.color-block-accent--yellow { background: #ffd500; color: #000000; }
```

### Black-Line Divider System
Thick black horizontal and vertical rules that serve as the primary structural element, replacing conventional whitespace gutters.
```css
.divider-h {
  width: 100%;
  height: 3px;
  background: #000000;
  border: none;
  margin: 0;
}
.divider-v {
  width: 3px;
  height: 100%;
  background: #000000;
  border: none;
  margin: 0;
}
```

## Iconography

Icons follow De Stijl's orthogonal discipline: linear treatment with strictly horizontal and vertical strokes where possible. The Lucide set is used for its clean geometry, rendered at 2px stroke weight to harmonize with the system's thick black lines.

- Treatment: linear
- Set: Lucide
- Stroke: 2px

## Do's & Don'ts

### Do
- Use only red (#e6201c), blue (#0048a3), yellow (#ffd500), black (#000000), and white (#ffffff)
- Build layouts as asymmetric rectangular grids divided by thick black lines
- Keep all corners at 0 radius — rectangles only
- Leave most of the canvas white; use color blocks sparingly for visual weight
- Use uppercase, geometric type for labels and captions

### Don't
- Use any color outside red/blue/yellow/black/white — no greys, no mixed hues, no shades
- Use curves, diagonals, or rounded corners — they violate Neoplasticism
- Apply gradients, shadows, or glows of any kind
- Use serif fonts or decorative typefaces
- Add ornamental elements, illustrations, or decorative flourishes

## Applications

De Stijl works best for art galleries, architecture portfolios, museum exhibitions, editorial layouts, and cultural institutions that want to signal rigorous modernist credibility. It is ideal for landing pages, posters, and dashboards where the grid itself is the hero — content lives inside the composition rather than floating on a generic surface. Not suited for data-dense applications or interfaces requiring extensive color-coding.
