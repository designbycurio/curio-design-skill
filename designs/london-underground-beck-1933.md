---
version: 1

meta:
  id: london-underground-beck-1933
  name: Tube Map (Beck)
  description: Harry Beck's 1933 Underground diagram as a design system — orthogonal-diagonal lines, roundel anchors, and crisp Johnston humanist type on a cooled printed card.
  isDark: false
  tags: [modernist, geometric, technical, professional, editorial]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1900–1950 (diagram first published January 1933; visual system maintained to present)"
  region: "London, United Kingdom"
  regionZh: "英国伦敦"
  keyFigures: [Harry Beck, Edward Johnston, London Transport / TfL]
  movements: [Information design, Modernist diagrammatic abstraction, Schematic cartography]

introduction: |
  In January 1933 a London Transport engineering draughtsman named Harry Beck
  redrew the Underground not as geography but as a circuit board: coloured lines
  running only at 0°, 45° and 90°, stations spaced evenly, interchanges marked by
  blobs and ticks. It threw away scale and kept only connection — and it worked so
  well it became the template for transit maps worldwide.

  The system pairs that diagrammatic discipline with Edward Johnston's 1916
  sans-serif and the red-ring, blue-bar roundel. The result is calm, exact, and
  unmistakably London: nothing decorative, every element load-bearing, every line
  legible at a glance on a pale pocket card.
introductionZh: |
  1933 年 1 月，伦敦地铁的制图员哈里·贝克把错综的线路图彻底重画了一遍——他不再
  照地理画，而是像画电路板：所有线路只走 0°、45° 和 90°，站点间距均等，换乘点用
  圆点和短杠标出。他扔掉了真实比例，只留下「怎么换乘」这一件事，结果反而清晰到成了
  全世界地铁图的范本。

  这套系统的另一半是爱德华·约翰斯顿 1916 年设计的无衬线字体，以及那个红圈蓝杠的
  「roundel」标志。整体气质冷静、精确、毫无多余装饰：每根线都有用，每个字都看得清，
  在一张偏冷的浅色卡片上一目了然。这就是信息设计的一座里程碑，也是伦敦的视觉名片。

colors:
  primary:    {"50": "#E6EBF3", "100": "#C2CFE3", "200": "#9AAFCF", "300": "#6E89B5", "400": "#3D5E97", "500": "#003688", "600": "#002F77", "700": "#002662", "800": "#001E4E", "900": "#00163A", "950": "#000E26"}
  secondary:  {"50": "#FDEAE8", "100": "#FACBC6", "200": "#F5A39B", "300": "#EF7468", "400": "#EA4839", "500": "#E32017", "600": "#C31A13", "700": "#9E150F", "800": "#7A100B", "900": "#560B08", "950": "#350605"}
  accent:     {"50": "#FFFBE6", "100": "#FFF6B8", "200": "#FFEF85", "300": "#FFE852", "400": "#FFE029", "500": "#FFD300", "600": "#D9B400", "700": "#B39500", "800": "#8C7500", "900": "#665400", "950": "#403400"}
  neutral:    {"50": "#F8F9FA", "100": "#F4F5F7", "200": "#EAE7DF", "300": "#D4D6DB", "400": "#A9ACB4", "500": "#7E828C", "600": "#5C6069", "700": "#43464D", "800": "#2A2C31", "900": "#1C1C1C", "950": "#101012"}
  semantic:
    success: { bg: "#E6F2EA", text: "#00782A", light: "#D9EBDF", border: "#00782A" }
    warning: { bg: "#FFF6E0", text: "#B36305", light: "#FBEAC6", border: "#B36305" }
    error:   { bg: "#FDEAE8", text: "#E32017", light: "#F8D2CE", border: "#E32017" }
    info:    { bg: "#E6EBF3", text: "#003688", light: "#D0DAEB", border: "#003688" }
  background:
    page:    "#F4F5F7"
    surface: "#FFFFFF"
    subtle:  "#EAE7DF"
  text:
    primary:   "#1C1C1C"
    secondary: "#43464D"
    muted:     "#7E828C"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Railway', 'Johnston', 'Nunito Sans', sans-serif"
    body:    "'Nunito Sans', 'Mukta', sans-serif"
    mono:    "'Roboto Mono', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,600;0,6..12,700;0,6..12,800&family=Mukta:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap"
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
  radius: {none: "0", sm: "2px", md: "4px", lg: "8px", xl: "16px", full: "9999px"}
  color:  {default: "#D4D6DB", subtle: "#EAE7DF", strong: "#1C1C1C", focus: "#003688"}
  width:  {thin: "1px", default: "2px", thick: "6px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,22,58,0.05)"
  sm: "0 1px 3px rgba(0,22,58,0.08)"
  md: "0 2px 6px rgba(0,22,58,0.10)"
  lg: "0 6px 16px rgba(0,22,58,0.12)"
  xl: "0 12px 28px rgba(0,22,58,0.14)"
  "2xl": "0 20px 48px rgba(0,22,58,0.16)"
  inner: "inset 0 1px 2px rgba(0,22,58,0.06)"
  focus: "0 0 0 3px rgba(0,54,136,0.35)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [stroke, tint, lift]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: soft
  rhythm:        8px

surfaceStyle: flat
blur:         none

iconography:
  treatment: linear
  set:       custom
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#003688", color: "#FFFFFF", border: "2px solid #003688", shadow: "none", hoverBackground: "#002662", hoverShadow: "0 2px 6px rgba(0,22,58,0.10)", hoverColor: "#FFFFFF"}
    secondary: {background: "#FFFFFF", color: "#003688", border: "2px solid #003688", shadow: "none", hoverBackground: "#E6EBF3", hoverShadow: "none", hoverColor: "#002662"}
    ghost:     {background: "transparent", color: "#1C1C1C", border: "2px solid transparent", shadow: "none", hoverBackground: "#EAE7DF", hoverShadow: "none", hoverColor: "#003688"}
    danger:    {background: "#E32017", color: "#FFFFFF", border: "2px solid #E32017", shadow: "none", hoverBackground: "#C31A13", hoverShadow: "0 2px 6px rgba(227,32,23,0.18)", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "52px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "4px"
    fontWeight: 700
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1C1C1C"
    border: "2px solid #D4D6DB"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "2px solid #003688"
    placeholderColor: "#A9ACB4"
  card:
    base:  {background: "#FFFFFF", border: "2px solid #EAE7DF", borderRadius: "8px", padding: "24px", shadow: "0 1px 3px rgba(0,22,58,0.08)"}
    hover: {shadow: "0 6px 16px rgba(0,22,58,0.12)", transform: "translateY(-2px)"}
---

# Tube Map (Beck)

> The London Underground diagram reborn as a design system — orthogonal lines, roundel anchors, and Johnston humanist type on a cooled printed card.

## Origin
In January 1933 Harry Beck, a temporary draughtsman in London Underground's signals office, redrew the network as an electrical schematic rather than a geographic map. He fixed every line to 0°, 45° or 90°, spaced stations evenly regardless of true distance, and marked interchanges with blobs and ticks. London Transport printed it as a folding pocket card; commuters took 750,000 copies in the first month. The diagram had abandoned scale and kept only the one thing a traveller needs — how the lines connect.

The visual language draws on Edward Johnston's 1916 typeface, commissioned by Frank Pick to unify the Underground's identity, and the bar-and-circle roundel that anchors every sign and map. TfL still maintains a formal colour standard for each line. The whole system is a foundational monument of information design: geometric, ruthlessly legible, and copied by transit authorities the world over, yet still unmistakably London.

## Overview
Composition cues:
- **Layout**: Grid-driven, aligned to an 8px rhythm with lines and connectors snapping to 0/45/90 angles.
- **Content width**: Centered `container` — the diagram-card metaphor, not full-bleed sprawl.
- **Framing**: Bordered — crisp 2px rules and panel outlines, no soft drop-shadow drama.
- **Grid intensity**: Soft — present and ordering, never a heavy visible mesh.

## Colors
The palette is the TfL line standard: a deep Piccadilly blue leads, the Central red and roundel ring carry emphasis, and Circle yellow accents. Everything sits on a cooled neutral card tone rather than bright white, with near-black reserved for labels. Lines are saturated and confident; surfaces stay quiet so the coloured strokes read first.

**Role usage**:
- Page background → `colors.background.page` (`#F4F5F7`)
- Aged-card panels & section bands → `colors.background.subtle` (`#EAE7DF`)
- Primary actions / link lines / roundel bar → `colors.primary.500` (`#003688`)
- Emphasis, alerts, roundel ring → `colors.secondary.500` (`#E32017`)
- Highlights / Circle-line accents → `colors.accent.500` (`#FFD300`)
- Body & heading labels → `colors.text.primary` (`#1C1C1C`)
- Hairline connectors / dividers → `colors.borders.color.default` (`#D4D6DB`)

## Typography
The voice is Johnston humanist: even-weight strokes, a true geometric `o`, generous counters, set with confidence and a touch of letter-spacing on labels. Headings are plain and structural — no condensed drama — because the diagram's authority comes from clarity, not flourish.

**Text styles**:
- `display-xl` — Railway/Johnston, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Railway/Johnston, 64px, weight 700, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Railway/Johnston, 36px, weight 700, line-height 1.15, letter-spacing -0.01em
- `body-lg` — Nunito Sans, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Nunito Sans, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Nunito Sans, 12px, weight 600, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Roboto Mono, 14px, weight 500, line-height 1.5, letter-spacing 0 (station codes, fares, timetables)

## Spacing & Layout
- Base unit 4px; rhythm locked to 8px for diagram alignment.
- Scale: 2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128px.
- Container max `1280px`; default reading column at `lg` (1024px).
- Section padding 64–96px vertical; equal inter-element spacing echoes the diagram's even station gaps.

## Elevation & Depth
The map is a flat printed card, so materiality is restrained: surfaces are matte, separation comes from 2px borders and hairline rules rather than blur or glass. Shadows are tinted with the Piccadilly blue and kept subtle — used to float a card off the page, never to fake glassmorphism.

- Surface style: flat, opaque, paper-like.
- Blur: none.
- Shadow ladder: `xs` for resting cards → `lg`/`xl` for hovered or modal panels, all in low-alpha `rgba(0,22,58,…)`.

## Shapes
- Corner radii small: 2px (sm), 4px (md, buttons/inputs), 8px (lg, cards), 16px (xl).
- `full` (9999px) reserved for roundel marks, interchange blobs, and pill tags.
- Default border width 2px — the line-weight of the diagram itself.

## Motion
Movement is restrained and mechanical, like a train easing into a station: short, eased, purposeful. Hover states change stroke colour or add a quiet tint; transitions never overshoot except for a single optional spring on interactive markers. Respect `prefers-reduced-motion`.

- Level: restrained.
- Durations: 120ms (fast) for hovers, 250ms (normal) for state changes, 400ms (slow) for panels.
- Easings: standard `cubic-bezier(0.4,0,0.2,1)` default; `out` for entrances.
- Hover patterns: stroke (border colour shift), tint (background wash), lift (2px translate).

## Techniques

### Roundel mark
The bar-and-circle Underground logotype: a red ring crossed by a blue bar carrying a label.
```css
.roundel {
  --ring: #E32017;
  --bar: #003688;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 96px;
  height: 96px;
  border: 14px solid var(--ring);
  border-radius: 9999px;
}
.roundel::after {
  content: attr(data-label);
  position: absolute;
  left: -14px;
  right: -14px;
  padding: 6px 0;
  background: var(--bar);
  color: #fff;
  font-family: 'Railway', 'Johnston', 'Nunito Sans', sans-serif;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-align: center;
  text-transform: uppercase;
}
```

### Orthogonal-diagonal line rule
Connectors and dividers that obey Beck's 0/45/90 law, drawn as coloured strokes with mitred joints.
```css
.tube-line {
  height: 8px;
  border-radius: 9999px;
  background: linear-gradient(90deg, #003688 0 50%, #E32017 50% 100%);
}
.tube-line--diag {
  width: 160px;
  transform: rotate(-45deg);
  transform-origin: left center;
}
.tube-corner { /* the only permitted turn: a 45° elbow */
  width: 48px;
  height: 48px;
  border-bottom: 8px solid #00782A;
  border-right: 8px solid #00782A;
  border-bottom-right-radius: 12px;
}
```

### Interchange marker (blob & tick)
The white-filled blob for an interchange, the small tick for a single-line stop.
```css
.station-blob {
  width: 18px;
  height: 18px;
  background: #FFFFFF;
  border: 3px solid #1C1C1C;
  border-radius: 9999px;
}
.station-tick {
  width: 3px;
  height: 14px;
  background: #1C1C1C;
}
```

## Iconography
Icons are linear and Johnston-flat: even 2px strokes, square-cut ends, simple geometric forms that sit beside the type as if printed on the same card. Favour a custom transit-flavoured set built around the roundel, directional arrows, and station marks; keep filled shapes for the blobs and roundel only.

- Treatment: linear, 2px stroke, no gradients.
- Set: custom (roundel / transit motifs), or a clean linear fallback.
- Stroke: 2px, matching diagram line weight.

## Do's & Don'ts
### ✓ Do
- Use Piccadilly blue `#003688` for primary actions, links, and the roundel bar.
- Lock connectors, dividers, and decorative lines to 0°, 45° and 90° only.
- Set headings in Johnston-humanist type (Railway/Johnston), body in Nunito Sans / Mukta.
- Anchor layouts with the red-ring / blue-bar roundel and even, diagram-like spacing.
- Keep surfaces flat and matte on the cooled `#F4F5F7` card ground.

### ✗ Don't
- Never use cream/ivory or plain-white page backgrounds — use the cooled card tones, not lazy white.
- No Inter or generic geometric sans; the type must read as Johnston humanist.
- No diagonal angles other than 45°; lines stay orthogonal or diagonal only.
- No realistic geography or photographic textures — it is a pure schematic.

## Applications
Best for transit and wayfinding UIs, data dashboards and network diagrams, technical documentation, and editorial pieces that prize legibility and structure. The system shines wherever clarity, ordered grids, and confident colour-coded lines matter more than ornament.
