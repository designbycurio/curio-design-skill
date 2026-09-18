---
version: 1

meta:
  id: google-material-3
  name: "Google Material 3 Expressive"
  description: "Friendly, color-adaptive design language built on dynamic theming, generous radii, and tonal surface hierarchy"
  isDark: false
  tags: [modernist, playful, friendly]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2014 (Material 1.0); 2021 (Material You / M3); 2024 (M3 Expressive)"
  region: "Mountain View, California"
  regionZh: "美国加利福尼亚州山景城"
  keyFigures: ["Matias Duarte", "Material Design team"]
  movements: ["Material Design", "Dynamic theming", "Android visual identity"]

introduction: |
  Material 3 Expressive is Google's most personal design language yet. Born from Material Design's original paper-and-ink metaphor, it evolved through Material You's dynamic color theming into a system that generates entire palettes from a user's wallpaper, making every device feel uniquely owned.

  The 2024 Expressive update pushed further — larger radii, emotive shape variation, and tonal color surfaces that shift warmth and depth without hard borders. It is geometric yet friendly, systematic yet playful, a living system designed to adapt.
introductionZh: |
  Material 3 Expressive 是 Google 迄今最具个性化的设计语言。它从最初以纸墨为隐喻的 Material Design 出发，经由 Material You 的动态取色机制演化为一套能从用户壁纸自动生成完整配色方案的系统，让每台设备都拥有独一无二的视觉个性。

  2024 年的 Expressive 更新将这一理念推向新高度——更大的圆角、富有表现力的形状变化、以色调递进取代硬边界的表面层级体系。它既几何又亲和，既系统化又充满趣味，是一套为适应而生的活的设计系统。

colors:
  primary:
    "50": "#F6EDFF"
    "100": "#EADDFF"
    "200": "#D0BCFF"
    "300": "#B69DF8"
    "400": "#9A82DB"
    "500": "#6750A4"
    "600": "#5B4497"
    "700": "#4F378B"
    "800": "#381E72"
    "900": "#21005D"
    "950": "#14003D"
  secondary:
    "50": "#F6F0F7"
    "100": "#E8DEF8"
    "200": "#C9C0D3"
    "300": "#AEA5BA"
    "400": "#938A9E"
    "500": "#625B71"
    "600": "#564F65"
    "700": "#4A4458"
    "800": "#332D41"
    "900": "#1D192B"
    "950": "#0F0D15"
  accent:
    "50": "#FFF0F3"
    "100": "#FFD8E4"
    "200": "#EFB8C8"
    "300": "#D29DAC"
    "400": "#B58392"
    "500": "#7D5260"
    "600": "#704656"
    "700": "#633B4C"
    "800": "#492532"
    "900": "#31111D"
    "950": "#1E0A12"
  neutral:
    "50": "#FDF8FD"
    "100": "#F5EFF4"
    "200": "#E7E0EC"
    "300": "#CAC4D0"
    "400": "#AEA8B4"
    "500": "#938F99"
    "600": "#79747E"
    "700": "#605D66"
    "800": "#49454F"
    "900": "#322F35"
    "950": "#1D1B20"
  semantic:
    success: { bg: "#1B6E2D", text: "#FFFFFF", light: "#C4EED0", border: "#1B6E2D" }
    warning: { bg: "#7C5800", text: "#FFFFFF", light: "#FFDEA8", border: "#7C5800" }
    error:   { bg: "#B3261E", text: "#FFFFFF", light: "#F9DEDC", border: "#B3261E" }
    info:    { bg: "#6750A4", text: "#FFFFFF", light: "#EADDFF", border: "#6750A4" }
  background:
    page:    "#FFFBFE"
    surface: "#FFFFFF"
    subtle:  "#FEF7FF"
  text:
    primary:   "#1D1B20"
    secondary: "#49454F"
    muted:     "#79747E"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Roboto Flex', 'Roboto', sans-serif"
    body:    "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    mono:    "'Roboto Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Roboto+Flex:wght@300..800&family=Roboto+Mono:wght@400;500&display=swap"
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
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:
    sm: "640px"
    md: "768px"
    lg: "1024px"
    xl: "1280px"
    full: "100%"
  gridGap:
    sm: "8px"
    md: "16px"
    lg: "24px"
    xl: "48px"
  sectionPadding:
    sm: "32px"
    md: "64px"
    lg: "96px"
    xl: "128px"

borders:
  radius:
    none: "0"
    sm: "8px"
    md: "12px"
    lg: "16px"
    xl: "28px"
    full: "9999px"
  color:
    default: "#CAC4D0"
    subtle: "#E7E0EC"
    strong: "#79747E"
    focus: "#6750A4"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.10)"
  sm: "0 1px 3px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.06)"
  md: "0 2px 6px rgba(0,0,0,0.10), 0 4px 12px rgba(0,0,0,0.08)"
  lg: "0 4px 8px rgba(0,0,0,0.10), 0 8px 16px rgba(0,0,0,0.08)"
  xl: "0 6px 12px rgba(0,0,0,0.12), 0 12px 24px rgba(0,0,0,0.10)"
  "2xl": "0 8px 24px rgba(0,0,0,0.14), 0 16px 48px rgba(0,0,0,0.12)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.04)"
  focus: "0 0 0 3px rgba(103,80,164,0.38)"

motion:
  level: "lively"
  durations:
    instant: "0ms"
    fast: "100ms"
    normal: "250ms"
    slow: "400ms"
    slower: "600ms"
  easings:
    default: "cubic-bezier(0.2, 0, 0, 1)"
    in:      "cubic-bezier(0.3, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0, 1)"
    spring:  "cubic-bezier(0.3, 1.4, 0.5, 1)"
  hoverPatterns: [lift, tint, scale]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "solid"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "filled"
  set: "custom"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "0"

components:
  button:
    primary:
      background: "#6750A4"
      color: "#FFFFFF"
      border: "none"
      shadow: "none"
      hoverBackground: "#5B4497"
      hoverShadow: "0 1px 3px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.06)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "#E8DEF8"
      color: "#1D192B"
      border: "none"
      shadow: "none"
      hoverBackground: "#D0BCFF"
      hoverShadow: "none"
      hoverColor: "#1D192B"
    ghost:
      background: "transparent"
      color: "#6750A4"
      border: "none"
      shadow: "none"
      hoverBackground: "rgba(103,80,164,0.08)"
      hoverShadow: "none"
      hoverColor: "#6750A4"
    danger:
      background: "#B3261E"
      color: "#FFFFFF"
      border: "none"
      shadow: "none"
      hoverBackground: "#8C1D18"
      hoverShadow: "none"
      hoverColor: "#FFFFFF"
    sizes:
      sm: { height: "32px", padding: "0 16px", fontSize: "0.75rem" }
      md: { height: "40px", padding: "0 24px", fontSize: "0.875rem" }
      lg: { height: "56px", padding: "0 32px", fontSize: "1rem" }
    borderRadius: "9999px"
    fontWeight: 500
    letterSpacing: "0.01em"
    textTransform: "none"
  input:
    background: "#E7E0EC"
    color: "#1D1B20"
    border: "none"
    borderRadius: "4px 4px 0 0"
    padding: "16px"
    focusBorder: "2px solid #6750A4"
    placeholderColor: "#79747E"
  card:
    base:
      background: "#FFFFFF"
      border: "none"
      borderRadius: "16px"
      padding: "16px"
      shadow: "0 1px 2px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.10)"
    hover:
      shadow: "0 2px 6px rgba(0,0,0,0.10), 0 4px 12px rgba(0,0,0,0.08)"
      transform: "translateY(-2px)"
---

# Google Material 3 Expressive

> A friendly, color-adaptive design language where dynamic theming, generous radii, and tonal surfaces make every interface feel personal.

## Origin

Material Design launched at Google I/O 2014 as a physics-inspired system of paper sheets and ink, pioneered by VP of Design Matias Duarte. It gave Android a unified visual language grounded in elevation, motion, and bold color. By 2021, Material You (M3) introduced dynamic color — an algorithm that extracts a complete palette from the user's wallpaper, making every Pixel device visually unique.

The 2024 "Material 3 Expressive" update pushed the system further. Larger card radii, emotive shape variation, and tonal surface layering replaced hard-edged containers. Google shipped these patterns across Android 14's system UI and its entire Workspace suite — Gmail, Calendar, Drive — creating a warm, geometric, slightly chunky visual identity that adapts to every user while remaining unmistakably Google.

## Overview
Composition cues:
- **Layout**: grid-based with responsive columns, flex for inline components
- **Content width**: container (1024–1280px), responsive breakpoints
- **Framing**: solid tonal surfaces with layered elevation — no glassy effects
- **Grid intensity**: soft — visible structure without heavy gridlines

## Colors
Material 3's color philosophy centers on dynamic theming: a single seed color generates an entire tonal palette across primary, secondary, tertiary, neutral, and error roles. The default M3 palette uses a lavender primary (#6750A4), mauve-grey secondary (#625B71), and rose tertiary (#7D5260) on a warm white background (#FFFBFE). Surfaces use tonal variants of the primary — lighter shades for containers, darker for emphasis — creating depth through color, not hard borders.

**Role usage**:
- Page background -> `colors.background.page` (#FFFBFE warm white)
- Card / surface container -> `colors.background.surface` (#FFFFFF)
- Subtle tonal fill -> `colors.background.subtle` (#FEF7FF)
- Primary action buttons -> `colors.primary.500` (#6750A4 lavender)
- Tonal button fills -> `colors.primary.100` (#EADDFF)
- Body text -> `colors.text.primary` (#1D1B20)
- Secondary text -> `colors.text.secondary` (#49454F)
- Muted / caption text -> `colors.text.muted` (#79747E)

## Typography
Roboto Flex serves as the display and heading typeface, leveraging its variable weight axis (300–800) for smooth typographic hierarchy. Roboto handles body text with its clean, mechanical humanist forms. Headings sit at medium weight (500–600), never heavy-bold — the system relies on size and spacing for hierarchy rather than extreme weight contrast. Letter-spacing is neutral (0em) for headings and slightly positive for buttons.

**Text styles**:
- `display-xl` — Roboto Flex, 96px, weight 400, line-height 1.0, letter-spacing 0
- `display-lg` — Roboto Flex, 57px, weight 400, line-height 1.12, letter-spacing -0.02em
- `heading-1` — Roboto Flex, 36px, weight 500, line-height 1.2, letter-spacing 0
- `heading-2` — Roboto Flex, 28px, weight 500, line-height 1.3, letter-spacing 0
- `body-lg` — Roboto, 18px, weight 400, line-height 1.5, letter-spacing 0.01em
- `body-md` — Roboto, 16px, weight 400, line-height 1.5, letter-spacing 0.03em
- `caption` — Roboto, 12px, weight 400, line-height 1.33, letter-spacing 0.04em
- `mono-md` — Roboto Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 8px (all spacing derives from 8px increments)
- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px
- Container max-width: 1280px centered
- Section padding: 64px vertical (desktop), 32px (mobile)
- Card internal padding: 16px
- Grid gap: 16px default, 24px for card grids

## Elevation & Depth
Material 3 replaces hard drop shadows with a tonal surface system. Elevation is communicated through tonal overlay — higher surfaces receive a lighter tint of the primary color — combined with minimal shadow for physical grounding. The result is a layered feel without heavy darkness.

- Surface level 0: #FFFBFE (page), no shadow
- Surface level 1: #F6EDFF (primary-tinted), shadow xs
- Surface level 2: #EADDFF (stronger tint), shadow sm
- Surface level 3: #D0BCFF, shadow md
- Shadow ladder: xs (1dp) -> sm (3dp) -> md (6dp) -> lg (8dp) -> xl (12dp)
- No blur-based glass effects — tonal shifts only

## Shapes
- Buttons: full pill radius (9999px)
- Cards: 16px radius (generous, signature M3)
- Dialogs / sheets: 28px radius (extra-large M3)
- Chips: 8px radius
- Inputs (filled): 4px top corners, 0 bottom (underline style)
- FAB: 16px radius (or full pill for extended FAB)

## Motion
Material 3 motion is lively and purposeful, using Google's emphasized easing curves. Elements enter with deceleration and exit with acceleration. Transitions feel springy but controlled — never bouncy or cartoonish. The system favors container transform patterns where one element morphs into another rather than simple fades.

- Level: lively
- Fast: 100ms (ripple, icon swap)
- Normal: 250ms (button state, card hover)
- Slow: 400ms (page transition, container transform)
- Slower: 600ms (shared-axis navigation)
- Default easing: cubic-bezier(0.2, 0, 0, 1) — M3 emphasized decelerate
- Enter: cubic-bezier(0, 0, 0, 1) — decelerate
- Exit: cubic-bezier(0.3, 0, 1, 1) — accelerate
- Hover patterns: lift (translateY -2px), tint (primary overlay 8%), scale (1.02)
- Reduced motion: durations collapse to 0ms, transforms removed

## Techniques

### Tonal Surface Elevation
Surfaces gain elevation through primary-tinted overlays rather than dark shadows, creating depth with color warmth.
```css
.surface-level-1 {
  background: color-mix(in srgb, #6750A4 5%, #FFFBFE);
  box-shadow: 0 1px 2px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.10);
}
.surface-level-2 {
  background: color-mix(in srgb, #6750A4 8%, #FFFBFE);
  box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.06);
}
.surface-level-3 {
  background: color-mix(in srgb, #6750A4 11%, #FFFBFE);
  box-shadow: 0 2px 6px rgba(0,0,0,0.10), 0 4px 12px rgba(0,0,0,0.08);
}
```

### Material Ripple Effect
Touch feedback radiates from the point of contact — a concentric circle of tinted primary that expands and fades.
```css
.ripple {
  position: relative;
  overflow: hidden;
}
.ripple::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at var(--ripple-x, 50%) var(--ripple-y, 50%), rgba(103,80,164,0.16) 0%, transparent 60%);
  opacity: 0;
  transform: scale(0);
  transition: opacity 100ms ease-out, transform 400ms cubic-bezier(0.2, 0, 0, 1);
}
.ripple:active::after {
  opacity: 1;
  transform: scale(2.5);
}
```

### Filled Tonal Button
The signature M3 button style: primary-tinted background with on-primary-container text, pill-shaped with no border.
```css
.btn-tonal {
  background: #E8DEF8;
  color: #1D192B;
  border: none;
  border-radius: 9999px;
  padding: 0 24px;
  height: 40px;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  letter-spacing: 0.01em;
  cursor: pointer;
  transition: background 250ms cubic-bezier(0.2, 0, 0, 1),
              box-shadow 250ms cubic-bezier(0.2, 0, 0, 1);
}
.btn-tonal:hover {
  background: #D0BCFF;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.06);
}
```

## Iconography
Material 3 uses filled icon variants by default — Google's Material Symbols set with optical size adjustments at 20dp and 24dp. Icons are optically balanced to align with Roboto's geometry. The filled treatment gives icons a friendly, solid presence that matches M3's tonal surface philosophy.

- Treatment: filled (Material Symbols Rounded, filled variant)
- Set: custom (Material Symbols via Google Fonts)
- Stroke: 0 (filled icons; outline variant uses grade -25)

## Do's & Don'ts

### Do
- Use generous corner radii (16px+ for cards, pill for buttons) to maintain the M3 personality
- Build depth through tonal color shifts, not heavy shadows
- Let the primary lavender (#6750A4) anchor key actions and focus states
- Use Roboto Flex at medium weight (500) for headings — avoid heavy bold
- Apply 8px-increment spacing for consistent rhythm across layouts

### Don't
- Use sharp 0-radius rectangles — M3 is generously rounded everywhere
- Apply brutalist anti-design patterns — M3 is friendly and approachable
- Default to cold corporate blue — M3's canonical primary is warm lavender
- Use heavy serif typography — the system is built around Roboto's geometric clarity
- Design for dark mode in this specimen — light is the canonical M3 Expressive mode

## Applications
Material 3 Expressive is ideal for productivity tools, mobile-first web apps, and dashboard interfaces that need a warm, approachable feel. Its tonal surface system and dynamic color architecture make it especially well-suited for consumer-facing products — task managers, reading apps, social platforms — where personalization and friendliness outweigh editorial formality. The generous radii and pill-shaped CTAs give any interface instant Material personality.
