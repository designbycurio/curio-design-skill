---
version: 1

meta:
  id: wabi-sabi-japanese
  name: Wabi-Sabi
  description: "A contemplative design system embracing imperfection, transience, and the beauty of weathered surfaces"
  isDark: false
  tags: [organic, editorial, friendly, minimal, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "14th–16th century philosophical roots; tea ceremony codification ~1580s; ongoing influence"
  region: "Japan, Kyoto"
  regionZh: "日本京都"
  keyFigures: ["Sen no Rikyū", "Murata Jukō", "Leonard Koren", "Naoto Fukasawa"]
  movements: ["Zen Buddhism", "tea ceremony (chanoyu)", "kintsugi"]

introduction: |
  Wabi-sabi is a Japanese aesthetic philosophy rooted in Zen Buddhism and the 16th-century tea ceremony. It finds beauty in imperfection, transience, and incompleteness — weathered wood over lacquer, asymmetry over balance, silence over noise.

  Translated into interface design, wabi-sabi becomes a system of muted earth tones, abundant negative space (ma, 間), hand-textured surfaces, and deliberate restraint. Every element breathes; nothing competes for attention.
introductionZh: |
  侘寂（わびさび）源自日本禅宗美学与十六世纪茶道精神，崇尚不完美之美、无常之韵、未尽之意。它以风化的木纹代替光鲜的漆面，以不对称取代工整，以留白映衬内容。

  将侘寂引入界面设计，便是一套以大地色调为基底、以"间"（ma）为节奏、以手工质感为肌理的设计体系。每个元素都有呼吸的空间，没有任何视觉噪音争夺注意力——恰如京都茶室中那份静谧的从容。

colors:
  primary:
    "50": "#f4f2ed"
    "100": "#e8e4da"
    "200": "#d1cdb8"
    "300": "#b9b696"
    "400": "#a1a585"
    "500": "#8a9474"
    "600": "#6f775d"
    "700": "#555b47"
    "800": "#3c4032"
    "900": "#24261e"
    "950": "#161712"
  secondary:
    "50": "#f0f2f4"
    "100": "#dfe3e8"
    "200": "#bfc7d1"
    "300": "#9faabb"
    "400": "#7f8ea4"
    "500": "#4a5a6a"
    "600": "#3d4b59"
    "700": "#313c47"
    "800": "#252d36"
    "900": "#191f25"
    "950": "#0f1317"
  accent:
    "50": "#f9f5ed"
    "100": "#f2e8d4"
    "200": "#e4d1aa"
    "300": "#d5b97f"
    "400": "#c7a25e"
    "500": "#b88c3c"
    "600": "#967130"
    "700": "#735625"
    "800": "#513c1a"
    "900": "#30230f"
    "950": "#1d1509"
  neutral:
    "50": "#f5f3ef"
    "100": "#eae6df"
    "200": "#d5cdbf"
    "300": "#bfb49f"
    "400": "#a99b80"
    "500": "#8a7d66"
    "600": "#6e6452"
    "700": "#534b3e"
    "800": "#3a3a35"
    "900": "#252420"
    "950": "#141311"
  semantic:
    success: { bg: "#8a9474", text: "#ffffff", light: "#e8e4da", border: "#6f775d" }
    warning: { bg: "#b88c3c", text: "#ffffff", light: "#f2e8d4", border: "#967130" }
    error: { bg: "#9e5b5b", text: "#ffffff", light: "#f0dede", border: "#7d4848" }
    info: { bg: "#4a5a6a", text: "#ffffff", light: "#dfe3e8", border: "#3d4b59" }
  background:
    page: "#ebe2d3"
    surface: "#f5f0e6"
    subtle: "#e3d9c8"
  text:
    primary: "#3a3a35"
    secondary: "#5c5a52"
    muted: "#8a8578"
    inverse: "#f5f0e6"

typography:
  families:
    heading: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    body: "'Lora', 'Noto Serif', Georgia, serif"
    mono: "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap"
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
  scale: ["2px", "4px", "6px", "8px", "12px", "16px", "24px", "32px", "48px", "64px", "96px", "128px"]
  container:
    sm: "640px"
    md: "768px"
    lg: "1024px"
    xl: "1280px"
    full: "100%"
  gridGap:
    sm: "12px"
    md: "24px"
    lg: "32px"
    xl: "64px"
  sectionPadding:
    sm: "48px"
    md: "96px"
    lg: "128px"
    xl: "160px"

borders:
  radius:
    none: "0"
    sm: "2px"
    md: "4px"
    lg: "6px"
    xl: "8px"
    full: "9999px"
  color:
    default: "#d5cdbf"
    subtle: "#e3d9c8"
    strong: "#8a8578"
    focus: "#b88c3c"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(58,58,53,0.04)"
  sm: "0 2px 4px rgba(58,58,53,0.06)"
  md: "0 4px 8px rgba(58,58,53,0.06)"
  lg: "0 8px 16px rgba(58,58,53,0.06)"
  xl: "0 12px 24px rgba(58,58,53,0.08)"
  "2xl": "0 20px 40px rgba(58,58,53,0.08)"
  inner: "inset 0 1px 3px rgba(58,58,53,0.06)"
  focus: "0 0 0 3px rgba(184,140,60,0.2)"

motion:
  level: "minimal"
  durations:
    instant: "0ms"
    fast: "150ms"
    normal: "300ms"
    slow: "500ms"
    slower: "800ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.22, 1, 0.36, 1)"
  hoverPatterns: [opacity, underline]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "narrow"
  framing: "minimal"
  gridIntensity: "none"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "linear"
  set: "lucide"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1px"

components:
  button:
    primary:
      background: "#3a3a35"
      color: "#f5f0e6"
      border: "1px solid #3a3a35"
      shadow: "none"
      hoverBackground: "#5c5a52"
      hoverShadow: "none"
      hoverColor: "#f5f0e6"
    secondary:
      background: "transparent"
      color: "#3a3a35"
      border: "1px solid #8a8578"
      shadow: "none"
      hoverBackground: "rgba(58,58,53,0.04)"
      hoverShadow: "none"
      hoverColor: "#3a3a35"
    ghost:
      background: "transparent"
      color: "#3a3a35"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(58,58,53,0.04)"
      hoverShadow: "none"
      hoverColor: "#3a3a35"
    danger:
      background: "#9e5b5b"
      color: "#ffffff"
      border: "1px solid #9e5b5b"
      shadow: "none"
      hoverBackground: "#7d4848"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    sizes:
      sm: { height: "32px", padding: "6px 16px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "8px 24px", fontSize: "1rem" }
      lg: { height: "48px", padding: "12px 32px", fontSize: "1.125rem" }
    borderRadius: "2px"
    fontWeight: 500
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "transparent"
    color: "#3a3a35"
    border: "1px solid transparent"
    borderRadius: "0"
    padding: "8px 0"
    focusBorder: "1px solid #b88c3c"
    placeholderColor: "#8a8578"
  card:
    base:
      background: "#f5f0e6"
      border: "1px solid #e3d9c8"
      borderRadius: "4px"
      padding: "32px"
      shadow: "0 2px 4px rgba(58,58,53,0.06)"
    hover:
      shadow: "0 4px 8px rgba(58,58,53,0.06)"
      transform: "none"
---

# Wabi-Sabi

> The beauty of imperfection, transience, and incompleteness — a design system rooted in Zen restraint and the weathered surfaces of old Kyoto.

## Origin

Wabi-sabi (侘寂) traces its philosophical roots to 14th-century Japanese Zen Buddhism, but its most tangible codification arrived in the 16th century through the tea master Sen no Rikyū. Rikyū stripped the tea ceremony of its ornate Chinese-influenced grandeur, replacing gilt tea rooms with humble, asymmetric spaces built from rough-hewn wood and bare earth. His tiny tea house at Myōki-an in Kyoto — barely two tatami mats — became the architectural manifesto of wabi-sabi: beauty found not in perfection but in the patina of use, the crack repaired with gold (kintsugi), the single flower placed off-center.

In the modern era, Leonard Koren's 1994 book "Wabi-Sabi for Artists, Designers, Poets & Philosophers" translated these principles for Western creative practice. Architects like Tadao Ando and product designers like Naoto Fukasawa (whose work shaped MUJI) carry this inheritance forward — proving that restraint, natural materials, and reverence for negative space can shape everything from concrete chapels to a wall-mounted CD player.

## Overview

Composition cues:
- **Layout**: Vertical stack — content flows downward with generous breathing room between sections, like a scroll painting.
- **Content width**: Narrow — text and imagery held to a contained measure, surrounded by expansive margins that embody *ma* (間).
- **Framing**: Minimal — surfaces are barely separated from their ground; borders are faint or absent, suggesting rather than enclosing.
- **Grid intensity**: None — deliberate asymmetry; elements are placed with intent but without rigid grid lines.

## Colors

The palette draws from the materials of a Kyoto tea room: the warm beige of aged washi paper, the muted green of moss on temple stones, the deep charcoal of wood smoke, and the quiet blue-grey of weathered indigo cloth. Nothing is bright. Nothing demands. The single accent — kintsugi gold — appears only at moments of intentional emphasis, like the gold lacquer tracing a crack in a ceramic bowl. Color in wabi-sabi is always the color of something that has been touched by time.

**Role usage**:
- Page background → `colors.background.page` — warm beige paper (#ebe2d3)
- Surface cards → `colors.background.surface` — slightly lighter parchment
- Primary text → `colors.text.primary` — soft charcoal (#3a3a35), never pure black
- Secondary text → `colors.text.secondary` — worn brown-grey
- Interactive focus / kintsugi accent → `colors.accent.500` — muted gold (#b88c3c)
- Nature elements / success → `colors.primary.500` — sage moss (#8a9474)
- Depth / secondary actions → `colors.secondary.500` — weathered indigo (#4a5a6a)

## Typography

The type voice is quiet, refined, and unhurried — a serif with the elegance of calligraphy but without its flourish. Cormorant Garamond at light weight provides headings that feel inscribed rather than stamped, with generous letter-spacing that lets each character breathe. Body text in Lora maintains warmth and readability at paragraph length. Line heights are always relaxed; density is the enemy of contemplation.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 300, line-height 1.0, letter-spacing 0.05em
- `display-lg` — Cormorant Garamond, 64px, weight 300, line-height 1.1, letter-spacing 0.05em
- `heading-1` — Cormorant Garamond, 48px, weight 400, line-height 1.2, letter-spacing 0.02em
- `body-lg` — Lora, 20px, weight 400, line-height 1.8, letter-spacing 0
- `body-md` — Lora, 16px, weight 400, line-height 1.8, letter-spacing 0
- `caption` — Lora, 13px, weight 400, line-height 1.5, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.6, letter-spacing 0

## Spacing & Layout

- Base unit: 8px — all spacing derives from multiples of 8
- Scale: 8, 16, 24, 32, 48, 64, 96, 128, 160px
- Container max-width: 768px (narrow) for text content; 1024px for mixed layouts
- Section padding: generous — 96px vertical minimum on desktop, expanding to 128–160px on larger screens
- Margins are deliberately wide; the empty space *is* the design

## Elevation & Depth

Surfaces in wabi-sabi are layered like sheets of washi paper resting on a wooden table — they have presence through subtle color shifts and faint borders rather than through drop shadows. When shadows do appear, they are extremely soft and warm-toned, suggesting a paper edge lifting slightly from the surface beneath. Nothing floats; everything rests.

- Surfaces are differentiated by slight warmth shifts: page (#ebe2d3) → surface (#f5f0e6) → subtle (#e3d9c8)
- Shadows use warm charcoal (rgba(58,58,53,...)) at very low opacity (0.04–0.08)
- No glossy effects, no glass, no blur — materiality is opaque and tactile
- Inner shadows suggest pressed or embossed texture, like a stamp on soft paper

## Shapes

- Corner radii are minimal: 2px default, 4px for cards — shapes should feel hand-cut, not machine-rounded
- No perfectly circular elements; prefer slightly squared or irregular forms
- Borders are thin (1px) and use muted warm tones, never harsh contrasts
- Buttons use barely-rounded corners (2px) to feel like carved wood or pressed paper

## Motion

Motion in wabi-sabi is nearly absent — like watching incense smoke drift. Transitions are slow and understated, used only to smooth state changes rather than to entertain. The system defaults to reduced motion; animation is a concession, not a feature.

- Level: minimal
- Default transition: 300ms with ease-out
- Hover effects: subtle opacity shifts (0.7 → 1.0) or quiet underline reveals
- No bouncing, no scaling, no sliding panels — stillness is preferred
- Easing: gentle out-curves that decelerate like a leaf settling
- `prefers-reduced-motion`: fully respected; all transitions collapse to instant

## Techniques

### Paper grain texture
A subtle noise overlay that gives surfaces the tactile quality of handmade washi paper.
```css
.element {
  position: relative;
  background-color: #ebe2d3;
}
.element::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  opacity: 0.05;
  pointer-events: none;
  mix-blend-mode: multiply;
}
```

### Kintsugi divider
A horizontal rule inspired by the golden-seam repair technique — a thin, irregular gold line that celebrates the break rather than hiding it.
```css
.kintsugi-divider {
  border: none;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    #b88c3c 15%,
    #d4a84a 30%,
    transparent 32%,
    transparent 45%,
    #b88c3c 48%,
    #c9a050 70%,
    #b88c3c 85%,
    transparent 100%
  );
  opacity: 0.6;
  margin: 64px auto;
  max-width: 60%;
}
```

### Ink-wash fade
Text or images that emerge from the background like a sumi-e ink wash painting — soft, bottom-heavy opacity gradients.
```css
.ink-wash-fade {
  mask-image: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(0, 0, 0, 0.3) 10%,
    rgba(0, 0, 0, 1) 30%,
    rgba(0, 0, 0, 1) 80%,
    rgba(0, 0, 0, 0.4) 100%
  );
  -webkit-mask-image: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(0, 0, 0, 0.3) 10%,
    rgba(0, 0, 0, 1) 30%,
    rgba(0, 0, 0, 1) 80%,
    rgba(0, 0, 0, 0.4) 100%
  );
}
```

## Iconography

Icons follow the same philosophy as the rest of the system: understated, thin, and unobtrusive. They should feel like they were drawn with a single brush stroke — present enough to guide, light enough to disappear into the composition when not needed.

- Treatment: linear (outline only), no fills
- Set: Lucide — its 1px-stroke default matches the system's delicacy
- Stroke width: 1px (thinner than Lucide's default 2px) for a calligraphic quality

## Do's & Don'ts

### ✓ Do
- Use generous negative space (*ma*) as an active design element, not empty filler
- Let the warm beige page color breathe — resist the urge to fill every section
- Use kintsugi gold (#b88c3c) sparingly and intentionally, like gold lacquer on a single crack
- Prefer asymmetric compositions — off-center headings, unequal column widths
- Allow text to be large and light (weight 300) with ample letter-spacing

### ✗ Don't
- Use bright or saturated colors — nothing in this system should feel new or loud
- Pursue geometric perfection — perfect symmetry, rigid grids, and mathematical precision are anti-wabi-sabi
- Apply glossy or polished surface effects — no glass, no sheen, no reflections
- Create dense, packed layouts — every element needs room to breathe
- Default to modern sans-serif typography — the system's voice is warm serif, not cold geometric

## Applications

Wabi-sabi is ideal for editorial platforms, personal portfolios, artisan brand sites, meditation and wellness apps, photography galleries, and any product that values contemplation over conversion pressure. It works beautifully for long-form reading, cultural content, and experiences where the user should feel invited to slow down rather than click faster.
