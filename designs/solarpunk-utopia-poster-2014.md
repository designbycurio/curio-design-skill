---
version: 1

meta:
  id: solarpunk-utopia-poster-2014
  name: "Solarpunk Utopia Poster (2014)"
  description: "Art Nouveau botanical curves meet photovoltaic infrastructure on a deep emerald forest ground"
  isDark: false
  tags: [organic, narrative, bold, futuristic, decorative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2008 Tumblr emergence; visual identity crystallized 2014–2017"
  region: "English-language internet (Tumblr, Twitter); Brazilian-Portuguese early adopters; Berlin / NYC art scenes"
  regionZh: "英语互联网（Tumblr、Twitter）；巴西葡语社区早期参与者；柏林／纽约艺术圈"
  keyFigures: [Adam Flynn, Olivia Louise, Phoebe Wagner, Andrew Dana Hudson]
  movements: [Solarpunk, Art Nouveau permaculture, post-cyberpunk optimism]

introduction: |
  Solarpunk is the optimistic counter-movement to cyberpunk pessimism — a vision of ecological utopia where Alphonse Mucha's whiplash curves wrap around photovoltaic panels and vertical-axis wind turbines. Born on Tumblr around 2008 and crystallized by Adam Flynn's 2014 manifesto, the aesthetic imagines communal green-roof cities rendered in emerald, saffron, and terracotta poster art.

  This design system captures the community-garden poster feel: hand-drawn botanical borders, sunburst radials, deep emerald grounds, and humanist serif typography that echoes Art Nouveau print culture updated for a solarpunk 2035.
introductionZh: |
  太阳朋克是对赛博朋克悲观主义的乐观回应——一种生态乌托邦愿景，将阿尔丰斯·穆夏的鞭线曲线缠绕在光伏板和垂直轴风力发电机上。这一美学约2008年在Tumblr萌芽，2014年亚当·弗林的宣言使其成形，想象着以翡翠绿、藏红花黄和赤陶色海报艺术呈现的社区绿色屋顶城市。

  本设计系统捕捉社区花园海报的质感：手绘植物边框、太阳放射线、深翡翠底色，以及呼应新艺术运动印刷文化的人文主义衬线字体——为2035年的太阳朋克世界而更新。

colors:
  primary:    {"50": "#e6f5ed", "100": "#c2e6d4", "200": "#99d4b8", "300": "#6fc29c", "400": "#4ea882", "500": "#2D8B5C", "600": "#267a50", "700": "#1f6543", "800": "#185036", "900": "#123b29", "950": "#0a2319"}
  secondary:  {"50": "#fff8e0", "100": "#ffefb3", "200": "#ffe680", "300": "#ffdc4d", "400": "#ffcf3d", "500": "#FFC233", "600": "#e6ad2b", "700": "#bf9023", "800": "#99731c", "900": "#735615", "950": "#4d3a0e"}
  accent:     {"50": "#fdf0e8", "100": "#f9d9c5", "200": "#f4bf9e", "300": "#efa577", "400": "#e88e56", "500": "#D17A3F", "600": "#b86835", "700": "#99562c", "800": "#7a4523", "900": "#5c341a", "950": "#3d2211"}
  neutral:    {"50": "#f4f7f5", "100": "#e4ebe7", "200": "#c9d7cf", "300": "#adc3b7", "400": "#8dab9c", "500": "#6d9381", "600": "#587a6a", "700": "#456155", "800": "#344a41", "900": "#24342e", "950": "#141f1b"}
  semantic:
    success: { bg: "#2D8B5C", text: "#E8F0E5", light: "#c2e6d4", border: "#267a50" }
    warning: { bg: "#FFC233", text: "#1A2620", light: "#ffefb3", border: "#e6ad2b" }
    error:   { bg: "#c0392b", text: "#E8F0E5", light: "#f9d5d1", border: "#a33025" }
    info:    { bg: "#2980b9", text: "#E8F0E5", light: "#d4eaf7", border: "#216a9e" }
  background:
    page:    "#1A4D3E"
    surface: "#E8F0E5"
    subtle:  "#2D8B5C"
  text:
    primary:   "#1A2620"
    secondary: "#344a41"
    muted:     "#6d9381"
    inverse:   "#E8F0E5"

typography:
  families:
    heading: "'Lora', Georgia, serif"
    body:    "'Source Serif Pro', 'Source Serif 4', Georgia, serif"
    mono:    "'Caveat', cursive"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=Lora:ital,wght@0,400;0,600;0,700;1,400&family=Source+Serif+Pro:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap"
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
  radius: {none: "0", sm: "6px", md: "10px", lg: "14px", xl: "18px", full: "9999px"}
  color:  {default: "#2D8B5C", subtle: "#99d4b8", strong: "#1A4D3E", focus: "#FFC233"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(26,77,62,0.08)"
  sm: "0 2px 6px rgba(26,77,62,0.12)"
  md: "0 3px 14px rgba(26,77,62,0.20)"
  lg: "0 8px 24px rgba(26,77,62,0.22)"
  xl: "0 16px 40px rgba(26,77,62,0.26)"
  "2xl": "0 24px 56px rgba(26,77,62,0.30)"
  inner: "inset 0 1px 2px rgba(26,77,62,0.06)"
  focus: "0 0 0 3px rgba(255,194,51,0.45)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, glow]
  reducedMotion: true

composition:
  layout:        "flex"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#FFC233", color: "#1A4D3E", border: "none", shadow: "0 2px 6px rgba(26,77,62,0.12)", hoverBackground: "#e6ad2b", hoverShadow: "0 3px 14px rgba(26,77,62,0.20)", hoverColor: "#1A4D3E"}
    secondary: {background: "#2D8B5C", color: "#E8F0E5", border: "none", shadow: "0 2px 6px rgba(26,77,62,0.12)", hoverBackground: "#267a50", hoverShadow: "0 3px 14px rgba(26,77,62,0.20)", hoverColor: "#E8F0E5"}
    ghost:     {background: "transparent", color: "#2D8B5C", border: "1px solid #2D8B5C", shadow: "none", hoverBackground: "rgba(45,139,92,0.08)", hoverShadow: "none", hoverColor: "#1A4D3E"}
    danger:    {background: "#c0392b", color: "#E8F0E5", border: "none", shadow: "0 2px 6px rgba(192,57,43,0.18)", hoverBackground: "#a33025", hoverShadow: "0 3px 14px rgba(192,57,43,0.24)", hoverColor: "#E8F0E5"}
    sizes:     {sm: {height: "32px", padding: "6px 14px", fontSize: "0.875rem"}, md: {height: "40px", padding: "8px 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "12px 28px", fontSize: "1.125rem"}}
    borderRadius: "14px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#E8F0E5"
    color: "#1A2620"
    border: "1px solid #2D8B5C"
    borderRadius: "10px"
    padding: "10px 14px"
    focusBorder: "#FFC233"
    placeholderColor: "#6d9381"
  card:
    base:  {background: "#E8F0E5", border: "1px solid #2D8B5C", borderRadius: "18px", padding: "24px", shadow: "0 3px 14px rgba(26,77,62,0.20)"}
    hover: {shadow: "0 8px 24px rgba(26,77,62,0.22)", transform: "translateY(-2px)"}
---

# Solarpunk Utopia Poster (2014)

> Art Nouveau botanical curves meet photovoltaic infrastructure on a deep emerald forest ground — the community-garden poster for a 2035 ecological utopia.

## Origin

Solarpunk emerged on Tumblr around 2008 as an optimistic counter-movement to cyberpunk dystopia. The term crystallized with Adam Flynn's 2014 essay *Solarpunk: Notes Toward a Manifesto*, published on the Hieroglyph project. Artists like Olivia Louise created early poster art blending Alphonse Mucha's whiplash curves with photovoltaic panels and vertical-axis wind turbines, rendering communal green-roof cities in emerald, saffron, and terracotta.

By 2017, Phoebe Wagner and Brontë Christopher Wieland's *Sunvault* anthology codified the literary side, while Andrew Dana Hudson and Becky Chambers expanded the movement's reach. The visual language draws equally from Art Nouveau botanical illustration and permaculture infrastructure diagrams — mycorrhizal root networks rendered as decorative borders, solar panels framed by vine tendrils, community gardens as architectural footers.

## Overview

Composition cues:
- **Layout**: Flexible poster-style compositions with asymmetric organic flow
- **Content width**: Container-bound with generous section padding
- **Framing**: Bordered panels with botanical 1px green borders on pale sky-milk surfaces
- **Grid intensity**: Soft — organic curves break rigid grids while maintaining readable rhythm

## Colors

The palette is rooted in a deep emerald forest floor (`#1A4D3E`) as the page ground — not cream, not white, but the canopy-floor darkness of a thriving ecosystem. Against this, emerald foliage (`#2D8B5C`) provides mid-tone structure, saffron sun-burst (`#FFC233`) delivers solar energy and call-to-action warmth, and terracotta (`#D17A3F`) grounds the composition in clay-pot earthiness. Pale sky-milk (`#E8F0E5`) appears only on inset card surfaces, never as page background.

**Role usage**:
- Page background → `colors.background.page` (#1A4D3E deep emerald forest)
- Card / panel surfaces → `colors.background.surface` (#E8F0E5 pale sky-milk)
- Mid-tone panels → `colors.background.subtle` (#2D8B5C emerald foliage)
- Primary actions / solar highlights → `colors.secondary.500` (#FFC233 saffron)
- Structural borders / foliage elements → `colors.primary.500` (#2D8B5C emerald)
- Warm accents / clay-pot details → `colors.accent.500` (#D17A3F terracotta)
- Body text on light surfaces → `colors.text.primary` (#1A2620)
- Body text on dark surfaces → `colors.text.inverse` (#E8F0E5)

## Typography

The type voice channels Art Nouveau print culture updated for ecological optimism. Lora provides humanist serif headings with subtle bracketed terminals that echo Mucha's poster lettering. Source Serif Pro delivers readable body text with the warmth of letterpress. Caveat serves as the hand-drawn poster caption voice — used sparingly for annotations, pull-quotes, and decorative labels that feel sketched onto the composition.

**Text styles**:
- `display-xl` — Lora, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Lora, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Lora, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Source Serif Pro, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Source Serif Pro, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Caveat, 18px, weight 400, line-height 1.375, letter-spacing 0
- `mono-md` — Caveat, 16px, weight 700, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px rhythm
- Scale: 2px → 128px (12-step)
- Container max-width: 1280px (xl)
- Section padding: 64px (md) default, 96px (lg) for hero sections
- Grid gap: 24px between poster panels
- Card internal padding: 24px

## Elevation & Depth

Surfaces are layered like poster prints stacked on a deep emerald table. Cards float above the forest-ground page with warm green-tinted shadows. The shadow color uses `rgba(26,77,62,...)` — the page color at varying opacities — so elevation feels like depth within the canopy rather than generic grey drop-shadows.

- Surface style: layered (cards as poster panels on forest ground)
- Blur: none (sharp-edged poster aesthetic, no glass effects)
- Shadow ladder: xs (subtle lift) → 2xl (dramatic poster-float)
- Focus ring: saffron glow (`rgba(255,194,51,0.45)`) for solar-energy feedback

## Shapes

- Button radius: 14px (organic, rounded but not pill-shaped)
- Card radius: 18px (poster-panel softness)
- Input radius: 10px
- Small elements: 6px
- Full: 9999px (badges, avatars)

## Motion

Motion is restrained — like a poster that occasionally catches a breeze. Transitions are smooth but unhurried, reflecting the solarpunk ethos of patience and natural rhythm rather than frantic digital urgency.

- Level: restrained
- Default duration: 250ms
- Hover: lift (translateY -2px), tint (background shift), glow (shadow expansion)
- Easing: ease-out for reveals, spring for playful micro-interactions
- Reduced motion: respected — all animations collapse to instant

## Techniques

### Art Nouveau Vine Border

A botanical border frame using CSS gradients and border-image to evoke Mucha's decorative panel edges with emerald vine tendrils.

```css
.vine-border {
  border: 2px solid #2D8B5C;
  border-radius: 18px;
  background-image:
    radial-gradient(ellipse 60px 8px at 50% 0%, #2D8B5C 0%, transparent 70%),
    radial-gradient(ellipse 60px 8px at 50% 100%, #2D8B5C 0%, transparent 70%),
    radial-gradient(ellipse 8px 60px at 0% 50%, #2D8B5C 0%, transparent 70%),
    radial-gradient(ellipse 8px 60px at 100% 50%, #2D8B5C 0%, transparent 70%);
  background-repeat: no-repeat;
  background-size: 120px 12px, 120px 12px, 12px 120px, 12px 120px;
  background-position: center top, center bottom, left center, right center;
}
```

### Saffron Sunburst Radial

A radial sunburst pattern behind hero elements, evoking solar energy and photovoltaic panel highlights.

```css
.sunburst {
  background:
    repeating-conic-gradient(
      from 0deg,
      rgba(255, 194, 51, 0.12) 0deg 10deg,
      transparent 10deg 20deg
    );
  border-radius: 50%;
  position: absolute;
  inset: -20%;
  z-index: 0;
  pointer-events: none;
}
```

### Paper-Grain Poster Texture

A subtle noise overlay that gives surfaces the tactile feel of letterpress poster stock.

```css
.poster-grain {
  position: relative;
}
.poster-grain::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  mix-blend-mode: overlay;
}
```

## Iconography

Icons use Lucide's linear style with 1.5px stroke weight, rendered in emerald or inverse depending on surface. The linear treatment echoes hand-drawn botanical illustration line work — technical but organic, precise but warm.

- Treatment: linear (hand-drawn feel)
- Set: Lucide
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use deep emerald (#1A4D3E) as the page ground — the forest floor is the canvas
- Pair saffron (#FFC233) with emerald for solar-energy call-to-action contrast
- Include terracotta (#D17A3F) accents to prevent a mono-green palette
- Frame content in bordered poster panels with botanical border details
- Let typography breathe with generous line-height and section padding

### ✗ Don't
- Use cream, beige, or pale-yellow as page background (page is deep emerald)
- Conflate with cyberpunk neon dystopia (solarpunk is the opposite)
- Apply greenwashing-ad sterility or clean stock photos on white
- Soften into cottagecore (solarpunk has hard tech infrastructure inside the curves)
- Use minimalist Scandinavian palette or sans-serif modernist body text
- Use stock photography or apocalypse/disaster framing
- Reduce to generic "eco" forest-green-only palette (must include saffron, terracotta)
- Adopt corporate sustainability brand-deck aesthetics

## Applications

This design system is ideal for community platforms, environmental project dashboards, cooperative tool interfaces, and editorial publications focused on climate optimism and ecological futures. The poster-panel composition works especially well for content-rich landing pages, event announcements, and storytelling layouts where each section feels like a page in an illustrated manifesto.
