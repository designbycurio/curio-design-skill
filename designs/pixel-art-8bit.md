---
version: 1

meta:
  id: pixel-art-8bit
  name: Pixel Art / 8-bit Retro
  description: CRT-lit arcade aesthetic of 1978–1985 — hard-edged sprites, scanlines, and phosphor glow.
  isDark: true
  tags: [retro, playful, bold, tech, subcultural]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1978–1985; arcade golden age and 8-bit home console era"
  region: "Tokyo, Japan & San Jose, California"
  regionZh: "日本东京 / 美国圣何塞"
  keyFigures: [Toru Iwatani, Shigeru Miyamoto, Tomohiro Nishikado, Nolan Bushnell]
  movements: [Arcade golden age, Home console revolution, Chiptune & pixel art]

introduction: |
  Born in smoky arcades between 1978 and 1985, 8-bit pixel art turned hardware limits into a language.
  With 16-color palettes, 256×224 screens, and sprites drawn cell by cell on an 8×8 grid, designers like
  Iwatani, Miyamoto, and Nishikado rendered whole universes — Pac-Man's maze, Mario's mushroom kingdom,
  Space Invaders' descending fleet. A CRT's phosphor glow and scanlines fused with those sprites into an
  unmistakable visual: hard-edged, luminous, and unapologetically synthetic. It still says *insert coin*.
introductionZh: |
  八位像素美学诞生于 1978 到 1985 年的街机黄金时代。硬件的苛刻限制——16 色调色板、256×224 分辨率、
  8×8 像素为单位的精灵——反而催生了一套独特的视觉语言。岩谷彻的《吃豆人》、宫本茂的《马力欧》、
  西角友宏的《太空侵略者》都在黑色显像管里绽放出荧光般的色彩。扫描线、磷光晕染、阶梯状的斜边,
  连同街机厅里低鸣的 CRT 监视器,共同构成了这种风格的灵魂。它硬朗、明亮、毫不掩饰自己的数字属性——
  每当你看见它,耳畔就会响起那句经典的口号:"投币开始"。

colors:
  primary:
    "50":  "#E6FFEC"
    "100": "#B8FFC9"
    "200": "#80FFA3"
    "300": "#4DFF7A"
    "400": "#26FF5D"
    "500": "#00FF41"
    "600": "#00D636"
    "700": "#00A82A"
    "800": "#007A1F"
    "900": "#004D13"
    "950": "#00260A"
  secondary:
    "50":  "#FCEBE8"
    "100": "#F7C9C2"
    "200": "#EE9A8E"
    "300": "#E26A5A"
    "400": "#D04535"
    "500": "#B53120"
    "600": "#94241A"
    "700": "#731C14"
    "800": "#52140E"
    "900": "#360D09"
    "950": "#1C0705"
  accent:
    "50":  "#EDF1FF"
    "100": "#D5DDFF"
    "200": "#B4C2FF"
    "300": "#94A8FF"
    "400": "#7D96FF"
    "500": "#6888FF"
    "600": "#476BE6"
    "700": "#3353BF"
    "800": "#233D8F"
    "900": "#16285E"
    "950": "#0B1638"
  neutral:
    "50":  "#F5F5F7"
    "100": "#DCDCE0"
    "200": "#B8B8C0"
    "300": "#91919C"
    "400": "#6C6C78"
    "500": "#4A4A56"
    "600": "#353540"
    "700": "#26263A"
    "800": "#1A1A2E"
    "900": "#10101E"
    "950": "#0A0A0A"
  semantic:
    success: { bg: "#00FF41", text: "#0A0A0A", light: "#0A2610", border: "#00D636" }
    warning: { bg: "#FFE138", text: "#0A0A0A", light: "#2E2610", border: "#D6B800" }
    error:   { bg: "#B53120", text: "#FFFFFF", light: "#360D09", border: "#D04535" }
    info:    { bg: "#6888FF", text: "#0A0A0A", light: "#16285E", border: "#7D96FF" }
  background:
    page:    "#0A0A0A"
    surface: "#1A1A2E"
    subtle:  "#10101E"
  text:
    primary:   "#FFFFFF"
    secondary: "#FFE138"
    muted:     "#91919C"
    inverse:   "#0A0A0A"

typography:
  families:
    heading: "'Press Start 2P', 'Courier New', monospace"
    body:    "'VT323', 'Courier New', monospace"
    mono:    "'Silkscreen', 'Press Start 2P', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Silkscreen:wght@400;700&family=VT323&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 400, normal: 400, medium: 400, semibold: 700, bold: 700, extrabold: 700}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "0", tight: "0", normal: "0.05em", wide: "0.1em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "0", md: "0", lg: "0", xl: "0", full: "0"}
  color:  {default: "#FFFFFF", subtle: "#4A4A56", strong: "#00FF41", focus: "#FFE138"}
  width:  {thin: "2px", default: "2px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "2px 2px 0 #000000"
  sm: "4px 4px 0 #000000"
  md: "0 0 8px rgba(0,255,65,0.55)"
  lg: "0 0 12px rgba(104,136,255,0.6), 4px 4px 0 #000000"
  xl: "0 0 16px rgba(255,225,56,0.7), 6px 6px 0 #000000"
  "2xl": "0 0 24px rgba(0,255,65,0.8), 8px 8px 0 #000000"
  inner: "inset 2px 2px 0 rgba(0,0,0,0.4)"
  focus: "0 0 0 3px rgba(255,225,56,0.7)"

motion:
  level: "playful"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "steps(4, end)"
    in:      "steps(3, end)"
    out:     "steps(3, end)"
    spring:  "cubic-bezier(0.68, -0.55, 0.27, 1.55)"
  hoverPatterns: [glow, tint, scale]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "strong"
  rhythm:        "8px"

surfaceStyle: "solid"
blur:         "none"

iconography:
  treatment: "filled"
  set:       "custom"
  size:      {sm: "16px", md: "24px", lg: "32px"}
  stroke:    "2px"

components:
  button:
    primary:
      background: "#00FF41"
      color: "#0A0A0A"
      border: "2px solid #FFFFFF"
      shadow: "4px 4px 0 #000000"
      hoverBackground: "#26FF5D"
      hoverShadow: "0 0 12px #00FF41, 2px 2px 0 #000000"
      hoverColor: "#0A0A0A"
    secondary:
      background: "#B53120"
      color: "#FFFFFF"
      border: "2px solid #FFFFFF"
      shadow: "4px 4px 0 #000000"
      hoverBackground: "#D04535"
      hoverShadow: "0 0 12px #B53120, 2px 2px 0 #000000"
      hoverColor: "#FFFFFF"
    ghost:
      background: "transparent"
      color: "#FFE138"
      border: "2px solid #FFE138"
      shadow: "none"
      hoverBackground: "#1A1A2E"
      hoverShadow: "0 0 8px #FFE138"
      hoverColor: "#FFFFFF"
    danger:
      background: "#B53120"
      color: "#FFFFFF"
      border: "2px solid #FFE138"
      shadow: "4px 4px 0 #000000"
      hoverBackground: "#D04535"
      hoverShadow: "0 0 12px #B53120, 2px 2px 0 #000000"
      hoverColor: "#FFFFFF"
    sizes:
      sm: {height: "32px", padding: "0 16px", fontSize: "0.625rem"}
      md: {height: "44px", padding: "0 24px", fontSize: "0.75rem"}
      lg: {height: "56px", padding: "0 32px", fontSize: "0.875rem"}
    borderRadius: "0"
    fontWeight: 400
    letterSpacing: "0.1em"
    textTransform: "uppercase"
  input:
    background: "#0A0A0A"
    color: "#FFFFFF"
    border: "2px solid #FFFFFF"
    borderRadius: "0"
    padding: "12px 16px"
    focusBorder: "2px solid #FFE138"
    placeholderColor: "#91919C"
  card:
    base:
      background: "#1A1A2E"
      border: "2px solid #FFFFFF"
      borderRadius: "0"
      padding: "24px"
      shadow: "6px 6px 0 #000000"
    hover:
      shadow: "0 0 12px rgba(0,255,65,0.5), 6px 6px 0 #000000"
      transform: "translate(-2px, -2px)"
---

# Pixel Art / 8-bit Retro

> Insert coin. CRT black, phosphor green, and 16-color sprites rendered on an 8×8 grid.

## Origin

Between 1978 and 1985, a generation of arcade and console pioneers in Tokyo and California turned severe
hardware constraints into a golden age. Taito's Tomohiro Nishikado wrote *Space Invaders* on a custom
Intel 8080 board; Namco's Toru Iwatani shipped *Pac-Man* (1980); Nintendo's Shigeru Miyamoto followed
with *Donkey Kong* (1981) and *Super Mario Bros.* (1985). Atari's Nolan Bushnell had already seeded the
industry in San Jose. Their canvas was a 256×224 raster on a shadow-mask CRT, their palette roughly
16 colors per scene, their sprites 8×8 or 16×16 pixels. They drew worlds one cell at a time.

That discipline congealed into a coherent visual movement: hard-edged shapes, staircase diagonals, loud
saturated primaries on deep CRT black, blinking cursors, tile-repeat backgrounds, and the characteristic
warm phosphor bloom of a cathode ray tube. Fine artists like eBoy and Paul Robertson later reclaimed the
style as a medium in its own right, and chiptune gave it a soundtrack. Today pixel art is as much a
posture — *handmade, finite, unashamedly digital* — as it is a technique.

## Overview

Composition cues:
- **Layout**: grid-based, everything snapped to an 8px rhythm like sprite cells on a tilemap
- **Content width**: fixed container frames evoking arcade cabinet bezels; no full-bleed flow
- **Framing**: heavy 2px pixel borders, "game screen" cards with hard drop shadows
- **Grid intensity**: strong — visible pixel grid, HUD bars at top, tile repeats as decor

## Colors

The palette is a constrained arcade set: a single CRT-black ground `#0A0A0A` anchors everything, and
above it sit five saturated sprite colors — arcade green, Mario red, Pac-Man yellow, NES sky blue, and
invader magenta. Colors never blend; they sit side by side like pixels in a sprite, with phosphor glow
as the only permitted "gradient." Treat each hue as a token, not a range.

**Role usage**:
- Page background → `colors.background.page` (`#0A0A0A` CRT black)
- Card / panel surface → `colors.background.surface` (`#1A1A2E` dark blue-tinted panel)
- Primary action & "ON" states → `colors.primary.500` (`#00FF41` arcade green)
- Danger, warnings, hero accents → `colors.secondary.500` (`#B53120` Mario red)
- Links, informational highlights → `colors.accent.500` (`#6888FF` NES sky blue)
- Score counters & numeric displays → `colors.text.secondary` (`#FFE138` Pac-Man yellow)
- Body text & sprite highlights → `colors.text.primary` (`#FFFFFF`)
- Disabled / HUD chrome → `colors.neutral.400` (`#6C6C78`)

## Typography

Type must live on the pixel grid. Headlines use **Press Start 2P** — the definitive arcade score font —
set in ALL CAPS with wide letter-spacing so characters breathe. Readable paragraphs fall to **VT323**,
a pixel-terminal typeface that stays legible at 20–24px. **Silkscreen** handles HUD labels and tiny
metadata. Never smooth, never italicize, never size below the grid.

**Text styles**:
- `display-xl` — 'Press Start 2P', 64px, weight 400, line-height 1.2, letter-spacing 0.1em, uppercase
- `display-lg` — 'Press Start 2P', 48px, weight 400, line-height 1.2, letter-spacing 0.1em, uppercase
- `heading-1` — 'Press Start 2P', 32px, weight 400, line-height 1.3, letter-spacing 0.08em, uppercase
- `heading-2` — 'Press Start 2P', 20px, weight 400, line-height 1.4, letter-spacing 0.08em, uppercase
- `heading-3` — 'Press Start 2P', 14px, weight 400, line-height 1.5, letter-spacing 0.05em, uppercase
- `body-lg` — 'VT323', 24px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — 'VT323', 20px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — 'Silkscreen', 12px, weight 400, line-height 1.4, letter-spacing 0.1em, uppercase
- `mono-md` — 'Silkscreen', 14px, weight 400, line-height 1.4, letter-spacing 0.05em

## Spacing & Layout
- Base unit **4px**; prefer multiples of **8px** to respect sprite-cell rhythm
- Scale: `2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128` px
- Containers capped at 1280px with thick pixel bezels; never full-bleed imagery
- Section padding 64–128px; grid gap 16–24px so tiles breathe like separate sprites

## Elevation & Depth

There is no smooth material here — only hard offset "drop-pixel" shadows (e.g. `4px 4px 0 #000`) and
additive CRT glow (`0 0 12px currentColor`). Surfaces stay flat and opaque; depth reads as a second
sprite-colored rectangle sitting behind the first. Blur is forbidden; the only "depth" is the warm hum
of phosphor bleed on luminous elements.

- Surface style: **solid** (no translucency, no frosted layers)
- Blur: **none** — sub-pixel smoothing is off-brand
- Shadow ladder: `xs → 2px hard offset` / `md → 8px colored glow` / `xl → 16px glow + hard offset`
- Focus ring: `0 0 0 3px rgba(255,225,56,0.7)` — Pac-Man yellow halo

## Shapes
- Border radius: **always 0** — no rounded corners, ever
- Border width: **2px** default, **4px** for framing elements (arcade cabinet bezels)
- Diagonals: render as staircase steps, never as smooth slopes
- Icons: 8×8, 16×16, or 32×32 sprite sizes; no in-between

## Motion

Motion is stepped, not smooth. Animations snap between discrete frames (`steps(n, end)`), the way a
sprite sheet cycles. Blinking cursors, bouncing score pops, and CRT flicker are on-brand; cubic-bezier
inertia is not. Hovers add phosphor glow or a small 1-pixel shift — micro, not choreographic.

- Level: **playful**
- Durations: 120ms → 600ms with 250ms as the default
- Easings: `steps(4, end)` for most transforms; spring only for bounce-pop emphasis
- Hover patterns: **glow**, **tint**, **scale** (1.02–1.05, stepped)

## Techniques

### CRT scanline overlay
Horizontal scanline pattern laid over any dark surface to simulate a cathode ray tube monitor.
```css
.crt-screen {
  position: relative;
  background: #0A0A0A;
  color: #FFFFFF;
}
.crt-screen::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0px,
    rgba(0, 0, 0, 0) 2px,
    rgba(0, 0, 0, 0.35) 3px,
    rgba(0, 0, 0, 0.35) 4px
  );
  mix-blend-mode: multiply;
}
```

### Phosphor glow text
Bright sprite colors bleed like an overdriven CRT beam — applied to scores, headlines, and active states.
```css
.phosphor {
  color: #00FF41;
  text-shadow:
    0 0 4px #00FF41,
    0 0 8px rgba(0, 255, 65, 0.7),
    0 0 16px rgba(0, 255, 65, 0.4);
  -webkit-font-smoothing: none;
  font-smooth: never;
  image-rendering: pixelated;
}
```

### Sprite-border button
Hard 2px pixel border plus an offset black "drop-pixel" shadow — the signature arcade control surface.
```css
.pixel-button {
  display: inline-block;
  padding: 12px 24px;
  background: #00FF41;
  color: #0A0A0A;
  border: 2px solid #FFFFFF;
  border-radius: 0;
  box-shadow: 4px 4px 0 #000000;
  font-family: 'Press Start 2P', monospace;
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  image-rendering: pixelated;
  transition: transform 120ms steps(3, end), box-shadow 120ms steps(3, end);
}
.pixel-button:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000, 0 0 12px #00FF41;
}
.pixel-button:active {
  transform: translate(2px, 2px);
  box-shadow: 0px 0px 0 #000000;
}
```

## Iconography

Icons are sprite-native — hand-set on an 8×8 or 16×16 pixel grid, filled (not outlined), and rendered
with `image-rendering: pixelated` so they never soften. Replace stroke icon sets with a custom sprite
sheet; treat each glyph as a miniature character, not a vector. Limit each icon to three colors.

- Treatment: **filled** sprite shapes, no gradients
- Set: **custom** sprite sheet (fallback: chunky Phosphor at 2px stroke)
- Stroke / edge: 2px hard pixel — never feathered

## Do's & Don'ts

### ✓ Do
- Lock every element to an 8px grid and use `image-rendering: pixelated` on bitmaps
- Reserve Press Start 2P for headlines and scores; let VT323 carry paragraphs
- Pair `box-shadow: 4px 4px 0 #000` with `text-shadow` glow to fuse hardness and phosphor
- Keep each scene to ~16 colors pulled from the arcade palette
- Use `steps()` easing so motion snaps like a sprite animation

### ✗ Don't
- Use smooth gradients or anti-aliased edges
- Reach for modern sans-serif fonts like Inter, Helvetica, or Roboto
- Apply rounded corners anywhere — border-radius stays at 0
- Drop in high-resolution photography or realistic imagery
- Soften the palette into pastels or dusty tones
- Use CSS that implies sub-pixel rendering (transforms at fractional pixels, subpixel antialiasing)

## Applications

Best for retro gaming brands, indie game studios, chiptune musicians, hackathon landing pages, developer
side-projects with nostalgic spirit, arcade event sites, and any product that wants to declare itself
handmade and unashamedly digital. Works beautifully for 404 pages, boot-screens, changelogs framed as
"patch notes," and marketing pages built around a single strong call-to-action labelled `PRESS START`.
