---
version: 1

meta:
  id: german-expressionist-cinema-1920
  name: "German Expressionist Cinema"
  description: "Hand-painted oblique shadows and acute angles raked across a near-black silent frame — the world is bent, the light is a knife."
  isDark: true
  tags: [historical, narrative, monochrome, experimental, ornate]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Weimar-era silent cinema, c. 1919–1927; Caligari premiered Berlin 1920"
  region: "Germany (Decla-Bioscop / UFA studios, Berlin)"
  regionZh: "德国（柏林，德克拉-比奥斯科普 / UFA 制片厂）"
  keyFigures: ["Robert Wiene", "Hermann Warm", "Walter Reimann", "Walter Röhrig", "Conrad Veidt"]
  movements: ["German Expressionism", "Weimar cinema", "precursor to film noir"]

introduction: |
  German Expressionist cinema, canonized by Das Cabinet des Dr. Caligari (1920), built its dread from hand-painted oblique shadows, jagged distorted sets, and acute angles raked across a black-and-white silent frame. Original nitrate prints were exhibited color-tinted — amber for daylight, steel-blue for night.

  The defining look is the near-black projected frame edged by painted Caligari shadows: the world is bent, the light is a knife, the dark is alive.
introductionZh: |
  德国表现主义电影以《卡里加里博士的小屋》（1920）为标志，用手绘的倾斜阴影、扭曲锯齿的布景与切入黑白默片画面的锐角，构筑出深沉的恐惧。原始硝酸片放映时曾整体染色——白昼染琥珀，夜晚染钢蓝——但真正的标志，是那道几近全黑的投影画面，被手绘的卡里加里阴影所镶边。

  这套设计语言提炼自魏玛默片的视觉：世界是歪斜的，光是一把刀，黑暗是活的。底色永远是放映机投出的近黑画框，阴影是画上去的，而非自然投射；字体在哥特黑体、雕刻罗马大写与默片字幕牌之间游走，保持染色单色——切忌饱和的现代色彩。

colors:
  primary:
    "50": "#FAF9F5"
    "100": "#F2F0E8"
    "200": "#E7E3D6"
    "300": "#D9D3C0"
    "400": "#D1CAB6"
    "500": "#C9C2AC"
    "600": "#A9A28C"
    "700": "#85806E"
    "800": "#5F5B4E"
    "900": "#3B3830"
    "950": "#22201B"
  secondary:
    "50": "#EEF1F6"
    "100": "#D6DCE6"
    "200": "#AEB9CC"
    "300": "#7E8CA6"
    "400": "#4D5C78"
    "500": "#1C2433"
    "600": "#18202D"
    "700": "#141A25"
    "800": "#0F141C"
    "900": "#0A0D13"
    "950": "#06080C"
  accent:
    "50": "#FAF4E8"
    "100": "#F2E5C9"
    "200": "#E6CD96"
    "300": "#D7B265"
    "400": "#C79E4E"
    "500": "#B98C3F"
    "600": "#9C7434"
    "700": "#7C5C2A"
    "800": "#5C4520"
    "900": "#3E2E16"
    "950": "#241B0D"
  neutral:
    "50": "#F1F2F4"
    "100": "#DEE0E4"
    "200": "#BEC2CA"
    "300": "#9BA1AC"
    "400": "#7E8794"
    "500": "#646C78"
    "600": "#4F555F"
    "700": "#3B404A"
    "800": "#282C33"
    "900": "#181B20"
    "950": "#0E0D14"
  semantic:
    success: { bg: "#3E2E16", text: "#E6CD96", light: "#5C4520", border: "#B98C3F" }
    warning: { bg: "#5C4520", text: "#F2E5C9", light: "#7C5C2A", border: "#C79E4E" }
    error: { bg: "#3B3830", text: "#D1CAB6", light: "#5F5B4E", border: "#85806E" }
    info: { bg: "#141A25", text: "#AEB9CC", light: "#1C2433", border: "#4D5C78" }
  background:
    page: "#0E0D14"
    surface: "#16151D"
    subtle: "#1C2433"
  text:
    primary: "#C9C2AC"
    secondary: "#9BA1AC"
    muted: "#7E8794"
    inverse: "#0E0D14"

typography:
  families:
    heading: "'UnifrakturCook', 'Cinzel', 'Times New Roman', serif"
    body: "'Cinzel', 'Special Elegant', 'Times New Roman', serif"
    mono: "'Special Elegant', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=Special+Elegant&family=UnifrakturCook:wght@700&display=swap"
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
    sm: "0"
    md: "1px"
    lg: "2px"
    xl: "3px"
    full: "9999px"
  color:
    default: "#2E2A22"
    subtle: "rgba(126, 135, 148, 0.25)"
    strong: "#C9C2AC"
    focus: "#B98C3F"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.5)"
  sm: "2px 4px 0 rgba(0,0,0,0.55)"
  md: "6px 10px 0 rgba(0,0,0,0.6)"
  lg: "12px 18px 0 rgba(0,0,0,0.65)"
  xl: "20px 28px 0 rgba(0,0,0,0.7)"
  "2xl": "32px 44px 0 rgba(0,0,0,0.75)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.5)"
  focus: "0 0 0 3px rgba(185, 140, 63, 0.45)"

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
    in: "cubic-bezier(0.7, 0, 0.84, 0)"
    out: "cubic-bezier(0.16, 1, 0.3, 1)"
    spring: "cubic-bezier(0.34, 1.3, 0.64, 1)"
  hoverPatterns: [tint, glow, opacity, stroke]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "wide"
  framing: "solid"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "solid"
blur: "none"

iconography:
  treatment: "linear"
  set: "custom"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#C9C2AC"
      color: "#0E0D14"
      border: "1px solid #2E2A22"
      shadow: "4px 6px 0 rgba(0,0,0,0.6)"
      hoverBackground: "#D9D3C0"
      hoverShadow: "6px 9px 0 rgba(0,0,0,0.7)"
      hoverColor: "#0E0D14"
    secondary:
      background: "transparent"
      color: "#C9C2AC"
      border: "1px solid #7E8794"
      shadow: "none"
      hoverBackground: "rgba(201, 194, 172, 0.08)"
      hoverShadow: "2px 3px 0 rgba(0,0,0,0.55)"
      hoverColor: "#C9C2AC"
    ghost:
      background: "transparent"
      color: "#9BA1AC"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(126, 135, 148, 0.1)"
      hoverShadow: "none"
      hoverColor: "#C9C2AC"
    danger:
      background: "#1C2433"
      color: "#AEB9CC"
      border: "1px solid #4D5C78"
      shadow: "4px 6px 0 rgba(0,0,0,0.6)"
      hoverBackground: "#141A25"
      hoverShadow: "6px 9px 0 rgba(0,0,0,0.7)"
      hoverColor: "#D6DCE6"
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "0.875rem" }
      md: { height: "42px", padding: "0 22px", fontSize: "1rem" }
      lg: { height: "52px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "0"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#16151D"
    color: "#C9C2AC"
    border: "1px solid #2E2A22"
    borderRadius: "0"
    padding: "11px 14px"
    focusBorder: "#B98C3F"
    placeholderColor: "#7E8794"
  card:
    base:
      background: "#16151D"
      border: "1px solid #2E2A22"
      borderRadius: "0"
      padding: "24px"
      shadow: "12px 18px 0 rgba(0,0,0,0.65)"
    hover:
      shadow: "20px 28px 0 rgba(0,0,0,0.7)"
      transform: "skewY(-1.5deg) translateY(-2px)"
---

# German Expressionist Cinema

> Hand-painted oblique shadows and acute angles raked across a near-black silent frame — the world is bent, the light is a knife, the dark is alive.

## Origin

German Expressionist cinema was canonized in 1920 when Robert Wiene's *Das Cabinet des Dr. Caligari* premiered in Berlin, produced by Decla-Bioscop (soon absorbed into UFA). Its dread was built not from photography but from painting: the designer-painters Hermann Warm, Walter Reimann, and Walter Röhrig brushed oblique shadows, leaning verticals, and jagged distorted sets directly onto canvas flats, so that light and dark were *applied*, never cast. Conrad Veidt and Werner Krauss moved through these acute angles like figures inside a nightmare drawn in charcoal.

Original nitrate prints were exhibited color-tinted — amber for daylight scenes, steel-blue for night — yet the defining image remains the near-black projected frame edged by painted Caligari shadows. The movement ran c. 1919–1927 across Weimar Berlin and became the direct ancestor of film noir and the horror film, exporting its raked angles and knife-edge contrast into world cinema for the next century.

## Overview

Composition cues:
- **Layout**: Stacked vertical scenes that lean and skew — off-kilter cards, raked dividers, intertitle-style title plates; never an upright rectilinear grid
- **Content width**: Wide framing that lets painted-shadow streaks bleed toward the edges, as on a projected silent frame
- **Framing**: Solid — hard high-contrast edges and painted-shadow borders rather than soft glassy panels
- **Grid intensity**: Soft — the underlying rhythm is present but deliberately distorted by acute angles and leaning verticals

## Colors

The palette is tinted monochrome drawn from color-tinted nitrate prints, never neutral gray-on-gray. The dominant ground is the near-black projected frame (`#0E0D14`) that carries the painted shadows. Highlights are an amber-lit black-and-white tone (`#C9C2AC`), the projected "light" of the silent image. Night scenes deepen toward a steel-blue tint (`#1C2433`); midtones sit at ash gray (`#7E8794`); ornament catches a gilt amber (`#B98C3F`); and the deepest painted shadows warm into shadow-brown (`#2E2A22`). Every hue stays inside the tinted-monochrome world — amber by day, steel-blue by night — and refuses any saturated modern color.

**Role usage**:
- Page background → `colors.background.page` (near-black projected frame `#0E0D14`)
- Content surface → `colors.background.surface` (faintly lifted black `#16151D`)
- Night-tint blocks → `colors.background.subtle` (steel-blue `#1C2433`)
- Primary highlight / amber-lit type → `colors.primary.500` (`#C9C2AC`)
- Gilt ornament / focus accent → `colors.accent.500` (gilt amber `#B98C3F`)
- Ash-gray midtone / muted text → `colors.neutral.400` (`#7E8794`)
- Painted-shadow borders → `borders.color.default` (shadow-brown `#2E2A22`)
- Text on dark ground → `colors.text.primary` (`#C9C2AC`)

## Typography

The type voice carries three registers of the Expressionist frame. **UnifrakturCook** supplies the gothic blackletter / fraktur horror-Expressionist headline — the jagged, ink-cut display voice of the intertitle cards. **Cinzel** delivers engraved Roman caps in the manner of restored title sequences, used for subheads and body in a period serif. **Special Elegant** lends a period display flavor for captions and the monospace role, evoking hand-set silent-era plates. All three are real Google Fonts. Uppercase tracking is held open (`0.05em`) so each engraved letter reads like a struck title-card glyph.

**Text styles**:
- `display-xl` — UnifrakturCook, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — UnifrakturCook, 64px, weight 700, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Cinzel, 48px, weight 700, line-height 1.2, letter-spacing 0.02em
- `body-lg` — Cinzel, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Cinzel, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Special Elegant, 14px, weight 400, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Special Elegant, 16px, weight 400, line-height 1.8, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px — used wide so shadows reach the frame edge
- Section padding: 64px vertical (md), 96px (lg), 128px (xl) — generous dark margins around each leaning scene
- Grid gaps: 16px (md) to 24px (lg), broken by intentional skew rather than held perfectly square

## Elevation & Depth

Depth is painted, not lit. Shadows are hard-edged streaks dropped offset and unblurred — flat black geometric casts brushed onto the set, with no atmospheric softening. Surfaces sit solid on the near-black ground; separation comes from a stark offset drop-shadow that reads like a painted shadow flat rather than a glow.

- Surface style: solid (painted flats on the dark frame)
- Blur: none (shadows are painted streaks, never atmospheric)
- Shadow ladder: hard-edged offset black drops — `xs` through `2xl` increase offset and opacity with **zero blur radius**
- Inner shadow: subtle dark inset for recessed inputs
- Focus ring: 3px gilt-amber glow at 45% opacity — the one warm accent

## Shapes

- `none`: 0 — hard rectilinear edge (then skewed by transform)
- `sm`: 0 — title plates and tags keep knife-sharp corners
- `md`: 1px — barest softening on minor containers
- `lg`: 2px — buttons and cards stay near-square
- `xl`: 3px — largest containers; corners remain acute
- `full`: 9999px — reserved for rare circular medallions / iris-vignette masks

## Motion

Motion is restrained and uneasy, like a hand-cranked projector at slightly wrong speed. Transitions favor a sharp ease-in and a long settle, with the occasional skew shift that recalls a leaning set righting itself. No bouncing, no playful spring on UI chrome — the temperament is dread held taut, not delight.

- Level: restrained
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)`; in `cubic-bezier(0.7, 0, 0.84, 0)`; out `cubic-bezier(0.16, 1, 0.3, 1)`
- Hover patterns: tint (toward amber), glow (gilt focus), opacity (nitrate fade), stroke (painted-shadow edge thickens)
- `reducedMotion: true` — flicker and skew effects respect `prefers-reduced-motion`

## Techniques

### Painted oblique shadow
A hard-edged, unblurred offset drop that reads as a shadow *painted* onto the set rather than cast by light — the signature Caligari shadow flat.
```css
.element {
  position: relative;
  background: #16151D;
  border: 1px solid #2E2A22;
  box-shadow: 12px 18px 0 rgba(0, 0, 0, 0.65);
}
.element::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(118deg, transparent 58%, rgba(0, 0, 0, 0.55) 58.2%, rgba(0, 0, 0, 0.55) 64%, transparent 64.2%);
  pointer-events: none;
}
```

### Raked skew frame
An off-kilter card that leans on an acute angle, counter-skewing its content so text stays legible while the frame distorts — the leaning verticals of an Expressionist set.
```css
.element {
  transform: skewY(-2deg) rotate(-1deg);
  border: 1px solid #2E2A22;
  background: #16151D;
  box-shadow: 12px 18px 0 rgba(0, 0, 0, 0.65);
}
.element > * {
  transform: skewY(2deg) rotate(1deg);
}
```

### Nitrate flicker grain
A film-grain flicker overlay that animates the amber-by-day / steel-blue-by-night tint of an old nitrate print across the dark frame.
```css
.element {
  position: relative;
  background: #0E0D14;
}
.element::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    repeating-linear-gradient(0deg, rgba(201,194,172,0.04) 0 1px, transparent 1px 3px),
    radial-gradient(120% 80% at 50% 0%, rgba(185,140,63,0.08), transparent 60%),
    radial-gradient(120% 80% at 50% 100%, rgba(28,36,51,0.18), transparent 60%);
  mix-blend-mode: screen;
  animation: nitrate-flicker 320ms steps(3) infinite;
}
@keyframes nitrate-flicker {
  0%, 100% { opacity: 0.85; }
  33% { opacity: 1; }
  66% { opacity: 0.78; }
}
@media (prefers-reduced-motion: reduce) {
  .element::before { animation: none; opacity: 0.9; }
}
```

## Iconography

Icons read like engraved title-card marks and painted-shadow glyphs rather than utilitarian pictograms — keys, daggers, somnambulist silhouettes, iris vignettes, and jagged shadow-streaks drawn with the same brush as the sets. Where functional icons are needed, render them as custom linear strokes at 1.5px, monochrome in the amber-lit primary tone, optionally edged with a single hard painted-shadow offset.

- Treatment: linear (engraved single-weight strokes)
- Set: custom (period film-card motifs)
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use the near-black projected frame `#0E0D14` as the page ground — the dark field carries every painted shadow
- Set headlines in UnifrakturCook blackletter and engraved caps in Cinzel to hold the horror-Expressionist and restored-title voices
- Skew, lean, and cut frames at acute angles so the geometry feels bent and distorted
- Paint shadows as hard-edged offset streaks — apply shadow, do not simulate cast light
- Keep the whole palette in tinted monochrome: amber for day, steel-blue for night, gilt amber for ornament

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — the ground is the near-black projected frame
- No clean upright rectilinear grids — geometry must lean, skew, and cut at acute angles
- No naturalistic photographic lighting — shadows are painted onto the set, not cast
- No saturated modern color — stay in tinted monochrome (amber day, steel-blue night)
- Don't soften shadows into blurred glows — the painted shadow is sharp-edged and flat

## Applications

This system suits film retrospectives, horror and thriller microsites, festival and repertory-cinema landing pages, and editorial features on Weimar art and silent film. It excels wherever dread, atmosphere, and a hand-made graphic menace are wanted — title sequences, album and poster art, narrative scrollytelling, and exhibition companions for German Expressionism. The near-black tinted-monochrome frame and blackletter voice also fit gothic literary brands and dramatic, story-driven product launches.
