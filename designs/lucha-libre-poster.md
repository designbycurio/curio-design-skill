---
version: 1

meta:
  id: lucha-libre-poster
  name: Lucha Libre Poster
  description: "Black-ground maximalist poster screaming fluorescent yellow, crimson diagonals, and masked-fighter energy from 1970s Arena México"
  isDark: true
  tags: [bold, decorative, historical, experimental, retro]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1960s–1980s peak; visual heritage active through today"
  region: "Mexico City (Arena México, Arena Coliseo), Guadalajara, Mexico"
  regionZh: "墨西哥城（墨西哥竞技场、罗马竞技场）、瓜达拉哈拉"
  keyFigures: [El Santo, Blue Demon, Mil Máscaras, anonymous Mexican screen printers]
  movements: [Lucha Libre wrestling culture, Mexican street poster tradition, Cantinflas-era popular culture]

introduction: |
  Lucha Libre posters are the loudest graphic vocabulary in Latin American print culture. Born from 1960s–80s Mexico City wrestling promotion, each A2 sheet crams diagonal-axis layouts, screaming hand-lettered display type, masked-fighter silhouettes, and a saturated red-yellow-blue-silver palette into a single broadsheet designed to grab attention from across a dusty street.

  This design system translates that maximalist poster energy into digital tokens: pure black grounds, fluorescent yellow headline banners, crimson diagonal price chips, cobalt blue accents, and the sharp-cornered, no-radius geometry of a screenprinted event flyer — all rendered in CSS with zero rounded corners and zero apology.
introductionZh: |
  墨西哥摔角海报是拉丁美洲印刷文化中最响亮的视觉语汇。诞生于 1960-80 年代墨西哥城竞技场的赛事宣传——每张 A2 海报都把对角线构图、嘶吼般的手写粗体字、蒙面摔角手剪影、以及饱和的红黄蓝银配色塞进一张纸里，在尘土飞扬的街头抢夺路人视线。

  这套设计系统将那种极繁海报能量转化为数字令牌：纯黑底色、荧光黄标题横幅、猩红对角线价格标签、钴蓝副标题——所有圆角归零、所有阴影归零，忠实还原丝网印刷海报那种刀切般的锋利感。

colors:
  primary:
    "50": "#FFFEF0"
    "100": "#FEFCD6"
    "200": "#FDF9AD"
    "300": "#FDF585"
    "400": "#FCF14D"
    "500": "#FCEE0A"
    "600": "#D4C808"
    "700": "#A69D06"
    "800": "#787205"
    "900": "#4A4603"
    "950": "#2D2B02"
  secondary:
    "50": "#FEF2F2"
    "100": "#FDE3E3"
    "200": "#FBC5C5"
    "300": "#F79898"
    "400": "#EF5555"
    "500": "#DC2626"
    "600": "#BA1E1E"
    "700": "#971818"
    "800": "#711212"
    "900": "#4C0D0D"
    "950": "#2E0808"
  accent:
    "50": "#EEF2FA"
    "100": "#D4DEF2"
    "200": "#A8BDE6"
    "300": "#7C9BD9"
    "400": "#4B6FC5"
    "500": "#1E40AF"
    "600": "#193593"
    "700": "#142A77"
    "800": "#0F1F5B"
    "900": "#0A153F"
    "950": "#060C26"
  neutral:
    "50": "#F5F5F5"
    "100": "#E5E5E5"
    "200": "#CCCCCC"
    "300": "#B0B0B0"
    "400": "#8A8A8A"
    "500": "#666666"
    "600": "#4D4D4D"
    "700": "#383838"
    "800": "#262626"
    "900": "#1A1A1A"
    "950": "#0F0F0F"
  semantic:
    success: { bg: "#1A2E1A", text: "#4ADE4A", light: "#0F1F0F", border: "#2A4F2A" }
    warning: { bg: "#2E2A16", text: "#FCEE0A", light: "#1F1C0F", border: "#4F4520" }
    error: { bg: "#2E1A18", text: "#EF5555", light: "#1F0F0E", border: "#4F2A27" }
    info: { bg: "#1A1F2E", text: "#7C9BD9", light: "#0F1420", border: "#2A3A4F" }
  background:
    page: "#0A0A0A"
    surface: "#1A1A1A"
    subtle: "#262626"
  text:
    primary: "#FFFFFF"
    secondary: "#FCEE0A"
    muted: "#8A8A8A"
    inverse: "#0A0A0A"

typography:
  families:
    heading: "'Anton', 'Bebas Neue', 'Impact', sans-serif"
    body: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    mono: "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Anton&family=Barlow+Condensed:wght@300;400;500;600;700&family=Oswald:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"
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
    tight: 0.9
    snug: 1.0
    normal: 1.3
    relaxed: 1.5
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
    sm: "4px"
    md: "8px"
    lg: "16px"
    xl: "24px"
  sectionPadding:
    sm: "24px"
    md: "48px"
    lg: "64px"
    xl: "96px"

borders:
  radius:
    none: "0"
    sm: "0"
    md: "0"
    lg: "0"
    xl: "0"
    full: "9999px"
  color:
    default: "#383838"
    subtle: "#262626"
    strong: "#FCEE0A"
    focus: "#FCEE0A"
  width:
    thin: "1px"
    default: "2px"
    thick: "4px"
  style: "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  "2xl": "none"
  inner: "none"
  focus: "0 0 0 3px rgba(252,238,10,0.4)"

motion:
  level: "lively"
  durations:
    instant: "0ms"
    fast: "100ms"
    normal: "200ms"
    slow: "350ms"
    slower: "500ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.55, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.22, 1, 0.36, 1)"
  hoverPatterns: [scale, tint, opacity, stroke]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "full-bleed"
  framing: "solid"
  gridIntensity: "strong"
  rhythm: "4px"

surfaceStyle: "flat"
blur: "none"

iconography:
  treatment: "filled"
  set: "phosphor"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "2px"

components:
  button:
    primary:
      background: "#FCEE0A"
      color: "#0A0A0A"
      border: "2px solid #0A0A0A"
      shadow: "none"
      hoverBackground: "#FFFFFF"
      hoverShadow: "none"
      hoverColor: "#0A0A0A"
    secondary:
      background: "#DC2626"
      color: "#FFFFFF"
      border: "2px solid #DC2626"
      shadow: "none"
      hoverBackground: "#EF5555"
      hoverShadow: "none"
      hoverColor: "#FFFFFF"
    ghost:
      background: "transparent"
      color: "#FCEE0A"
      border: "2px solid #FCEE0A"
      shadow: "none"
      hoverBackground: "rgba(252,238,10,0.1)"
      hoverShadow: "none"
      hoverColor: "#FFFFFF"
    danger:
      background: "#DC2626"
      color: "#FFFFFF"
      border: "2px solid #FFFFFF"
      shadow: "none"
      hoverBackground: "#BA1E1E"
      hoverShadow: "none"
      hoverColor: "#FFFFFF"
    sizes:
      sm: { height: "36px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "44px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "56px", padding: "0 36px", fontSize: "1.25rem" }
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "-0.02em"
    textTransform: "uppercase"
  input:
    background: "#0A0A0A"
    color: "#FFFFFF"
    border: "2px solid #666666"
    borderRadius: "0"
    padding: "10px 14px"
    focusBorder: "2px solid #FCEE0A"
    placeholderColor: "#666666"
  card:
    base:
      background: "#1A1A1A"
      border: "2px solid #383838"
      borderRadius: "0"
      padding: "24px"
      shadow: "none"
    hover:
      shadow: "none"
      transform: "scale(1.02)"
---

# Lucha Libre Poster

> Black-ground maximalist poster screaming fluorescent yellow, crimson diagonals, and masked-fighter energy from 1970s Arena México.

## Origin

Lucha Libre — Mexican professional wrestling — has been a mass spectacle since the 1930s, but its poster tradition hit its visual peak between the 1960s and 1980s. Arena México and Arena Coliseo in Mexico City were the cathedrals of the sport, and their weekly event posters became an art form unto themselves. Anonymous screen printers working on tight deadlines developed a visual language of extreme economy and maximum impact: black grounds to save ink, fluorescent yellow and crimson to burn through urban visual noise, and condensed all-caps type jammed so tight it vibrated. Legendary luchadores like El Santo, Blue Demon, and Mil Máscaras became icons whose masked silhouettes were as recognizable as any corporate logo.

The posters were glued to street walls, taped to tienda windows, and plastered over previous weeks' announcements in layers that created accidental archaeological strata of graphic design. Their visual DNA — diagonal composition, color-on-black contrast, horror-vacui density — influenced everything from El Santo's film posters to Lucha Libre magazine covers and eventually the global Lucha Libre merchandise aesthetic. The style says: "There is no such thing as too loud — the next fight is more important than your taste."

## Overview
Composition cues:
- **Layout**: Grid-based with aggressive diagonal axis — banners, text blocks, and price chips rotated 8°–15° off horizontal
- **Content width**: Full-bleed — every pixel of the black ground is contested territory
- **Framing**: Solid filled blocks (yellow banners, crimson chips) with hard 2px black outlines, no transparency
- **Grid intensity**: Strong — packed multi-column grids with minimal gutters, every cell filled

## Colors
The palette is a Mexican wrestling ring translated to print: pure black void as the ground, fluorescent yellow (#FCEE0A) for the headlines that must scream louder than the crowd, pure crimson (#DC2626) for the price chips and accent stripes that create diagonal energy, and cobalt blue (#1E40AF) for secondary headlines and masked-fighter accent details. Metallic silver (#E5E5E5) appears sparingly for foil-mask shimmer effects. White (#FFFFFF) is for shouted small text — card names, dates, venue addresses. There are no earth tones, no cream, no pastels, no muted anything. Every color is at full saturation because this poster has to be readable from across a dusty street.

**Role usage**:
- Page background → `colors.background.page` (#0A0A0A pure black void)
- Card / surface panels → `colors.background.surface` (#1A1A1A ring-mat dark)
- Primary headline banners → `colors.primary.500` (#FCEE0A fluorescent yellow)
- Diagonal price chips and accent stripes → `colors.secondary.500` (#DC2626 crimson)
- Secondary headlines and accents → `colors.accent.500` (#1E40AF cobalt blue)
- Body text → `colors.text.primary` (#FFFFFF pure white)
- Highlight text on dark → `colors.text.secondary` (#FCEE0A yellow)
- Black text on yellow banners → `colors.text.inverse` (#0A0A0A)

## Typography
The typographic voice is a screaming ringside announcer — all caps, jammed tight, shaking with momentum. Display headlines use Anton, a grotesque condensed face whose extreme vertical proportions and tight default spacing replicate the hand-lettered compression of vintage Lucha posters. Subheadlines use Oswald at heavy weights for secondary hierarchy. Body text uses Barlow Condensed — a narrow humanist sans that maintains readability at small sizes while preserving the poster's condensed energy. Every heading is uppercase, every letter jammed tight with negative tracking. Text rotated 8°–15° on diagonal banners is the signature move.

**Text styles**:
- `display-xl` — Anton, 96px, weight 400, line-height 0.9, letter-spacing -0.02em, uppercase
- `display-lg` — Anton, 72px, weight 400, line-height 0.9, letter-spacing -0.02em, uppercase
- `heading-1` — Anton, 48px, weight 400, line-height 1.0, letter-spacing -0.02em, uppercase
- `body-lg` — Barlow Condensed, 18px, weight 400, line-height 1.3, letter-spacing 0
- `body-md` — Barlow Condensed, 16px, weight 400, line-height 1.3, letter-spacing 0
- `caption` — Barlow Condensed, 12px, weight 600, line-height 1.0, letter-spacing 0.05em, uppercase
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.3, letter-spacing 0

## Spacing & Layout
- Base unit: 4px; primary rhythm on a 4px grid (tighter than standard — poster density demands it)
- Spacing scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container: full-bleed preferred; when constrained, max 1280px
- Section padding: 24–64px vertical — tight, maximalist, no wasteful whitespace
- Grid gaps: 4–8px (poster-tight) — content blocks press against each other
- Cards use 24px internal padding with 2px solid borders, 0px radius

## Elevation & Depth
Flat. Absolutely flat. This is screenprint on paper — there are no shadows, no glass, no blur, no floating layers. Depth is created through color stacking (yellow banner over black ground, crimson chip over yellow banner) and overlapping rotated elements. The material metaphor is ink on paper: opaque, hard-edged, zero z-axis. If you reach for `box-shadow`, you have left the wrestling ring and entered a SaaS dashboard.

- Surface style: Flat opaque color blocks
- Blur: None
- Shadow ladder: All `none` — flat poster aesthetic
- Focus ring: `0 0 0 3px rgba(252,238,10,0.4)` — yellow halo (only concession to interactivity)

## Shapes
- All border-radius: 0px — sharp corners are non-negotiable
- Buttons: 0px radius, hard rectangles
- Cards: 0px radius, hard rectangles with 2px borders
- Inputs: 0px radius
- Diagonal-cut edges achieved via CSS `clip-path` or `transform: skewX()`, not border-radius
- Masked-fighter silhouettes as CSS clip-path or SVG cutouts

## Motion
Motion is lively and punchy — the energy of a luchador leaping from the top rope. Transitions are fast and snappy, not elegant or eased. Elements slam into place rather than floating. Scale-up on hover mimics the poster's "coming at you" aggression. No gentle fades — hard cuts preferred.

- Level: Lively
- Durations: fast 100ms (micro), normal 200ms (state changes), slow 350ms (reveals), slower 500ms (page transitions)
- Easings: default `cubic-bezier(0.4, 0, 0.2, 1)`, spring `cubic-bezier(0.22, 1, 0.36, 1)` for punch
- Hover patterns: scale-up (1.02–1.05), yellow tint shift, opacity punch, stroke thickening
- Reduced-motion: fully supported

## Techniques

### Diagonal Banner Stripe
The signature Lucha Libre poster device — a rotated filled banner that cuts diagonally across the layout, carrying headline text in black-on-yellow.
```css
.diagonal-banner {
  background: #FCEE0A;
  color: #0A0A0A;
  font-family: 'Anton', sans-serif;
  font-size: 2.5rem;
  text-transform: uppercase;
  letter-spacing: -0.02em;
  padding: 12px 48px;
  transform: rotate(-5deg);
  display: inline-block;
  position: relative;
  z-index: 2;
  border: 2px solid #0A0A0A;
}
```

### Crimson Price Chip
The diagonal price tag — a skewed rectangle with bold numerals, used for pricing, dates, or any "grab your attention NOW" callout.
```css
.price-chip {
  background: #DC2626;
  color: #FFFFFF;
  font-family: 'Anton', sans-serif;
  font-size: 1.5rem;
  text-transform: uppercase;
  padding: 8px 24px;
  transform: skewX(-12deg);
  display: inline-block;
  border: 2px solid #0A0A0A;
}
.price-chip > span {
  display: inline-block;
  transform: skewX(12deg);
}
```

### Halftone Dot Overlay
A CSS halftone dot screen that mimics the screenprint registration texture of vintage Lucha posters — applied as an overlay on photographic or hero sections.
```css
.halftone-overlay {
  position: relative;
}
.halftone-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle, #0A0A0A 1px, transparent 1px);
  background-size: 4px 4px;
  opacity: 0.3;
  pointer-events: none;
  mix-blend-mode: multiply;
}
```

## Iconography
Icons are bold and filled — matching the poster's ink-heavy, no-subtlety ethos. Phosphor icons in filled weight provide the chunky, unapologetic silhouettes that echo masked-fighter iconography. Stroke weight is 2px, heavier than typical UI, because delicate linework disappears against the visual noise of a Lucha poster layout.

- Treatment: Filled (solid silhouettes)
- Set: Phosphor
- Stroke: 2px

## Do's & Don'ts

### ✓ Do
- Use fluorescent yellow (#FCEE0A) for all primary headlines and banner backgrounds
- Set all display type in Anton at maximum condensed uppercase with negative tracking
- Rotate banners and text blocks 5°–15° off-axis for diagonal energy
- Fill every available space — horror vacui is the Lucha Libre way
- Use sharp 0px corners on every element without exception

### ✗ Don't
- Use rounded corners of any kind — sharpness is non-negotiable
- Use pastel anything — this is a saturated, full-volume palette
- Use cream or white page backgrounds — black ground is the poster's void
- Use modern sans-serif body fonts like Inter, Geist, or Manrope
- Use soft pink, sage green, or dusty rose — these are anti-lucha
- Leave generous whitespace — fill the canvas like a packed Arena México poster
- Use SaaS gradient backgrounds — this is screenprint, not software

## Applications
Lucha Libre Poster is ideal for event promotion sites, music festival landing pages, streetwear brand launches, sports and entertainment platforms, and any digital experience that needs to scream louder than its competition. It thrives where maximalism is a virtue — concert tickets, fight cards, food truck menus, pop-up shop announcements, and cultural festival programs. Best deployed when the brief says "louder" and the designer says "how much louder?" and the answer is "yes."
