---
version: 1

meta:
  id: nintendo-game-boy
  name: Nintendo Game Boy
  description: Four shades of green, an 8×8 pixel grid, and the handheld constraint that built a universe.
  isDark: false
  tags: [retro, tech, playful, subcultural]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1989 launch; peak cultural impact 1989–1998 (pre-Game Boy Color)"
  region: "Kyoto, Japan"
  regionZh: "日本京都"
  keyFigures: ["Gunpei Yokoi", "Satoru Iwata", "Shigeru Miyamoto", "Hirokazu Tanaka"]
  movements: ["Handheld gaming", "Dot-matrix pixel art", "Chiptune"]

introduction: |
  The Nintendo Game Boy (1989) was engineered around a deliberate limitation: a 160×144 dot-matrix LCD that could render only four shades of swampy green. Gunpei Yokoi's philosophy of "lateral thinking with withered technology" turned that constraint into a visual language, and Tetris, Pokémon, and Link's Awakening proved that whole worlds fit inside `#0F380F`–`#9BBC0F`.

  This system treats those four greens as non-negotiable canvas, with a maroon `#8B1A30` accent lifted from the DMG-01's A/B buttons. Everything snaps to an 8×8 pixel grid, corners are hard, gradients are dithered, and type is pixel-native. The mood is constraint, craft, and cartridge-era optimism.
introductionZh: |
  1989 年任天堂推出 Game Boy DMG-01，一块 160×144 的点阵液晶屏只能显示四种绿色——从最深的 `#0F380F` 到最浅的 `#9BBC0F`。横井军平"枯れた技術の水平思考"的理念，把硬件限制变成了整整一代便携游戏的美学基因。《俄罗斯方块》《宝可梦 红/绿》《塞尔达传说 梦见岛》都生长在这四格绿色之间。

  这套设计系统把"四绿配色 + 酒红按钮 `#8B1A30`"当作铁律：8×8 像素网格是基本度量，边角全部硬切，渐变以抖动点阵呈现，字体必须是像素字体（Press Start 2P、VT323、Silkscreen）。整体气质是复古、掌机、克制却顽皮——像一台被阳光晒得微微发暖的 DMG-01 被重新开机。

colors:
  primary:
    "50":  "#E8F0C8"
    "100": "#D4E29C"
    "200": "#BED078"
    "300": "#A8BE4A"
    "400": "#8BAC0F"
    "500": "#0F380F"
    "600": "#0D310D"
    "700": "#0B2A0B"
    "800": "#082108"
    "900": "#051805"
    "950": "#020F02"
  secondary:
    "50":  "#FCEAEE"
    "100": "#F7CAD2"
    "200": "#EE97A5"
    "300": "#E26478"
    "400": "#C73B52"
    "500": "#8B1A30"
    "600": "#7A1629"
    "700": "#651120"
    "800": "#4F0D19"
    "900": "#380910"
    "950": "#1E0508"
  accent:
    "50":  "#F2F7D4"
    "100": "#E6EFAA"
    "200": "#D4E57A"
    "300": "#BAD547"
    "400": "#9BBC0F"
    "500": "#8BAC0F"
    "600": "#6F8A0C"
    "700": "#546809"
    "800": "#3D4B07"
    "900": "#2A3405"
    "950": "#141A02"
  neutral:
    "50":  "#F4F6E6"
    "100": "#E4E8C8"
    "200": "#D4D9B0"
    "300": "#C4CFA1"
    "400": "#9FA780"
    "500": "#7A8160"
    "600": "#5D6348"
    "700": "#464A36"
    "800": "#2F3226"
    "900": "#1A1C14"
    "950": "#0A0B07"
  semantic:
    success: { bg: "#D4E29C", text: "#0F380F", light: "#E8F0C8", border: "#8BAC0F" }
    warning: { bg: "#F7CAD2", text: "#8B1A30", light: "#FCEAEE", border: "#C73B52" }
    error:   { bg: "#EE97A5", text: "#38090F", light: "#F7CAD2", border: "#8B1A30" }
    info:    { bg: "#C4CFA1", text: "#0F380F", light: "#E4E8C8", border: "#306230" }
  background:
    page:    "#9BBC0F"
    surface: "#8BAC0F"
    subtle:  "#C4CFA1"
  text:
    primary:   "#0F380F"
    secondary: "#306230"
    muted:     "#5D6348"
    inverse:   "#9BBC0F"

typography:
  families:
    heading: "'Press Start 2P', 'VT323', 'Courier New', monospace"
    body:    "'VT323', 'IBM Plex Mono', 'Courier New', monospace"
    mono:    "'Silkscreen', 'Press Start 2P', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&family=Silkscreen:wght@400;700&family=IBM+Plex+Mono:wght@400;500;700&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 400, normal: 400, medium: 400, semibold: 700, bold: 700, extrabold: 700}
  lineHeights: {tight: 1.1, snug: 1.25, normal: 1.4, relaxed: 1.6, loose: 1.8}
  letterSpacing: {tighter: "0", tight: "0", normal: "0.02em", wide: "0.1em"}

spacing:
  base: "4px"
  scale: ["2px","4px","8px","16px","24px","32px","48px","64px","96px","128px","160px","192px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "32px"}
  sectionPadding: {sm: "32px", md: "48px", lg: "64px", xl: "96px"}

borders:
  radius: {none: "0", sm: "0", md: "0", lg: "0", xl: "0", full: "0"}
  color:  {default: "#0F380F", subtle: "#306230", strong: "#0F380F", focus: "#8B1A30"}
  width:  {thin: "2px", default: "3px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "2px 2px 0 #0F380F"
  sm: "3px 3px 0 #0F380F"
  md: "4px 4px 0 #0F380F"
  lg: "6px 6px 0 #0F380F"
  xl: "8px 8px 0 #0F380F"
  "2xl": "12px 12px 0 #0F380F"
  inner: "inset 2px 2px 0 #306230"
  focus: "0 0 0 3px rgba(139, 26, 48, 0.6)"

motion:
  level: playful
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "steps(4, end)"
    in:      "steps(3, end)"
    out:     "steps(3, end)"
    spring:  "cubic-bezier(0.68, -0.55, 0.27, 1.55)"
  hoverPatterns: [lift, tint, underline]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        "8px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: filled
  set:       custom
  size:      {sm: "16px", md: "24px", lg: "32px"}
  stroke:    "2px"

components:
  button:
    primary:
      background:      "#0F380F"
      color:           "#9BBC0F"
      border:          "3px solid #0F380F"
      shadow:          "4px 4px 0 #306230"
      hoverBackground: "#306230"
      hoverShadow:     "2px 2px 0 #0F380F"
      hoverColor:      "#9BBC0F"
    secondary:
      background:      "#8BAC0F"
      color:           "#0F380F"
      border:          "3px solid #0F380F"
      shadow:          "4px 4px 0 #0F380F"
      hoverBackground: "#9BBC0F"
      hoverShadow:     "2px 2px 0 #0F380F"
      hoverColor:      "#0F380F"
    ghost:
      background:      "transparent"
      color:           "#0F380F"
      border:          "3px dashed #0F380F"
      shadow:          "none"
      hoverBackground: "#C4CFA1"
      hoverShadow:     "2px 2px 0 #0F380F"
      hoverColor:      "#0F380F"
    danger:
      background:      "#8B1A30"
      color:           "#9BBC0F"
      border:          "3px solid #0F380F"
      shadow:          "4px 4px 0 #0F380F"
      hoverBackground: "#C73B52"
      hoverShadow:     "2px 2px 0 #0F380F"
      hoverColor:      "#9BBC0F"
    sizes:
      sm: {height: "32px", padding: "0 12px", fontSize: "0.625rem"}
      md: {height: "44px", padding: "0 20px", fontSize: "0.75rem"}
      lg: {height: "56px", padding: "0 28px", fontSize: "0.875rem"}
    borderRadius:  "0"
    fontWeight:    700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background:       "#C4CFA1"
    color:            "#0F380F"
    border:           "3px solid #0F380F"
    borderRadius:     "0"
    padding:          "12px 16px"
    focusBorder:      "3px solid #8B1A30"
    placeholderColor: "#5D6348"
  card:
    base:
      background:   "#8BAC0F"
      border:       "4px solid #0F380F"
      borderRadius: "0"
      padding:      "24px"
      shadow:       "6px 6px 0 #0F380F"
    hover:
      shadow:    "8px 8px 0 #0F380F"
      transform: "translate(-2px, -2px)"
---

# Nintendo Game Boy

> Four shades of green, an 8×8 pixel grid, and the handheld constraint that built a universe.

## Origin

The Nintendo Game Boy launched on April 21, 1989 in Japan, designed by Gunpei Yokoi and his Research & Development 1 team in Kyoto. Yokoi's guiding philosophy — *kareta gijutsu no suihei shikō*, "lateral thinking with withered technology" — chose a cheap, battery-efficient monochrome LCD over the color screens of rivals like the Atari Lynx and Sega Game Gear. The DMG-01 could render exactly four shades of green at 160×144 pixels, and it outsold every competitor for nearly a decade.

Inside that four-green box, Alexey Pajitnov's *Tetris* became the pack-in killer app (1989), Satoshi Tajiri and Game Freak built the original *Pokémon Red/Green* (1996), and EAD's *The Legend of Zelda: Link's Awakening* (1993) proved a console-grade adventure could fit in a pocket. Composer Hirokazu Tanaka's chiptune scores and Shigeru Miyamoto's design sensibility turned the hardware's limits into an aesthetic dialect that still shapes indie pixel art today.

## Overview

Composition cues:
- **Layout**: strict 8×8 pixel tile grid; everything snaps to 8px multiples
- **Content width**: `container` (1024–1280px) framed by chunky bezel borders
- **Framing**: `bordered` — every card is a "game screen" in a dark green bezel
- **Grid intensity**: `strong` — visible dot-matrix grid overlay on page background
- **Rhythm**: 8px base step, mirroring the 8×8 tile

## Colors

The entire palette is imprisoned inside the four original DMG greens — `#0F380F`, `#306230`, `#8BAC0F`, `#9BBC0F` — with one and only one escape hatch: the maroon `#8B1A30` from the A/B buttons and Nintendo logo. Neutrals are the DMG-01 plastic body (`#C4CFA1`). There are no "smart" tints and no extra hues; constraint is the brand.

**Role usage**:
- Page background → `colors.background.page` (`#9BBC0F`, lightest green)
- Surface / card → `colors.background.surface` (`#8BAC0F`)
- Elevated / bezel → `colors.primary.500` (`#0F380F`)
- Primary text → `colors.text.primary` (`#0F380F`)
- Secondary text → `colors.text.secondary` (`#306230`)
- Accent / danger / CTA emphasis → `colors.secondary.500` (`#8B1A30`)
- Hardware plastic / subtle surface → `colors.background.subtle` (`#C4CFA1`)
- Inverse text on dark green → `colors.text.inverse` (`#9BBC0F`)

## Typography

Type is pixel-native, not pixel-inspired. Display lines run in *Press Start 2P* — an authentic 8×8 bitmap redraw — usually ALL CAPS, like a title card in *Link's Awakening*. Body copy shifts to *VT323*, a CRT-era terminal pixel font that stays readable at paragraph length. Small UI tags and labels use *Silkscreen*. When real monospace readability is required (code, long data), *IBM Plex Mono* steps in as a non-pixel fallback.

**Text styles**:
- `display-xl` — 'Press Start 2P', 4rem (64px), weight 400, line-height 1.1, letter-spacing 0.02em, UPPERCASE
- `display-lg` — 'Press Start 2P', 3rem (48px), weight 400, line-height 1.1, letter-spacing 0.02em, UPPERCASE
- `heading-1` — 'Press Start 2P', 1.875rem (30px), weight 400, line-height 1.25, letter-spacing 0.05em, UPPERCASE
- `heading-2` — 'Press Start 2P', 1.25rem (20px), weight 400, line-height 1.3, letter-spacing 0.05em, UPPERCASE
- `body-lg` — 'VT323', 1.5rem (24px), weight 400, line-height 1.4, letter-spacing 0.01em
- `body-md` — 'VT323', 1.25rem (20px), weight 400, line-height 1.5, letter-spacing 0.01em
- `caption` — 'Silkscreen', 0.75rem (12px), weight 400, line-height 1.3, letter-spacing 0.1em, UPPERCASE
- `mono-md` — 'IBM Plex Mono', 0.875rem (14px), weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: **4px**, with a strong preference for the **8px** "tile step" in real layouts
- Scale: 2, 4, 8, 16, 24, 32, 48, 64, 96, 128, 160, 192 px
- Container: up to 1280px, centered, with 4px pixel borders framing the content area
- Section padding: 32 / 48 / 64 / 96 px by breakpoint — sections feel like stacked game screens
- Everything is grid-locked; no half-pixels, no fractional rems

## Elevation & Depth

Depth is faked the way 1989 faked it: with hard offset drop shadows in `#0F380F` instead of blur. Nothing is translucent. Nothing uses `backdrop-filter`. A "raised" card is simply a panel with a 6px solid color shadow to the lower-right, like a sprite rendered one scanline above the tilemap.

- Surface style: `solid` — flat color fills, no gradients
- Blur: `none` — never
- Shadow ladder: 2px → 3px → 4px → 6px → 8px → 12px hard offsets in darkest green
- Inner shadow uses mid-green `#306230` to mimic LCD ghosting
- Focus ring: 3px maroon `#8B1A30` halo — the only time the accent appears around interactive elements

## Shapes

- Corner radii: **`0` everywhere** — hard pixel edges, no rounding, no anti-aliasing
- Borders: 2–4px solid, always `#0F380F` unless the element is `danger` (maroon border allowed)
- "Curves" are drawn by stepping pixels (stair-stepped diagonals), never by `border-radius`
- Dividers: 2px dashed `#306230`, reminiscent of menu selectors in *Pokémon*

## Motion

Motion is chunky, stepped, and slightly goofy — the visual equivalent of chiptune. Animations use `steps()` easing so transitions happen in 3–4 discrete frames instead of smoothly tweening, echoing the way a sprite walks on a Game Boy. Hovers "lift" by translating a card up-left by 2px while its offset shadow shortens, mimicking the feel of a button being pressed on a D-pad.

- Level: `playful`
- Durations: instant 0ms, fast 100ms, normal 200ms, slow 400ms, slower 600ms
- Easings: `steps(4, end)` default; spring only for bounce moments
- Hover patterns: `lift` (translate -2px/-2px), `tint` (swap to lighter green), `underline` (2px dashed)
- Respects `prefers-reduced-motion` — all stepped transitions fall back to instant

## Techniques

### Dot-matrix screen overlay
The 160×144 LCD grid rendered as a repeating 4px pixel lattice over any "screen" surface. Apply to heroes, cards, and the page background to sell the dot-matrix illusion.

```css
.gb-screen {
  background-color: #9BBC0F;
  background-image:
    linear-gradient(rgba(15, 56, 15, 0.12) 1px, transparent 1px),
    linear-gradient(90deg, rgba(15, 56, 15, 0.12) 1px, transparent 1px);
  background-size: 4px 4px;
  image-rendering: pixelated;
  border: 4px solid #0F380F;
  box-shadow:
    inset 0 0 0 2px #306230,
    6px 6px 0 #0F380F;
}
```

### Dithered green gradient
Smooth gradients are forbidden, so tonal shifts are faked with a checkerboard Bayer dither between two of the four greens — just like Link's Awakening renders a sunset.

```css
.gb-dither {
  background-color: #8BAC0F;
  background-image:
    linear-gradient(45deg, #0F380F 25%, transparent 25%),
    linear-gradient(-45deg, #0F380F 25%, transparent 25%),
    linear-gradient(45deg, transparent 75%, #0F380F 75%),
    linear-gradient(-45deg, transparent 75%, #0F380F 75%);
  background-size: 4px 4px;
  background-position: 0 0, 0 2px, 2px -2px, -2px 0;
  image-rendering: pixelated;
}
```

### Pixel bezel frame (DMG-01 screen)
Reproduces the chunky plastic-and-screen sandwich of a real Game Boy: a `#C4CFA1` plastic body outside, a `#2C2C2C` bezel ring inside, and the green screen at the center — the canonical card frame for this system.

```css
.gb-bezel {
  padding: 12px;
  background: #C4CFA1;
  border: 3px solid #0F380F;
  box-shadow: 4px 4px 0 #0F380F;
}
.gb-bezel::before {
  content: "";
  display: block;
  padding: 16px;
  background: #9BBC0F;
  border: 4px solid #2C2C2C;
  box-shadow: inset 0 0 0 2px #306230;
  image-rendering: pixelated;
}
```

## Iconography

Icons are custom 16×16 or 24×24 pixel sprites rendered on the same 8×8 grid — think heart containers, rupees, Poké Balls, and arrow selectors. Strokes are always 2px whole pixels, never fractional. Filled treatment dominates; when lines are needed, they are stepped diagonals rather than smooth curves.

- Treatment: `filled` pixel sprites with optional 2px pixel outline
- Set: `custom` — hand-drawn on an 8×8 grid; Lucide or Tabler are *not* suitable
- Stroke: 2px (one whole pixel at native scale)

## Do's & Don'ts

### ✓ Do
- Treat the four greens as a hard law — every on-screen surface must live inside `#0F380F`–`#9BBC0F`
- Reserve maroon `#8B1A30` for the A-button moment: primary CTA emphasis, focus rings, and danger states only
- Snap every dimension, padding, and offset to the 8×8 pixel grid
- Use dithering patterns whenever you need tonal variation — never a smooth gradient
- Set `image-rendering: pixelated` and keep all type in pixel fonts (Press Start 2P, VT323, Silkscreen)

### ✗ Don't
- Don't use smooth gradients — use dithering patterns instead
- Don't anti-alias curves — pixel art is hard-edged
- Don't use modern sans-serif body fonts on primary surfaces
- Don't introduce colors outside the 4-shade green palette on game-screen areas
- Don't apply glassmorphism, `backdrop-filter`, or any blur
- Don't use serif fonts anywhere in the system

## Applications

Best-fit use cases: indie-game landing pages, retro-tech product stories, pixel-art portfolios, chiptune album sites, Game Jam microsites, nostalgic marketing for 30-something gamers, and any UI that wants to shout *"handheld, handmade, hard-edged."* Less suitable for enterprise dashboards, luxury goods, medical software, or long-form reading experiences where paragraph legibility dominates.
