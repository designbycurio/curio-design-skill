---
version: 1

meta:
  id: bollywood-poster-1970s
  name: Bollywood Poster Art (1970s)
  description: Hand-painted Mumbai cinema billboards — saturated saffron, dramatic diagonals, and 3D-shadowed display type.
  isDark: false
  tags: [bold, decorative, narrative, retro, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1960s–1980s peak hand-painted tradition; golden age ~1970s"
  region: "Mumbai (Bombay), India — D.N. Road poster studios"
  regionZh: "印度孟买 · D.N. 路海报工坊"
  keyFigures: ["M.F. Husain", "Diwakar Karkare", "S.M. Pandit", "Balkrishna Arts"]
  movements: ["Indian hand-painted cinema billboard tradition", "Hindi film industry visual culture", "South Asian popular art"]

introduction: |
  Bollywood Poster Art of the 1970s is the hand-painted cinema billboard tradition of India — larger-than-life actor portraits, clashing saturated colors, and dramatic diagonal compositions painted by master artists in the studios along Mumbai's D.N. Road. This is the visual grammar of Hindi cinema's golden age, the era of Sholay, Deewaar, and Amitabh Bachchan's "angry young man."

  The belief is simple: subtlety is for people who can't afford a 40-foot billboard. Every hex is turned to maximum saturation, every title is 3D-shadowed, every figure leaps across the frame. The hero is ten meters tall, the colors are as loud as the music, and the background is never white.
introductionZh: |
  七十年代宝莱坞海报，是印度孟买 D.N. 路海报工坊里手绘师傅们留下的电影招贴传统。巨幅的主角肖像、夸张的对角构图、永远开到最饱和的撞色，画在影院门口那块十米高的铁皮广告牌上——这是印地语电影黄金时代的视觉语言，是《Sholay》《Deewaar》以及"愤怒青年"阿米特巴·巴沙坎的年代。

  它的信条很直接：节制，是买不起四十英尺海报的人才谈的事情。每一种颜色都拉到最浓的一档，每一个片名都带三维投影，每一个主角都斜斜扑出画面。背景从来不是白的，是藏红花橙、是孟加拉红、是午夜藏青，再压上一层手绘笔触的厚重与电影灯光的晕光。

colors:
  primary:
    "50":  "#FFF3E0"
    "100": "#FFE0B2"
    "200": "#FFCC80"
    "300": "#FFB74D"
    "400": "#FF9800"
    "500": "#E65100"
    "600": "#CC4700"
    "700": "#B33D00"
    "800": "#8F3000"
    "900": "#662200"
    "950": "#401500"
  secondary:
    "50":  "#E8EAF6"
    "100": "#C5CAE9"
    "200": "#9FA8DA"
    "300": "#7986CB"
    "400": "#3F51B5"
    "500": "#1A237E"
    "600": "#171F6D"
    "700": "#141B5C"
    "800": "#0F1449"
    "900": "#0A0E33"
    "950": "#05071A"
  accent:
    "50":  "#FCE4EC"
    "100": "#F8BBD0"
    "200": "#F48FB1"
    "300": "#F06292"
    "400": "#EC407A"
    "500": "#E91E63"
    "600": "#D81B60"
    "700": "#C2185B"
    "800": "#AD1457"
    "900": "#880E4F"
    "950": "#4A0028"
  neutral:
    "50":  "#FFF8E1"
    "100": "#FAF1D4"
    "200": "#EFE3BC"
    "300": "#D8C69A"
    "400": "#AFA078"
    "500": "#7A6D4F"
    "600": "#5C5238"
    "700": "#423B27"
    "800": "#2A2518"
    "900": "#15120B"
    "950": "#0A0805"
  semantic:
    success: { bg: "#1B5E20", text: "#FFF8E1", light: "#C8E6C9", border: "#2E7D32" }
    warning: { bg: "#FFD600", text: "#1A1A1A", light: "#FFF8C4", border: "#F9A825" }
    error:   { bg: "#CC2200", text: "#FFF8E1", light: "#FFCDD2", border: "#B71C1C" }
    info:    { bg: "#1A237E", text: "#FFF8E1", light: "#C5CAE9", border: "#283593" }
  background:
    page:    "#E65100"
    surface: "#FFF8E1"
    subtle:  "#FAF1D4"
  text:
    primary:   "#1A1A1A"
    secondary: "#423B27"
    muted:     "#7A6D4F"
    inverse:   "#FFD600"

typography:
  families:
    heading: "'Teko', 'Bungee', 'Impact', sans-serif"
    body:    "'Mukta', 'Baloo 2', 'Segoe UI', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Teko:wght@400;500;600;700&family=Bungee&family=Bungee+Shade&family=Baloo+2:wght@500;600;700;800&family=Mukta:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.0, snug: 1.15, normal: 1.5, relaxed: 1.65, loose: 1.85}
  letterSpacing: {tighter: "-0.02em", tight: "0", normal: "0.02em", wide: "0.08em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "4px", md: "8px", lg: "12px", xl: "16px", full: "9999px"}
  color:  {default: "#1A1A1A", subtle: "#CC4700", strong: "#000000", focus: "#FFD600"}
  width:  {thin: "1px", default: "2px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "1px 1px 0 rgba(0,0,0,0.4)"
  sm: "2px 2px 0 rgba(0,0,0,0.5)"
  md: "4px 4px 0 rgba(0,0,0,0.55)"
  lg: "6px 6px 0 rgba(0,0,0,0.6), 0 0 24px rgba(255,214,0,0.25)"
  xl: "8px 8px 0 rgba(0,0,0,0.65), 0 0 48px rgba(233,30,99,0.3)"
  "2xl": "12px 12px 0 rgba(0,0,0,0.7), 0 0 80px rgba(255,214,0,0.35)"
  inner: "inset 0 2px 0 rgba(255,248,225,0.4), inset 0 -2px 0 rgba(0,0,0,0.25)"
  focus: "0 0 0 4px rgba(255,214,0,0.55)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.55, 0, 1, 0.45)"
    out:     "cubic-bezier(0, 0.55, 0.45, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, scale, glow, tint]
  reducedMotion: true

composition:
  layout:        stack
  contentWidth:  wide
  framing:       bordered
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: layered
blur:         none

iconography:
  treatment: filled
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:
      background: "#CC2200"
      color: "#FFD600"
      border: "2px solid #1A1A1A"
      shadow: "4px 4px 0 #1A1A1A"
      hoverBackground: "#E91E63"
      hoverShadow: "6px 6px 0 #1A1A1A, 0 0 24px rgba(255,214,0,0.4)"
      hoverColor: "#FFF8E1"
    secondary:
      background: "#1A237E"
      color: "#FFD600"
      border: "2px solid #1A1A1A"
      shadow: "4px 4px 0 #1A1A1A"
      hoverBackground: "#283593"
      hoverShadow: "6px 6px 0 #1A1A1A"
      hoverColor: "#FFF8E1"
    ghost:
      background: "transparent"
      color: "#FFD600"
      border: "2px solid #FFD600"
      shadow: "none"
      hoverBackground: "rgba(255,214,0,0.15)"
      hoverShadow: "2px 2px 0 rgba(255,214,0,0.5)"
      hoverColor: "#FFF8E1"
    danger:
      background: "#CC2200"
      color: "#FFF8E1"
      border: "2px solid #000000"
      shadow: "4px 4px 0 #000000"
      hoverBackground: "#B71C1C"
      hoverShadow: "6px 6px 0 #000000"
      hoverColor: "#FFD600"
    sizes:
      sm: {height: "36px", padding: "0 16px", fontSize: "0.875rem"}
      md: {height: "48px", padding: "0 24px", fontSize: "1.125rem"}
      lg: {height: "60px", padding: "0 36px", fontSize: "1.5rem"}
    borderRadius: "8px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFF8E1"
    color: "#1A1A1A"
    border: "2px solid #1A1A1A"
    borderRadius: "8px"
    padding: "12px 16px"
    focusBorder: "2px solid #E91E63"
    placeholderColor: "#7A6D4F"
  card:
    base:
      background: "#FFF8E1"
      border: "3px solid #1A1A1A"
      borderRadius: "8px"
      padding: "24px"
      shadow: "8px 8px 0 #1A1A1A"
    hover:
      shadow: "12px 12px 0 #1A1A1A, 0 0 48px rgba(255,214,0,0.3)"
      transform: "translate(-2px, -2px)"
---

# Bollywood Poster Art (1970s)

> The hero is ten meters tall and the colors are as loud as the music.

## Origin

Bollywood poster art of the 1970s is the hand-painted cinema billboard tradition of India, produced by master painters working in studios along Mumbai's D.N. Road — Balkrishna Arts, the ateliers of Diwakar Karkare and S.M. Pandit, and even M.F. Husain in his early commercial years. Through the 1960s, '70s, and early '80s, these artists hand-painted tens of thousands of unique posters and forty-foot billboards for Hindi cinema, one brushstroke at a time, onto canvas and tin.

The 1970s were the golden age: *Sholay* (1975), *Bobby* (1973), *Deewaar* (1975), *Don* (1978). Amitabh Bachchan's "angry young man" figure, leaping across a saffron sky with a pistol in his hand, defined the visual grammar. When photo-offset printing killed the handmade tradition in the 1990s, what remained was a legacy of dramatic diagonals, saturated color clashes, and a belief that subtlety is for people who can't afford a four-story billboard.

## Overview

Composition cues:
- **Layout**: stacked dramatic bands — hero figure bleeds over backdrop, title sits on a diagonal banner
- **Content width**: wide, edge-to-edge saturated fills; no polite margins
- **Framing**: heavy black borders around poster panels, like cinema-hall hoardings
- **Grid intensity**: soft — the grid is theatrical, not Swiss; rules are broken for drama
- **Rhythm**: 8px base, but typographic rhythm dominates over geometric grid

## Colors

Every hex is turned to maximum saturation, then a 3D black shadow is placed behind it. Saffron orange is the hero backdrop; deep vermillion is reserved for violence and passion; royal blue signals night and villainy; hot pink is romance; marigold yellow is the sun and the title type; emerald is the jungle. Nothing is muted — if a color looks tasteful on screen, turn it up until the paint is about to drip.

**Role usage**:
- Page background → `colors.background.page` (`#E65100` saffron, full-bleed)
- Content card surface → `colors.background.surface` (`#FFF8E1` warm cream)
- Body text on cream → `colors.text.primary` (`#1A1A1A`)
- Title / hero text on saturated bg → `colors.text.inverse` (`#FFD600` marigold, 3D-shadowed)
- Primary CTA fill → `colors.accent.500` (`#E91E63` hot pink) or `#CC2200` vermillion
- Secondary / night panels → `colors.secondary.500` (`#1A237E` royal blue)
- Hero accent strokes → `colors.accent.500` (`#E91E63`)
- Destructive / dramatic → `colors.semantic.error.bg` (`#CC2200` vermillion)

## Typography

Type should feel like it was painted, not typed. Display headlines use **Bungee** for blocky poster energy, `Teko` for condensed theatrical headlines, and `Baloo 2` for Devanagari-ready rounded subheads. Body copy sits in **Mukta**, a workhorse Devanagari-and-Latin family that keeps the page readable without losing the South Asian voice. Mix colors per letter on hero titles, keep a 2–4px hard black offset on every display run.

**Text styles**:
- `display-xl` — Bungee, 96px, weight 400, line-height 1.0, letter-spacing 0.02em, 3D shadow `4px 4px 0 #1A1A1A`
- `display-lg` — Bungee, 72px, weight 400, line-height 1.0, letter-spacing 0.02em, 3D shadow
- `heading-1` — Teko, 56px, weight 700, line-height 1.1, letter-spacing 0.04em, uppercase, shadow `2px 2px 0 rgba(0,0,0,0.5)`
- `heading-2` — Teko, 40px, weight 600, line-height 1.15, letter-spacing 0.04em, uppercase
- `heading-3` — Baloo 2, 28px, weight 700, line-height 1.25, letter-spacing 0.01em
- `body-lg` — Mukta, 18px, weight 500, line-height 1.6, letter-spacing 0
- `body-md` — Mukta, 16px, weight 400, line-height 1.65, letter-spacing 0
- `caption` — Mukta, 13px, weight 600, line-height 1.4, letter-spacing 0.08em, uppercase
- `mono-md` — JetBrains Mono, 14px, weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: `4px`; canonical scale `2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128` px
- Container: `wide` (`1280px` max), generous `section-padding` at `96–128px`
- Grid gap: `16–24px` typical; posters are stacked, not gridded
- Section rhythm: saturated full-bleed bands separated by heavy black rules or painted banners

## Elevation & Depth

Depth is painted, not rendered. Instead of diffuse Gaussian shadows, every surface throws a hard-offset black drop-shadow like a poster pasted over another poster. Cards sit on the page with a 6–12px black block shadow, then pick up a soft warm glow (`rgba(255,214,0,0.3)`) on hover, as if a cinema-hall spotlight just found them.

- Surface style: `layered` — cream content panels pasted over saturated backdrops
- Blur: `none` — hand-painted world, no CSS blur
- Shadow ladder: `xs 1px` hint → `sm 2px` text shadow → `md 4px` card rest → `lg 6px` card hover + glow → `xl 8px` hero panel → `2xl 12px` marquee
- Inner shadow reserved for inset badges / title plates

## Shapes

- Corner radii: `none 0`, `sm 4px`, `md 8px` (default for cards/buttons), `lg 12px`, `xl 16px`, `full 9999px` (starburst badges / circular portrait vignettes)
- Borders: `2px` default, `4px` thick for hero panels, always `#1A1A1A` (painter's outline)
- Embrace diagonal and circular masks (`clip-path: polygon(...)`, `border-radius: 50%`) for portrait vignettes

## Motion

Motion should feel like a cinema-hall hoarding catching a passing breeze: a decisive lift, a slight rotation, a flicker of warm light. Avoid long eased-out fades — posters don't ease, they snap into place.

- Level: `lively`
- Durations: `instant 0`, `fast 120`, `normal 250`, `slow 400`, `slower 600` ms
- Easings: spring (`cubic-bezier(0.34, 1.56, 0.64, 1)`) for card hover; default cubic for state changes
- Hover patterns: `lift` (translate by -2px), `scale` (1.02), `glow` (yellow halo), `tint` (saturate +10%)
- `prefers-reduced-motion`: honored — drop the lift, keep the tint

## Techniques

### 3D poster-shadow display type
Stack two hard-offset shadows (black drop + cream highlight) to get the painted "popped off the billboard" feel that defined Amitabh Bachchan-era title cards.
```css
.poster-title {
  font-family: 'Bungee', 'Teko', sans-serif;
  font-size: clamp(3.5rem, 8vw, 6rem);
  color: #FFD600;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  line-height: 1.0;
  text-shadow:
    2px 2px 0 #CC2200,
    4px 4px 0 #1A1A1A,
    6px 6px 0 #1A237E,
    8px 8px 12px rgba(0, 0, 0, 0.4);
  transform: rotate(-2deg);
}
```

### Diagonal saffron banner
The angled title banner crossing a saturated backdrop is the single most recognizable Bollywood compositional move — hero face peeking above, action scene below.
```css
.diagonal-banner {
  position: relative;
  background: linear-gradient(95deg, #E65100 0%, #CC2200 60%, #E91E63 100%);
  color: #FFD600;
  padding: 48px 64px;
  clip-path: polygon(0 10%, 100% 0, 100% 90%, 0 100%);
  border-top: 4px solid #1A1A1A;
  border-bottom: 4px solid #1A1A1A;
  box-shadow: 0 8px 0 #1A1A1A, 0 16px 48px rgba(0, 0, 0, 0.35);
}
.diagonal-banner::after {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 30% 50%, rgba(255, 214, 0, 0.35), transparent 60%);
  mix-blend-mode: screen;
  pointer-events: none;
}
```

### Starburst price / label badge
Painted starburst badges punched onto posters to shout a ticket price, a new release, or a marquee name.
```css
.starburst-badge {
  --spikes: 16;
  width: 120px; height: 120px;
  display: grid; place-items: center;
  background: #FFD600;
  color: #CC2200;
  font-family: 'Bungee', sans-serif;
  font-size: 1.25rem;
  text-align: center;
  border: 3px solid #1A1A1A;
  clip-path: polygon(
    50% 0%, 58% 18%, 79% 12%, 71% 32%, 92% 38%, 74% 52%,
    92% 62%, 71% 68%, 79% 88%, 58% 82%, 50% 100%, 42% 82%,
    21% 88%, 29% 68%, 8% 62%, 26% 52%, 8% 38%, 29% 32%,
    21% 12%, 42% 18%
  );
  filter: drop-shadow(4px 4px 0 #1A1A1A);
  transform: rotate(-8deg);
}
```

## Iconography

Use filled, weighty icon shapes rather than thin linear strokes — Phosphor's "fill" cut, or custom hand-painted glyphs, with a 2px black outline where possible. Icons should read as painted silhouettes at billboard distance, never as hairline UI marks. Allow occasional rotation (−8° to +8°) to echo the painted imperfection of hand-lettered posters.

- Treatment: `filled`, sometimes `duotone` (saffron + black)
- Set: `phosphor` (fill weight) or custom
- Stroke: `2px` outline when a stroke is needed

## Do's & Don'ts

### ✓ Do
- Push every brand hex to full saturation — if it looks tasteful, turn it up.
- Layer a hard 3D drop-shadow (`2–4px 2–4px 0 #1A1A1A`) behind every display title.
- Compose with diagonals, circular vignettes, and starburst badges instead of orthogonal grids.
- Use saffron `#E65100` as the dominant page backdrop and marigold `#FFD600` for hero text on it.
- Mix display families freely — Bungee for blocky titles, Teko for condensed lines, Baloo 2 for Devanagari-ready subheads.

### ✗ Don't
- Don't use muted or pastel palettes — Bollywood is SATURATED.
- Don't pursue minimalism; this tradition is maximalist by design.
- Don't set display type in modern clean sans-serif — it reads as 2020s startup, not 1975 cinema.
- Don't use white or neutral page backgrounds — commit to full-bleed saturated color.
- Don't apply a restrained Swiss-style grid; the composition must feel theatrical and dynamic.
- Don't set subtle flat typography on hero surfaces — text should be 3D and dramatic.

## Applications

Best-fit use cases: film and festival microsites, music-streaming campaign pages, food-and-drink brands with a South Asian story, cultural institution exhibitions, merch drops, retro-gaming launch art, and any hero marketing moment that needs to shout across a scroll distance the way a hand-painted billboard shouts across a Mumbai intersection. Less suitable for dense dashboards, medical or fintech compliance UI, or anywhere "calm" is a product requirement.
