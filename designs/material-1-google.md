---
version: 1

meta:
  id: material-1-google
  name: Material Design 1.0
  description: "Google's 2014 paper-metaphor design system — flat surfaces with elevation, ink ripples, and bold color accents"
  isDark: false
  tags: [modernist, bold, professional]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Announced Google I/O June 2014; shipped Android 5.0 Lollipop November 2014; canonical through ~2018"
  region: "Mountain View, California"
  regionZh: "美国加利福尼亚州山景城"
  keyFigures: [Matias Duarte, Christian Robertson, Google Design team]
  movements: [Flat-with-depth design, Paper-metaphor UI, Design-system-as-product]

introduction: |
  Material Design 1.0 is Google's foundational design language, launched in 2014 to unify Android, web, and Chrome OS under a single coherent system. It introduced the "digital paper" metaphor — surfaces that stack with real elevation shadows, respond to touch with ink ripples, and obey consistent spatial rules on an 8dp grid.

  The system married flat aesthetics with physical depth: cards float above backgrounds, FABs anchor primary actions, and a strict primary-plus-accent color model keeps interfaces focused. Roboto, Christian Robertson's modernist sans-serif, provided the typographic backbone at every scale from 96px thin displays down to 12px captions.
introductionZh: |
  Material Design 1.0 是 Google 于 2014 年推出的基础设计语言，旨在以统一的视觉体系连接 Android、Web 和 Chrome OS。它创造性地提出"数字纸张"隐喻——界面元素如同不同层叠的纸面，通过真实的投影传达层级，通过墨水涟漪回应触摸交互，一切遵循 8dp 基线网格的空间秩序。

  这套体系将扁平美学与物理深度融为一体：卡片悬浮于背景之上，悬浮操作按钮（FAB）锚定核心操作，严格的主色加强调色模型让界面始终保持克制与聚焦。由 Christian Robertson 设计的现代无衬线字体 Roboto 贯穿从 96px 轻量标题到 12px 说明文字的全部层级。

colors:
  primary:
    "50": "#E3F2FD"
    "100": "#BBDEFB"
    "200": "#90CAF9"
    "300": "#64B5F6"
    "400": "#42A5F5"
    "500": "#2196F3"
    "600": "#1E88E5"
    "700": "#1976D2"
    "800": "#1565C0"
    "900": "#0D47A1"
    "950": "#0A3A84"
  secondary:
    "50": "#ECEFF1"
    "100": "#CFD8DC"
    "200": "#B0BEC5"
    "300": "#90A4AE"
    "400": "#78909C"
    "500": "#607D8B"
    "600": "#546E7A"
    "700": "#455A64"
    "800": "#37474F"
    "900": "#263238"
    "950": "#1C272C"
  accent:
    "50": "#FCE4EC"
    "100": "#F8BBD0"
    "200": "#F48FB1"
    "300": "#F06292"
    "400": "#EC407A"
    "500": "#FF4081"
    "600": "#F50057"
    "700": "#C51162"
    "800": "#AD1457"
    "900": "#880E4F"
    "950": "#6D0B3F"
  neutral:
    "50": "#FAFAFA"
    "100": "#F5F5F5"
    "200": "#EEEEEE"
    "300": "#E0E0E0"
    "400": "#BDBDBD"
    "500": "#9E9E9E"
    "600": "#757575"
    "700": "#616161"
    "800": "#424242"
    "900": "#212121"
    "950": "#121212"
  semantic:
    success: { bg: "#4CAF50", text: "#FFFFFF", light: "#E8F5E9", border: "#388E3C" }
    warning: { bg: "#FF9800", text: "#FFFFFF", light: "#FFF3E0", border: "#F57C00" }
    error:   { bg: "#F44336", text: "#FFFFFF", light: "#FFEBEE", border: "#D32F2F" }
    info:    { bg: "#2196F3", text: "#FFFFFF", light: "#E3F2FD", border: "#1976D2" }
  background:
    page:    "#FAFAFA"
    surface: "#FFFFFF"
    subtle:  "#F5F5F5"
  text:
    primary:   "#212121"
    secondary: "#424242"
    muted:     "#757575"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    body:    "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    mono:    "'Roboto Mono', 'Consolas', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700&family=Roboto+Mono:wght@400;500&display=swap"
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
  lineHeights: { tight: 1.2, snug: 1.375, normal: 1.4, relaxed: 1.625, loose: 1.8 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.01em", normal: "0", wide: "0.05em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px",  md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "2px", md: "4px", lg: "6px", xl: "8px", full: "9999px" }
  color:  { default: "#E0E0E0", subtle: "#EEEEEE", strong: "#BDBDBD", focus: "#2196F3" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)"
  sm: "0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)"
  md: "0 4px 5px rgba(0,0,0,0.14), 0 1px 10px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.20)"
  lg: "0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)"
  xl: "0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)"
  "2xl": "0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.04)"
  focus: "0 0 0 3px rgba(33,150,243,0.35)"

motion:
  level: "lively"
  durations: { instant: "0ms", fast: "100ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.175, 0.885, 0.32, 1.275)"
  hoverPatterns: [lift, tint, scale]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "solid"
  gridIntensity: "strong"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "none"

iconography:
  treatment: "filled"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:   { background: "#2196F3", color: "#FFFFFF", border: "none", shadow: "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)", hoverBackground: "#1E88E5", hoverShadow: "0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)", hoverColor: "#FFFFFF" }
    secondary: { background: "transparent", color: "#2196F3", border: "1px solid #2196F3", shadow: "none", hoverBackground: "rgba(33,150,243,0.08)", hoverShadow: "none", hoverColor: "#1976D2" }
    ghost:     { background: "transparent", color: "#757575", border: "none", shadow: "none", hoverBackground: "rgba(0,0,0,0.04)", hoverShadow: "none", hoverColor: "#212121" }
    danger:    { background: "#F44336", color: "#FFFFFF", border: "none", shadow: "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)", hoverBackground: "#D32F2F", hoverShadow: "0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)", hoverColor: "#FFFFFF" }
    sizes:     { sm: { height: "32px", padding: "0 12px", fontSize: "0.8125rem" }, md: { height: "36px", padding: "0 16px", fontSize: "0.875rem" }, lg: { height: "48px", padding: "0 24px", fontSize: "1rem" } }
    borderRadius: "4px"
    fontWeight: 500
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "transparent"
    color: "#212121"
    border: "none"
    borderRadius: "0"
    padding: "8px 0"
    focusBorder: "2px solid #2196F3"
    placeholderColor: "#9E9E9E"
  card:
    base:  { background: "#FFFFFF", border: "none", borderRadius: "2px", padding: "16px", shadow: "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)" }
    hover: { shadow: "0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)", transform: "translateY(-1px)" }
---

# Material Design 1.0

> Flat surfaces with physics — Google's digital-paper design language that gave depth to flat design through elevation shadows, ink ripples, and bold primary-accent color.

## Origin

Material Design 1.0 was unveiled by Matias Duarte at Google I/O in June 2014 and shipped with Android 5.0 Lollipop that November. Born from a desire to unify Google's fragmented platform UI — post-Holo Android, Chrome OS, and the web — into a single coherent system, Material introduced the metaphor of "digital paper": weightless surfaces that could split, join, stack, and cast shadows according to real-world physics. It was Google's answer to Apple's iOS 7 flat revolution, accepting the premise of flatness but restoring spatial hierarchy through elevation.

The spec, published at material.io, became the first design system distributed as both guidelines and a component library, making "design-system-as-product" a category. Christian Robertson refined Roboto into a versatile modernist sans that anchored the entire typographic system. Inbox by Gmail (2014) and the Android 5.0 system UI became the canonical reference implementations. Material 1 defined Android's visual identity through 2018, until Material 2 and later Material You (M3) evolved the language further.

## Overview
Composition cues:
- **Layout**: Grid-based, 8dp baseline grid aligning all elements
- **Content width**: Container (max ~1280px), responsive columns
- **Framing**: Solid paper surfaces with elevation-based layering
- **Grid intensity**: Strong — every element snaps to the 8dp grid

## Colors
Material 1's color philosophy is disciplined restraint with bold punctuation. The system mandates exactly two chromatic roles: a primary color (applied to app bars, large surfaces) and an accent color (applied to FABs, toggles, highlights). Everything else is neutral. The 2014 palette specifies 19 hues each with 14 shades (50–900 plus A100–A700 accent variants), but any given app uses only one primary hue and one accent hue. White `#FFFFFF` surfaces float above the paper-white `#FAFAFA` background; depth comes from shadows, not color variation.

**Role usage**:
- Page background → `colors.background.page` (#FAFAFA)
- Card / surface → `colors.background.surface` (#FFFFFF)
- App bar / toolbar → `colors.primary.500` (#2196F3)
- Status bar → `colors.primary.700` (#1976D2)
- FAB / accent toggle → `colors.accent.500` (#FF4081)
- Body text → `colors.text.primary` (#212121)
- Secondary text → `colors.text.muted` (#757575)
- Dividers → `colors.neutral.300` (#E0E0E0)

## Typography
Roboto is Material 1's sole typeface — a modernist geometric sans-serif designed by Christian Robertson and refined for the Material spec in 2014. Display headlines use light weight (300) at large sizes to achieve an airy, editorial quality. Body text sits at 14–16px with a 1.4 line-height for comfortable reading density. Button labels are always medium weight (500), uppercased with wide letter-spacing — a distinctive Material 1 signature.

**Text styles**:
- `display-xl` — Roboto, 96px, weight 300, line-height 1.0, letter-spacing -0.01em
- `display-lg` — Roboto, 60px, weight 300, line-height 1.1, letter-spacing -0.01em
- `heading-1` — Roboto, 34px, weight 400, line-height 1.2, letter-spacing 0
- `heading-2` — Roboto, 24px, weight 400, line-height 1.3, letter-spacing 0
- `body-lg` — Roboto, 16px, weight 400, line-height 1.4, letter-spacing 0
- `body-md` — Roboto, 14px, weight 400, line-height 1.4, letter-spacing 0
- `caption` — Roboto, 12px, weight 400, line-height 1.33, letter-spacing 0.03em
- `mono-md` — Roboto Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 8dp (all spacing, sizing, and positioning snap to 8dp multiples)
- Scale: 4, 8, 16, 24, 32, 48, 64, 96, 128px
- Touch targets: minimum 48×48dp
- Container max-width: 1280px centered
- Section padding: 64–96px vertical, 16–24px horizontal gutter
- Card internal padding: 16px (dense) to 24px (comfortable)

## Elevation & Depth
Material 1's defining innovation: depth without texture. Surfaces are infinitely thin sheets of "digital paper" stacked along the z-axis. Each elevation level (measured in dp) casts a proportionally larger shadow. There are six canonical elevation levels — 1dp (cards at rest), 2dp (raised buttons), 4dp (app bar), 8dp (menu/picker), 16dp (nav drawer), 24dp (dialog). The shadow is the only visual cue for depth; surfaces themselves are pure flat color.

- Surface: pure white `#FFFFFF`, no gradients, no texture
- Blur: none — Material 1 shadows are crisp, not diffused
- Shadow 1dp: `0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)`
- Shadow 4dp: `0 4px 5px rgba(0,0,0,0.14), 0 1px 10px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.20)`
- Shadow 8dp: `0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)`
- Shadow 16dp: `0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)`
- Shadow 24dp: `0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)`

## Shapes
- Card border-radius: 2px (barely rounded — the Material 1 signature)
- Button border-radius: 4px
- FAB border-radius: 50% (circular, 56px diameter)
- Dialog border-radius: 4px
- Maximum radius for rectangular elements: 8px (anything rounder is Material 3 territory)

## Motion
Material 1 treats motion as a core design element, not decoration. Every animation must be intentional and physics-informed — elements accelerate and decelerate along natural curves, never teleport. The system favors "standard curve" (`cubic-bezier(0.4, 0, 0.2, 1)`) for most transitions, "deceleration curve" for entering elements, and "acceleration curve" for exiting elements. Ink ripples — concentric circles radiating from the touch point — are the signature interaction feedback.

- Level: lively
- Standard curve: `cubic-bezier(0.4, 0, 0.2, 1)` — 250ms default
- Deceleration (enter): `cubic-bezier(0, 0, 0.2, 1)` — 250ms
- Acceleration (exit): `cubic-bezier(0.4, 0, 1, 1)` — 200ms
- Ink ripple: 300ms radial expand from touch point
- Hover patterns: lift (increase elevation shadow), tint (overlay 4% primary), scale (1.02)
- Reduced motion: honor `prefers-reduced-motion` — collapse to opacity fade

## Techniques

### Ink Ripple Touch Feedback
Concentric circle expanding from touch/click point with primary-color fill at low opacity — the signature Material 1 interaction pattern.
```css
.ripple-container {
  position: relative;
  overflow: hidden;
}
.ripple-container::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(33, 150, 243, 0.25);
  transform: translate(-50%, -50%);
  transition: width 0.4s cubic-bezier(0, 0, 0.2, 1),
              height 0.4s cubic-bezier(0, 0, 0.2, 1),
              opacity 0.4s ease-out;
  opacity: 0;
}
.ripple-container:active::after {
  width: 300px;
  height: 300px;
  opacity: 1;
}
```

### Elevation Lift on Hover
Cards and buttons increase their elevation shadow on hover/focus, creating a "picking up" effect that reinforces the paper metaphor.
```css
.material-card {
  background: #FFFFFF;
  border-radius: 2px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.material-card:hover {
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  transform: translateY(-2px);
}
```

### Underline Input Focus Transition
Material 1 text inputs use a bottom-border-only style. On focus, a primary-colored line scales from center outward — a distinctive animation that avoids the "box input" pattern entirely.
```css
.material-input {
  border: none;
  border-bottom: 1px solid #9E9E9E;
  background: transparent;
  padding: 8px 0;
  font-size: 16px;
  color: #212121;
  outline: none;
  position: relative;
}
.material-input-wrapper::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: #2196F3;
  transition: width 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              left 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.material-input:focus ~ .material-input-wrapper::after,
.material-input-wrapper:focus-within::after {
  width: 100%;
  left: 0;
}
```

## Iconography
Material 1 uses filled iconography — solid shapes that read clearly at small sizes and align with the system's emphasis on bold, confident surfaces. Icons sit on the 24dp grid with 2dp internal padding, maintaining consistent optical weight across the set.

- Treatment: filled (solid shapes, not outlines)
- Set: Material Icons (Google's canonical set; Lucide as open-source alternative)
- Stroke: N/A for filled; 1.5px if using outline variants

## Do's & Don'ts

### Do
- Use Material blue `#2196F3` for primary actions and app bar backgrounds
- Use exactly one accent color (`#FF4081`) for FABs, toggles, and highlights
- Keep display headlines at light weight (300) for the characteristic airy feel
- Uppercase button labels with medium weight (500) and wide letter-spacing
- Use elevation shadows as the primary mechanism for visual hierarchy

### Don't
- Use border-radius greater than 8px on rectangular elements (sharp corners define Material 1; rounded is M3 territory)
- Apply skeuomorphic textures, gradients, or ornamental surfaces
- Use bold or extra-bold weights for display-level headings (Material 1 display is thin/light)
- Introduce multiple chromatic surfaces — stick to one primary plus one accent only
- Apply translucent blur or frosted-glass effects (that's iOS territory, not Material)

## Applications
Material Design 1.0 is ideal for productivity apps, dashboards, admin panels, and any interface where information density and clear hierarchy matter. Its strict elevation system and grid discipline make it especially effective for data-heavy interfaces — email clients, project managers, CRMs — where users need to quickly scan and act on structured content. The system also works well for Android-first products wanting visual consistency with the platform's native design language.
