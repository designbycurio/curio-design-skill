---
version: 1

meta:
  id: swiss-rail-sbb-clock-1944
  name: Swiss Railway Clock
  description: Vitreous-enamel precision in black, white, and one decisive signal red.
  isDark: false
  tags: [modernist, minimal, professional, geometric, technical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1944 (clock designed); SBB visual system current ~2000s–present"
  region: "Switzerland (SBB Swiss Federal Railways)"
  regionZh: "瑞士（瑞士联邦铁路 SBB）"
  keyFigures: [Hans Hilfiker, Mondaine]
  movements: [Swiss / International Typographic Style, Functionalist transport design]

introduction: |
  In 1944 SBB engineer Hans Hilfiker drew a station clock so legible it became
  a national instrument: a white vitreous-enamel dial, black baton markers, and
  a single red second hand carrying a round signal-disc paddle. Nothing on it is
  decorative — every element answers the question "what time is the train."

  This system rebuilds that logic for the screen. High black-and-white contrast,
  hard edges, tabular Helvetica-grade type, and exactly one red. The red leads;
  everything else recedes. Precision is the brand, and restraint is the technique.
introductionZh: |
  1944 年，瑞士联邦铁路的工程师汉斯·希尔菲克设计了一面车站时钟，清晰到成了一件
  国民器物：白色珐琅表盘、黑色矩形刻度、一根顶着圆形信号桨片的红色秒针。盘面上没有
  任何装饰，每个元素只回答一个问题——下一班车几点。

  这套系统把那种逻辑搬到屏幕上。极致的黑白对比、硬朗的边缘、表格般规整的字体排印，
  以及唯一的一抹红。红色主导一切，其余尽数后退。精准就是品牌，克制就是手法。

colors:
  primary:    {"50": "#FFE5E5", "100": "#FFB8B8", "200": "#FF8585", "300": "#FF4D4D", "400": "#F71F1F", "500": "#EB0000", "600": "#C70000", "700": "#A30000", "800": "#7A0000", "900": "#520000", "950": "#2E0000"}
  secondary:  {"50": "#F7F7F7", "100": "#E4E4E2", "200": "#CACAC8", "300": "#AEAEAC", "400": "#9A9A98", "500": "#7C7C7A", "600": "#5E5E5C", "700": "#454543", "800": "#2C2C2A", "900": "#1A1A1A", "950": "#000000"}
  accent:     {"50": "#FFE5E5", "100": "#FFB8B8", "200": "#FF8585", "300": "#FF4D4D", "400": "#F71F1F", "500": "#EB0000", "600": "#C70000", "700": "#A30000", "800": "#7A0000", "900": "#520000", "950": "#2E0000"}
  neutral:    {"50": "#F4F4F2", "100": "#E4E4E2", "200": "#D2D2D0", "300": "#B8B8B6", "400": "#9A9A98", "500": "#787876", "600": "#565654", "700": "#3A3A38", "800": "#1A1A1A", "900": "#0D0D0D", "950": "#000000"}
  semantic:
    success: { bg: "#E6F4EA", text: "#1E6B33", light: "#F2FAF4", border: "#BFE0C9" }
    warning: { bg: "#FBF0E0", text: "#8A5A00", light: "#FDF8EF", border: "#EAD3A8" }
    error:   { bg: "#FFE5E5", text: "#A30000", light: "#FFF2F2", border: "#FFB8B8" }
    info:    { bg: "#EAEAEA", text: "#1A1A1A", light: "#F4F4F2", border: "#D2D2D0" }
  background:
    page:    "#F4F4F2"
    surface: "#FFFFFF"
    subtle:  "#E4E4E2"
  text:
    primary:   "#1A1A1A"
    secondary: "#565654"
    muted:     "#9A9A98"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Archivo', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    body:    "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    mono:    "'Inter', 'Helvetica Neue', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap"
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
  radius: {none: "0", sm: "0", md: "1px", lg: "2px", xl: "4px", full: "9999px"}
  color:  {default: "#1A1A1A", subtle: "#D2D2D0", strong: "#000000", focus: "#EB0000"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "0 0 0 1px rgba(26,26,26,0.08)"
  md: "0 0 0 1px rgba(26,26,26,0.12)"
  lg: "0 1px 0 0 rgba(0,0,0,0.16)"
  xl: "0 2px 0 0 rgba(0,0,0,0.20)"
  "2xl": "0 0 0 2px rgba(26,26,26,0.16)"
  inner: "inset 0 0 0 1px rgba(26,26,26,0.10)"
  focus: "0 0 0 3px rgba(235,0,0,0.30)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [stroke, tint, underline]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        "8px"

surfaceStyle: flat
blur:         none

iconography:
  treatment: linear
  set:       lucide
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#EB0000", color: "#FFFFFF", border: "1px solid #EB0000", shadow: "none", hoverBackground: "#C70000", hoverShadow: "none", hoverColor: "#FFFFFF"}
    secondary: {background: "#1A1A1A", color: "#FFFFFF", border: "1px solid #1A1A1A", shadow: "none", hoverBackground: "#000000", hoverShadow: "none", hoverColor: "#FFFFFF"}
    ghost:     {background: "transparent", color: "#1A1A1A", border: "1px solid #1A1A1A", shadow: "none", hoverBackground: "#1A1A1A", hoverShadow: "none", hoverColor: "#FFFFFF"}
    danger:    {background: "#A30000", color: "#FFFFFF", border: "1px solid #A30000", shadow: "none", hoverBackground: "#7A0000", hoverShadow: "none", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "0 16px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 24px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 32px", fontSize: "1.125rem"}}
    borderRadius: "0"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFFFFF"
    color: "#1A1A1A"
    border: "1px solid #1A1A1A"
    borderRadius: "0"
    padding: "10px 14px"
    focusBorder: "1px solid #EB0000"
    placeholderColor: "#9A9A98"
  card:
    base:  {background: "#FFFFFF", border: "1px solid #1A1A1A", borderRadius: "0", padding: "24px", shadow: "none"}
    hover: {shadow: "none", transform: "none"}
---

# Swiss Railway Clock

> Vitreous-enamel precision in black, white, and one decisive signal red.

## Origin
In 1944 Hans Hilfiker, an engineer at the Swiss Federal Railways (SBB), designed a station clock to make platform time unmistakable at a glance. The dial is white vitreous enamel, the hour and minute markers are black batons, and a single bright red second hand sweeps the face — tipped with a round signal disc that echoes a railway guard's paddle. The hand pauses briefly at the top of each minute, waiting for the master clock's impulse, a behavior as recognizable as the form itself.

The clock became inseparable from SBB's identity and, through a long licensing partnership with Mondaine, a globally collected wristwatch. It is a textbook artifact of the Swiss / International Typographic Style: function first, ornament never, geometry exact. Its discipline — high contrast, grotesque type, rigid grids, and exactly one accent color — is the blueprint this system follows.

## Overview
Composition cues:
- **Layout**: Strict orthogonal grid; everything snaps to an 8px rhythm with hairline rules.
- **Content width**: Centered container, generous margins, timetable-like columns.
- **Framing**: Bordered surfaces — 1px black keylines, no fills, no float.
- **Grid intensity**: Strong; the grid is visible structure, not a hidden aid.

## Colors
The palette is a near-monochrome of black on cool enamel white, interrupted by exactly one red. #EB0000 is the official SBB brand red, reserved for the single most decisive element on any view — never decoration, always direction. The whites are cool and vitreous (#F4F4F2, never cream), and gray (#9A9A98) carries only secondary marks.

**Role usage**:
- Page background → `colors.background.page` (#F4F4F2)
- Card / dial surface → `colors.background.surface` (#FFFFFF)
- Primary text & markers → `colors.text.primary` (#1A1A1A)
- The single accent → `colors.primary.500` (#EB0000)
- Secondary marks / rules → `colors.neutral.400` (#9A9A98)
- Hairline borders → `colors.borders.color.default` (#1A1A1A)
- Subtle dividers → `colors.background.subtle` (#E4E4E2)

## Typography
The voice is grotesque and tabular: even color, tight grids, no flourish. Archivo carries headings and bold numerals with its rail-signage weight; Inter handles body, UI, and schedule rows with neutral clarity. Helvetica Neue is the canonical reference face the system emulates. Numbers align in monospaced columns like a departures board.

**Text styles**:
- `display-xl` — Archivo, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Archivo, 64px, weight 700, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Archivo, 36px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Inter, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 12px, weight 600, line-height 1.375, letter-spacing 0.05em, uppercase
- `mono-md` — Inter (tabular-nums), 16px, weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit 4px; primary rhythm on the 8px grid.
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container max 1280px, centered, with timetable-style column gaps.
- Section padding 64–128px vertical; content kept on hairline-aligned columns.

## Elevation & Depth
The world is flat enamel. There is no depth, only edges: separation comes from 1px black keylines and white-on-cool-white surface shifts, never from shadow or blur. Where a "shadow" token exists it is a hairline ring, not a soft drop.

- Surface style: flat, fully opaque, hard-edged.
- Blur: none.
- Shadow ladder: none → hairline ring → 2px ring; no soft drop shadows anywhere.

## Shapes
- Corner radii effectively zero — sharp rectangles are the rule.
- `sm`/`md`/`lg` radii cap at 0–2px for incidental softening only.
- `full` (9999px) reserved exclusively for circular dial/disc motifs and the red paddle tip.

## Motion
Motion is mechanical and exact, like the clock's impulse-driven sweep: brief, eased, decisive — never bouncy or playful. Hover states change stroke, tint, or underline rather than lift or scale. The one signature flourish is a red second-hand sweep that pauses at the top.

- Level: restrained.
- Durations: 120ms fast, 250ms normal, 400ms slow.
- Easings: standard cubic-bezier for UI; a stop-pause sweep for the clock motif.
- Hover patterns: stroke (border darkens), tint (red appears), underline.

## Techniques
### Red second-hand sweep
The signature clock motion — a sweep that overshoots a full turn then pauses at top, like Hilfiker's impulse clock.
```css
.clock-second {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 2px;
  height: 50%;
  background: #EB0000;
  transform-origin: bottom center;
  animation: sbb-sweep 60s steps(60, end) infinite;
}
.clock-second::after {
  content: "";
  position: absolute;
  top: 12%;
  left: 50%;
  width: 14px;
  height: 14px;
  border-radius: 9999px;
  background: #EB0000;
  transform: translateX(-50%);
}
@keyframes sbb-sweep {
  to { transform: rotate(360deg); }
}
```

### Hairline keyline frame
The bordered-surface idiom — flat white panels separated only by 1px black rules, no shadow.
```css
.sbb-panel {
  background: #FFFFFF;
  border: 1px solid #1A1A1A;
  border-radius: 0;
  box-shadow: none;
}
.sbb-panel + .sbb-panel {
  border-top: none; /* shared hairline, like timetable rows */
}
```

### Signal-red lead accent
Exactly one red element per view, set against pure black-and-white to read as direction, not decoration.
```css
.sbb-lead {
  color: #EB0000;
  border-left: 4px solid #EB0000;
  padding-left: 12px;
  font-weight: 700;
  letter-spacing: -0.02em;
}
```

## Iconography
Icons are crisp linear glyphs on a strict grid, matched to the 2px hairline weight of the system. Use a geometric grotesque set (Lucide) with no fills, no rounded corners beyond the form's own geometry, and black strokes — red only when an icon is the single lead element on its view.

- Treatment: linear, uniform 2px stroke.
- Set: Lucide.
- Stroke: 2px, square joins.

## Do's & Don'ts
### ✓ Do
- Use SBB red (#EB0000) for exactly one decisive element per view.
- Keep the ground cool vitreous white (#F4F4F2) — clean, never warm.
- Separate surfaces with 1px black keylines, not shadows.
- Set type in Archivo/Inter with tabular numerals and tight grids.
- Square every corner except true dial and disc motifs.

### ✗ Don't
- Never use cream/ivory or warm paper white — the dial is cool vitreous enamel.
- No additional accent colors; only the single SBB red leads, on black-and-white.
- No soft shadows, gradients, rounded card UI, or decorative flourishes.
- No serif or handwritten type; the system is strictly grotesque/Helvetica precision.

## Applications
Best for transit and timetable interfaces, dashboards, technical documentation, data tables, and any product where legibility and precision are the brand. Its monochrome-plus-one-red discipline also suits editorial and wayfinding work that wants Swiss rigor without ornament.
