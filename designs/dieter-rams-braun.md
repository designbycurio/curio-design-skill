---
version: 1

meta:
  id: dieter-rams-braun
  name: Dieter Rams / Braun
  description: Warm-gray functionalism where a single green dot is the only moment of color.
  isDark: false
  tags: [modernist, minimal, professional, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1955–1995 (Rams at Braun); 10 Principles codified ~1970s; influence peaks again 2000s via Jony Ive/Apple"
  region: "Kronberg im Taunus, Germany"
  regionZh: "德国克龙贝格(陶努斯)"
  keyFigures: [Dieter Rams, Hans Gugelot, Dietrich Lubs, Fritz Eichler]
  movements: [German functionalism, Ulm School of Design, Good Design]

introduction: |
  Dieter Rams' Braun is "less but better" made physical — the white-and-gray functionalism
  that defined consumer electronics from the 1956 SK4 record player to the 1987 ET66
  calculator, and quietly shaped Apple, MUJI and countless descendants. Every control has
  a reason; every surface is matte; every color is earned.

  The aesthetic is warm gray, pure white, charcoal text, and one precise green dot — the
  ON indicator, the single moment that color is permitted. Typography is invisible by
  design. Geometry is rectangles and circles, aligned to a grid. The brand's voice is
  simply: I do not need to shout. I work.
introductionZh: |
  迪特·拉姆斯的博朗是"少,但更好"的物质化身——那种用暖灰与纯白搭建出的功能主义,从 1956
  年的 SK4 唱机、1958 年的 T3 袖珍收音机,到 1987 年的 ET66 计算器,每一件都严格遵循拉姆斯
  亲手写下的《好设计十诫》。它后来被苹果的乔纳森·伊夫继承,又间接塑造了无印良品,以及
  整整一代人对"优秀工业产品"的想象。

  色彩被严格克制:博朗功能灰作为主背景,纯白为面板,炭灰色承载文字与控件,仅有一抹博朗绿
  作为开机指示——这是全系统唯一被允许的高饱和色。字体刻意低调,Inter 与 IBM Plex Sans
  延续了德国工业排印的克制;圆角仅 8px,阴影几近于无;每一个网格对齐的按钮、每一个圆点
  指示灯,都在重复拉姆斯那句话:我不必大声,我只是工作。

colors:
  primary:
    "50": "#EDF7EE"
    "100": "#D3ECD6"
    "200": "#A8D9AE"
    "300": "#7DC685"
    "400": "#63BB6B"
    "500": "#4CAF50"
    "600": "#3E9142"
    "700": "#317435"
    "800": "#245728"
    "900": "#173A1A"
    "950": "#0B1D0D"
  secondary:
    "50": "#FAFAFA"
    "100": "#F2F2F2"
    "200": "#E5E5E5"
    "300": "#D8D8D8"
    "400": "#CCCCCC"
    "500": "#C0C0C0"
    "600": "#9A9A9A"
    "700": "#747474"
    "800": "#4E4E4E"
    "900": "#282828"
    "950": "#141414"
  accent:
    "50": "#F5F5F5"
    "100": "#E0E0E0"
    "200": "#BDBDBD"
    "300": "#9E9E9E"
    "400": "#666666"
    "500": "#333333"
    "600": "#2B2B2B"
    "700": "#222222"
    "800": "#191919"
    "900": "#111111"
    "950": "#080808"
  neutral:
    "50": "#FAFAF8"
    "100": "#F4F3F0"
    "200": "#ECEAE6"
    "300": "#E8E5E0"
    "400": "#C9C6C1"
    "500": "#A7A4A0"
    "600": "#85827E"
    "700": "#636160"
    "800": "#424140"
    "900": "#212120"
    "950": "#111111"
  semantic:
    success: { bg: "#EDF7EE", text: "#245728", light: "#D3ECD6", border: "#A8D9AE" }
    warning: { bg: "#FFF7E6", text: "#7A5200", light: "#FFE4A3", border: "#E6B54D" }
    error:   { bg: "#FBEAEA", text: "#7A1F1F", light: "#F3C2C2", border: "#D95656" }
    info:    { bg: "#EEF2F5", text: "#2E3E48", light: "#D4DDE3", border: "#8A9BA6" }
  background:
    page:    "#E8E5E0"
    surface: "#FFFFFF"
    subtle:  "#F4F3F0"
  text:
    primary:   "#333333"
    secondary: "#777777"
    muted:     "#A7A4A0"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Space Grotesk', 'IBM Plex Sans', 'Inter', system-ui, sans-serif"
    body:    "'Inter', 'IBM Plex Sans', system-ui, -apple-system, sans-serif"
    mono:    "'IBM Plex Mono', 'JetBrains Mono', 'Menlo', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
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
  radius: {none: "0", sm: "4px", md: "8px", lg: "12px", xl: "16px", full: "9999px"}
  color:  {default: "#D8D6D2", subtle: "#ECEAE6", strong: "#A7A4A0", focus: "#4CAF50"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.04)"
  sm: "0 1px 3px rgba(0,0,0,0.06)"
  md: "0 2px 6px rgba(0,0,0,0.07)"
  lg: "0 4px 12px rgba(0,0,0,0.08)"
  xl: "0 8px 20px rgba(0,0,0,0.09)"
  "2xl": "0 16px 32px rgba(0,0,0,0.10)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.04)"
  focus: "0 0 0 3px rgba(76,175,80,0.28)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.2, 0.64, 1)"
  hoverPatterns: [tint, stroke, opacity]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: linear
  set:       feather
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "#333333"
      color: "#FFFFFF"
      border: "1px solid #333333"
      shadow: "0 1px 2px rgba(0,0,0,0.05)"
      hoverBackground: "#222222"
      hoverShadow: "0 1px 3px rgba(0,0,0,0.08)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "#FFFFFF"
      color: "#333333"
      border: "1px solid #D8D6D2"
      shadow: "none"
      hoverBackground: "#F4F3F0"
      hoverShadow: "none"
      hoverColor: "#333333"
    ghost:
      background: "transparent"
      color: "#333333"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "#ECEAE6"
      hoverShadow: "none"
      hoverColor: "#333333"
    danger:
      background: "#FFFFFF"
      color: "#7A1F1F"
      border: "1px solid #D95656"
      shadow: "none"
      hoverBackground: "#FBEAEA"
      hoverShadow: "none"
      hoverColor: "#7A1F1F"
    sizes:
      sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}
      md: {height: "40px", padding: "0 16px", fontSize: "0.9375rem"}
      lg: {height: "48px", padding: "0 24px", fontSize: "1rem"}
    borderRadius: "8px"
    fontWeight: 500
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#333333"
    border: "1px solid #D8D6D2"
    borderRadius: "8px"
    padding: "10px 12px"
    focusBorder: "1px solid #4CAF50"
    placeholderColor: "#A7A4A0"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid #ECEAE6"
      borderRadius: "8px"
      padding: "24px"
      shadow: "0 1px 3px rgba(0,0,0,0.06)"
    hover:
      shadow: "0 2px 6px rgba(0,0,0,0.08)"
      transform: "none"
---

# Dieter Rams / Braun

> Less, but better — warm gray, pure white, one green dot.

## Origin

Dieter Rams joined Braun in 1955 and led design until 1995, shaping a catalogue of
consumer electronics that still defines what "industrial design" means. Working out
of Kronberg im Taunus in West Germany, and drawing heavily on the Ulm School of
Design (HfG Ulm) where functionalism had taken root, Rams collaborated with Hans
Gugelot on the 1956 SK4 record player — nicknamed *Snow White's Coffin* for its
unprecedented clear acrylic lid — and with Dietrich Lubs on the 1987 ET66
calculator, whose button grid and restrained markings Apple would later absorb
almost wholesale into iOS Calculator.

Rams codified his thinking in the 10 Principles of Good Design: good design is
innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting,
thorough, environmentally friendly, and as little design as possible. Every Braun
product, and later the Vitsœ 606 shelving system he designed in 1960 and still
sells today, is a literal translation of those ten rules. The aesthetic is warm
gray plastic, brushed aluminum, charcoal text, and exactly one green indicator dot
to say: *on*. Nothing else is permitted to shout.

## Overview

Composition cues:
- **Layout**: a calm, grid-aligned composition — every control and panel sits on
  an 8px rhythm. Think ET66 button grid, not magazine spread.
- **Content width**: disciplined container (1024–1280px); full-bleed is reserved
  for neutral gray ground that lets white panels breathe.
- **Framing**: bordered. Hairline 1px dividers in `#D8D6D2` do the work that
  shadows would do elsewhere.
- **Grid intensity**: soft. The grid is felt, not seen; all controls align, but
  no visible grid lines intrude.

## Colors

The palette is deliberately restrained: warm Braun gray `#E8E5E0` for the page
ground, pure white `#FFFFFF` for panels, charcoal `#333333` for text and primary
controls, aluminum silver `#C0C0C0` for metallic details, and a single Braun
green `#4CAF50` used only as the "ON" indicator or active accent — never as
decoration. No gradient, no tint, no secondary chromatic accent. Saturation is a
resource to be spent exactly once per screen.

**Role usage**:
- Page background → `colors.background.page` (`#E8E5E0`, warm functional gray)
- Panel / card surface → `colors.background.surface` (`#FFFFFF`)
- Body text → `colors.text.primary` (`#333333`)
- Secondary text, captions → `colors.text.secondary` (`#777777`)
- Single active accent, ON indicators, focus rings → `colors.primary.500` (`#4CAF50`)
- Metallic details, dividers at rest → `colors.secondary.500` (`#C0C0C0`)
- Structural dark controls (primary buttons, icons) → `colors.accent.500` (`#333333`)
- Hairline borders → `colors.borders.color.default` (`#D8D6D2`)

## Typography

Type is invisible by design. Braun historically used Akzidenz-Grotesk and Univers;
the digital equivalents that carry the same quiet engineering voice are **Space
Grotesk** for display, **IBM Plex Sans** for German-industrial body/UI, and
**Inter** — which traces its lineage back through Jony Ive's Apple to Rams —
for running text. Weights stay in the 400–600 band; tracking is neutral or very
slightly negative at display sizes. The content speaks; the font steps back.

**Text styles**:
- `display-xl` — Space Grotesk, 96px, weight 500, line-height 1.0, letter-spacing -0.03em
- `display-lg` — Space Grotesk, 64px, weight 500, line-height 1.05, letter-spacing -0.02em
- `display-md` — Space Grotesk, 48px, weight 500, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Space Grotesk, 36px, weight 600, line-height 1.15, letter-spacing -0.01em
- `heading-2` — Space Grotesk, 30px, weight 600, line-height 1.2, letter-spacing -0.01em
- `heading-3` — IBM Plex Sans, 24px, weight 600, line-height 1.3, letter-spacing 0
- `body-lg` — Inter, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `body-sm` — Inter, 14px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — IBM Plex Sans, 12px, weight 500, line-height 1.4, letter-spacing 0.05em (uppercase label use only)
- `mono-md` — IBM Plex Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit **4px**, with a primary 8px rhythm (everything visible aligns to 8px)
- Scale: `2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128`
- Containers: `sm 640 / md 768 / lg 1024 / xl 1280 / full 100%`
- Section padding: `sm 32px / md 64px / lg 96px / xl 128px` — generous vertical breathing room, like Vitsœ shelf spacing
- Grid gaps: `sm 8 / md 16 / lg 24 / xl 48` — strongly favor 16 and 24 for card grids

## Elevation & Depth

Materiality is **matte plastic on warm gray** — no gloss, no translucency, no blur.
Depth is communicated almost entirely by hairline borders and barely-there
shadows. A card is a white rectangle with a 1px `#ECEAE6` border and a 1px-blur
shadow at 6% black; you should be able to miss the shadow at first glance, which
is the point.

- Surface style: **solid** (no glass, no frost)
- Blur: **none**
- Shadow ladder:
  - `xs` — 0 1px 2px rgba(0,0,0,0.04) for inputs at rest
  - `sm` — 0 1px 3px rgba(0,0,0,0.06) for default cards
  - `md` — 0 2px 6px rgba(0,0,0,0.07) for hover states
  - `lg` — 0 4px 12px rgba(0,0,0,0.08) for popovers
  - `xl`/`2xl` — reserved for modals; still soft, never dramatic

## Shapes

- Corner radii follow the Braun product language: rectangles with gently softened
  corners, not pills
- `radius.sm` 4px — inputs, chips, tags
- `radius.md` 8px — buttons, cards, panels (the default)
- `radius.lg` 12px — large product-style panels, modals
- `radius.xl` 16px — hero modules only, sparingly
- `radius.full` 9999px — reserved for circular indicator dots and avatars

## Motion

Motion is **restrained**: things do not bounce, stretch, or rotate. Interactions
are short, linear, engineered — a 120ms tint change, a 250ms opacity fade, the
green focus ring appearing instantly and leaving softly. Transitions feel like a
switch being flipped on a well-built appliance.

- Level: **restrained**
- Durations: `instant 0 / fast 120 / normal 250 / slow 400 / slower 600`
- Easings: standard `cubic-bezier(0.4, 0, 0.2, 1)` default; linear for indicator lights
- Hover patterns: **tint** (subtle background shift), **stroke** (border darkens), **opacity** (secondary elements fade in). Avoid lift, scale, glow.
- Honors `prefers-reduced-motion` fully

## Techniques

### ON-indicator dot
The single permitted moment of color — a 6px Braun-green disc used beside active
items (nav, selected tab, live status, focused field). Never more than one
per visual group.

```css
.rams-indicator {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 9999px;
  background: #4CAF50;
  /* optional subtle glow, engineered not decorative */
  box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.18);
  vertical-align: middle;
}

.rams-nav-item[aria-current="page"]::before {
  content: "";
  display: inline-block;
  width: 6px;
  height: 6px;
  margin-right: 10px;
  border-radius: 9999px;
  background: #4CAF50;
}
```

### Perforated speaker-grille background
A quiet homage to the SK4 speaker grille: a dot-grid pattern rendered with a
single radial gradient, used as a subtle texture on gray ground panels. Almost
invisible — which is the intent.

```css
.rams-grille {
  background-color: #E8E5E0;
  background-image: radial-gradient(
    circle,
    rgba(51, 51, 51, 0.14) 1px,
    transparent 1.5px
  );
  background-size: 8px 8px;
  background-position: 0 0;
}
```

### Hairline panel on warm gray
The Braun card: pure-white panel, 1px hairline border, nearly-invisible shadow.
The border does the work of separation; the shadow only hints that the panel is
a physical object resting on the gray ground.

```css
.rams-panel {
  background: #FFFFFF;
  border: 1px solid #ECEAE6;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
  transition:
    box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1),
    border-color 250ms cubic-bezier(0.4, 0, 0.2, 1);
}

.rams-panel:hover {
  border-color: #D8D6D2;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}
```

## Iconography

Linear icons only, drawn on a 24px grid with a consistent 1.5px stroke — think
Feather or a custom set matching Braun's control glyphs. No filled icons, no
duotones, no gradients. Size `sm 16 / md 20 / lg 24`. Icons are charcoal `#333`
at rest; the single green dot is reserved for active state, never applied to an
icon fill.

- Treatment: linear, 1.5px stroke
- Set: Feather (or a custom Braun-control-style set)
- Stroke: 1.5px, rounded caps/joins

## Do's & Don'ts

### ✓ Do
- Use warm Braun gray `#E8E5E0` as the page ground — never cold gray, never pure white full-bleed.
- Spend the green accent `#4CAF50` exactly once per visual group, as an ON/active indicator.
- Align every control, label, and card to the 8px grid; let geometry do the decoration.
- Keep typography quiet — Inter/IBM Plex Sans in the 400–600 band, neutral tracking.
- Prefer a 1px hairline border over a shadow whenever possible; "less, but better."

### ✗ Don't
- Don't introduce decorative ornament of any kind.
- Don't use bold or saturated color palettes — one green dot is the entire budget.
- Don't use script, display, or playful fonts; keep the voice functional and invisible.
- Don't reach for glassmorphism, gradients, or heavy shadows — they violate "unobtrusive."
- Don't add whimsy, mascots, or depth effects; anything that breaks "less, but better" breaks the system.

## Applications

Best-fit use cases are product documentation, hardware/appliance brand sites,
design-engineering portfolios, developer tools with a focus on precision, and
any interface where trust, clarity, and long-lasting calm matter more than
novelty. Think: a CAD application's dashboard, a serious audio manufacturer's
product page, the admin panel for industrial equipment, or a designer's personal
site that wants to feel like a Vitsœ shelf — quiet, exact, built to outlast
fashion.
