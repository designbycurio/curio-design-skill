---
version: 1

meta:
  id: times-new-roman-morison-1932
  name: Times New Roman by Morison
  description: Dense newspaper roman on aged grey-tan newsprint, built for the 1932 front page of The Times.
  isDark: false
  tags: [editorial, historical, professional, narrative, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1932 debut in The Times (Monotype); based on the earlier Plantin"
  region: "London, England — the newspaper composing room"
  regionZh: "英国伦敦"
  keyFigures: [Stanley Morison, Victor Lardent]
  movements: [20th-century newspaper typography, Monotype revival programme]

introduction: |
  Times New Roman was cut by Stanley Morison and draughtsman Victor Lardent at Monotype and printed for the first time in The Times of London on 3 October 1932. Narrow, economical, and high in stroke contrast, it was engineered to pack legible copy into tight newspaper columns.
  This system rebuilds that habitat: dense ink-black roman set justified on aged grey-tan newsprint, ruled with hairline column rules and topped by a single red masthead band. The page reads like a front page — headline deck, standfirst, small-caps byline — never a clean white screen.
introductionZh: |
  《泰晤士报》新罗马体（Times New Roman）由斯坦利·莫里森与绘图员维克多·拉登特在蒙纳（Monotype）公司完成，1932 年 10 月 3 日首次印在伦敦《泰晤士报》上。它字身狭窄、笔画对比强、极为省版面，专为把大量正文塞进狭窄报纸栏而生。
  这套系统还原的正是那个场景：浓黑如印刷油墨的罗马体，两端对齐地排在泛灰泛黄的旧报纸上，靠发丝般的栏线分隔，顶部压一道红色报头横条。整个页面读起来像一张报纸头版——大标题、导语、小型大写字母署名——而绝不是一块干净的白屏。

colors:
  primary:    {"50": "#F3F1EE", "100": "#E4E0DA", "200": "#C7C0B6", "300": "#A29A8C", "400": "#6E675C", "500": "#1A1815", "600": "#171512", "700": "#131210", "800": "#0E0D0B", "900": "#080706", "950": "#040403"}
  secondary:  {"50": "#F7F5F0", "100": "#EFEBE1", "200": "#E0D9C8", "300": "#D3CBB6", "400": "#C9C1AE", "500": "#B3A98F", "600": "#948B72", "700": "#6F6857", "800": "#4B463A", "900": "#2C2921", "950": "#181712"}
  accent:     {"50": "#FAEDEA", "100": "#F3D3CC", "200": "#E6A79A", "300": "#D97C68", "400": "#C55A44", "500": "#B0402F", "600": "#963628", "700": "#762A20", "800": "#561F17", "900": "#37140F", "950": "#1E0B08"}
  neutral:    {"50": "#F7F7F6", "100": "#EDEBE7", "200": "#DAD6CE", "300": "#C0BAAE", "400": "#8C8577", "500": "#6C665A", "600": "#544F46", "700": "#3B3833", "800": "#2A2823", "900": "#1A1815", "950": "#0F0E0C"}
  semantic:
    success: { bg: "#E9EAE1", text: "#3E4A2E", light: "#F3F4EC", border: "#C4CBAF" }
    warning: { bg: "#F3E9D6", text: "#6B4E1E", light: "#FAF3E6", border: "#D8C49A" }
    error:   { bg: "#F3DAD3", text: "#762A20", light: "#FAEDEA", border: "#D9AEA2" }
    info:    { bg: "#DFE3E4", text: "#2F4247", light: "#EEF1F2", border: "#B2C0C4" }
  background:
    page:    "#F7F7F6"
    surface: "#FBFBFA"
    subtle:  "#EDEBE7"
  text:
    primary:   "#1A1815"
    secondary: "#3B3833"
    muted:     "#8C8577"
    inverse:   "#F7F7F6"

typography:
  families:
    heading: "'Playfair Display', 'Times New Roman', Georgia, serif"
    body:    "'PT Serif', 'Noto Serif', 'Times New Roman', Georgia, serif"
    mono:    "'Courier Prime', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Noto+Serif:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Courier+Prime:wght@400;700&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.15, snug: 1.3, normal: 1.45, relaxed: 1.6, loose: 1.75}
  letterSpacing: {tighter: "-0.02em", tight: "-0.01em", normal: "0", wide: "0.04em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "0", md: "1px", lg: "2px", xl: "3px", full: "9999px"}
  color:  {default: "#C0BAAE", subtle: "#DAD6CE", strong: "#1A1815", focus: "#B0402F"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 1px rgba(26,24,21,0.05)"
  sm: "0 1px 2px rgba(26,24,21,0.07)"
  md: "0 2px 4px rgba(26,24,21,0.08)"
  lg: "0 3px 8px rgba(26,24,21,0.10)"
  xl: "0 6px 16px rgba(26,24,21,0.12)"
  "2xl": "0 10px 28px rgba(26,24,21,0.14)"
  inner: "inset 0 1px 2px rgba(26,24,21,0.05)"
  focus: "0 0 0 3px rgba(176,64,47,0.30)"

motion:
  level: minimal
  durations: {instant: "0ms", fast: "120ms", normal: "220ms", slow: "360ms", slower: "560ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.2, 0.64, 1)"
  hoverPatterns: [underline, tint, opacity]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        4px

surfaceStyle: flat
blur:         none

iconography:
  treatment: linear
  set:       feather
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.25px"

components:
  button:
    primary:   {background: "#1A1815", color: "#F7F7F6", border: "1px solid #1A1815", shadow: "none", hoverBackground: "#3B3833", hoverShadow: "none", hoverColor: "#F7F7F6"}
    secondary: {background: "transparent", color: "#1A1815", border: "1px solid #1A1815", shadow: "none", hoverBackground: "#EDEBE7", hoverShadow: "none", hoverColor: "#1A1815"}
    ghost:     {background: "transparent", color: "#3B3833", border: "1px solid transparent", shadow: "none", hoverBackground: "transparent", hoverShadow: "none", hoverColor: "#B0402F"}
    danger:    {background: "#B0402F", color: "#F7F7F6", border: "1px solid #B0402F", shadow: "none", hoverBackground: "#963628", hoverShadow: "none", hoverColor: "#F7F7F6"}
    sizes:     {sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "1px"
    fontWeight: 700
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "#FBFBFA"
    color: "#1A1815"
    border: "1px solid #C0BAAE"
    borderRadius: "1px"
    padding: "10px 12px"
    focusBorder: "1px solid #1A1815"
    placeholderColor: "#8C8577"
  card:
    base:  {background: "#FBFBFA", border: "1px solid #DAD6CE", borderRadius: "1px", padding: "24px", shadow: "0 1px 2px rgba(26,24,21,0.07)"}
    hover: {shadow: "0 3px 8px rgba(26,24,21,0.10)", transform: "none"}
---

# Times New Roman by Morison

> The 1932 front page of The Times — dense ink-black roman, justified in narrow columns on aged grey-tan newsprint.

## Origin

Times New Roman was commissioned after Stanley Morison, then typographic advisor to Monotype and The Times, publicly criticised the newspaper for being badly printed in an antiquated face. Challenged to do better, he sketched a design and had draughtsman Victor Lardent at The Times draw it out. Rooted in Plantin — a sturdy sixteenth-century-derived Monotype face — it was made narrower and given sharper stroke contrast and crisper serifs, so more words fit per line while staying black and legible on fast mechanical presses. It debuted in the paper on 3 October 1932.

Within a year Monotype released it commercially, and it spread from the composing room into books, offices, and eventually the default document face of the personal computer. But its native ground was never white paper or a screen: it was cheap mechanical newsprint — a warm grey-tan stock that yellows and greys with age, taking dense black ink with a faint tooth and spread. This system honours that habitat rather than the sterile word-processor version.

## Overview

Composition cues:
- **Layout**: multi-column newspaper grid — a bold masthead band above, then justified body columns divided by hairline rules.
- **Content width**: contained measure; narrow, economical columns rather than wide airy blocks.
- **Framing**: bordered and ruled — hairline column rules, section rules, and a single red-top masthead rule; flat surfaces, no cards floating on shadow.
- **Grid intensity**: strong. The column grid is visible structure, not decoration.

## Colors

The palette is ink on aged stock plus one editorial accent. Everything sits on a warm grey-tan newsprint ground; type is a dense near-black that reads as pressed ink; a single red-top rule is the only saturated note, reserved for the masthead and the most urgent emphasis. Nothing is bright, and nothing is pure white.

**Role usage**:
- Page background → `colors.background.page` (`#F7F7F6`, aged newsprint)
- Body & headline ink → `colors.text.primary` (`#1A1815`)
- Secondary / caption ink → `colors.text.secondary` (`#3B3833`)
- Byline & muted meta → `colors.text.muted` (`#8C8577`)
- Stock-tone panels & rules → `colors.secondary.400` (`#C9C1AE`)
- Masthead red-top rule & urgent emphasis → `colors.accent.500` (`#B0402F`)
- Column & section hairlines → `colors.borders.default` (`#C0BAAE`)

## Typography

The voice is the newspaper serif itself: narrow, high-contrast roman set tight and justified. Times New Roman is the period-exact face, with PT Serif and Noto Serif as faithful open stand-ins for body copy, and Playfair Display (with Georgia as a system fallback) carrying high-contrast display headlines. Leading is tight, measure is narrow, and hierarchy comes from size, weight, italics, small caps, and drop caps rather than colour.

**Text styles**:
- `display-xl` — Playfair Display, 96px, weight 900, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Playfair Display, 64px, weight 700, line-height 1.05, letter-spacing -0.01em
- `heading-1` — PT Serif, 36px, weight 700, line-height 1.15, letter-spacing -0.01em
- `heading-2` — PT Serif, 24px, weight 700, line-height 1.25, letter-spacing 0
- `standfirst` — Noto Serif italic, 20px, weight 400, line-height 1.4, letter-spacing 0
- `body-lg` — PT Serif, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — PT Serif, 16px, weight 400, line-height 1.55, letter-spacing 0
- `byline` — PT Serif small-caps, 13px, weight 700, line-height 1.3, letter-spacing 0.04em
- `caption` — Noto Serif, 13px, weight 400, line-height 1.4, letter-spacing 0
- `mono-md` — Courier Prime, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit 4px; scale `2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`.
- Container maxes at 1280px; body sets in narrow justified columns (~34–40em measure).
- Column gaps stay tight (16–24px) with a hairline rule dropped into the gutter.
- Section padding `32 / 64 / 96 / 128` across breakpoints; vertical rhythm on a 4px grid.

## Elevation & Depth

The page is flat ink on paper. Depth is drawn, not lit — ruled boxes, stock-tone panels, and hairline separations do the work that shadow does elsewhere. Shadows exist only as the faintest lift for interactive surfaces; there is no blur and no glass.

- Surfaces are opaque and matte (`surfaceStyle: flat`, `blur: none`).
- Structure reads through rules and tonal panels, not elevation.
- Shadow ladder is deliberately shallow: `xs`→`2xl` climb only from 1px to a soft 28px, all low-alpha warm-black.
- Focus is a 3px red-top halo (`rgba(176,64,47,0.30)`).

## Shapes

- Corners are effectively square — `sm: 0`, `md: 1px`, `lg: 2px`, `xl: 3px`. Print has no rounded rectangles.
- `full: 9999px` reserved strictly for tiny dot markers or avatar clips.
- Emphasis comes from rule weight and boxing, never from rounding.

## Motion

Motion is a printing press, not an animation: it barely moves. Transitions are short and functional — a link underline drawing in, a tint on hover, a quiet opacity shift. Nothing bounces, slides far, or draws attention to itself; the reading experience stays still and legible.

- Level: minimal.
- Durations `120 / 220 / 360ms` for the common cases; slower reserved for rare page-level fades.
- Easings default to standard material curves; `spring` kept nearly critically damped.
- Hover patterns: underline, tint, opacity. Respects `prefers-reduced-motion`.

## Techniques

### Red-top masthead band
The single saturated element on the page — a bold ruled band carrying the masthead, with a red-top rule beneath in the manner of a front page.
```css
.masthead {
  padding: 16px 0 12px;
  border-top: 2px solid #1A1815;
  border-bottom: 3px solid #B0402F;
  font-family: 'Playfair Display', 'Times New Roman', Georgia, serif;
  font-weight: 900;
  letter-spacing: -0.01em;
  color: #1A1815;
  text-align: center;
}
```

### Hairline-ruled column grid
Justified newspaper columns divided by hairline rules dropped into the gutter, so structure reads as ink rather than whitespace.
```css
.columns {
  column-count: 3;
  column-gap: 24px;
  column-rule: 1px solid #C0BAAE;
  text-align: justify;
  hyphens: auto;
  font-family: 'PT Serif', 'Noto Serif', Georgia, serif;
  line-height: 1.55;
  color: #1A1815;
}
```

### Drop-cap lead with small-caps byline
The article opener: a large roman drop cap keyed to the column, above a small-caps byline in tracked capitals.
```css
.lead::first-letter {
  float: left;
  font-family: 'Playfair Display', 'Times New Roman', Georgia, serif;
  font-size: 4.4em;
  line-height: 0.82;
  font-weight: 700;
  padding: 4px 8px 0 0;
  color: #1A1815;
}
.byline {
  font-variant: small-caps;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: #3B3833;
}
```

## Iconography

Icons are sparing and utilitarian — thin linear glyphs (Feather at ~1.25px stroke) that behave like typographic marks rather than illustrations. They sit inline with text at reading size, inked in the same near-black, and never carry colour except a rare red-top for alerts. Prefer real punctuation and rules over icons wherever type can carry the meaning.

- Treatment: linear, hairline stroke.
- Set: feather.
- Stroke: 1.25px, matched to the text colour.

## Do's & Don'ts

### ✓ Do
- Set body copy in PT Serif or Noto Serif, justified in narrow columns with tight leading.
- Ground every page on aged grey-tan newsprint `#F7F7F6`, never white.
- Reserve the red-top `#B0402F` for the masthead rule and the single most urgent emphasis.
- Build hierarchy from size, weight, italics, small caps, and drop caps — not colour.
- Divide columns with hairline rules and box sections with thin rules, keeping surfaces flat.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — the ground is aged grey-tan newsprint.
- No sans-serif body text — this is a newspaper serif.
- No wide, airy tracking — the design is narrow and economical.
- No neon or saturated palettes — muted ink, stock tone and one red-top rule only.

## Applications

Best fit for editorial and long-form reading: newspaper-style front pages, longread articles, print-feel newsletters, annual reports, and any document that wants the authority of the printed page. It excels where dense justified text, ruled structure, and a single restrained accent carry gravitas — and is a poor fit for playful marketing, dashboards needing many status colours, or airy sans-serif interfaces.
