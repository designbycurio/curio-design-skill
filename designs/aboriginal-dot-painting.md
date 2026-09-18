---
version: 1

meta:
  id: aboriginal-dot-painting
  name: "Aboriginal Dot Painting"
  description: "Red ochre earth ground with concentric dot circles, U-shapes, and ancestor tracks — 40,000 years of Western Desert visual storytelling"
  isDark: false
  tags: [decorative, organic, historical, narrative, bold]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Contemporary canvas tradition since 1971 (Papunya); oldest continuous art tradition on Earth (40,000+ years)"
  region: "Central Australian Desert — Papunya, Yuendumu, Kintore (Western Desert peoples)"
  regionZh: "澳大利亚中部沙漠——帕潘亚、尤恩杜穆、金托尔（西部沙漠民族）"
  keyFigures: [Geoffrey Bardon, Clifford Possum Tjapaltjarri, Emily Kngwarreye, Mick Namarari]
  movements: [Western Desert dot painting, Papunya Tula school, contemporary Aboriginal art]

introduction: |
  Aboriginal dot painting emerged in 1971 when schoolteacher Geoffrey Bardon encouraged Papunya elders to translate sacred body-painting traditions onto canvas. The resulting works — dense fields of acrylic dots encoding Dreaming narratives as map-from-above compositions — launched the most significant Indigenous art movement of the twentieth century.

  This design system distills the visual vocabulary of Western Desert painting into interface tokens: red ochre earth grounds, concentric circle motifs (waterholes), U-shapes (sitting figures), and radiating dot fields, all held within a strict mineral-pigment palette of ochre, umber, bone white, and brick red.
introductionZh: |
  1971年，教师杰弗里·巴登鼓励帕潘亚长老将神圣的身体彩绘传统转移到画布上，由此催生了澳大利亚原住民点画运动——地球上最古老艺术传统的当代延续。克利福德·波瑟姆、艾米莉·昂瓦雷耶等大师用密集的丙烯圆点编码"梦境时代"的祖先故事，以俯视地图式构图描绘水源、足迹与营地。

  本设计系统提炼西部沙漠画派的视觉语汇：红赭石大地底色、同心圆（水源地）、U形（坐姿人物）与放射状点阵，严格限制在矿物颜料色调之内——赭石、焦褐、骨白与砖红，呈现四万年不断线的视觉叙事传统。

colors:
  primary:
    "50": "#f8ebe7"
    "100": "#e8c4bc"
    "200": "#d89d91"
    "300": "#c87666"
    "400": "#b04f3b"
    "500": "#8B2A1F"
    "600": "#7a241b"
    "700": "#691e17"
    "800": "#581813"
    "900": "#47120f"
    "950": "#2e0b09"
  secondary:
    "50": "#faf4e6"
    "100": "#f0dfb3"
    "200": "#e6ca80"
    "300": "#dcb54d"
    "400": "#d8ad3a"
    "500": "#D4A547"
    "600": "#bb923e"
    "700": "#a27f35"
    "800": "#896c2c"
    "900": "#705923"
    "950": "#4a3b17"
  accent:
    "50": "#f0ebe5"
    "100": "#d4c7b7"
    "200": "#b8a389"
    "300": "#9c7f5b"
    "400": "#7c5c3d"
    "500": "#5C3A1F"
    "600": "#51331b"
    "700": "#462c17"
    "800": "#3b2513"
    "900": "#301e0f"
    "950": "#1f1309"
  neutral:
    "50": "#faf7f2"
    "100": "#f5e8c9"
    "200": "#e8d5a8"
    "300": "#d4bd88"
    "400": "#bfa568"
    "500": "#a08656"
    "600": "#856e47"
    "700": "#6a5738"
    "800": "#4f4029"
    "900": "#34291a"
    "950": "#1a150d"
  semantic:
    success:
      bg: "#4a7a3d"
      text: "#FDF5E6"
      light: "#e8f0e4"
      border: "#4a7a3d"
    warning:
      bg: "#D4A547"
      text: "#0A0A0A"
      light: "#faf4e6"
      border: "#D4A547"
    error:
      bg: "#8B2A1F"
      text: "#FDF5E6"
      light: "#f8ebe7"
      border: "#8B2A1F"
    info:
      bg: "#5C3A1F"
      text: "#FDF5E6"
      light: "#f0ebe5"
      border: "#5C3A1F"
  background:
    page: "#A0522D"
    surface: "#FDF5E6"
    subtle: "#5C3A1F"
  text:
    primary: "#0A0A0A"
    secondary: "#5C3A1F"
    muted: "#6a5738"
    inverse: "#FDF5E6"

typography:
  families:
    heading: "'Spartan', 'Public Sans', sans-serif"
    body: "'Crimson Pro', 'Lora', Georgia, serif"
    mono: "'IBM Plex Mono', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700;800&family=Crimson+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Caveat:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
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
    sm: "4px"
    md: "8px"
    lg: "12px"
    xl: "16px"
    full: "9999px"
  color:
    default: "#5C3A1F"
    subtle: "#d4bd88"
    strong: "#0A0A0A"
    focus: "#D4A547"
  width:
    thin: "1px"
    default: "2px"
    thick: "3px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(10,10,10,0.05)"
  sm: "0 1px 3px rgba(10,10,10,0.08)"
  md: "0 4px 6px rgba(10,10,10,0.07)"
  lg: "0 10px 15px rgba(10,10,10,0.06)"
  xl: "0 20px 25px rgba(10,10,10,0.08)"
  "2xl": "0 25px 50px rgba(10,10,10,0.12)"
  inner: "inset 0 1px 2px rgba(10,10,10,0.04)"
  focus: "0 0 0 3px rgba(212,165,71,0.35)"

motion:
  level: "restrained"
  durations:
    instant: "0ms"
    fast: "120ms"
    normal: "250ms"
    slow: "400ms"
    slower: "600ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [opacity, tint, scale]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "container"
  framing: "solid"
  gridIntensity: "none"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "filled"
  set: "phosphor"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#8B2A1F"
      color: "#FDF5E6"
      border: "2px dotted #D4A547"
      shadow: "none"
      hoverBackground: "#691e17"
      hoverShadow: "none"
      hoverColor: "#FDF5E6"
    secondary:
      background: "#D4A547"
      color: "#0A0A0A"
      border: "2px solid #D4A547"
      shadow: "none"
      hoverBackground: "#bb923e"
      hoverShadow: "none"
      hoverColor: "#0A0A0A"
    ghost:
      background: "transparent"
      color: "#FDF5E6"
      border: "2px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(253,245,230,0.1)"
      hoverShadow: "none"
      hoverColor: "#F5E8C9"
    danger:
      background: "#8B2A1F"
      color: "#ffffff"
      border: "2px solid #8B2A1F"
      shadow: "none"
      hoverBackground: "#581813"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    sizes:
      sm:
        height: "34px"
        padding: "0 14px"
        fontSize: "0.875rem"
      md:
        height: "42px"
        padding: "0 20px"
        fontSize: "1rem"
      lg:
        height: "50px"
        padding: "0 28px"
        fontSize: "1.125rem"
    borderRadius: "12px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#FDF5E6"
    color: "#0A0A0A"
    border: "2px solid #5C3A1F"
    borderRadius: "8px"
    padding: "10px 14px"
    focusBorder: "#D4A547"
    placeholderColor: "#6a5738"
  card:
    base:
      background: "#FDF5E6"
      border: "2px solid #5C3A1F"
      borderRadius: "16px"
      padding: "24px"
      shadow: "none"
    hover:
      shadow: "0 4px 6px rgba(10,10,10,0.07)"
      transform: "translateY(-2px)"
---

# Aboriginal Dot Painting

> Red ochre earth, concentric dot circles, and ancestor tracks — 40,000 years of Dreaming country, mapped from above.

## Origin

Aboriginal dot painting traces its contemporary canvas form to 1971, when schoolteacher Geoffrey Bardon arrived at the Papunya settlement in Central Australia and encouraged Anmatyerre, Luritja, and Pintupi elders to translate their ancient body-painting and ground-painting traditions onto boards and canvas. The resulting works — vast acrylic dot fields encoding sacred Dreaming (Tjukurrpa) narratives — were unlike anything the Western art world had seen. Clifford Possum Tjapaltjarri's monumental *Warlugulong* (1977) and Tim Leura Tjapaltjarri's collaborative canvases established the movement. The Papunya Tula Artists cooperative, founded in 1972, gave the artists collective ownership and marked the beginning of the most significant Indigenous art movement of the twentieth century.

Emily Kngwarreye of Utopia brought the tradition to global prominence in the 1990s with her late-career masterpieces — enormous canvases of pure dot-and-line energy that transcended narrative into something close to Abstract Expressionism. The dot technique itself serves a dual purpose: it encodes ancestral stories (songlines, waterholes, ancestor tracks) as map-from-above compositions while simultaneously concealing sacred elements from uninitiated viewers. Each concentric circle is a waterhole or meeting place, each U-shape a sitting figure, each wavy line an ancestor's path across country. The palette is strictly mineral-pigment: red ochre, yellow ochre, bone white, burnt umber, and black — the colours of the Central Australian desert itself.

## Overview

Composition cues:
- **Layout**: Stacked vertical compositions with organic, asymmetric placement — no Western rectangular grids
- **Content width**: Container-bound, with generous ochre-earth margins breathing around content
- **Framing**: Solid ochre panels and bone-cream cards — flat and warm, never glassy
- **Grid intensity**: None — composition follows the map-from-above logic of concentric circles radiating outward, not columnar grids

## Colors

The palette is derived entirely from mineral pigments found in the Central Australian desert. Red ochre (#A0522D) is the dominant ground — the colour of the dry earth itself, present everywhere as the page background. Brick red (#8B2A1F) provides warmth for primary actions and emphasis, evoking the iron-rich soils and the sacred significance of blood and fire. Yellow ochre (#D4A547) brings the warmth of sun and ancestor colour as a secondary accent. Burnt umber (#5C3A1F) anchors dark panels and track-line elements. Bone white (#F5E8C9) and old lace (#FDF5E6) provide the dot-highlight and card-surface relief. Black (#0A0A0A) serves as the outline and base layer beneath dot fields. There are no bright primaries, no chromatic blues or greens — only the mineral earth.

**Role usage**:
- Page background → `colors.background.page` (red ochre #A0522D)
- Card / content surface → `colors.background.surface` (bone cream #FDF5E6)
- Dark panels / alt sections → `colors.background.subtle` (burnt umber #5C3A1F)
- Primary actions & emphasis → `colors.primary.500` (brick red #8B2A1F)
- Secondary accents & highlights → `colors.secondary.500` (yellow ochre #D4A547)
- Track lines & borders → `colors.accent.500` (burnt umber #5C3A1F)
- Body text → `colors.text.primary` (black #0A0A0A)
- Inverse text on ochre ground → `colors.text.inverse` (bone cream #FDF5E6)

## Typography

The type voice balances modern clarity with warm, organic character — geometric sans for structure, warm serif for storytelling. Spartan (League Spartan) provides bold, geometric headings with wide letter-spacing that echoes the spatial rhythm of dot fields. Crimson Pro serves body text with warm, humanist serif forms that feel grounded and narrative rather than clinical. Caveat is reserved exclusively for attribution accents and cultural respect notes, bringing a hand-lettered quality that honours the handmade tradition. Letter-spacing runs slightly wide on display sizes, giving headlines room to breathe like dots spaced across canvas.

**Text styles**:
- `display-xl` — Spartan, 96px, weight 800, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Spartan, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Spartan, 48px, weight 700, line-height 1.2, letter-spacing 0
- `body-lg` — Crimson Pro, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Crimson Pro, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Crimson Pro, 12px, weight 500, line-height 1.5, letter-spacing 0.05em
- `mono-md` — IBM Plex Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm at 8px
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640 / md 768 / lg 1024 / xl 1280 px
- Section padding: sm 32 / md 64 / lg 96 / xl 128 px — generous vertical space evokes the vast emptiness of desert landscape between story-sites

## Elevation & Depth

The surface language is flat and layered, like ochre pigment applied to canvas in successive dot layers. There are no glossy gradients, no drop shadows, no glass effects — the aesthetic is pure matte mineral pigment on woven canvas. Depth comes from colour layering: bone-cream cards sit visually above the red ochre ground through contrast alone. Dark burnt-umber panels recede. The only concession to elevation is a subtle lift on card hover, suggesting a canvas edge peeling slightly from the wall.

- Surface style: layered solid colour planes (ochre ground → cream cards → umber panels)
- Blur: none — no frosted or glass effects
- Shadow ladder: none by default; minimal xs–md on hover only for interactivity cues

## Shapes

- Corner radii are organic and rounded: sm 4px / md 8px / lg 12px / xl 16px
- Buttons at 12px radius — soft, organic, never sharp-cornered
- Cards at 16px radius — warm and approachable
- Full radius (9999px) for dot-pattern pills and circular badges
- No sharp rectangular grids — shapes follow the rounded, organic logic of dot circles

## Motion

Restrained and grounded — movements should feel like the slow, deliberate hand placing dots one by one on canvas. Nothing bounces, nothing slides in from offscreen. Transitions are gentle opacity shifts and subtle scale changes, like watching a pattern emerge dot by dot under a painter's hand.

- Level: restrained
- Durations: fast 120ms / normal 250ms / slow 400ms
- Default easing: cubic-bezier(0.4, 0, 0.2, 1) — ease-in-out
- Hover patterns: opacity fade, colour tint shift, subtle scale (1.02)
- No flashy entrances, no SaaS-style slide-ins — the desert is patient

## Techniques

### Dot Pattern Border

A decorative dotted border that evokes the concentric dot-circle motif of Western Desert painting. Used on primary CTAs and featured cards.

```css
.dot-border-element {
  border: 2px dotted #D4A547;
  border-radius: 12px;
  position: relative;
}
.dot-border-element::before {
  content: "";
  position: absolute;
  inset: -6px;
  border: 2px dotted rgba(212, 165, 71, 0.4);
  border-radius: 16px;
  pointer-events: none;
}
```

### Concentric Circle Ornament

An SVG-based concentric circle motif (waterhole symbol) used as a decorative corner ornament on cards and section headers.

```css
.concentric-ornament {
  position: relative;
}
.concentric-ornament::after {
  content: "";
  position: absolute;
  top: -12px;
  right: -12px;
  width: 48px;
  height: 48px;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 48 48' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='24' cy='24' r='22' fill='none' stroke='%23D4A547' stroke-width='2' stroke-dasharray='3 3'/%3E%3Ccircle cx='24' cy='24' r='15' fill='none' stroke='%23D4A547' stroke-width='2' stroke-dasharray='3 3'/%3E%3Ccircle cx='24' cy='24' r='8' fill='none' stroke='%23D4A547' stroke-width='2' stroke-dasharray='3 3'/%3E%3Ccircle cx='24' cy='24' r='3' fill='%23D4A547'/%3E%3C/svg%3E");
  background-size: contain;
  pointer-events: none;
  opacity: 0.7;
}
```

### Canvas Weave Texture

A subtle canvas-grain overlay that gives surfaces the tactile feel of woven linen — the substrate onto which Papunya artists apply their acrylic dots.

```css
.canvas-weave {
  position: relative;
}
.canvas-weave::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='canvas'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23canvas)' opacity='0.06'/%3E%3C/svg%3E");
  pointer-events: none;
  mix-blend-mode: multiply;
}
```

## Iconography

Icons should feel solid and warm, complementing the dense, filled quality of dot-painted surfaces. Phosphor icons in their filled treatment provide rounded, organic forms that harmonise with the dot-circle vocabulary. The weight should feel present but not heavy — like a painted symbol on ochre ground.

- Treatment: filled (matching the solid, layered dot aesthetic)
- Set: Phosphor — rounded, organic forms that suit the cultural warmth
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use red ochre (#A0522D) as the dominant page ground — it IS the desert
- Keep the palette strictly to mineral-pigment earth tones (ochre, umber, bone, brick, black)
- Use concentric circles and U-shapes as decorative vocabulary (abstracted, non-narrative)
- Include a cultural attribution note in footer acknowledging Western Desert visual traditions
- Let dot-pattern borders and concentric-circle ornaments carry the brand identity

### ✗ Do not
- Use bright primary colours (red/blue/yellow CMY) — earth-pigment palette only
- Use Inter or Geist — Spartan is the heading typeface
- Impose sharp rectangular grids — use organic concentric-circle and radial compositions
- Use white or cream as page ground — red ochre earth IS the page
- Apply SaaS gradients or glossy effects
- Generate specific Dreaming story or songline imagery — stick to abstracted general dot patterns, concentric circles, and U-shapes as visual vocabulary

## Applications

This system is ideal for cultural heritage platforms, storytelling and narrative interfaces, museum and gallery digital experiences, environmental and land-stewardship applications, and educational content about Indigenous Australian culture. It pairs well with photography of desert landscapes and organic materials, and is especially suited for projects that prioritise warmth, grounded authenticity, and deep cultural respect over tech-forward minimalism.
