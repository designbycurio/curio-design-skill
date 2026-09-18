---
version: 1

meta:
  id: persian-nastaliq-calligraphy
  name: "Persian Nastaliq Calligraphy"
  description: "Burnished gold hanging script and illuminated cloud bands glowing on a deep afshan ink-field ground"
  isDark: true
  tags: [historical, luxurious, decorative, narrative, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "c. 1500 (Timurid–Safavid perfection of Nastaliq); album arts flourish 16th–17th century"
  region: "Persia (Tabriz, Isfahan, Herat), Middle East"
  regionZh: "波斯（大不里士、伊斯法罕、赫拉特），中东"
  keyFigures: ["Mir Ali Tabrizi", "Mir Emad al-Hasani", "Sultan Ali Mashhadi"]
  movements: ["Persian Nastaliq calligraphy", "Safavid manuscript illumination (tazhib)", "Album (muraqqa) arts"]

introduction: |
  Nastaliq is the "hanging" cursive of Persian book arts — lamp-black ink flowing down a diagonal slope, its letters swinging like dancers before settling on the line. Perfected in the Safavid ateliers of Tabriz and Isfahan by masters such as Mir Emad al-Hasani, it is the most prized of all Islamic scripts.

  This design system reads Nastaliq at its deep presentation value: burnished gold letters and illuminated cloud bands glowing on a near-black, gold-flecked afshan ground, headed by gold-and-lapis cartouches and laced with vine and polychrome flowers.
introductionZh: |
  纳斯塔利克体是波斯书籍艺术中的「悬挂体」草书——灯黑墨沿对角斜坡流泻，字母如舞者般摆荡，最终落定于行线。它在萨法维王朝大不里士与伊斯法罕的画坊中臻于至境，由米尔·伊玛德等大师铸就，是伊斯兰书法中最受珍视的一体。

  本设计系统取其最华贵的呈现方式：在近乎墨黑、洒金（afshan）的底面上，让烫金字母与镶金云带（abr）熠熠生辉，以金蓝相间的卷首题识（cartouche）领起，缠枝与彩绘花卉交织其间。中文读者可将它想见为一页波斯洒金抄本，金与青金石在暗夜般的底色上愈显璀璨。

colors:
  primary:
    "50": "#FAF6EA"
    "100": "#F4EAC9"
    "200": "#E8D9A0"
    "300": "#DCC57D"
    "400": "#D2B364"
    "500": "#C8A24A"
    "600": "#A9863A"
    "700": "#86692D"
    "800": "#634D21"
    "900": "#453615"
    "950": "#26200D"
  secondary:
    "50": "#FBEDED"
    "100": "#F5D2D2"
    "200": "#E5A3A3"
    "300": "#D07373"
    "400": "#B44E4E"
    "500": "#8E2B2B"
    "600": "#782424"
    "700": "#5F1D1D"
    "800": "#471616"
    "900": "#300F0F"
    "950": "#1E0909"
  accent:
    "50": "#EDF2F7"
    "100": "#D2DEEA"
    "200": "#A6BDD3"
    "300": "#7799BA"
    "400": "#4E7196"
    "500": "#2E4E6E"
    "600": "#27415C"
    "700": "#1F3449"
    "800": "#182838"
    "900": "#111C27"
    "950": "#0A1017"
  neutral:
    "50": "#F6F3EC"
    "100": "#E9E3D5"
    "200": "#D0C7B2"
    "300": "#B0A487"
    "400": "#8A7E62"
    "500": "#6B6049"
    "600": "#524A38"
    "700": "#3D372A"
    "800": "#2A251C"
    "900": "#1A1712"
    "950": "#100E0A"
  semantic:
    success: { bg: "#3E6B52", text: "#EAF2ED", light: "#D6E4DC", border: "#315843" }
    warning: { bg: "#C8A24A", text: "#26200D", light: "#F4EAC9", border: "#A9863A" }
    error: { bg: "#8E2B2B", text: "#FBEDED", light: "#F5D2D2", border: "#782424" }
    info: { bg: "#2E4E6E", text: "#EDF2F7", light: "#D2DEEA", border: "#27415C" }
  background:
    page: "#1A1712"
    surface: "#241F17"
    subtle: "#201C15"
  text:
    primary: "#E8D9A0"
    secondary: "#C8A24A"
    muted: "#8A7E62"
    inverse: "#1A1712"

typography:
  families:
    heading: "'Aref Ruqaa', 'Noto Nastaliq Urdu', 'Amiri', serif"
    body: "'Gulzar', 'Noto Nastaliq Urdu', 'Amiri', serif"
    mono: "'Noto Naskh Arabic', 'Gulzar', serif"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Gulzar&family=Noto+Nastaliq+Urdu:wght@400;500;600;700&family=Noto+Naskh+Arabic:wght@400;500;700&display=swap"
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
    sm: "3px"
    md: "6px"
    lg: "10px"
    xl: "16px"
    full: "9999px"
  color:
    default: "#C8A24A"
    subtle: "rgba(200, 162, 74, 0.28)"
    strong: "#A9863A"
    focus: "#E8D9A0"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.35)"
  sm: "0 1px 4px rgba(0,0,0,0.42)"
  md: "0 2px 10px rgba(0,0,0,0.5)"
  lg: "0 6px 20px rgba(0,0,0,0.55)"
  xl: "0 12px 32px rgba(0,0,0,0.6)"
  "2xl": "0 20px 48px rgba(0,0,0,0.65)"
  inner: "inset 0 1px 3px rgba(0,0,0,0.5)"
  focus: "0 0 0 3px rgba(200, 162, 74, 0.45)"

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
    in: "cubic-bezier(0.55, 0, 1, 0.45)"
    out: "cubic-bezier(0, 0.55, 0.45, 1)"
    spring: "cubic-bezier(0.34, 1.4, 0.64, 1)"
  hoverPatterns: [glow, tint, underline]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "narrow"
  framing: "bordered"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "duotone"
  set: "phosphor"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#C8A24A"
      color: "#1A1712"
      border: "1px solid #E8D9A0"
      shadow: "0 2px 10px rgba(0,0,0,0.5)"
      hoverBackground: "#D2B364"
      hoverShadow: "0 0 0 1px rgba(232, 217, 160, 0.5), 0 6px 20px rgba(0,0,0,0.55)"
      hoverColor: "#100E0A"
    secondary:
      background: "transparent"
      color: "#C8A24A"
      border: "1px solid #C8A24A"
      shadow: "none"
      hoverBackground: "rgba(200, 162, 74, 0.12)"
      hoverShadow: "0 2px 10px rgba(0,0,0,0.4)"
      hoverColor: "#E8D9A0"
    ghost:
      background: "transparent"
      color: "#E8D9A0"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(200, 162, 74, 0.1)"
      hoverShadow: "none"
      hoverColor: "#C8A24A"
    danger:
      background: "#8E2B2B"
      color: "#FBEDED"
      border: "1px solid #B44E4E"
      shadow: "0 2px 10px rgba(0,0,0,0.5)"
      hoverBackground: "#782424"
      hoverShadow: "0 6px 18px rgba(0,0,0,0.55)"
      hoverColor: "#FBEDED"
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "0.875rem" }
      md: { height: "42px", padding: "0 22px", fontSize: "1rem" }
      lg: { height: "52px", padding: "0 30px", fontSize: "1.125rem" }
    borderRadius: "10px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#201C15"
    color: "#E8D9A0"
    border: "1px solid rgba(200, 162, 74, 0.4)"
    borderRadius: "6px"
    padding: "11px 14px"
    focusBorder: "#C8A24A"
    placeholderColor: "#8A7E62"
  card:
    base:
      background: "#241F17"
      border: "1px solid rgba(200, 162, 74, 0.35)"
      borderRadius: "16px"
      padding: "28px"
      shadow: "0 6px 20px rgba(0,0,0,0.55)"
    hover:
      shadow: "0 12px 32px rgba(0,0,0,0.6)"
      transform: "translateY(-2px)"
---

# Persian Nastaliq Calligraphy

> Burnished gold script hanging on a downward slope, glowing against a deep gold-flecked ink-field ground.

## Origin

Nastaliq — from *naskh* wedded to *ta'liq* — is the hanging cursive that Persian book arts brought to perfection around 1500. Its invention is traditionally credited to Mir Ali Tabrizi in the late 14th century; Sultan Ali Mashhadi codified its proportions in Herat, and the Safavid master Mir Emad al-Hasani raised it to a peak of grace that scribes have copied ever since. Written with lamp-black ink and a reed pen cut on a bias, its letters descend a diagonal slope, each word swinging out and settling like a dancer coming to rest.

In album (*qit'a*) and *muraqqa* pages, the script rarely sits alone. Illuminators of the Safavid ateliers at Tabriz and Isfahan set it inside gold cloud bands (*abr*) laced with vine and polychrome flowers, headed by gold-and-lapis cartouches, and scattered the ground with gold flecks (*afshan*). Read at its deepest presentation value, a Nastaliq folio is burnished gold lettering glowing on a near-black manuscript field — the aesthetic this system distills.

## Overview

Composition cues:
- **Layout**: Vertical stacked columns reading like manuscript folios — content flows down the page rather than across a rigid multi-column grid
- **Content width**: Narrow measure, honoring the intimate scale of an album page held in the hand
- **Framing**: Bordered — thin gold hairline frames and illuminated cloud-band reserves enclose text blocks
- **Grid intensity**: Soft — an underlying rhythm exists, but type hangs on a diagonal slope and is never grid-locked horizontally

## Colors

The palette is drawn straight from the illuminator's shell: lamp-black-into-umber for the afshan ground, burnished illumination gold as the dominant voice, a pale gold highlight for the flecks and highlights, and the two mineral accents that always accompanied gold in Safavid tazhib — shanjarf (cinnabar) red and lapis blue — with a vine green for foliate detail. The signature reading is warm gold script and cloud bands glowing on a dark field; nothing should read as flat digital "gold."

**Role usage**:
- Page background → `colors.background.page` (afshan ink-field `#1A1712`, the dominant ground)
- Panel / card surface → `colors.background.surface` (`#241F17`, a lifted manuscript panel)
- Illumination gold / script, primary actions → `colors.primary.500` (`#C8A24A`)
- Pale gold highlight / body text → `colors.primary.200` (`#E8D9A0`)
- Cartouche & rubric accents → `colors.secondary.500` (shanjarf-red `#8E2B2B`)
- Header cartouche / info → `colors.accent.500` (lapis-blue `#2E4E6E`)
- Foliate / success detail → `#3E6B52` (vine green)
- Muted captions on the ground → `colors.text.muted` (`#8A7E62`)

## Typography

The type voice is entirely Perso-Arabic and right-to-left in spirit. **Aref Ruqaa** carries ornate display headings with the swelling weight of a reed pen; **Noto Nastaliq Urdu** renders the hanging Nastaliq display lines that descend the diagonal slope; and **Gulzar** — itself a Nastaliq typeface — sets running body text at generous line-height so the sloping words have room to breathe. **Noto Naskh Arabic** fills the monospace role for tabular and technical text. Line-heights run loose; Nastaliq needs vertical air below the baseline for its descending tails.

**Text styles**:
- `display-xl` — Noto Nastaliq Urdu, 96px, weight 700, line-height 1.6, letter-spacing 0
- `display-lg` — Noto Nastaliq Urdu, 64px, weight 600, line-height 1.6, letter-spacing 0
- `heading-1` — Aref Ruqaa, 44px, weight 700, line-height 1.3, letter-spacing 0
- `body-lg` — Gulzar, 20px, weight 400, line-height 1.8, letter-spacing 0
- `body-md` — Gulzar, 16px, weight 400, line-height 1.8, letter-spacing 0
- `caption` — Aref Ruqaa, 14px, weight 400, line-height 1.5, letter-spacing 0.05em
- `mono-md` — Noto Naskh Arabic, 15px, weight 400, line-height 1.625, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px — but prefer the narrow measure
- Section padding: 64px vertical (md), 96px (lg) — album-page margins around the text field
- Grid gaps: 16px (md) to 24px (lg)

## Elevation & Depth

Depth is the layering of an illuminated album: cloud-band reserves float above the flecked ground, gold catches light against dark. Because the field is near-black, elevation reads through deepening dark shadow plus a faint gold rim rather than through soft gray. Shadows carry no color of their own; the warmth comes from the gold edges they surround.

- Surface style: layered (cloud bands and cartouches stacked over the afshan ground)
- Blur: none — burnished gold and ink are crisply rendered
- Shadow ladder: near-black `rgba(0,0,0,...)` at ascending opacity, from xs to 2xl
- Inner shadow: dark inset for recessed input fields
- Focus ring: 3px gold glow at 45% opacity

## Shapes

- `none`: 0 — cloud-band edges and rule lines
- `sm`: 3px — tags, small chips
- `md`: 6px — inputs, minor containers
- `lg`: 10px — buttons
- `xl`: 16px — cards and manuscript-panel containers
- `full`: 9999px — circular *shamsa* medallions and avatar frames

## Motion

Motion is restrained and calligraphic — the unhurried descent of a pen down its slope, the slow catch of light on burnished gold. Nothing bounces; hovers glow and tint as if a lamp were brought closer to the leaf.

- Level: restrained
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)`
- Hover patterns: glow (gold catching light), tint (shift toward pale gold), underline (a drawn rule beneath links)
- `reducedMotion: true` — all animations respect `prefers-reduced-motion`

## Techniques

### Abr cloud-band gold reserve
The illuminated cloud band that reserves the script from the flecked ground — a rounded gold-rimmed panel with a soft inner gold wash.
```css
.element {
  position: relative;
  padding: 20px 28px;
  border-radius: 9999px / 40px;
  background:
    radial-gradient(120% 140% at 50% 0%, rgba(200, 162, 74, 0.12), transparent 60%),
    #241F17;
  box-shadow:
    inset 0 0 0 1px rgba(232, 217, 160, 0.45),
    inset 0 0 22px rgba(200, 162, 74, 0.12);
}
```

### Diagonal hanging Nastaliq line
Sets a display line on the downward slope of Nastaliq instead of a flat horizontal baseline.
```css
.element {
  font-family: 'Noto Nastaliq Urdu', serif;
  direction: rtl;
  display: inline-block;
  transform: rotate(-4deg);
  transform-origin: right center;
  color: #C8A24A;
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5),
               0 0 14px rgba(200, 162, 74, 0.3);
  line-height: 1.8;
}
```

### Afshan gold-fleck ground
The scattered gold flecks of an afshan-decorated manuscript field, layered under content as a page background.
```css
.element {
  background-color: #1A1712;
  background-image:
    radial-gradient(circle at 15% 25%, rgba(200, 162, 74, 0.5) 0 1px, transparent 1.5px),
    radial-gradient(circle at 62% 12%, rgba(232, 217, 160, 0.4) 0 1px, transparent 1.5px),
    radial-gradient(circle at 40% 70%, rgba(200, 162, 74, 0.35) 0 1px, transparent 1.5px),
    radial-gradient(circle at 85% 55%, rgba(232, 217, 160, 0.3) 0 1px, transparent 1.5px);
  background-size: 180px 180px, 220px 220px, 160px 160px, 240px 240px;
}
```

## Iconography

Icons lean ornamental, drawn from the vocabulary of Safavid illumination: *shamsa* sun-medallions, vine tendrils, split-leaf arabesques, tulips and carnations. Where functional icons are needed, use Phosphor duotone at 1.5px stroke so a gold accent layer can sit over a darker base, echoing gold-on-pigment layering. Keep icon color to gold, pale gold, or the lapis and shanjarf accents.

- Treatment: duotone (gold accent over darker base)
- Set: Phosphor
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use the afshan ink-field `#1A1712` as the dominant ground so gold and lapis pop
- Set illumination gold `#C8A24A` on script, primary actions, and cloud-band rims
- Hang Nastaliq display lines on a downward diagonal slope, right-to-left
- Frame text in `abr` cloud-band reserves with gold-and-lapis header cartouches
- Give body type loose line-height so descending tails have vertical air

### ✗ Don't
- Use cream, ivory, or plain-white backgrounds — keep the burnished dark panel
- Grid-lock type horizontally — Nastaliq hangs on a downward diagonal slope
- Fill "gold" as a flat digital swatch — pair warm illumination gold with lapis and shanjarf
- Default to Inter or Helvetica — use the grounded Nastaliq/Arabic set only

## Applications

This system suits cultural-heritage and museum microsites, luxury storytelling for perfume, jewelry, and hospitality brands with a Persian or Middle Eastern provenance, and editorial platforms presenting poetry, calligraphy, and manuscript arts. It excels wherever a single luminous column of text on a dark, jewel-lit field carries more presence than a busy dashboard — landing pages, collector portfolios, and illustrated literary companions.
