---
version: 1

meta:
  id: polaroid-instant
  name: Polaroid Instant
  description: Warm analog nostalgia with white-bordered photos, rainbow stripes, and handwritten captions
  isDark: false
  tags: [retro, friendly, narrative, playful, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1948 first instant camera; 1972 SX-70; rainbow stripe era 1970s–1980s; Impossible Project revival 2008; brand revival 2020s"
  region: "Cambridge, Massachusetts"
  regionZh: "美国马萨诸塞州剑桥"
  keyFigures: ["Edwin Land", "Andy Warhol", "Ansel Adams"]
  movements: ["Instant photography", "Lo-fi nostalgia", "Analog revival"]

introduction: |
  Polaroid is the white-bordered instant photo — shake it, wait, watch it
  develop, stick it on the fridge. Born in 1948 from Edwin Land's Cambridge
  lab, it made memory tangible.

  The SX-70 camera and the rainbow spectrum stripe became shorthand for
  authentic moments decades before digital filters tried to replicate them.
  Warm chocolate brown, photo white, and a casual tilt say: this happened,
  and I can hold it in my hand.
introductionZh: |
  宝丽来是那张带白边的即时照片——摇一摇、等一等、看着它显影，然后贴在冰箱上。
  从一九四八年埃德温·兰德在剑桥实验室的发明开始，它把"记忆"做成了可以握在
  手里的实体。七十年代的 SX-70 相机与标志性的彩虹条纹，在数字滤镜出现前
  就已经成了"真实瞬间"的代名词。

  这个系统以巧克力棕作为相机机身色，以泛黄的相纸白作为画面底色，辅以
  红橙黄绿蓝的彩虹色带、手写体标注、以及 2° 到 5° 的随意倾斜。它不追求
  极简和冷峻，而是像一本贴得满满当当的相册——温暖、热闹、有故事，
  让每一个界面都像从抽屉深处翻出来的那张照片。

colors:
  primary:
    "50":  "#F5EDE5"
    "100": "#E8D5C2"
    "200": "#D4B29A"
    "300": "#B58B6B"
    "400": "#8B5F3F"
    "500": "#5C3317"
    "600": "#4E2B13"
    "700": "#3E2310"
    "800": "#2E1A0C"
    "900": "#1F1108"
    "950": "#120A04"
  secondary:
    "50":  "#FDECEB"
    "100": "#FAC9C6"
    "200": "#F49D98"
    "300": "#ED6F68"
    "400": "#EA524B"
    "500": "#E53935"
    "600": "#CC2E2A"
    "700": "#A82522"
    "800": "#821B19"
    "900": "#5C1211"
    "950": "#3B0A09"
  accent:
    "50":  "#E6F2FD"
    "100": "#BEDCFA"
    "200": "#8EC3F6"
    "300": "#5CA8F0"
    "400": "#3A97EC"
    "500": "#1E88E5"
    "600": "#1A76CC"
    "700": "#155FA6"
    "800": "#104880"
    "900": "#0B325A"
    "950": "#061E37"
  neutral:
    "50":  "#FAF5EC"
    "100": "#F0E6D3"
    "200": "#E1D2B5"
    "300": "#CBB894"
    "400": "#A99573"
    "500": "#85745A"
    "600": "#6D4C41"
    "700": "#553B32"
    "800": "#3E2723"
    "900": "#2A1A17"
    "950": "#180D0B"
  semantic:
    success: { bg: "#43A047", text: "#FFFFFF", light: "#E8F5E9", border: "#66BB6A" }
    warning: { bg: "#FF8F00", text: "#2E1A0C", light: "#FFF3E0", border: "#FDD835" }
    error:   { bg: "#E53935", text: "#FFFFFF", light: "#FDECEB", border: "#EA524B" }
    info:    { bg: "#1E88E5", text: "#FFFFFF", light: "#E6F2FD", border: "#5CA8F0" }
  background:
    page:    "#F0E6D3"
    surface: "#F5F5F0"
    subtle:  "#FAF5EC"
  text:
    primary:   "#3E2723"
    secondary: "#6D4C41"
    muted:     "#8D6E63"
    inverse:   "#F5F5F0"

typography:
  families:
    heading: "'Nunito', -apple-system, BlinkMacSystemFont, sans-serif"
    body:    "'Lato', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    mono:    "'JetBrains Mono', 'Courier New', monospace"
    hand:    "'Caveat', 'Bradley Hand', cursive"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Lato:wght@300;400;700&family=Caveat:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "12px", md: "20px", lg: "28px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "6px", md: "10px", lg: "12px", xl: "16px", full: "9999px"}
  color:  {default: "#D4B29A", subtle: "#E8D5C2", strong: "#6D4C41", focus: "#1E88E5"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(62,39,35,0.06)"
  sm: "0 2px 6px rgba(62,39,35,0.08)"
  md: "0 3px 10px rgba(0,0,0,0.12)"
  lg: "0 8px 20px rgba(62,39,35,0.15)"
  xl: "0 14px 32px rgba(62,39,35,0.18)"
  "2xl": "0 24px 48px rgba(62,39,35,0.22)"
  inner: "inset 0 1px 2px rgba(62,39,35,0.08)"
  focus: "0 0 0 3px rgba(30,136,229,0.35)"

motion:
  level: "playful"
  durations: {instant: "0ms", fast: "140ms", normal: "280ms", slow: "450ms", slower: "700ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, scale]
  reducedMotion: true

composition:
  layout:        "masonry"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "soft"
  rhythm:        "4px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.75px"

components:
  button:
    primary:
      background: "#5C3317"
      color: "#F5F5F0"
      border: "none"
      shadow: "0 3px 10px rgba(0,0,0,0.12)"
      hoverBackground: "#4E2B13"
      hoverShadow: "0 6px 16px rgba(0,0,0,0.18)"
      hoverColor: "#F5F5F0"
    secondary:
      background: "#F5F5F0"
      color: "#3E2723"
      border: "1px solid #D4B29A"
      shadow: "0 2px 6px rgba(62,39,35,0.08)"
      hoverBackground: "#FAF5EC"
      hoverShadow: "0 4px 12px rgba(62,39,35,0.12)"
      hoverColor: "#3E2723"
    ghost:
      background: "transparent"
      color: "#5C3317"
      border: "none"
      shadow: "none"
      hoverBackground: "rgba(92,51,23,0.08)"
      hoverShadow: "none"
      hoverColor: "#4E2B13"
    danger:
      background: "#E53935"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 3px 10px rgba(229,57,53,0.25)"
      hoverBackground: "#CC2E2A"
      hoverShadow: "0 6px 16px rgba(229,57,53,0.32)"
      hoverColor: "#FFFFFF"
    sizes:
      sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}
      md: {height: "40px", padding: "0 20px", fontSize: "1rem"}
      lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}
    borderRadius: "10px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#F5F5F0"
    color: "#3E2723"
    border: "1px solid #D4B29A"
    borderRadius: "10px"
    padding: "10px 14px"
    focusBorder: "1px solid #1E88E5"
    placeholderColor: "#8D6E63"
  card:
    base:
      background: "#F5F5F0"
      border: "none"
      borderRadius: "10px"
      padding: "16px 16px 48px 16px"
      shadow: "0 3px 10px rgba(0,0,0,0.12)"
    hover:
      shadow: "0 8px 22px rgba(0,0,0,0.18)"
      transform: "translateY(-2px) rotate(-1deg)"
---

# Polaroid Instant

> Shake it, wait, stick it on the fridge — memory you can hold.

## Origin

Polaroid was founded in 1948 in Cambridge, Massachusetts by physicist Edwin
Land, who had been prototyping self-developing film since the mid-1940s. The
breakthrough product was the Model 95 Land Camera, but the aesthetic most
people carry in their heads comes from later: the 1972 SX-70 folding camera
(walnut-trimmed, integral film that ejected already developing) and the
1977 OneStep. Andy Warhol obsessed over his Big Shot, producing thousands
of portraits; Ansel Adams spent decades as Polaroid's consultant pushing
tonal range.

The rainbow spectrum stripe — red, orange, yellow, green, blue — was
introduced in the 1970s and defined the brand's visual identity through
the 1980s. After the company's 2001 bankruptcy, the Impossible Project
resurrected instant film manufacturing in 2008, and in 2017 the brand
relaunched as Polaroid Originals, re-embracing the rainbow stripe and
the iconic fat-bottom-border square. Today Polaroid is shorthand for
analog authenticity — a physical object, developed in your hand.

## Overview
Composition cues:
- **Layout**: masonry — photos at casual angles, overlapping like a pinboard
- **Content width**: `container` (1024–1280px), not full-bleed
- **Framing**: bordered — every card is a "photo" with white margin and fat bottom
- **Grid intensity**: soft — rhythmic but not rigid; 2°–5° rotations allowed
- **Rhythm**: 4px base unit

## Colors
Chocolate-brown SX-70 body as the anchor, photo white for surfaces, aged
paper tone as the page. The rainbow spectrum — red, orange, yellow, green,
blue — appears as accent stripes and category markers, never as dominant
fields. Warm vintage tint throughout: colors lean slightly amber, never
clinical.

**Role usage**:
- Page background → `colors.background.page` (`#F0E6D3`, aged paper)
- Photo / card surface → `colors.background.surface` (`#F5F5F0`, photo white)
- Camera-body brown (primary CTA, links) → `colors.primary.500` (`#5C3317`)
- Rainbow red (destructive, highlights) → `colors.secondary.500` (`#E53935`)
- Rainbow blue (info, secondary accent) → `colors.accent.500` (`#1E88E5`)
- Primary text → `colors.text.primary` (`#3E2723`, warm dark brown)
- Secondary text, handwritten captions → `colors.text.secondary` (`#6D4C41`)
- Rainbow stripe (dividers): `#E53935 → #FF8F00 → #FDD835 → #43A047 → #1E88E5`

## Typography
Warm and approachable, never formal. Nunito (rounded geometric) is the
billboard voice of the brand — friendly capitals that feel like printed
camera packaging. Lato carries running text with gentle humanist curves.
Caveat is reserved for the single moment where the photo is handed to you —
a caption scrawled across the fat bottom border.

**Text styles**:
- `display-xl` — Nunito, 96px, weight 800, line-height 1.0, letter-spacing -0.03em
- `display-lg` — Nunito, 64px, weight 800, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Nunito, 48px, weight 700, line-height 1.15, letter-spacing -0.02em
- `heading-2` — Nunito, 36px, weight 700, line-height 1.2, letter-spacing -0.01em
- `heading-3` — Nunito, 28px, weight 700, line-height 1.25, letter-spacing 0
- `body-lg` — Lato, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Lato, 16px, weight 400, line-height 1.6, letter-spacing 0
- `caption` — Caveat, 20px, weight 500, line-height 1.3, letter-spacing 0 (handwritten on photo borders)
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.55, letter-spacing 0

## Spacing & Layout
- Base unit: **4px**; scale: 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128
- Container: `lg = 1024px`, `xl = 1280px`; prefer `container`, not full-bleed
- Section padding: 32 / 64 / 96 / 128px, with generous breathing room around "photos"
- Grid gap: 12–28px between cards (enough overlap for a scrapbook feel)
- Cards have asymmetric padding: 16px top/sides, 48px bottom (the iconic fat Polaroid border)

## Elevation & Depth
Physical, papery, layered — but gentle. Every surface behaves like a
printed photo lying on a wooden table: soft drop shadow from a single
warm light, no glass, no neon glow. Depth comes from stacking and
slight rotation, not from blur.

- Surface style: `layered` (photos on top of paper)
- Blur: **none** (analog has no frosted glass)
- Shadow ladder: `xs` hairline contact → `md` (`0 3px 10px rgba(0,0,0,0.12)`) for photos at rest → `lg` / `xl` for lifted/dragged photos → `2xl` for modal "held up" moments
- Inner shadow used sparingly for inset input fields (suggests a pressed stamp)

## Shapes
- Corner radii: **10px** (buttons, inputs), **12px** (camera-body surfaces), **6px** (small chips), **9999px** (avatars, pill tags)
- No sharp 0px corners — Polaroid is soft and warm
- Photo cards: consistent 10px radius with 48px fat bottom border
- Rotation: cards may sit at 2°–5° off-axis for scrapbook feel

## Motion
Warm and a touch bouncy — things behave like a photo sliding out of the
camera's ejection slot, or being pinned to a corkboard. Never snappy-cold.
Spring easing on picks-up and drops; linear tint on image development.

- Level: **playful**
- Durations: instant 0, fast 140ms, normal 280ms, slow 450ms, slower 700ms
- Easings: `default` (standard), `spring` for lifts and drops (`cubic-bezier(0.34, 1.56, 0.64, 1)`)
- Hover patterns: `lift` (translateY -2px + rotate slightly), `tint` (darken brown), `scale` (1.02 on photo cards)
- Reduced motion: respected — disables rotation and spring, keeps fades

## Techniques

### Polaroid photo frame
The signature card. White photo border on three sides, a fat caption border
at the bottom, drop shadow to lift it off the paper background, and an
optional 2° casual tilt.

```css
.polaroid-card {
  background: #F5F5F0;
  padding: 16px 16px 48px 16px;  /* fat bottom = caption space */
  border-radius: 10px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.12);
  transform: rotate(-2deg);
  transition: transform 280ms cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 280ms ease;
}
.polaroid-card:nth-child(even) { transform: rotate(3deg); }
.polaroid-card:hover {
  transform: rotate(0deg) translateY(-4px);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.18);
}
.polaroid-card__image {
  width: 100%;
  aspect-ratio: 1 / 1;           /* square photo */
  object-fit: cover;
  border-radius: 2px;
  filter: saturate(0.9) sepia(0.06);  /* warm vintage tint */
}
.polaroid-card__caption {
  font-family: 'Caveat', cursive;
  font-size: 20px;
  color: #6D4C41;
  margin-top: 16px;
  text-align: center;
}
```

### Rainbow spectrum stripe
The 1970s brand divider — five bands in fixed order (red → orange → yellow
→ green → blue). Works as a section break, a top-of-page banner, or a
corner ribbon.

```css
.rainbow-stripe {
  height: 8px;
  background: linear-gradient(
    to right,
    #E53935 0%, #E53935 20%,
    #FF8F00 20%, #FF8F00 40%,
    #FDD835 40%, #FDD835 60%,
    #43A047 60%, #43A047 80%,
    #1E88E5 80%, #1E88E5 100%
  );
  border-radius: 2px;
}
.rainbow-stripe--banner {
  height: 6px;
  width: 100%;
  border-radius: 0;
}
```

### Aged-paper backdrop with warm grain
The page isn't pure white — it's `#F0E6D3`, an aged notebook tone, with a
very subtle warm noise that reads as photo-paper texture.

```css
.paper-backdrop {
  background-color: #F0E6D3;
  background-image:
    radial-gradient(ellipse at top, rgba(255,143,0,0.05), transparent 60%),
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 0.36  0 0 0 0 0.26  0 0 0 0 0.15  0 0 0 0.08 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
  background-size: auto, 120px 120px;
}
```

## Iconography
Linear icons with a slightly chunkier stroke (1.75px) to match Nunito's
rounded body. Lucide as the default set — its geometry reads as friendly
without being cute. Icons in warm brown (`primary.500`) or the rainbow
accent colors when they represent categories; never cold gray.

- Treatment: linear, rounded line caps and joins
- Set: lucide
- Stroke: 1.75px

## Do's & Don'ts
### ✓ Do
- Frame every image as a Polaroid photo — white border + fat 48px bottom + soft shadow
- Use warm chocolate brown (`#5C3317`) for primary CTAs and navigation
- Deploy the rainbow stripe sparingly — section dividers, corner ribbons, not as a background fill
- Tilt cards 2°–5° to create a scrapbook, pinboard, fridge-magnet feel
- Reach for Caveat only when a handwritten caption makes the moment feel personal

### ✗ Don't
- Reach for cold blue/gray tech palettes — Polaroid is warm
- Use sharp 0px corners — everything should feel soft and rounded
- Build dark moody screens — this system is fundamentally light and friendly
- Design in modern digital-clean / minimalist / sparse layouts — Polaroid is about abundant collected memories
- Introduce neon colors — Polaroid's palette is warm analog, never electric
- Set serif fonts for primary UI text — stay with Nunito + Lato

## Applications
Best for **memory-keeping products** (photo apps, family albums,
scrapbooking tools, travel journals), **lifestyle and nostalgia brands**
(vintage shops, analog photography services, indie zines), and
**narrative storytelling interfaces** (case studies, editorial portfolios,
year-in-review summaries). Use anywhere the content is personal,
hand-collected, and meant to feel like an object you'd pin to the fridge.
