---
version: 1

meta:
  id: tarot-deck-marseille-1700
  name: Tarot de Marseille
  description: Hand-coloured woodcut tarot — bold black outlines and flat pochoir stencil colour on a deep Marseille-blue ground.
  isDark: true
  tags: [historical, decorative, bold, narrative, handmade]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Conver pattern dated 1760; the Marseille tradition runs earlier (1600s–1700s)"
  region: "Marseille, France"
  regionZh: "法国马赛"
  keyFigures: [Nicolas Conver, Jean Dodal, Pierre Madenié]
  movements: [woodblock printing, pochoir stencil colouring, divinatory imagery]

introduction: |
  The Tarot de Marseille is the canonical European tarot pattern: bold black
  woodblock outlines filled with flat pochoir stencil colour in a strict
  limited palette. Nicolas Conver's 1760 deck fixed the form — red, ochre,
  blue, flesh and occasional green sit in unshaded fields, registration
  drifting a hair off the line. It is craft, not illustration.
  Here the deck is staged on its own stencil-blue ground, the stated primary
  pulled from background to centre stage. Vermilion and ochre carry accent,
  the black outline holds everything together, and nothing is allowed to
  blend, gradient, or soften into modern shading.
introductionZh: |
  马赛塔罗是欧洲塔罗的范本：粗黑的木刻轮廓，内里用镂版（pochoir）一色一色平涂
  填上去，颜色被限定在一组很窄的传统色里——红、赭、蓝、肉色，偶尔一点绿，全是
  没有过渡的平涂色块。尼古拉·孔韦尔 1760 年的那副牌把这套样式定了型，套色时刻意
  让颜色压不准轮廓线，差那么一丝，正是手工木刻的标记。
  这套设计把牌面立在它自己的镂版蓝底上——蓝本是背景，如今被请到台前，作为主色。
  朱红与赭黄做点缀，黑色轮廓把一切框住。这里不许任何渐变、照片式的明暗，也不许
  现代韦特牌那种柔和的描绘——只有时代里那组严格的有限色。

colors:
  primary:    {"50": "#FBEAE8", "100": "#F6D2CD", "200": "#EBA59B", "300": "#E07869", "400": "#D54E3C", "500": "#C0392B", "600": "#A22E22", "700": "#82251B", "800": "#631C15", "900": "#46140F", "950": "#2A0C09"}
  secondary:  {"50": "#EAEFF7", "100": "#CBD8EC", "200": "#9DB3D8", "300": "#6F8EC4", "400": "#4A6CAE", "500": "#2E5499", "600": "#264785", "700": "#1F3A6B", "800": "#182D52", "900": "#11203A", "950": "#0B1525"}
  accent:     {"50": "#FBF4E9", "100": "#F7E8CF", "200": "#EFD2A1", "300": "#E8BE7B", "400": "#E4B36C", "500": "#E1A95F", "600": "#C98E45", "700": "#A56F33", "800": "#7E5426", "900": "#5A3B1B", "950": "#382410"}
  neutral:    {"50": "#F5F4F1", "100": "#E6E4DE", "200": "#CDCABF", "300": "#ABA89B", "400": "#827F72", "500": "#605E53", "600": "#47463D", "700": "#34332C", "800": "#25241F", "900": "#1A1A17", "950": "#0E0E0C"}
  semantic:
    success: { bg: "#E4F0E8", text: "#1E4A34", light: "#C9E1D2", border: "#2E6F4E" }
    warning: { bg: "#FBF0DC", text: "#6E4A14", light: "#F3DDB3", border: "#E1A95F" }
    error:   { bg: "#F9E3E0", text: "#7A2018", light: "#EFC2BB", border: "#C0392B" }
    info:    { bg: "#E4ECF7", text: "#1F3A6B", light: "#C2D2EC", border: "#2E5499" }
  background:
    page:    "#1F3A6B"
    surface: "#264785"
    subtle:  "#182D52"
  text:
    primary:   "#F2EBDC"
    secondary: "#CBC1AC"
    muted:     "#9AA6BE"
    inverse:   "#1A1A17"

typography:
  families:
    heading: "'Cinzel Decorative', 'IM Fell French Canon', serif"
    body:    "'IM Fell DW Pica', Georgia, serif"
    mono:    "'IM Fell DW Pica', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=IM+Fell+French+Canon:ital@0;1&family=IM+Fell+DW+Pica:ital@0;1&family=UnifrakturCook&display=swap"
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
  radius: {none: "0", sm: "0", md: "2px", lg: "3px", xl: "4px", full: "9999px"}
  color:  {default: "#1A1A17", subtle: "#264785", strong: "#1A1A17", focus: "#E1A95F"}
  width:  {thin: "1px", default: "2px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "1px 1px 0 rgba(26,26,23,0.45)"
  sm: "2px 2px 0 rgba(26,26,23,0.50)"
  md: "3px 3px 0 rgba(26,26,23,0.55)"
  lg: "4px 5px 0 rgba(26,26,23,0.55)"
  xl: "6px 7px 0 rgba(26,26,23,0.60)"
  "2xl": "8px 10px 0 rgba(26,26,23,0.60)"
  inner: "inset 0 1px 2px rgba(26,26,23,0.30)"
  focus: "0 0 0 3px rgba(225,169,95,0.55)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, stroke, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        4px

surfaceStyle: solid
blur:         none

iconography:
  treatment: outline
  set:       custom
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#C0392B", color: "#F2EBDC", border: "2px solid #1A1A17", shadow: "3px 3px 0 rgba(26,26,23,0.55)", hoverBackground: "#A22E22", hoverShadow: "4px 5px 0 rgba(26,26,23,0.55)", hoverColor: "#FBEAE8"}
    secondary: {background: "#E1A95F", color: "#1A1A17", border: "2px solid #1A1A17", shadow: "3px 3px 0 rgba(26,26,23,0.55)", hoverBackground: "#C98E45", hoverShadow: "4px 5px 0 rgba(26,26,23,0.55)", hoverColor: "#1A1A17"}
    ghost:     {background: "transparent", color: "#F2EBDC", border: "2px solid #E1A95F", shadow: "none", hoverBackground: "rgba(225,169,95,0.12)", hoverShadow: "none", hoverColor: "#E1A95F"}
    danger:    {background: "#82251B", color: "#F2EBDC", border: "2px solid #1A1A17", shadow: "3px 3px 0 rgba(26,26,23,0.55)", hoverBackground: "#631C15", hoverShadow: "4px 5px 0 rgba(26,26,23,0.55)", hoverColor: "#FBEAE8"}
    sizes:     {sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "42px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "52px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "2px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#182D52"
    color: "#F2EBDC"
    border: "2px solid #1A1A17"
    borderRadius: "2px"
    padding: "10px 14px"
    focusBorder: "2px solid #E1A95F"
    placeholderColor: "#9AA6BE"
  card:
    base:  {background: "#264785", border: "2px solid #1A1A17", borderRadius: "2px", padding: "24px", shadow: "4px 5px 0 rgba(26,26,23,0.55)"}
    hover: {shadow: "6px 7px 0 rgba(26,26,23,0.60)", transform: "translate(-2px, -2px)"}
---

# Tarot de Marseille

> Hand-coloured woodcut tarot — bold black outlines and flat pochoir stencil colour on a deep Marseille-blue ground.

## Origin
The Tarot de Marseille is the standard pattern of European tarot, descended from the cardmaking workshops of Marseille in the 1600s and 1700s. Cards were printed from carved woodblocks — a single bold black key-line — then coloured by hand through cut stencils, one flat pass per colour. The strict palette of red, yellow-ochre, blue, flesh and the occasional green was a constraint of the craft and the trade, not an aesthetic choice, yet it became the signature of the form.

Nicolas Conver's deck, dated 1760, is the canonical reference: its Major Arcana figures, double-rule borders, title cartouches and Roman-numeral numbering set the template that revivalists and occultists have copied ever since. Because each colour was stencilled separately, registration never sat perfectly on the outline — a hair of drift between black line and colour field that no modern reprint should hide. It is the fingerprint of the hand.

## Overview
Composition cues:
- **Layout**: Symmetrical, centred figure compositions framed by double-rule borders and title cartouches.
- **Content width**: Container — card-like panels, not full-bleed washes.
- **Framing**: Bordered — every surface gets a bold black 2px woodblock key-line.
- **Grid intensity**: Strong — a strict rectilinear grid echoing a spread of cards laid out in rows.

## Colors
Colour is flat, unshaded and limited — the authenticity marker of the form. The deep Marseille blue is the ground (the stated primary), with vermilion red carrying the loudest accent and yellow-ochre warming the second tier. Black woodblock outline separates every field; flesh and muted green appear as supporting fills. Never blend or gradient — each colour is a single pochoir pass.
**Role usage**:
- Page background → `colors.background.page` (#1F3A6B, deep stencil-blue ground)
- Primary action / loudest accent → `colors.primary.500` (#C0392B vermilion)
- Secondary fill / warm titling → `colors.accent.500` (#E1A95F yellow-ochre)
- Card / surface panels → `colors.background.surface` (#264785)
- Woodblock outline & borders → `colors.neutral.900` (#1A1A17)
- Primary text on blue → `colors.text.primary` (#F2EBDC warm parchment)
- Supporting positive fields → semantic success border (#2E6F4E muted green)

## Typography
The voice is period letterpress: high-contrast titling serifs with ornamental capitals, set against a workmanlike book-serif body, with blackletter reserved for the rare incantatory flourish. Titles carry wide tracking and uppercase, as if cut into a wood title-block.
**Text styles**:
- `display-xl` — Cinzel Decorative, 96px, weight 900, line-height 1.0, letter-spacing 0.02em
- `display-lg` — Cinzel Decorative, 64px, weight 700, line-height 1.05, letter-spacing 0.02em
- `heading-1` — IM Fell French Canon, 36px, weight 400, line-height 1.2, letter-spacing 0.01em
- `body-lg` — IM Fell DW Pica, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — IM Fell DW Pica, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — IM Fell French Canon italic, 13px, weight 400, line-height 1.375, letter-spacing 0.02em
- `mono-md` — IM Fell DW Pica, 15px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px, scale runs 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128.
- Container max 1280px; figures and panels stay within container width, never full-bleed.
- Section padding 64–128px on large screens for a deck-laid-out rhythm.
- Grid gaps 16–24px — tight enough that cards read as a spread.

## Elevation & Depth
Materiality is paper and ink, not glass. Surfaces are flat solid blue panels lifted by hard offset ink shadows — no blur, no soft penumbra — as if a printed card sits a millimetre above the cloth.
- Surface style: solid flat colour fields, no translucency.
- Blur: none.
- Shadow ladder: hard-edged ink offsets (1px → 8px) in warm near-black `rgba(26,26,23,…)`, never soft grey.

## Shapes
- Corner radii kept near-zero: 0 / 0 / 2px / 3px / 4px — cards and panels are crisp rectangles.
- Borders are bold: 2px default, 4px thick, always in #1A1A17 woodblock black.
- `full` (9999px) reserved only for the odd seal or numeral medallion.

## Motion
Motion is restrained and mechanical — things settle into place like a card laid on the table, never bounce or float. Hovers lift on the hard ink shadow or warm the stroke; nothing fades through translucency.
- Level: restrained.
- Durations: 120–400ms for most transitions.
- Easings: standard ease in/out; spring reserved for a single emphatic "deal" gesture.
- Hover patterns: lift (translate + grow ink shadow), stroke (border to ochre), tint (subtle ochre wash).

## Techniques
Brand-specific recipes for the woodcut-and-stencil look.

### Pochoir registration drift
The colour fill sits a hair off the black key-line, mimicking hand-stencilled mis-registration.
```css
.pochoir {
  position: relative;
  color: #1A1A17;            /* the woodblock key-line */
  background: #1F3A6B;
}
.pochoir::before {
  content: "";
  position: absolute;
  inset: 0;
  background: #C0392B;        /* the flat stencil colour */
  transform: translate(2px, 1.5px);  /* the drift */
  mix-blend-mode: multiply;
  z-index: -1;
}
```

### Woodblock key-line frame
A bold black outline with an inset double-rule, the card cartouche border.
```css
.card-cartouche {
  border: 2px solid #1A1A17;
  box-shadow:
    inset 0 0 0 3px #1F3A6B,
    inset 0 0 0 4px #1A1A17,      /* inner double rule */
    4px 5px 0 rgba(26,26,23,0.55); /* hard ink offset */
  background: #264785;
  border-radius: 2px;
}
```

### Flat stencil field
Strictly unshaded colour blocks — guards against gradients sneaking in.
```css
.stencil-field {
  background: #E1A95F;          /* one flat ochre pass */
  background-image: none;        /* never a gradient */
  color: #1A1A17;
  border: 2px solid #1A1A17;
  box-shadow: none;              /* no soft shading */
}
```

## Iconography
Icons read as woodcut marks: bold 2px black outlines, flat single-colour fills, geometric and slightly naive — suns, moons, stars, swords, cups, coins, batons from the suit symbology. Treat them as carved stamps rather than fine line drawings; allow the same registration drift between outline and fill as the cards.
- Treatment: outline (bold key-line with optional flat stencil fill).
- Set: custom woodcut glyphs (suit and arcana symbols).
- Stroke: 2px, uniform and heavy.

## Do's & Don'ts
### ✓ Do
- Stage everything on the deep Marseille blue `#1F3A6B` ground — it is the stated primary.
- Fill colour in flat, unshaded pochoir fields — one pass, one colour, no blends.
- Outline every figure and panel with the bold black `#1A1A17` woodblock key-line.
- Keep a hair of registration drift between outline and colour for hand-printed authenticity.
- Reserve vermilion `#C0392B` for the loudest accent and ochre `#E1A95F` for warm secondary fills.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — the blue ground is the stated primary.
- No gradient or photographic shading; colour must stay flat, unshaded stencil fields.
- No thin elegant linework; keep bold black woodblock outlines with registration drift.
- No modern Rider-Waite imagery or pastel/neon palette; stay in the strict period limited palette.

## Applications
Best suited to anything that benefits from ceremony and antiquarian gravity: divination and oracle apps, occult or esoteric publishing, fortune-telling and game packaging, period-flavoured event posters, and editorial features on folklore, history or the tarot itself. The strict palette and heavy frames also make striking card-based UI and collectible series.
