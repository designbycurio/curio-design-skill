---
version: 1

meta:
  id: ikea-blue-yellow
  name: IKEA
  description: Swedish-flag blue-and-yellow furniture democracy — mass-market warmth meets flat-pack rationalism
  isDark: false
  tags: [friendly, modernist, bold, professional, playful]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1943 founded; current visual identity ~1981–2024"
  region: "Älmhult, Sweden"
  regionZh: "瑞典阿姆霍特"
  keyFigures: [Ingvar Kamprad, Anders Dahlvig, Stockholm Design Lab]
  movements: [Scandinavian-modern furniture democracy, flat-pack industrial design, retail-as-experience]

introduction: |
  IKEA is the Swedish-flag blue-and-yellow box — a furniture democracy born in 1943 Småland that turned flat-pack rationalism into a global lifestyle. The brand's visual identity is inseparable from its bicolor palette: saturated Swedish-flag blue (#0058A3) and yellow (#FFDA1A), paired with kraft-brown cardboard and hand-drawn Allen-key assembly diagrams that need no language at all.

  The design system channels mass-market warmth over tech minimalism: generous photography panels, bold color blocks, tight sans-serif type, and the iconic rounded-rectangle lockup. Every surface reads as accessible, democratic, and unmistakably Scandinavian.
introductionZh: |
  宜家是那个蓝黄配色的瑞典国旗色盒子——1943年诞生于瑞典斯莫兰的家具民主品牌，用平板包装理性主义改变了全球生活方式。品牌视觉离不开瑞典国旗的饱和蓝（#0058A3）与黄（#FFDA1A），搭配牛皮纸棕色和无需文字的手绘六角扳手组装图。

  这套设计系统追求大众市场的温暖感而非科技极简：大幅生活场景摄影、大胆色块、紧凑无衬线字体，以及标志性的圆角矩形品牌锁定图形。每一个界面都传递着平易近人、民主化、不可错认的北欧气质。

colors:
  primary:    {"50": "#E6F0F9", "100": "#CCE1F3", "200": "#99C3E7", "300": "#66A5DB", "400": "#3387CF", "500": "#0058A3", "600": "#00407A", "700": "#003562", "800": "#002A4F", "900": "#001F3B", "950": "#001528"}
  secondary:  {"50": "#FFFDF0", "100": "#FFFBE0", "200": "#FFF7C2", "300": "#FFF3A3", "400": "#FFEF85", "500": "#FFDA1A", "600": "#E6C400", "700": "#BFA300", "800": "#998200", "900": "#736200", "950": "#4D4100"}
  accent:     {"50": "#FAF5EE", "100": "#F5EBDD", "200": "#EBD7BB", "300": "#E1C399", "400": "#D7AF77", "500": "#C19A6B", "600": "#A67E52", "700": "#8A6843", "800": "#6E5335", "900": "#523E28", "950": "#36291A"}
  neutral:    {"50": "#FAFAFA", "100": "#F5F5F5", "200": "#E8E8E8", "300": "#D4D4D4", "400": "#A3A3A3", "500": "#737373", "600": "#525252", "700": "#404040", "800": "#2A2A2A", "900": "#1A1A1A", "950": "#0F0F0F"}
  semantic:
    success: { bg: "#0A7B3E", text: "#FFFFFF", light: "#E6F5ED", border: "#0A7B3E" }
    warning: { bg: "#E6A800", text: "#1A1A1A", light: "#FFF8E0", border: "#E6A800" }
    error:   { bg: "#CC0000", text: "#FFFFFF", light: "#FFE6E6", border: "#CC0000" }
    info:    { bg: "#0058A3", text: "#FFFFFF", light: "#E6F0F9", border: "#0058A3" }
  background:
    page:    "#0058A3"
    surface: "#FFDA1A"
    subtle:  "#0066BC"
  text:
    primary:   "#1A1A1A"
    secondary: "#5C7A9D"
    muted:     "#737373"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'IKEA Sans', 'Noto Sans', 'Verdana', sans-serif"
    body:    "'IKEA Sans', 'Noto Sans', 'Verdana', sans-serif"
    mono:    "'JetBrains Mono', 'Consolas', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&display=swap"
  scale: {"2xs": "0.625rem", "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
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
  radius: {none: "0", sm: "4px", md: "8px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "#D4D4D4", subtle: "#E8E8E8", strong: "#0058A3", focus: "#FFDA1A"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,88,163,0.06)"
  sm: "0 2px 4px rgba(0,88,163,0.08)"
  md: "0 2px 8px rgba(0,88,163,0.12)"
  lg: "0 4px 16px rgba(0,88,163,0.16)"
  xl: "0 8px 32px rgba(0,88,163,0.20)"
  "2xl": "0 16px 48px rgba(0,88,163,0.24)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.04)"
  focus: "0 0 0 3px rgba(255,218,26,0.5)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "120ms", normal: "200ms", slow: "350ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, scale]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "wide"
  framing:       "solid"
  gridIntensity: "strong"
  rhythm:        "8px"

surfaceStyle: "solid"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#0058A3", color: "#FFFFFF", border: "none", shadow: "0 2px 4px rgba(0,88,163,0.08)", hoverBackground: "#00407A", hoverShadow: "0 4px 16px rgba(0,88,163,0.16)", hoverColor: "#FFFFFF"}
    secondary: {background: "#FFDA1A", color: "#0058A3", border: "none", shadow: "none", hoverBackground: "#E6C400", hoverShadow: "none", hoverColor: "#0058A3"}
    ghost:     {background: "transparent", color: "#0058A3", border: "2px solid #0058A3", shadow: "none", hoverBackground: "#E6F0F9", hoverShadow: "none", hoverColor: "#0058A3"}
    danger:    {background: "#CC0000", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#A30000", hoverShadow: "none", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "4px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1A1A1A"
    border: "2px solid #D4D4D4"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "#0058A3"
    placeholderColor: "#A3A3A3"
  card:
    base:  {background: "#FFFFFF", border: "1px solid #E8E8E8", borderRadius: "8px", padding: "24px", shadow: "0 2px 8px rgba(0,88,163,0.12)"}
    hover: {shadow: "0 4px 16px rgba(0,88,163,0.16)", transform: "translateY(-2px)"}
---

# IKEA

> Swedish-flag blue-and-yellow furniture democracy — mass-market warmth meets flat-pack rationalism.

## Origin

IKEA was founded in 1943 by seventeen-year-old Ingvar Kamprad in Småland, Sweden, initially as a mail-order business selling pens and wallets before pivoting to furniture in 1948. The flat-pack concept arrived in 1956 when designer Gillis Lundgren removed the legs of a table to fit it in his car — and an empire of self-assembly was born. The brand's visual identity crystallized around the Swedish flag's exact blue (#0058A3) and yellow (#FFDA1A), locked inside a rounded-rectangle wordmark that has barely changed since 1981.

Today IKEA operates 460+ stores across 62 markets, guided by Stockholm Design Lab's 2017 brand refresh and an in-house team that maintains the bicolor system across everything from warehouse signage to the IKEA Place AR app. The design language is inseparable from its democratic mission: bold, legible, multilingual, and warm enough to feel like home rather than a corporation.

## Overview

Composition cues:
- **Layout**: Strong grid with full-bleed photography panels alternating with solid blue/yellow color blocks
- **Content width**: Wide — generous use of horizontal space, room-set imagery edge-to-edge
- **Framing**: Solid color blocks and cards with minimal border treatment; no glass or blur
- **Grid intensity**: Strong — visible structure, clear columns, generous gutters

## Colors

The palette is strictly bicolor: Swedish-flag blue and yellow dominate every surface, with kraft-brown as a tertiary material accent and cream as a catalog-paper substrate. Blue is authoritative and structural (backgrounds, headers, CTAs); yellow is energetic and highlighting (surfaces, badges, secondary actions). The system avoids pastels — both blue and yellow must remain at full Swedish-flag saturation.

**Role usage**:
- Page background → `colors.background.page` (#0058A3 blue)
- Card / panel surface → `colors.background.surface` (#FFDA1A yellow)
- Subtle background variation → `colors.background.subtle` (#0066BC lighter blue)
- Primary text on cream/white → `colors.text.primary` (#1A1A1A charcoal)
- Secondary/muted text → `colors.text.secondary` (#5C7A9D)
- Text on blue backgrounds → `colors.text.inverse` (#FFFFFF)
- Kraft/material accent → `colors.accent.500` (#C19A6B)
- Catalog paper substrate → accent cream (#FAF6EE)

## Typography

IKEA's type voice is functional, multilingual, and unpretentious — a Verdana-derived custom sans (IKEA Sans, 2009) that prioritizes legibility at every size from warehouse aisle signage to mobile product cards. Headlines are semibold with tight tracking; body is regular weight at comfortable reading sizes. The wordmark "IKEA" always appears in ALL-CAPS bold. Fallback to Noto Sans ensures global script coverage.

**Text styles**:
- `display-xl` — IKEA Sans, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — IKEA Sans, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — IKEA Sans, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `heading-2` — IKEA Sans, 36px, weight 600, line-height 1.25, letter-spacing 0
- `body-lg` — IKEA Sans, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — IKEA Sans, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — IKEA Sans, 12px, weight 500, line-height 1.4, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px (all spacing derives from multiples of 8)
- Scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px (xl), with full-bleed breakouts for photography
- Section padding: 64px vertical (md), 96px (lg) on desktop
- Grid gap: 16px (md) default, 24px (lg) for card grids

## Elevation & Depth

IKEA's materiality is flat and solid — no glass, no blur, no translucency. Depth comes from layered color blocks (blue behind yellow behind white) and subtle card shadows tinted with brand blue rather than neutral black. The system feels like stacked cardboard and printed paper, not floating glass.

- Surface style: solid opaque fills, no backdrop-filter
- Blur: none
- Shadow ladder: xs (subtle lift) → md (card default at `0 2px 8px rgba(0,88,163,0.12)`) → lg (hover state) → xl (modal/dropdown)
- All shadows use blue-tinted rgba, never pure black

## Shapes

- Button border-radius: 4px (slightly rounded, functional)
- Card border-radius: 8px (friendly but not bubbly)
- Lockup / badge border-radius: 24px (the iconic rounded-rectangle frame)
- Input border-radius: 4px
- Full-round: 9999px (avatars, dots)

## Motion

IKEA's motion is restrained and purposeful — transitions serve wayfinding, not decoration. Hover states lift cards gently; page transitions are quick fades. Nothing bounces or overshoots. The brand's physicality is cardboard and Allen keys, not springs and rubber.

- Level: restrained
- Durations: fast 120ms (micro-interactions), normal 200ms (hover/focus), slow 350ms (panel reveals)
- Default easing: cubic-bezier(0.4, 0, 0.2, 1)
- Hover patterns: lift (translateY -2px), tint (background darken), scale (1.02 on cards)
- Reduced motion: respected — all animations collapse to instant

## Techniques

### Blue-Yellow Block Split

Full-width sections split into a blue half and yellow half, creating the iconic IKEA bicolor rhythm.

```css
.block-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 400px;
}
.block-split__blue {
  background: #0058A3;
  color: #FFFFFF;
  padding: 64px 48px;
}
.block-split__yellow {
  background: #FFDA1A;
  color: #0058A3;
  padding: 64px 48px;
}
```

### Kraft Paper Price Tag

Product price tags styled as kraft-brown cardboard labels with a punched-hole detail.

```css
.price-tag {
  background: #C19A6B;
  color: #1A1A1A;
  padding: 12px 20px 12px 32px;
  border-radius: 4px;
  position: relative;
  font-weight: 700;
  font-size: 1.5rem;
}
.price-tag::before {
  content: '';
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #FAF6EE;
}
```

### Rounded Lockup Badge

The iconic IKEA rounded-rectangle frame used for logos, category labels, and featured badges.

```css
.lockup-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #0058A3;
  color: #FFDA1A;
  border: 3px solid #FFDA1A;
  border-radius: 24px;
  padding: 8px 24px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

## Iconography

Icons follow IKEA's hand-drawn instruction-manual spirit: simple linear strokes that communicate without language. They should feel like they belong on a flat-pack assembly sheet — clear, universal, and friendly.

- Treatment: linear (outline only, no fills)
- Set: Lucide (clean geometric, multilingual-friendly)
- Stroke: 2px consistent weight

## Do's & Don'ts

### ✓ Do
- Use Swedish-flag saturated blue (#0058A3) and yellow (#FFDA1A) as the dominant bicolor pair
- Keep typography in IKEA Sans / Noto Sans / Verdana family — no serifs
- Use kraft-brown (#C19A6B) sparingly as a material/tertiary accent
- Maintain generous grid structure with full-bleed photography panels
- Design for multilingual legibility at every breakpoint

### ✗ Don't
- Use pastel or desaturated blue/yellow — must remain Swedish-flag intensity
- Introduce decorative serifs or display typefaces
- Use photographic backgrounds that aren't IKEA-style room-sets
- Add multiple competing accent colors — strict bicolor + brown kraft only
- Apply slick-tech / SaaS minimal aesthetic — IKEA is mass-market warmth
- Design for dark mode

## Applications

This system is ideal for e-commerce product pages, retail signage, catalog-style editorial layouts, and internal tools that need to feel accessible and democratic rather than corporate. It works best at scale — large photography, bold color blocks, and clear wayfinding — mirroring the IKEA store experience translated to screen.
