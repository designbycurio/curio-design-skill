---
version: 1

meta:
  id: polish-poster-school-1960s
  name: Polish Poster School (1960s)
  description: "Hand-painted surrealist theatre posters on mustard and oxblood grounds — brush, collage, and wild lettering from behind the Iron Curtain"
  isDark: false
  tags: [bold, editorial, historical, decorative, experimental]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1960s peak (extended to 1980s, continuing influence today)"
  region: "Warsaw, Kraków — Poland"
  regionZh: "波兰华沙、克拉科夫"
  keyFigures: [Jan Lenica, Henryk Tomaszewski, Roman Cieslewicz, Waldemar Świerzy, Franciszek Starowieyski]
  movements: [Polish Poster School (Polska Szkoła Plakatu), post-WWII Polish graphic design, theatre poster tradition]

introduction: |
  The Polish Poster School emerged in 1960s Warsaw as a startling paradox — state-funded art that rejected state aesthetics. Under nominal communism, designers like Jan Lenica and Henryk Tomaszewski produced hand-painted, surrealist posters for theatre, film, and jazz that read more like gallery paintings than propaganda.

  This design system captures that painterly rebellion: mustard and oxblood grounds recalling gouache on toned paper, hand-drawn brush typography, collage composition over rigid grids, and the deliberate imperfection of ink on coarse stock.
introductionZh: |
  波兰海报学派诞生于 1960 年代的华沙，是冷战铁幕后最不像宣传品的国家艺术。杨·莱尼察、亨里克·托马谢夫斯基、罗曼·切希莱维奇等大师虽然端着国家剧院的饭碗，画出来的却是超现实主义画作——手绘笔触、拼贴剪影、癫狂的手写字母，为戏剧、爵士与马戏团招魂。

  本设计系统提炼了那份颜料味：芥末黄与牛血红交替铺底，刷痕体标题跃于粗纹纸上，版面拒绝网格而拥抱拼贴，一切锋利的数字感都被刻意磨去，只留下印刷厂里的手工温度。

colors:
  primary:
    "50": "#f9eded"
    "100": "#f0d4d4"
    "200": "#dca5a5"
    "300": "#c87676"
    "400": "#a44848"
    "500": "#7C2D2D"
    "600": "#682525"
    "700": "#541D1D"
    "800": "#401616"
    "900": "#2c0f0f"
    "950": "#1a0909"
  secondary:
    "50": "#e8ecf5"
    "100": "#c5cfe8"
    "200": "#8fa0d1"
    "300": "#5a72ba"
    "400": "#2e50a4"
    "500": "#1E3A8A"
    "600": "#193072"
    "700": "#14265b"
    "800": "#0f1c44"
    "900": "#0a122d"
    "950": "#05091a"
  accent:
    "50": "#fef2e6"
    "100": "#fddfc0"
    "200": "#fbbf80"
    "300": "#f99f40"
    "400": "#f37e14"
    "500": "#EA580C"
    "600": "#c24a0a"
    "700": "#9a3b08"
    "800": "#732c06"
    "900": "#4b1d04"
    "950": "#2d1102"
  neutral:
    "50": "#f5f0e4"
    "100": "#F0E8D8"
    "200": "#e0d4be"
    "300": "#c8b898"
    "400": "#b09c72"
    "500": "#9B7B1F"
    "600": "#7f651a"
    "700": "#634f14"
    "800": "#47390f"
    "900": "#2b230a"
    "950": "#171305"
  semantic:
    success: { bg: "#3a7a2d", text: "#F0E8D8", light: "#e8f0e4", border: "#3a7a2d" }
    warning: { bg: "#EA580C", text: "#F0E8D8", light: "#fef2e6", border: "#c24a0a" }
    error:   { bg: "#7C2D2D", text: "#F0E8D8", light: "#f9eded", border: "#682525" }
    info:    { bg: "#1E3A8A", text: "#F0E8D8", light: "#e8ecf5", border: "#193072" }
  background:
    page:    "#9B7B1F"
    surface: "#F0E8D8"
    subtle:  "#7C2D2D"
  text:
    primary:   "#0F0F0F"
    secondary: "#47390f"
    muted:     "#7f651a"
    inverse:   "#F0E8D8"

typography:
  families:
    heading: "'Abril Fatface', 'Georgia', serif"
    body:    "'Lora', 'Crimson Pro', serif"
    mono:    "'Caveat', 'Patrick Hand', cursive"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,700&family=Caveat:wght@400;500;600;700&display=swap"
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
  lineHeights: { tight: 1.1, snug: 1.3, normal: 1.5, relaxed: 1.625, loose: 1.8 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px", md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "2px", md: "4px", lg: "6px", xl: "8px", full: "9999px" }
  color:  { default: "#0F0F0F", subtle: "#A0522D", strong: "#0F0F0F", focus: "#1E3A8A" }
  width:  { thin: "1px", default: "2px", thick: "3px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  "2xl": "none"
  inner: "none"
  focus: "0 0 0 3px rgba(30,58,138,0.35)"

motion:
  level: "minimal"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.25, 0.46, 0.45, 0.94)"
  hoverPatterns: [opacity, tint, underline]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "solid"
  gridIntensity: "none"
  rhythm:        "8px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "tabler"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "2px"

components:
  button:
    primary:   { background: "#7C2D2D", color: "#F0E8D8", border: "2px solid #0F0F0F", shadow: "none", hoverBackground: "#541D1D", hoverShadow: "none", hoverColor: "#F0E8D8" }
    secondary: { background: "#9B7B1F", color: "#0F0F0F", border: "2px solid #0F0F0F", shadow: "none", hoverBackground: "#7f651a", hoverShadow: "none", hoverColor: "#0F0F0F" }
    ghost:     { background: "transparent", color: "#0F0F0F", border: "2px solid #0F0F0F", shadow: "none", hoverBackground: "#F0E8D8", hoverShadow: "none", hoverColor: "#0F0F0F" }
    danger:    { background: "#7C2D2D", color: "#F0E8D8", border: "2px solid #401616", shadow: "none", hoverBackground: "#682525", hoverShadow: "none", hoverColor: "#F0E8D8" }
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "0.75rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "0.875rem" }
      lg: { height: "48px", padding: "0 28px", fontSize: "1rem" }
    borderRadius: "6px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#F0E8D8"
    color: "#0F0F0F"
    border: "2px solid #A0522D"
    borderRadius: "4px"
    padding: "8px 12px"
    focusBorder: "2px solid #1E3A8A"
    placeholderColor: "#7f651a"
  card:
    base:  { background: "#F0E8D8", border: "2px solid #0F0F0F", borderRadius: "4px", padding: "24px", shadow: "none" }
    hover: { shadow: "none", transform: "translateY(-2px)" }
---

# Polish Poster School (1960s)

> Hand-painted surrealism on mustard and oxblood grounds — the theatre poster tradition that turned state patronage into avant-garde rebellion.

## Origin

The Polish Poster School (Polska Szkoła Plakatu) crystallized in the 1960s when Poland's communist government, seeking cultural prestige, gave graphic designers unusual creative latitude. Henryk Tomaszewski, considered the godfather of the movement, taught at the Warsaw Academy of Fine Arts and trained a generation — including Jan Lenica, Roman Cieslewicz, Waldemar Świerzy, and Franciszek Starowieyski — to treat the poster as an autonomous artwork rather than a commercial vehicle. State theatres, film distributors, jazz festivals, and circuses all commissioned posters, creating a pipeline of public art that reached millions.

The result was unlike any other Eastern Bloc graphic tradition. Where Soviet design was rigid and photographic, Polish posters were painterly, surrealist, and deeply personal. Lenica's *Wozzeck* (1964) combined insect anatomy with gothic lettering; Cieslewicz collaged photography into hallucinatory composites; Starowieyski drew baroque grotesques in sepia ink. The designers worked in gouache, ink, and crayon on coarse paper, embracing the visible hand of the maker — brush strokes, paper grain, registration wobble — as proof that art, not the machine, made the image.

## Overview

Composition cues:
- **Layout**: Collage-driven vertical stack — overlapping hand-cut silhouettes, not aligned columns
- **Content width**: Container-bound (1024–1280px), but internal elements overlap and break alignment intentionally
- **Framing**: Solid — heavy ink outlines and filled color blocks, not glass or gradient
- **Grid intensity**: None — collage composition rejects rigid grids; elements overlap, float, and cluster organically

## Colors

The palette is gouache on toned paper. Mustard yellow (#9B7B1F) serves as the dominant ground — the warm, slightly dirty yellow of cheap Polish poster board. Oxblood (#7C2D2D) alternates as a moody secondary ground and primary accent. Cadmium orange (#EA580C) provides the hand-painted heat of a Lenica brush stroke. Cobalt (#1E3A8A) supplies the cold surrealist counterpoint. Ink black (#0F0F0F) draws every outline. Aged paper (#F0E8D8) is the surface for content areas, not a background — more parchment than digital white.

**Role usage**:
- Page background → `colors.background.page` (mustard #9B7B1F)
- Content surface → `colors.background.surface` (aged paper #F0E8D8)
- Alternate section background → `colors.background.subtle` (oxblood #7C2D2D)
- Primary actions, CTAs → `colors.primary.500` (oxblood #7C2D2D)
- Surrealist accents, links → `colors.secondary.500` (cobalt #1E3A8A)
- Hand-painted highlights, badges → `colors.accent.500` (cadmium orange #EA580C)
- Body text, outlines → `colors.text.primary` (ink black #0F0F0F)
- Inverse text on dark grounds → `colors.text.inverse` (aged paper #F0E8D8)

## Typography

Typography in the Polish Poster School is hand-painted, theatrical, and deliberately rough. Display titles should feel like they were brushed onto paper with a loaded sable — heavy, serif, slightly irregular. Abril Fatface provides that theatrical weight for headlines, channeling the fat-face poster type of 19th-century playbills that Polish designers revived. Lora handles body copy with an organic warmth that avoids the clinical feel of geometric sans-serifs. Caveat provides the hand-lettered accent voice — margin notes, annotations, the artist's personal touch.

**Text styles**:
- `display-xl` — Abril Fatface, 96px, weight 400, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Abril Fatface, 64px, weight 400, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Abril Fatface, 48px, weight 400, line-height 1.1, letter-spacing 0
- `body-lg` — Lora, 18px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — Lora, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Lora, 12px, weight 500, line-height 1.3, letter-spacing 0.05em
- `mono-md` — Caveat, 16px, weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px (poster proportions, not pixel-precise UI grids)
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Grid gap: 16–24px between content blocks, but expect overlapping elements to break gap rhythm
- Section padding: 64px vertical (md), 96–128px on larger viewports
- Rhythm: 8px — looser than Swiss 4px, matching the hand-drawn imprecision

## Elevation & Depth

Paint on paper has no shadows. Polish posters achieve depth through overlap, color contrast, and the physical layering of collage — a hand-cut silhouette sitting atop a brushed ground, ink lines drawn over dried gouache. This system uses zero box-shadows. Depth comes from border weight, color blocking, and z-index stacking of overlapping elements.

- Surface style: flat — paint on paper, no digital layering
- Blur: none (0px throughout)
- Shadow ladder: all `none` — depth is achieved through collage overlap and border contrast, not cast shadow
- Hover interaction: opacity shift and subtle vertical lift (translateY), no shadow animation

## Shapes

- `sm`: 2px (barely perceptible hand-wobble)
- `md`: 4px (card corners — slight softness as if paper was cut by hand)
- `lg`: 6px (button corners — deliberate hand-irregular rounding per brief)
- `xl`: 8px (large containers)
- `full`: 9999px (circular badges, painted dot motifs)

## Motion

Polish posters are static objects — ink on paper, pinned to a kiosk wall. Motion in this system is minimal and deliberate: state changes communicate function, not personality. Nothing bounces, nothing springs. Transitions are quick opacity shifts or gentle position changes, like turning a page in a portfolio.

- Level: minimal
- Durations: fast 120ms, normal 250ms, slow 400ms
- Easings: standard ease-out; no spring or bounce
- Hover patterns: opacity fade, background tint shift, underline reveal
- `prefers-reduced-motion`: fully respected

## Techniques

### Mustard-ground theatre title

A full-width section with the mustard page background exposed, featuring a large Abril Fatface title with visible brush-texture simulation via a subtle text-shadow offset — evoking hand-painted poster lettering.

```css
.theatre-title {
  background-color: #9B7B1F;
  padding: 96px 48px;
  font-family: 'Abril Fatface', Georgia, serif;
  font-size: clamp(3rem, 8vw, 6rem);
  color: #0F0F0F;
  line-height: 1.0;
  text-shadow: 2px 2px 0 #A0522D, -1px -1px 0 rgba(234,88,12,0.25);
  position: relative;
}
.theatre-title::after {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='200' height='200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/%3E%3C/svg%3E");
  pointer-events: none;
  mix-blend-mode: multiply;
}
```

### Oxblood collage card

A card component styled as a hand-cut paper element on an oxblood ground — thick ink border with slightly uneven width (achieved via border-image), aged-paper surface, and a subtle rotation to break digital grid rigidity.

```css
.collage-card {
  background-color: #F0E8D8;
  border: 3px solid #0F0F0F;
  border-radius: 4px;
  padding: 32px;
  position: relative;
  transform: rotate(-1.2deg);
  transition: transform 250ms cubic-bezier(0, 0, 0.2, 1);
}
.collage-card:hover {
  transform: rotate(0deg) translateY(-4px);
}
.collage-card::before {
  content: '';
  position: absolute;
  top: -6px;
  left: -6px;
  right: -6px;
  bottom: -6px;
  background-color: #7C2D2D;
  z-index: -1;
  border-radius: 6px;
}
```

### Crayon underline accent

A hand-drawn-style underline for emphasis text, simulating a crayon stroke beneath key words using a wavy SVG border-image in cadmium orange. Used for links, highlighted terms, and section subtitles.

```css
.crayon-underline {
  text-decoration: none;
  background-image: url("data:image/svg+xml,%3Csvg width='100' height='8' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 6 Q10 2 20 5 T40 4 T60 6 T80 3 T100 5' fill='none' stroke='%23EA580C' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: repeat-x;
  background-position: 0 100%;
  background-size: 100px 8px;
  padding-bottom: 6px;
}
.crayon-underline:hover {
  background-image: url("data:image/svg+xml,%3Csvg width='100' height='8' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 6 Q10 2 20 5 T40 4 T60 6 T80 3 T100 5' fill='none' stroke='%231E3A8A' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E");
}
```

## Iconography

Icons should feel hand-drawn and slightly rough, as if sketched in ink on poster stock. Tabler icons provide the right weight and openness — their 2px strokes and generous negative space feel closer to pen illustration than to pixel-perfect UI glyphs. Avoid filled or duotone treatments; the poster tradition is line-art and silhouette.

- Treatment: linear (stroke only)
- Set: Tabler (open, hand-drawn feel)
- Stroke: 2px, round caps, round joins

## Do's & Don'ts

### ✓ Do
- Use oxblood (#7C2D2D) for primary actions and mustard (#9B7B1F) for page grounds
- Let Abril Fatface titles dominate — large, theatrical, unapologetic
- Embrace collage composition — overlap elements, break alignment, rotate cards slightly
- Apply paper texture and brush-stroke effects to reinforce the hand-painted origin
- Mix Caveat hand-lettering with Lora body text for visual tension between polish and rawness

### ✗ Don't
- Use clean modernist sans-serifs — this is the anti-Swiss-Style
- Seek geometric perfection — hand-imperfection is the brand
- Use white or pure cream backgrounds — use mustard or aged paper
- Apply SaaS gradients or glassmorphism effects
- Use pastel colors — every pigment should feel full-strength, like gouache from the tube
- Impose 12-column grids — use collage composition instead
- Use stock photography — only surrealist hand-drawn or collaged imagery

## Applications

This system is built for cultural institutions, theatre companies, film festivals, jazz venues, gallery websites, and editorial publications that want to project artistic seriousness without corporate sterility. It works powerfully for event posters, exhibition sites, arts magazines, and creative portfolios where the hand-made quality signals authenticity. The deliberately anti-digital aesthetic also suits indie publishers, art bookshops, and any brand that positions itself against the clean-tech mainstream.
