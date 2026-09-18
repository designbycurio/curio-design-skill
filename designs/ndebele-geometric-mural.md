---
version: 1

meta:
  id: ndebele-geometric-mural
  name: Ndebele Geometric Mural
  description: "Mirror-symmetric saturated-color geometric panels on pitch-black ground, inspired by South African Ndebele house painting"
  isDark: true
  tags: [decorative, bold, historical, organic, experimental]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "19th century to present; global recognition from 1980s onwards via Esther Mahlangu"
  region: "Mpumalanga province, South Africa"
  regionZh: "南非姆普马兰加省"
  keyFigures: [Esther Mahlangu, Francina Ndimande]
  movements: [Ndebele traditional house painting, African contemporary art, BMW Art Car collaboration]

introduction: |
  Ndebele house painting is a 200-year-old South African design language in which women paint mirror-symmetric geometric murals on home exteriors. Pitch-black outlines define every shape; saturated emerald, cobalt, crimson, and citron blocks fill the panels with sovereign color.

  Esther Mahlangu brought this matrilineal art form to global consciousness through the 1991 BMW Art Car and exhibitions at Centre Pompidou and MoMA. This design system translates the Ndebele mural vocabulary into digital interfaces — rectilinear, flat, outlined, and rigorously symmetric.
introductionZh: |
  恩德贝勒壁画是南非延续两百年的女性艺术传统——妇女在自家外墙绘制镜像对称的几何壁画，以漆黑轮廓线界定每一个色块，用饱和的翠绿、钴蓝、深红与柠檬黄宣示身份与审美主权。

  1991 年，埃丝特·马赫兰古将这门代代相传的艺术带上了宝马 525i 艺术车，此后走进蓬皮杜中心与 MoMA。本设计系统将恩德贝勒壁画的视觉法则——直线、平涂、粗黑描边、严格对称——转译为数字界面语言。

colors:
  primary:
    "50": "#ECFDF5"
    "100": "#D1FAE5"
    "200": "#A7F3D0"
    "300": "#6EE7B7"
    "400": "#34D399"
    "500": "#10B981"
    "600": "#059669"
    "700": "#047857"
    "800": "#065F46"
    "900": "#064E3B"
    "950": "#022C22"
  secondary:
    "50": "#EFF6FF"
    "100": "#DBEAFE"
    "200": "#BFDBFE"
    "300": "#93C5FD"
    "400": "#60A5FA"
    "500": "#1E40AF"
    "600": "#1E3A8A"
    "700": "#1A3278"
    "800": "#162B65"
    "900": "#122353"
    "950": "#0B1530"
  accent:
    "50": "#FEF2F2"
    "100": "#FEE2E2"
    "200": "#FECACA"
    "300": "#FCA5A5"
    "400": "#F87171"
    "500": "#DC2626"
    "600": "#B91C1C"
    "700": "#991B1B"
    "800": "#7F1D1D"
    "900": "#671E1E"
    "950": "#450A0A"
  neutral:
    "50": "#FAFAFA"
    "100": "#F5F5F5"
    "200": "#E5E5E5"
    "300": "#D4D4D4"
    "400": "#A3A3A3"
    "500": "#737373"
    "600": "#525252"
    "700": "#404040"
    "800": "#262626"
    "900": "#171717"
    "950": "#0A0A0A"
  semantic:
    success: { bg: "#10B981", text: "#FFFFFF", light: "#065F46", border: "#059669" }
    warning: { bg: "#FCD34D", text: "#000000", light: "#78350F", border: "#F59E0B" }
    error:   { bg: "#DC2626", text: "#FFFFFF", light: "#7F1D1D", border: "#B91C1C" }
    info:    { bg: "#1E40AF", text: "#FFFFFF", light: "#162B65", border: "#1E3A8A" }
  background:
    page:    "#000000"
    surface: "#FFFFFF"
    subtle:  "#1A1A1A"
  text:
    primary:   "#FFFFFF"
    secondary: "#D4D4D4"
    muted:     "#737373"
    inverse:   "#000000"

typography:
  families:
    heading: "'Sora', 'Spartan', sans-serif"
    body:    "'Spartan', 'Public Sans', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=League+Spartan:wght@300;400;500;600;700;800&display=swap"
  scale:
    2xs: "0.625rem"
    xs: "0.75rem"
    sm: "0.875rem"
    base: "1rem"
    lg: "1.125rem"
    xl: "1.25rem"
    2xl: "1.5rem"
    3xl: "1.875rem"
    4xl: "2.25rem"
    5xl: "3rem"
    6xl: "4rem"
    7xl: "6rem"
  weights: { light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800 }
  lineHeights: { tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px",  md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "0", md: "0", lg: "0", xl: "0", full: "0" }
  color:  { default: "#000000", subtle: "#262626", strong: "#000000", focus: "#10B981" }
  width:  { thin: "1px", default: "3px", thick: "5px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  2xl: "none"
  inner: "none"
  focus: "0 0 0 3px rgba(16, 185, 129, 0.5)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [tint, opacity, stroke]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "strong"
  rhythm:        "8px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "outline"
  set:       "tabler"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "2px"

components:
  button:
    primary:   { background: "#10B981", color: "#FFFFFF", border: "3px solid #000000", shadow: "none", hoverBackground: "#059669", hoverShadow: "none", hoverColor: "#FFFFFF" }
    secondary: { background: "#1E40AF", color: "#FFFFFF", border: "3px solid #000000", shadow: "none", hoverBackground: "#1E3A8A", hoverShadow: "none", hoverColor: "#FFFFFF" }
    ghost:     { background: "transparent", color: "#FFFFFF", border: "3px solid #FFFFFF", shadow: "none", hoverBackground: "#FFFFFF", hoverShadow: "none", hoverColor: "#000000" }
    danger:    { background: "#DC2626", color: "#FFFFFF", border: "3px solid #000000", shadow: "none", hoverBackground: "#B91C1C", hoverShadow: "none", hoverColor: "#FFFFFF" }
    sizes:
      sm: { height: "36px", padding: "6px 16px", fontSize: "0.875rem" }
      md: { height: "44px", padding: "10px 24px", fontSize: "1rem" }
      lg: { height: "52px", padding: "14px 32px", fontSize: "1.125rem" }
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFFFFF"
    color: "#000000"
    border: "3px solid #000000"
    borderRadius: "0"
    padding: "10px 16px"
    focusBorder: "3px solid #10B981"
    placeholderColor: "#737373"
  card:
    base:  { background: "#FFFFFF", border: "3px solid #000000", borderRadius: "0", padding: "24px", shadow: "none" }
    hover: { shadow: "none", transform: "none" }
---

# Ndebele Geometric Mural

> Mirror-symmetric saturated-color geometric panels on pitch-black ground — a 200-year-old South African design language translated to digital interfaces.

## Origin

Ndebele house painting originated in the 19th century among the amaNdebele people of what is now Mpumalanga province, South Africa. Women developed a matrilineal tradition of painting bold geometric murals on home exteriors, using earth pigments and later commercial paints. Each composition encoded cultural identity, marital status, and aesthetic mastery. During colonial displacement, the painted house became an act of cultural resistance — declaring presence through color and geometry.

Esther Mahlangu (b. 1935) brought Ndebele art to global audiences when she painted BMW's 525i Art Car in 1991, the first African and first woman to receive the commission. Her work has since appeared at Centre Pompidou, MoMA, and the Virginia Museum of Fine Arts. Francina Ndimande and generations of unnamed women muralists maintained the tradition's rigorous visual grammar: pitch-black outlines defining every shape, saturated color blocks in emerald, cobalt, crimson, and citron, and mirror symmetry as inviolable law.

## Overview

Composition cues:
- **Layout**: Mirror-symmetric panel grid — rectangular blocks of saturated color arranged in bilateral symmetry, echoing the Ndebele wall-panel structure
- **Content width**: Container-width with strong internal grid divisions
- **Framing**: Heavy 3–5px black outlines on every element — the outline IS the brand
- **Grid intensity**: Strong — visible panel divisions with hard black borders throughout

## Colors

The Ndebele palette is culturally non-negotiable. Pitch black outlines define every shape. Saturated emerald, cobalt, crimson, and citron fill the panels. White appears only as content panels within the dark matrix — never as a page background. The palette comes directly from traditional mural pigments: the green of malachite, the blue of ultramarine, the red of iron oxide, the yellow of ochre, all amplified to maximum saturation in the modern commercial-paint era.

**Role usage**:
- Page background → `colors.background.page` (#000000 — the black ground of the mural)
- Content panels → `colors.background.surface` (#FFFFFF — white blocks within the grid)
- Primary actions / emerald blocks → `colors.primary.500`
- Secondary blocks → `colors.secondary.500`
- Accent / crimson blocks → `colors.accent.500`
- Highlight / citron blocks → semantic `warning.bg` (#FCD34D)
- All outlines and borders → `borders.color.default` (#000000)
- Body text on dark → `colors.text.primary` (#FFFFFF)

## Typography

Typography in the Ndebele system is architectural — block letters that belong inside the geometric panel grid. Sora provides the geometric sans-serif precision for headlines, with its optically balanced letterforms echoing the mathematical symmetry of Ndebele compositions. League Spartan carries the body text with the same geometric DNA. All caps is preferred for headlines, reinforcing the monumental, mural-scale presence.

**Text styles**:
- `display-xl` — Sora, 96px, weight 800, line-height 1.0, letter-spacing -0.04em, uppercase
- `display-lg` — Sora, 64px, weight 800, line-height 1.1, letter-spacing -0.02em, uppercase
- `heading-1` — Sora, 48px, weight 700, line-height 1.2, letter-spacing -0.02em, uppercase
- `body-lg` — League Spartan, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — League Spartan, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — League Spartan, 12px, weight 500, line-height 1.4, letter-spacing 0.05em, uppercase
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px (the Ndebele grid is built on bold, even divisions)
- Scale: 8 / 16 / 24 / 32 / 48 / 64 / 96 / 128px — large jumps reflect the mural's monumental scale
- Container max-width: 1280px
- Section padding: 64–128px vertical — generous breathing room between panel groups
- Grid gap: 0px between panels when emulating the mural wall (panels touch at their outlines), 16–24px for UI card grids

## Elevation & Depth

There is no elevation. Ndebele murals are painted flat on walls — no shadow, no depth, no gradient. Every element exists on a single plane. The visual hierarchy comes entirely from color saturation, outline weight, and panel size. This flatness is not a limitation but the aesthetic law: depth would betray the mural tradition.

- Surface style: flat — no box-shadow anywhere
- Blur: none
- Shadow ladder: all values are `none`
- Hierarchy is achieved through color weight, outline thickness, and scale

## Shapes

- All border radii: 0 — Ndebele geometry is rigorously rectilinear
- Buttons: sharp rectangles with 3px black outline
- Cards: sharp rectangles with 3px black outline
- Inputs: sharp rectangles with 3px black outline
- Occasional 45° diagonals for decorative chevrons and triangles (achieved via CSS clip-path, not border-radius)

## Motion

Motion is restrained and architectural. Ndebele murals are static by nature — painted walls do not move. Digital motion should feel like light shifting across a wall surface: subtle color transitions, not spatial displacement.

- Level: restrained
- Hover transitions: 250ms default easing
- Hover patterns: tint shift (emerald ↔ darker emerald), opacity fade, stroke-width pulse
- No lift, no scale, no bounce — movement contradicts the flat mural plane
- Reduced motion: fully supported, transitions collapse to instant

## Techniques

### Ndebele Panel Grid

A CSS grid that replicates the mirror-symmetric panel layout of a Ndebele house wall, with thick black outlines creating the characteristic compartmentalized structure.

```css
.ndebele-panel-grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto;
  gap: 0;
  border: 5px solid #000000;
  background: #000000;
}
.ndebele-panel-grid > * {
  border: 3px solid #000000;
  padding: 24px;
}
.ndebele-panel-grid > *:nth-child(odd) {
  background: #10B981;
  color: #FFFFFF;
}
.ndebele-panel-grid > *:nth-child(even) {
  background: #1E40AF;
  color: #FFFFFF;
}
```

### Chevron Divider

A decorative zigzag border inspired by the 45° diagonal chevron patterns found in Ndebele wall murals, built with repeating CSS gradients.

```css
.chevron-divider {
  height: 32px;
  background:
    linear-gradient(135deg, #DC2626 25%, transparent 25%) -16px 0,
    linear-gradient(225deg, #DC2626 25%, transparent 25%) -16px 0,
    linear-gradient(315deg, #FCD34D 25%, transparent 25%),
    linear-gradient(45deg,  #FCD34D 25%, transparent 25%);
  background-size: 32px 32px;
  background-color: #000000;
}
```

### Outlined Block Button

The signature Ndebele button treatment: saturated flat fill, heavy black outline, uppercase geometric text — a miniature mural panel rendered as an interactive element.

```css
.ndebele-button {
  display: inline-block;
  padding: 12px 32px;
  background: #10B981;
  color: #FFFFFF;
  border: 3px solid #000000;
  border-radius: 0;
  font-family: 'Sora', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
  transition: background 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.ndebele-button:hover {
  background: #059669;
}
```

## Iconography

Icons follow the Ndebele principle of bold outline and geometric simplicity. Tabler icons provide the right balance of geometric construction and clear stroke weight. Every icon should feel like it could be a small motif within a Ndebele mural panel.

- Treatment: outline only — filled icons contradict the outlined aesthetic
- Set: Tabler (geometric construction, consistent stroke)
- Stroke: 2px (echoing the bold outline language at icon scale)

## Do's & Don'ts

### ✓ Do
- Use 3–5px black outlines on every interactive element — the outline is the brand
- Maintain mirror symmetry in page layouts whenever possible
- Use saturated emerald, cobalt, crimson, and citron at full intensity
- Keep all surfaces flat — no shadows, no gradients, no glossy effects
- Use uppercase geometric sans-serif for headlines (Sora or Spartan)

### ✗ Don't
- Use curves or rounded corners — Ndebele is rectilinear with occasional 45° diagonals
- Use Inter, Geist, or SF Pro — use Sora or Spartan instead
- Use soft pastels or muted earth tones — saturated solids only
- Apply gradients or glossy effects — Ndebele is matte flat
- Use cream or beige backgrounds — the ground is black, panels are saturated
- Break mirror symmetry — bilateral symmetry is the core composition law
- Default to 9-grid SaaS layouts — Ndebele uses its own panel grid system

## Applications

This system is ideal for cultural institution websites, art exhibition landing pages, and portfolio sites that demand bold visual identity. It excels in editorial layouts where large color blocks and strong typographic hierarchy create immediate impact. The panel-grid structure also suits dashboard interfaces that need clear compartmentalization without relying on shadow-based card elevation.
