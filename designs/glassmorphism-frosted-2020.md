---
version: 1

meta:
  id: glassmorphism-frosted-2020
  name: "Glassmorphism"
  description: "Frosted-glass UI: translucent white panels with heavy backdrop-blur floating over a saturated violet-to-magenta-to-blue gradient field"
  isDark: true
  tags: [tech, futuristic, modernist, experimental, bold]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2020 onward (term coined 2020 alongside macOS Big Sur); roots in 2010s translucency"
  region: "Global / internet"
  regionZh: "全球 / 互联网"
  keyFigures: ["Michał Malewicz", "Apple (macOS Big Sur team)"]
  movements: ["Frosted-glass UI", "Neo-translucency", "Post-flat depth"]

introduction: |
  Glassmorphism is the frosted-glass interface language popularized by macOS Big Sur and named in 2020 by designer Michał Malewicz. Its essence is translucency: panels of light-tinted glass, edged with thin luminous borders and heavy backdrop-blur, hover over a saturated gradient field.

  The ground is deep violet — never cream, never white, never neutral black — because the glass needs something colorful behind it to blur. Vivid blobs of magenta and electric blue bleed through the frost, creating layered depth where every surface feels lit from within.
introductionZh: |
  玻璃拟态（Glassmorphism）是随 macOS Big Sur 走红的「磨砂玻璃」界面语言，由设计师米哈尔·马莱维奇于 2020 年正式命名。它的灵魂在于半透明：浅色玻璃面板配上极细的发光描边与厚重的背景模糊，悬浮于饱和的渐变色场之上。

  底色必须是深紫色——绝不用米白、纯白或中性黑——因为玻璃需要背后有鲜艳的色彩可供模糊。品红与电光蓝的色块从磨砂层后透出，营造层层叠叠的纵深感，让每一个表面都仿佛自内部发光。

colors:
  primary:
    "50": "#EEEBFE"
    "100": "#DDD8FD"
    "200": "#C0B8FB"
    "300": "#A399F9"
    "400": "#8F82F8"
    "500": "#7B6CF6"
    "600": "#5B4AE3"
    "700": "#4636C4"
    "800": "#362A99"
    "900": "#28206F"
    "950": "#1A1547"
  secondary:
    "50": "#F8ECF3"
    "100": "#F0D6E6"
    "200": "#E2AECC"
    "300": "#D885A5"
    "400": "#D76D77"
    "500": "#C24F60"
    "600": "#A33C4E"
    "700": "#7E2E3D"
    "800": "#5C2A86"
    "900": "#5B2A86"
    "950": "#3A1C71"
  accent:
    "50": "#E5F6FF"
    "100": "#CCEDFF"
    "200": "#99DBFF"
    "300": "#66C9FF"
    "400": "#2CA8FF"
    "500": "#00C2FF"
    "600": "#009BD6"
    "700": "#0079A8"
    "800": "#005C80"
    "900": "#00425C"
    "950": "#002A3B"
  neutral:
    "50": "#F7F6FB"
    "100": "#ECEAF4"
    "200": "#D6D2E6"
    "300": "#B4AECC"
    "400": "#8C85A8"
    "500": "#6A6386"
    "600": "#514B68"
    "700": "#3E3950"
    "800": "#2C283A"
    "900": "#1E1B2C"
    "950": "#13111D"
  semantic:
    success: { bg: "#10B981", text: "#ECFDF5", light: "rgba(16, 185, 129, 0.18)", border: "rgba(110, 231, 183, 0.4)" }
    warning: { bg: "#F59E0B", text: "#FFFBEB", light: "rgba(245, 158, 11, 0.18)", border: "rgba(253, 224, 71, 0.4)" }
    error:   { bg: "#F43F5E", text: "#FFF1F2", light: "rgba(244, 63, 94, 0.18)", border: "rgba(253, 164, 175, 0.4)" }
    info:    { bg: "#00C2FF", text: "#ECFAFF", light: "rgba(0, 194, 255, 0.18)", border: "rgba(125, 211, 252, 0.4)" }
  background:
    page: "#3A1C71"
    surface: "rgba(255, 255, 255, 0.15)"
    subtle: "rgba(255, 255, 255, 0.08)"
  text:
    primary: "#FFFFFF"
    secondary: "rgba(255, 255, 255, 0.78)"
    muted: "rgba(255, 255, 255, 0.55)"
    inverse: "#28206F"

typography:
  families:
    heading: "'Poppins', 'SF Pro Display', 'Inter', system-ui, sans-serif"
    body: "'Inter', 'SF Pro Display', 'Poppins', system-ui, sans-serif"
    mono: "'JetBrains Mono', 'SF Mono', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Poppins:wght@300;400;500;600;700;800&display=swap"
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
    md: "16px"
    lg: "24px"
    xl: "32px"
    full: "9999px"
  color:
    default: "rgba(255, 255, 255, 0.3)"
    subtle: "rgba(255, 255, 255, 0.15)"
    strong: "rgba(255, 255, 255, 0.5)"
    focus: "#7B6CF6"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(20, 8, 50, 0.18)"
  sm: "0 2px 8px rgba(20, 8, 50, 0.22)"
  md: "0 8px 24px rgba(20, 8, 50, 0.28)"
  lg: "0 16px 40px rgba(20, 8, 50, 0.34)"
  xl: "0 24px 60px rgba(20, 8, 50, 0.40)"
  "2xl": "0 32px 80px rgba(20, 8, 50, 0.48)"
  inner: "inset 0 1px 1px rgba(255, 255, 255, 0.25)"
  focus: "0 0 0 3px rgba(123, 108, 246, 0.45)"

motion:
  level: "lively"
  durations:
    instant: "0ms"
    fast: "120ms"
    normal: "250ms"
    slow: "400ms"
    slower: "600ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.55, 0, 1, 0.45)"
    out: "cubic-bezier(0, 0.55, 0.45, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, glow, tint, scale]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "glassy"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "glass"
blur: "20px"

iconography:
  treatment: "linear"
  set: "lucide"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#7B6CF6"
      color: "#FFFFFF"
      border: "1px solid rgba(255, 255, 255, 0.3)"
      shadow: "0 8px 24px rgba(123, 108, 246, 0.4)"
      hoverBackground: "#8F82F8"
      hoverShadow: "0 12px 32px rgba(123, 108, 246, 0.55)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "rgba(255, 255, 255, 0.15)"
      color: "#FFFFFF"
      border: "1px solid rgba(255, 255, 255, 0.3)"
      shadow: "0 8px 24px rgba(20, 8, 50, 0.28)"
      hoverBackground: "rgba(255, 255, 255, 0.25)"
      hoverShadow: "0 12px 32px rgba(20, 8, 50, 0.36)"
      hoverColor: "#FFFFFF"
    ghost:
      background: "transparent"
      color: "rgba(255, 255, 255, 0.78)"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(255, 255, 255, 0.1)"
      hoverShadow: "none"
      hoverColor: "#FFFFFF"
    danger:
      background: "#F43F5E"
      color: "#FFF1F2"
      border: "1px solid rgba(255, 255, 255, 0.3)"
      shadow: "0 8px 24px rgba(244, 63, 94, 0.4)"
      hoverBackground: "#FB5C73"
      hoverShadow: "0 12px 32px rgba(244, 63, 94, 0.55)"
      hoverColor: "#FFF1F2"
    sizes:
      sm: { height: "32px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "44px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "52px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "16px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "rgba(255, 255, 255, 0.12)"
    color: "#FFFFFF"
    border: "1px solid rgba(255, 255, 255, 0.3)"
    borderRadius: "16px"
    padding: "12px 16px"
    focusBorder: "#7B6CF6"
    placeholderColor: "rgba(255, 255, 255, 0.5)"
  card:
    base:
      background: "rgba(255, 255, 255, 0.15)"
      border: "1px solid rgba(255, 255, 255, 0.3)"
      borderRadius: "24px"
      padding: "24px"
      shadow: "0 16px 40px rgba(20, 8, 50, 0.34)"
    hover:
      shadow: "0 24px 60px rgba(20, 8, 50, 0.42)"
      transform: "translateY(-4px)"
---

# Glassmorphism

> Frosted-glass panels floating over a saturated violet gradient — translucency, light borders, and heavy backdrop-blur as the entire texture.

## Origin

Glassmorphism is the frosted-glass interface aesthetic that crystallized in 2020, when designer Michał Malewicz coined the term to describe a wave of UI work imitating Apple's then-new macOS Big Sur. Big Sur replaced flat opaque surfaces with translucent, blurred materials — menu bars, dock, and sidebars that sampled and frosted whatever sat behind them — and the look spread rapidly across Dribbble, design Twitter, and product UIs worldwide.

Its lineage runs back through Apple's earlier "Aero" and iOS frosted layers and the broader 2010s translucency trend, but glassmorphism crystallized it into a repeatable recipe: a saturated multi-color gradient ground, semi-transparent white panels, a single hairline highlight border, and a heavy backdrop-blur. The ground is deliberately colorful and deep — a violet-to-magenta-to-blue blob field — because the glass effect only reads when there is something vivid behind it to soften and bleed through.

## Overview

Composition cues:
- **Layout**: Floating-card grid — translucent panels stacked at varying depths over a fixed gradient background, with blurred blobs drifting behind them
- **Content width**: Container width; generous gutters so each glass panel breathes and the colorful ground stays visible around the edges
- **Framing**: Glassy — every surface is a frosted panel with a single hairline light border catching a top-edge highlight
- **Grid intensity**: Soft — gentle column alignment, no hard rules; structure comes from blur layering and elevation, not gridlines

## Colors

The palette is built around a saturated gradient ground that gives the glass something to blur. The page is deep violet (`#3A1C71`), washed with a canonical gradient that runs violet (`#5B2A86`) → rose-magenta (`#D76D77`) → warm peach-orange (`#FFAF7B`). On top float translucent white panels — `rgba(255,255,255,0.15)` glass edged with `rgba(255,255,255,0.3)` borders. The primary action color is blue-violet (`#7B6CF6`); signature accents are vivid blues and teals (`#2CA8FF`, `#00C2FF`). Saturation is non-negotiable: the ground must stay rich and luminous, never dull or muted, or the frost loses its glow.

**Role usage**:
- Page background → `colors.background.page` (deep violet `#3A1C71`, the gradient base)
- Glass panel surface → `colors.background.surface` (translucent white `rgba(255,255,255,0.15)`)
- Subtle / recessed glass → `colors.background.subtle` (`rgba(255,255,255,0.08)`)
- Primary actions → `colors.primary.500` (blue-violet `#7B6CF6`)
- Magenta gradient stop / secondary highlights → `colors.secondary.400` (`#D76D77`)
- Vivid blue/teal accents → `colors.accent.400`/`accent.500` (`#2CA8FF`, `#00C2FF`)
- Text on glass → `colors.text.primary` (white `#FFFFFF`) and `colors.text.secondary` (`rgba(255,255,255,0.78)`)
- Panel borders → `borders.color.default` (`rgba(255,255,255,0.3)`)

## Typography

The type voice is clean, rounded geometric sans that stays crisp when read over blur. **Poppins** carries headlines — its circular, geometric letterforms feel friendly and modern and hold their shape against busy frosted backgrounds. **Inter** does the body and UI work as a free analog to **SF Pro Display**, Apple's native Big Sur typeface, with excellent legibility at small sizes over translucent surfaces. Tracking is near-neutral; the fonts are doing the work, so letters need only slight tightening at display sizes. White and high-opacity-white text sit directly on glass, leaning on the backdrop-blur to guarantee contrast.

**Text styles**:
- `display-xl` — Poppins, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Poppins, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Poppins, 48px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Inter, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 14px, weight 500, line-height 1.375, letter-spacing 0
- `mono-md` — JetBrains Mono, 16px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Section padding: 64px vertical (md), 96px (lg) — open spacing so floating panels never crowd
- Grid gaps: 16px (md) to 24px (lg) — generous gutters that keep the colorful ground visible between cards

## Elevation & Depth

Depth is the entire point. Surfaces are not opaque planes but layered sheets of frosted glass, each applying a `backdrop-filter: blur()` to whatever sits behind it. Elevation reads through three stacked cues: increasing blur, a single hairline light border catching a top-edge highlight, and a soft drop-shadow tinted deep violet rather than neutral gray. The higher a panel floats, the heavier its shadow and the brighter its border highlight.

- Surface style: glass — translucent white fills with `backdrop-filter: blur()`
- Blur: 20px default; navbars and cards range 12–32px
- Shadow ladder: deep-violet-tinted `rgba(20, 8, 50, ...)` at ascending opacity (xs → 2xl)
- Inner shadow: `inset 0 1px 1px rgba(255,255,255,0.25)` — the top-edge highlight that makes glass catch light
- Focus ring: 3px blue-violet glow at 45% opacity (`rgba(123, 108, 246, 0.45)`)

## Shapes

- `none`: 0 — full-bleed gradient grounds and dividers
- `sm`: 8px — tags, chips, small controls
- `md`: 16px — buttons, inputs, minor panels
- `lg`: 24px — cards and primary glass panels
- `xl`: 32px — hero panels and large feature surfaces
- `full`: 9999px — pills, avatars, floating action buttons

## Motion

Motion is lively but smooth — surfaces glide and lift like physical sheets of glass, never jittery or abrupt. Hovering a panel raises it toward the viewer with a gentle translate-and-shadow change; background blobs drift slowly on long loops to keep the frost alive. Transitions favor soft ease-out curves so glass feels weighted and fluid, with an optional spring for playful elements.

- Level: lively
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)` — smooth glass glide
- Spring easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` for playful lifts
- Hover patterns: lift (translateY up), glow (border/shadow intensifies), tint (fill opacity rises), scale (subtle 1.02)
- `reducedMotion: true` — drifting blobs and lift animations respect `prefers-reduced-motion`

## Techniques

### Frosted glass panel
The core recipe — a translucent white fill with heavy backdrop-blur, a hairline light border, and a top-edge inner highlight that makes the surface catch light like real glass.
```css
.glass-panel {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 24px;
  box-shadow: 0 16px 40px rgba(20, 8, 50, 0.34),
              inset 0 1px 1px rgba(255, 255, 255, 0.25);
}
```

### Saturated gradient blob field
The colorful ground the glass blurs — a deep violet page painted with the canonical violet→magenta→peach gradient plus drifting radial blobs of vivid blue and magenta.
```css
.gradient-ground {
  background-color: #3A1C71;
  background-image:
    radial-gradient(40% 50% at 20% 25%, rgba(44, 168, 255, 0.55) 0%, transparent 70%),
    radial-gradient(45% 55% at 80% 70%, rgba(215, 109, 119, 0.55) 0%, transparent 70%),
    linear-gradient(135deg, #5B2A86 0%, #D76D77 55%, #FFAF7B 100%);
  min-height: 100vh;
}
```

### Light-edge highlight border
A gradient border that brightens along the top-left edge, simulating light grazing the rim of a glass panel.
```css
.glass-edge {
  position: relative;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
}
.glass-edge::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg,
    rgba(255, 255, 255, 0.6) 0%,
    rgba(255, 255, 255, 0.1) 45%,
    rgba(255, 255, 255, 0.25) 100%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  pointer-events: none;
}
```

## Iconography

Icons are clean, thin-stroke line icons that read crisply over blur and pair with the geometric sans type. Use Lucide (or Feather) outline icons at a 1.5px stroke, rendered in white or high-opacity white so they sit on glass like the rest of the UI. Avoid heavy filled or skeuomorphic icons — the frost and translucency carry the visual weight, so iconography stays light and structural.

- Treatment: linear (outline)
- Set: Lucide
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Keep the page ground deep violet (`#3A1C71`) with a saturated violet→magenta→blue gradient — the glass needs vivid color behind it to blur
- Build every panel as translucent white (`rgba(255,255,255,0.15)`) with `backdrop-filter: blur()` of 12–32px
- Edge every glass surface with a single 1px light/white border at low opacity to catch the highlight
- Use blue-violet `#7B6CF6` for primary actions and vivid blue/teal (`#2CA8FF`, `#00C2FF`) for accents
- Set white or high-opacity-white type in Poppins/Inter and let the blur guarantee contrast

### ✗ Don't
- Use cream, ivory, or plain-white backgrounds — the ground is a saturated violet gradient
- Make panels opaque or flat — the glass must stay translucent with real backdrop-blur
- Let the ground go dull or muted — keep the gradient field saturated so the frost reads
- Apply heavy or hard borders — borders are thin (1px), light/white, at low opacity
- Use a pure-black background — the ground is deep violet, never neutral dark

## Applications

This system fits modern product dashboards, SaaS landing pages, fintech and crypto apps, music and media players, and any forward-looking tech surface that wants depth and polish without heavy chrome. It shines in hero sections and overlay UIs — modals, notification panels, and navbars — where floating frosted layers over a colorful gradient feel premium and contemporary. Best reserved for content-light, visually-driven interfaces; dense data tables and text-heavy reading views fight the translucency and are better served by a more opaque variant.
