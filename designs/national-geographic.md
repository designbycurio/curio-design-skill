---
version: 1

meta:
  id: national-geographic
  name: National Geographic
  description: The yellow border — editorial authority married to awe-inspiring documentary photography.
  isDark: false
  tags: [editorial, professional, narrative, bold, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1888 founded; yellow border introduced 1910; current visual refined 2000s"
  region: "Washington, D.C., USA"
  regionZh: "美国华盛顿特区"
  keyFigures: [Gilbert Hovey Grosvenor, Steve McCurry, David Guttenfelder]
  movements: [Documentary photography, Long-form scientific journalism, Exploration media]

introduction: |
  National Geographic is the yellow border — the most recognized frame in publishing history. Since 1888 that `#FFCE00` rectangle has signaled exploration, science, and the beauty of the planet, wrapping photography so strong it needs no filter.

  The visual language pairs a confident slab-serif voice with dense, readable editorial body text, full-bleed imagery, and generous paper-warm grounds. Chrome is minimal; the photograph is always the hero, and the yellow is always structural — a frame, an accent, a mark of authority, never a fill.
introductionZh: |
  国家地理的视觉符号是那一枚黄色矩形——出版史上辨识度最高的边框。自1888年创刊，特别是1910年引入这枚 `#FFCE00` 黄框以来，它便代表着探险、科学与地球之美，把每一张摄影作品庄重地框住。

  设计语言以权威的板状衬线字体、密实而易读的编辑正文、满版摄影与温润的米白纸感共同构建。界面元素被压到最低，让照片成为主角。黄色从不被当作大面积填色，而始终作为结构化的边框与点缀，标示内容的品质与可信度。那是一种典型的华盛顿特区式的编辑气质：沉稳、博学、带着泥土与风沙的温度。

colors:
  primary:    {"50": "#FFFBEA", "100": "#FFF5C2", "200": "#FFEB85", "300": "#FFE04D", "400": "#FFD71F", "500": "#FFCE00", "600": "#E0B500", "700": "#B89400", "800": "#8F7300", "900": "#665200", "950": "#3D3100"}
  secondary:  {"50": "#E8F0F5", "100": "#C7DAE5", "200": "#95B8CC", "300": "#6296B2", "400": "#3A7D9C", "500": "#1B4965", "600": "#163C54", "700": "#112F42", "800": "#0C2230", "900": "#08161F", "950": "#040B10"}
  accent:     {"50": "#F5F1E7", "100": "#E8DFC7", "200": "#D4C39A", "300": "#C0A76D", "400": "#B09860", "500": "#A08B5B", "600": "#86744C", "700": "#6B5C3C", "800": "#50452D", "900": "#352E1E", "950": "#1B170F"}
  neutral:    {"50": "#FAF7F1", "100": "#F5F0E8", "200": "#EAE4D6", "300": "#D4CCB8", "400": "#A39B88", "500": "#757062", "600": "#5A5A5A", "700": "#3F3F3F", "800": "#2A2A2A", "900": "#1A1A1A", "950": "#0D0D0D"}
  semantic:
    success: { bg: "#E8F0E9", text: "#1F4F2E", light: "#F3F7F3", border: "#2D6A4F" }
    warning: { bg: "#FFF5C2", text: "#665200", light: "#FFFBEA", border: "#FFCE00" }
    error:   { bg: "#F5DCD6", text: "#6B2217", light: "#FAEEEA", border: "#B4392A" }
    info:    { bg: "#E8F0F5", text: "#112F42", light: "#F3F7FA", border: "#1B4965" }
  background:
    page:    "#F5F0E8"
    surface: "#FFFFFF"
    subtle:  "#EAE4D6"
  text:
    primary:   "#1A1A1A"
    secondary: "#5A5A5A"
    muted:     "#8A8578"
    inverse:   "#F5F0E8"

typography:
  families:
    heading: "'Bitter', 'Zilla Slab', Georgia, serif"
    body:    "'Source Serif 4', 'Merriweather', Georgia, serif"
    mono:    "'Roboto Mono', 'IBM Plex Mono', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Bitter:wght@400;500;600;700;800&family=Source+Serif+4:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Roboto+Condensed:wght@400;500;700&family=Roboto+Mono:wght@400;500&display=swap"
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
  radius: {none: "0", sm: "0", md: "0", lg: "0", xl: "0", full: "9999px"}
  color:  {default: "#D4CCB8", subtle: "#EAE4D6", strong: "#1A1A1A", focus: "#FFCE00"}
  width:  {thin: "1px", default: "1px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(26,26,26,0.05)"
  sm: "0 1px 3px rgba(26,26,26,0.08), 0 1px 2px rgba(26,26,26,0.04)"
  md: "0 4px 8px rgba(26,26,26,0.08), 0 2px 4px rgba(26,26,26,0.04)"
  lg: "0 12px 24px rgba(26,26,26,0.10), 0 4px 8px rgba(26,26,26,0.05)"
  xl: "0 24px 48px rgba(26,26,26,0.14), 0 8px 16px rgba(26,26,26,0.06)"
  "2xl": "0 40px 80px rgba(26,26,26,0.18)"
  inner: "inset 0 1px 2px rgba(26,26,26,0.05)"
  focus: "0 0 0 3px rgba(255,206,0,0.45)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.25, 0.64, 1)"
  hoverPatterns: [lift, stroke, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: linear
  set:       lucide
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "#1A1A1A"
      color: "#F5F0E8"
      border: "4px solid #FFCE00"
      shadow: "0 1px 3px rgba(26,26,26,0.08)"
      hoverBackground: "#000000"
      hoverShadow: "0 4px 12px rgba(26,26,26,0.18)"
      hoverColor: "#FFCE00"
    secondary:
      background: "#F5F0E8"
      color: "#1A1A1A"
      border: "1px solid #1A1A1A"
      shadow: "none"
      hoverBackground: "#EAE4D6"
      hoverShadow: "0 1px 3px rgba(26,26,26,0.08)"
      hoverColor: "#1A1A1A"
    ghost:
      background: "transparent"
      color: "#1A1A1A"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(255,206,0,0.18)"
      hoverShadow: "none"
      hoverColor: "#1A1A1A"
    danger:
      background: "#B4392A"
      color: "#F5F0E8"
      border: "1px solid #B4392A"
      shadow: "0 1px 3px rgba(180,57,42,0.20)"
      hoverBackground: "#8F2C21"
      hoverShadow: "0 4px 12px rgba(180,57,42,0.28)"
      hoverColor: "#F5F0E8"
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "1rem" }
      lg: { height: "52px", padding: "0 28px", fontSize: "1.125rem" }
    borderRadius: "0"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFFFFF"
    color: "#1A1A1A"
    border: "1px solid #D4CCB8"
    borderRadius: "0"
    padding: "12px 16px"
    focusBorder: "2px solid #1A1A1A"
    placeholderColor: "#8A8578"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid #EAE4D6"
      borderRadius: "0"
      padding: "32px"
      shadow: "0 1px 3px rgba(26,26,26,0.06)"
    hover:
      shadow: "0 12px 24px rgba(26,26,26,0.10)"
      transform: "translateY(-2px)"
---

# National Geographic

> The yellow border — a century of exploration, framed.

## Origin

National Geographic was founded in January 1888 in Washington, D.C. by a group of 33 scientists, explorers, and financiers gathered at the Cosmos Club. Under editor Gilbert Hovey Grosvenor, the Society pioneered the use of lavish photography in a scientific journal — a radical move at the time — and in 1910 introduced the yellow rectangular cover border that would become the brand's most enduring mark. The frame was meant to signal that anything inside it had been vetted for truth and wonder alike.

Across more than a century the magazine became synonymous with expedition — Peary at the pole, Cousteau's seas, Jane Goodall's chimpanzees, Steve McCurry's "Afghan Girl" on the June 1985 cover, David Guttenfelder's reportage from closed nations. Today the mark lives on magazine covers, the Nat Geo TV bug, natgeo.com, and an Instagram account of 280M+ followers, but the recipe is unchanged: serif authority, warm editorial paper, and a yellow rectangle wrapped around the best photograph in the room.

## Overview

Composition cues:
- **Layout**: structured two- and three-column editorial grids with full-bleed photography breakouts
- **Content width**: container (max ~1280px) with generous outer margins; hero imagery goes full-bleed
- **Framing**: bordered — a 4px `#FFCE00` frame is the hero motif; other surfaces use quiet 1px hairlines
- **Grid intensity**: soft, with strict 8px rhythm underneath
- **Density**: dense body copy, generous leading, photography dominant

## Colors

The palette begins and ends with one hex: `#FFCE00` National Geographic Yellow, used structurally as a frame and accent — never as a page fill. Rich warm black `#1A1A1A` anchors type and UI; a warm off-white `#F5F0E8` provides the paper ground, evoking uncoated editorial stock. Secondary hues pull from the earth itself — a deep ocean blue `#1B4965` for depth and dataviz, and expedition khaki `#A08B5B` for maps, captions, and supporting chrome. Semantic colors stay muted and editorial, never neon.

**Role usage**:
- Page background → `colors.background.page` (`#F5F0E8`)
- Content surface → `colors.background.surface` (`#FFFFFF`)
- Primary accent / frame → `colors.primary.500` (`#FFCE00`)
- Body & headline text → `colors.text.primary` (`#1A1A1A`)
- Captions & metadata → `colors.text.secondary` (`#5A5A5A`)
- Dataviz / links / depth → `colors.secondary.500` (`#1B4965`)
- Map tints / subtle accents → `colors.accent.500` (`#A08B5B`)
- Dividers & rules → `colors.neutral.300` (`#D4CCB8`)

## Typography

Typography is serif-first, authoritative, and built for long reading. Slab-serif headlines carry the voice of a century-old science journal, while a lean editorial text serif handles dense body copy at magazine-grade leading. A condensed sans is reserved strictly for captions, bylines, folios, and metadata — the kind of small, confident text that lives in the margins of a photo spread. Nothing decorative, nothing sans-serif in the body, nothing rounded.

**Text styles**:
- `display-xl` — Bitter, 96px, weight 800, line-height 1.0, letter-spacing -0.03em
- `display-lg` — Bitter, 64px, weight 700, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Bitter, 48px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-2` — Bitter, 36px, weight 700, line-height 1.2, letter-spacing -0.01em
- `heading-3` — Bitter, 24px, weight 600, line-height 1.25, letter-spacing 0
- `body-lg` — Source Serif 4, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Source Serif 4, 17px, weight 400, line-height 1.7, letter-spacing 0
- `caption` — Roboto Condensed, 13px, weight 500, line-height 1.4, letter-spacing 0.05em, uppercase
- `mono-md` — Roboto Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- **Base unit** — 4px; layout rhythm snaps to 8px
- **Scale** — 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128px
- **Container** — max-width 1280px; editorial reading column capped near 680px
- **Section padding** — 64px mobile, 96–128px desktop between major sections
- **Grid gap** — 24px default (md), 48px between feature blocks
- **Column structure** — 12-col desktop, most editorial content spans 8 cols with wide outside margin

## Elevation & Depth

Materiality is paper, not glass. Surfaces are opaque, warm, and slightly tactile; shadows are short and neutral, used to lift a card a few millimeters off the page — never to float it. Depth mostly comes from *framing*: a yellow rectangle, a hairline rule, a caption indented from a photo's edge.

- **Surface style** — solid paper-warm white on editorial off-white
- **Blur** — none (no glassmorphism)
- **Shadow ladder** — `xs` for hairline lift, `sm` for resting cards, `md` for hover, `lg` for floating overlays, `xl` for modal elevation
- **Inset shadow** — used only on depressed inputs
- **Focus ring** — 3px yellow alpha halo (`rgba(255,206,0,0.45)`)

## Shapes

- **Border radius** — `0` everywhere except full-pill for avatars and status dots
- **Corners** — sharp; editorial rectangles are the building block
- **Frames** — 4px `#FFCE00` solid; 1px `#D4CCB8` for secondary containers
- **Dividers** — 1px `#1A1A1A` for rules in running text, 1px `#D4CCB8` for UI

## Motion

Motion is restrained and editorial. Transitions feel like turning a magazine page: confident, deliberate, never springy. Hover states adjust tone and lift, not scale. Long durations are reserved for hero imagery fading in over the paper ground.

- **Level** — restrained
- **Durations** — 120ms micro, 250ms default, 400ms content transitions, 600ms hero reveals
- **Easings** — `ease-out` for entrances, linear-cubic `(0.4, 0, 0.2, 1)` default; spring only on yellow accent reveals
- **Hover patterns** — subtle `translateY(-2px)` lift, stroke darkening on hairlines, yellow tint on ghost controls
- **Reduced motion** — honored: disable translate and fade-only swaps

## Techniques

### The Yellow Frame
The signature 4px `#FFCE00` border wrapped around editorial content blocks — NatGeo's most recognizable design element, used for featured imagery, pull quotes, and hero cards.
```css
.ngs-yellow-frame {
  position: relative;
  padding: 4px;
  background: #FFCE00;
  display: inline-block;
}
.ngs-yellow-frame > .ngs-yellow-frame__inner {
  display: block;
  background: #FFFFFF;
  padding: 24px;
}
/* photographic variant: the frame hugs a full-bleed image */
.ngs-yellow-frame--photo {
  padding: 4px;
  background: #FFCE00;
}
.ngs-yellow-frame--photo > img {
  display: block;
  width: 100%;
  height: auto;
}
```

### Paper Grain Ground
A subtle warm noise texture over `#F5F0E8` that gives pages the tactility of uncoated editorial stock without overpowering photography.
```css
.ngs-paper {
  background-color: #F5F0E8;
  background-image:
    radial-gradient(rgba(160, 139, 91, 0.06) 1px, transparent 1px),
    radial-gradient(rgba(26, 26, 26, 0.025) 1px, transparent 1px);
  background-size: 3px 3px, 7px 7px;
  background-position: 0 0, 1px 2px;
}
```

### Caption Block
The condensed-uppercase caption with a 2px yellow rule above — the visual signature of a NatGeo photo cutline, used beneath any image or data figure.
```css
.ngs-caption {
  font-family: 'Roboto Condensed', system-ui, sans-serif;
  font-size: 13px;
  font-weight: 500;
  line-height: 1.4;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #5A5A5A;
  border-top: 2px solid #FFCE00;
  padding-top: 8px;
  margin-top: 12px;
  max-width: 60ch;
}
.ngs-caption strong {
  color: #1A1A1A;
  font-weight: 700;
  margin-right: 8px;
}
```

## Iconography

Icons are linear, single-weight, and scientific in feel — more "field notebook margin" than decorative. Use a restrained outline set such as Lucide at 1.5px stroke. Icons live in neutral `#1A1A1A` by default and may shift to `#FFCE00` only when paired with a primary action.

- **Treatment** — linear outline, 1.5px stroke
- **Set** — Lucide (fallback: Feather)
- **Stroke** — 1.5px, round caps and joins

## Do's & Don'ts

### ✓ Do
- Use `#FFCE00` as a frame, rule, or accent — structural, never as a filled background
- Let full-bleed photography dominate; keep UI chrome to a whisper
- Set body copy in a text serif (Source Serif 4 / Merriweather) with generous 1.625–1.7 leading
- Anchor typography with Bitter slab-serif headlines in weight 700–800
- Use Roboto Condensed uppercase for captions, bylines, and metadata

### ✗ Don't
- Don't use sans-serif for body text — NatGeo is serif-first
- Don't introduce neon or artificial palettes
- Don't soften corners into rounded playful shapes
- Don't lean on minimalist tech aesthetics (no glass, no gradients-for-gradient's-sake)
- Don't default to dark backgrounds — NatGeo is warm and light
- Don't replace photography with decorative illustration

## Applications

Best-fit use cases: long-form journalism and science storytelling, documentary photo essays, museum and exhibition microsites, travel and expedition brands, educational publishing, and any editorial product where the photograph and the sentence have to carry equal weight. The system also suits nonprofit reports and conservation campaigns that need gravitas without darkness.
