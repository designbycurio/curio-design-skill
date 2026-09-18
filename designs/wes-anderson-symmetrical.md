---
version: 1

meta:
  id: wes-anderson-symmetrical
  name: Wes Anderson Symmetrical
  description: "Frontal symmetric framing and hand-painted pastels inspired by Wes Anderson's dollhouse cinema"
  isDark: false
  tags: [decorative, narrative, retro, friendly, editorial]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1998 (Rushmore) – present; peak iconography 2014–2023"
  region: "USA (Texas-born, European-set films)"
  regionZh: "美国（德克萨斯出生，电影多设于欧洲）"
  keyFigures: [Wes Anderson, Adam Stockhausen, Milena Canonero, Annie Atkins]
  movements: [Auteur cinema, Dollhouse aesthetic, Modern symmetric framing]

introduction: |
  Wes Anderson's visual language is the most recognizable auteur aesthetic in contemporary cinema — frontal symmetric framing, hand-painted pastel palettes of salmon pink and mint green, Futura typography on every prop, and obsessive dollhouse art direction where every object is intentional. This system distills that mannered candy palette and paper-cutout materiality into a complete design token set.

  From *The Grand Budapest Hotel*'s Mendl's pastry box to *Asteroid City*'s desert diorama, the aesthetic says: every frame is a stage set, symmetry is the highest beauty, and warmth lives in cream paper and gouache color.
introductionZh: |
  韦斯·安德森的视觉语言是当代电影中最具辨识度的作者美学——正面对称构图、手绘粉彩色板（鲑鱼粉与薄荷绿）、每一件道具上的Futura字体，以及强迫症般的玩偶屋美术指导。本系统将这种精致的糖果色调与纸质剪贴质感提炼为完整的设计令牌体系。

  从《布达佩斯大饭店》的Mendl's糕点盒到《小行星城》的沙漠立体模型，这套美学宣告：每一帧都是舞台布景，对称是最高的美，温暖存在于奶油色纸张与水粉颜料之中。

colors:
  primary:
    "50": "#FCF0F1"
    "100": "#F9E1E2"
    "200": "#F4C8CA"
    "300": "#EEB5B8"
    "400": "#E8A4A8"
    "500": "#E8A4A8"
    "600": "#D4787D"
    "700": "#B85A5F"
    "800": "#944548"
    "900": "#6E3234"
    "950": "#4A2123"
  secondary:
    "50": "#F0F8F4"
    "100": "#E1F1EA"
    "200": "#C8E5D8"
    "300": "#B5D4C7"
    "400": "#B5D4C7"
    "500": "#B5D4C7"
    "600": "#8FBAA8"
    "700": "#6A9D8A"
    "800": "#4F7D6C"
    "900": "#3A5D50"
    "950": "#253D34"
  accent:
    "50": "#FDF8E8"
    "100": "#FBF0CC"
    "200": "#F5E19A"
    "300": "#F0D26E"
    "400": "#ECC54A"
    "500": "#E8B946"
    "600": "#C99A2E"
    "700": "#A47B24"
    "800": "#7F5E1C"
    "900": "#5C4415"
    "950": "#3A2B0D"
  neutral:
    "50": "#FAF6EF"
    "100": "#F5EDE0"
    "200": "#EBE0CC"
    "300": "#DDD0B5"
    "400": "#C4B494"
    "500": "#A89776"
    "600": "#8A7A5E"
    "700": "#6B5D47"
    "800": "#4E4333"
    "900": "#3D2817"
    "950": "#2A1B0F"
  semantic:
    success: { bg: "#B5D4C7", text: "#253D34", light: "#E1F1EA", border: "#6A9D8A" }
    warning: { bg: "#E8B946", text: "#3A2B0D", light: "#FDF8E8", border: "#C99A2E" }
    error:   { bg: "#A14841", text: "#FFFFFF", light: "#FCF0F1", border: "#B85A5F" }
    info:    { bg: "#A8C5DA", text: "#2A3D4A", light: "#EDF4F8", border: "#7BAAC4" }
  background:
    page: "#F2E8D1"
    surface: "#F9F0DC"
    subtle: "#EBE0CC"
  text:
    primary: "#3D2817"
    secondary: "#6B5D47"
    muted: "#8A7A5E"
    inverse: "#F2E8D1"

typography:
  families:
    heading: "'Cabin', sans-serif"
    body: "'Cabin', sans-serif"
    mono: "'JetBrains Mono', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cabin:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Cormorant+SC:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
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
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container: {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap: {sm: "8px", md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "4px", md: "8px", lg: "12px", xl: "16px", full: "9999px"}
  color: {default: "#3D2817", subtle: "#DDD0B5", strong: "#3D2817", focus: "#E8A4A8"}
  width: {thin: "1px", default: "1px", thick: "2px"}
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(61,40,23,0.04)"
  sm: "0 1px 4px rgba(125,91,49,0.06)"
  md: "0 2px 8px rgba(125,91,49,0.10)"
  lg: "0 4px 16px rgba(125,91,49,0.12)"
  xl: "0 8px 24px rgba(125,91,49,0.14)"
  "2xl": "0 12px 40px rgba(125,91,49,0.16)"
  inner: "inset 0 1px 2px rgba(61,40,23,0.04)"
  focus: "0 0 0 3px rgba(232,164,168,0.35)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, opacity]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "strong"
  rhythm: "8px"

surfaceStyle: "solid"
blur: "none"

iconography:
  treatment: "linear"
  set: "lucide"
  size: {sm: "16px", md: "20px", lg: "24px"}
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#E8A4A8"
      color: "#F2E8D1"
      border: "1px solid #A14841"
      shadow: "0 1px 4px rgba(125,91,49,0.06)"
      hoverBackground: "#D4787D"
      hoverShadow: "0 2px 8px rgba(125,91,49,0.10)"
      hoverColor: "#F2E8D1"
    secondary:
      background: "#B5D4C7"
      color: "#3D2817"
      border: "1px solid #6A9D8A"
      shadow: "none"
      hoverBackground: "#8FBAA8"
      hoverShadow: "0 1px 4px rgba(125,91,49,0.06)"
      hoverColor: "#3D2817"
    ghost:
      background: "transparent"
      color: "#3D2817"
      border: "1px solid #3D2817"
      shadow: "none"
      hoverBackground: "#EBE0CC"
      hoverShadow: "none"
      hoverColor: "#3D2817"
    danger:
      background: "#A14841"
      color: "#F2E8D1"
      border: "1px solid #6E3234"
      shadow: "none"
      hoverBackground: "#6E3234"
      hoverShadow: "none"
      hoverColor: "#F2E8D1"
    sizes:
      sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}
      md: {height: "40px", padding: "0 20px", fontSize: "1rem"}
      lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}
    borderRadius: "16px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#F9F0DC"
    color: "#3D2817"
    border: "1px solid #3D2817"
    borderRadius: "8px"
    padding: "10px 14px"
    focusBorder: "#E8A4A8"
    placeholderColor: "#8A7A5E"
  card:
    base:
      background: "#F9F0DC"
      border: "1px solid #3D2817"
      borderRadius: "12px"
      padding: "24px"
      shadow: "0 2px 8px rgba(125,91,49,0.10)"
    hover:
      shadow: "0 4px 16px rgba(125,91,49,0.12)"
      transform: "translateY(-2px)"
---

# Wes Anderson Symmetrical

> Frontal symmetric framing, hand-painted pastels, and dollhouse precision — every pixel is a stage set.

## Origin

Wes Anderson's visual language crystallized across two decades of filmmaking, from *Rushmore* (1998) through *The Grand Budapest Hotel* (2014) and *Asteroid City* (2023). Born in Houston, Texas, Anderson developed an unmistakable auteur aesthetic defined by rigorous frontal symmetry, hand-painted pastel palettes, and obsessive prop design. Production designer Adam Stockhausen and graphic prop artist Annie Atkins translated his vision into physical objects — from Mendl's pink pastry boxes to forged telegrams — that became cultural shorthand for mannered beauty.

The "Accidentally Wes Anderson" phenomenon (2017–present) proved the aesthetic transcends cinema: real-world architecture, interiors, and landscapes are now evaluated against his compositional grammar. The palette — salmon pink paired with mint green, mustard yellow accents on warm cream grounds — reads as simultaneously nostalgic and precisely modern, like a dollhouse designed by a perfectionist with a gouache set.

## Overview

Composition cues:
- **Layout**: Rigid symmetric grid with a strong vertical centerline — every element mirrors across the axis
- **Content width**: Container (max 1024–1280px) centered with generous cream margins
- **Framing**: Bordered panels with 1px walnut hairline frames — the hotel-room panel aesthetic
- **Grid intensity**: Strong — visible structure references multi-story building facades and stacked horizontal banding

## Colors

The palette is hand-mixed gouache on cream paper — saturated but powdery, never neon or synthetic. Salmon pink and mint green form the primary complementary pair (the Mendl's pastry box), mustard yellow provides sunlit warmth, baby blue evokes sky and uniform shirts, and walnut brown grounds everything as ink on vintage paper stock. Every color feels like it was mixed by a set painter, not generated by a screen.

**Role usage**:
- Page background → `colors.background.page` (#F2E8D1 warm cream paper)
- Card / panel surface → `colors.background.surface` (#F9F0DC lighter cream)
- Primary actions & hero accents → `colors.primary.500` (#E8A4A8 salmon pink)
- Secondary accents & success states → `colors.secondary.500` (#B5D4C7 mint green)
- Warm highlights & badges → `colors.accent.500` (#E8B946 mustard yellow)
- Body text & borders → `colors.text.primary` (#3D2817 walnut ink)
- Muted labels & captions → `colors.text.muted` (#8A7A5E)
- Danger / ribbon accent → semantic error (#A14841 brick red)

## Typography

Futura is Wes Anderson's signature typeface — it appears in every credit sequence, chapter card, and prop. This system uses Cabin as the geometric sans substitute (matching Futura's round, friendly geometry) for all heading and body text. Cormorant SC provides formal small-caps display for hotel-signage moments. Tracking is tight, all-caps is preferred for chapter titles and buttons, and the overall voice is precise, mannered, and warmly authoritative.

**Text styles**:
- `display-xl` — Cormorant SC, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Cormorant SC, 64px, weight 600, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Cabin, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `heading-2` — Cabin, 36px, weight 600, line-height 1.2, letter-spacing 0
- `body-lg` — Cabin, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — Cabin, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Cabin, 12px, weight 500, line-height 1.4, letter-spacing 0.05em, uppercase
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px rhythm throughout
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1024px (centered, generous cream margins)
- Section padding: 64–96px vertical for breathing room between acts
- Grid gap: 16–24px between symmetric panels
- All spacing reinforces the orthogonal, stacked-facade composition

## Elevation & Depth

Materiality is flat gouache on paper — depth is suggested through layered card-stock panels rather than dramatic shadows. Shadows are warm-tinted (walnut-brown alpha) and extremely subtle, evoking the soft ambient light of a dollhouse interior. No harsh drop shadows; elevation is communicated through border framing and slight vertical lift on hover.

- Surface style: solid cream panels with 1px walnut hairline borders
- Blur: none (no glass or frosted effects — this is paper, not screen)
- Shadow ladder: xs (barely visible) → md (cream-room ambient) → lg (gentle lift for modals)
- All shadows use warm rgba(125,91,49) tint, never cool gray

## Shapes

- Card corners: 12px (dollhouse-friendly softness)
- Button corners: 16px (candy-pastry pill shape)
- Input corners: 8px (subtle rounding)
- No sharp 0px corners anywhere — the aesthetic requires rounded warmth
- Full-round (9999px) reserved for badges and avatar circles

## Motion

Motion is restrained and mannered — like a stop-motion camera dolly or a chapter-card fade. Nothing bounces or springs aggressively. Transitions are deliberate and slightly theatrical, as if each state change is a scene cut.

- Level: restrained
- Durations: fast 120ms (micro-interactions), normal 250ms (state changes), slow 400ms (page transitions)
- Easing: ease-out for entrances, ease-in-out for transforms
- Hover patterns: gentle lift (translateY -2px), subtle tint shift, opacity fade
- Reduced motion: respected — all animation disabled when prefers-reduced-motion is set

## Techniques

### Paper-grain texture overlay
A subtle noise texture applied to the cream background to evoke vintage paper stock and hand-painted gouache surfaces.
```css
.element {
  background-color: #F2E8D1;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
}
```

### Symmetric chapter-card header
A centered title block with horizontal rules and small-caps — the Wes Anderson chapter title card.
```css
.chapter-card {
  text-align: center;
  font-family: 'Cormorant SC', serif;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 32px 0;
  border-top: 1px solid #3D2817;
  border-bottom: 1px solid #3D2817;
  margin: 64px auto;
  max-width: 480px;
}
```

### Pastel accent corner block
A small colored rectangle in the top-left corner of a card panel — referencing the hand-painted color swatches on Anderson's set-design boards.
```css
.card-with-accent::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 48px;
  height: 48px;
  background: #E8A4A8;
  border-radius: 0 0 12px 0;
  border-right: 1px solid #3D2817;
  border-bottom: 1px solid #3D2817;
}
```

## Iconography

Icons are linear and lightweight — thin strokes that echo the 1px walnut hairline borders used throughout. They should feel like hand-drawn illustrations in a prop notebook, not heavy UI chrome.

- Treatment: linear (outline only)
- Set: Lucide (clean geometric strokes matching Cabin's geometry)
- Stroke: 1.5px in walnut brown (#3D2817)

## Do's & Don'ts

### ✓ Do
- Center every composition on a vertical axis — symmetry is doctrinal
- Use warm cream (#F2E8D1) as the ground for all pages — never stark white
- Frame cards and panels with 1px walnut hairline borders
- Set chapter titles and button labels in uppercase with wide tracking
- Pair salmon pink with mint green as the primary complementary accent duo

### ✗ Don't
- Use pure white backgrounds — cream is correct, Wes never uses stark white
- Apply saturated synthetic neon colors — the palette is gouache, not LED
- Compose asymmetric or off-center layouts — symmetry is non-negotiable
- Use sharp 0px corners — the candy-pastry softness requires rounded edges
- Add harsh drop shadows — only warm, subtle cream-room ambient shadows
- Set body text in decorative serifs — geometric sans (Cabin) only
- Use full-bleed photography without paper-cutout treatment

## Applications

This system is ideal for editorial portfolios, boutique hospitality branding, stationery and invitation design, cultural event programs, and any product that values mannered warmth over corporate efficiency. It excels at storytelling interfaces — chapter-based layouts, curated collections, and narrative landing pages where every element feels intentionally placed.
