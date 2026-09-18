---
version: 1

meta:
  id: minecraft-creeper-2011
  name: "Minecraft Creeper"
  description: "Mottled lime-and-grass-green voxel patchwork stamped in 16x16 texels against dark cave-stone gray"
  isDark: true
  tags: [tech, retro, geometric, playful, subcultural]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2010–now (public alpha 2009, full release 2011)"
  region: "Western Europe (Mojang, Stockholm, Sweden)"
  regionZh: "西欧（瑞典斯德哥尔摩，Mojang 工作室）"
  keyFigures: ["Markus \"Notch\" Persson", "Jens Bergensten"]
  movements: ["Voxel / sandbox gaming", "Indie pixel-texture aesthetics"]

introduction: |
  The Minecraft creeper is the game's most iconic mob — a silent, four-legged figure whose skin is a mottled patchwork of lime and grass greens stamped into a blocky 16x16 texel grid. Born in 2009 from a coding accident by Markus "Notch" Persson, the creeper became shorthand for the entire voxel-sandbox aesthetic: hard cubes, dithered shading, and zero anti-aliasing.

  This design system distills that look — dark cave-stone gray grounds, a multi-tone green ramp that reads patchy never flat, thick blocky borders, and period pixel typefaces. Everything is built from chunky texels with hard voxel edges.
introductionZh: |
  苦力怕（Creeper）是《我的世界》中最具标志性的怪物——一个沉默的四足身影，皮肤由青柠绿与草绿斑驳拼缀，压印在 16x16 的方块像素网格中。它诞生于 2009 年，源自创始人马库斯·"Notch"·佩尔松的一次编码意外，从此成为整个体素沙盒美学的代名词：硬质方块、抖动着色、毫无抗锯齿。

  本设计系统提炼了这一视觉：深邃的洞穴石灰底色、永不平涂的多色调绿色斑块、厚重的方块边框，以及时代感十足的像素字体。一切皆由粗粝的像素方块构成，棱角分明、绝无圆角。

colors:
  primary:
    "50": "#EAF8E7"
    "100": "#CFF0C8"
    "200": "#A6E398"
    "300": "#85D873"
    "400": "#72D05E"
    "500": "#5FCB50"
    "600": "#4FB141"
    "700": "#3E8E34"
    "800": "#2E6A27"
    "900": "#1F471A"
    "950": "#10250D"
  secondary:
    "50": "#EFF6E6"
    "100": "#D9EBC2"
    "200": "#C0DE98"
    "300": "#A4CE6C"
    "400": "#8DC354"
    "500": "#74BB43"
    "600": "#629F39"
    "700": "#4E7E2E"
    "800": "#3B5F23"
    "900": "#274017"
    "950": "#15220C"
  accent:
    "50": "#E6F4E7"
    "100": "#C2E4C4"
    "200": "#94D096"
    "300": "#6BBD6E"
    "400": "#54B057"
    "500": "#43A047"
    "600": "#39883D"
    "700": "#2D6B30"
    "800": "#214E24"
    "900": "#163517"
    "950": "#0B1D0C"
  neutral:
    "50": "#EDEFEC"
    "100": "#D2D7D0"
    "200": "#AAB2A8"
    "300": "#828D80"
    "400": "#626E60"
    "500": "#4A5448"
    "600": "#3C4439"
    "700": "#31382F"
    "800": "#2A302A"
    "900": "#262B26"
    "950": "#171A17"
  semantic:
    success: { bg: "#43A047", text: "#EAF8E7", light: "#CFF0C8", border: "#3E8E34" }
    warning: { bg: "#C0A400", text: "#1F1A00", light: "#F2E9B0", border: "#9C8500" }
    error: { bg: "#B0341F", text: "#F8E0DB", light: "#E8B4AA", border: "#8E2A18" }
    info: { bg: "#3A6BB0", text: "#DBE6F8", light: "#B4C9E8", border: "#2E558E" }
  background:
    page: "#262B26"
    surface: "#2E342E"
    subtle: "#31382F"
  text:
    primary: "#EDEFEC"
    secondary: "#AAB2A8"
    muted: "#828D80"
    inverse: "#171A17"

typography:
  families:
    heading: "'Press Start 2P', 'Silkscreen', monospace"
    body: "'VT323', 'Silkscreen', monospace"
    mono: "'VT323', 'Press Start 2P', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Silkscreen:wght@400;700&family=VT323&display=swap"
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
    md: "0"
    lg: "0"
    xl: "0"
    full: "0"
  color:
    default: "#5FCB50"
    subtle: "#3C4439"
    strong: "#74BB43"
    focus: "#85D873"
  width:
    thin: "2px"
    default: "3px"
    thick: "6px"
  style: "solid"

shadows:
  none: "none"
  xs: "2px 2px 0 rgba(16,37,13,0.6)"
  sm: "3px 3px 0 rgba(16,37,13,0.7)"
  md: "4px 4px 0 rgba(16,37,13,0.8)"
  lg: "6px 6px 0 rgba(16,37,13,0.85)"
  xl: "8px 8px 0 rgba(16,37,13,0.9)"
  "2xl": "12px 12px 0 rgba(16,37,13,0.95)"
  inner: "inset 3px 3px 0 rgba(16,37,13,0.5)"
  focus: "0 0 0 3px rgba(133,216,115,0.6)"

motion:
  level: "playful"
  durations:
    instant: "0ms"
    fast: "80ms"
    normal: "160ms"
    slow: "320ms"
    slower: "500ms"
  easings:
    default: "steps(4, end)"
    in: "steps(3, end)"
    out: "steps(3, end)"
    spring: "steps(6, end)"
  hoverPatterns: [scale, tint, stroke]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "strong"
  rhythm: "8px"

surfaceStyle: "flat"
blur: "none"

iconography:
  treatment: "filled"
  set: "custom"
  size:
    sm: "16px"
    md: "24px"
    lg: "32px"
  stroke: "0"

components:
  button:
    primary:
      background: "#5FCB50"
      color: "#10250D"
      border: "3px solid #2E6A27"
      shadow: "4px 4px 0 rgba(16,37,13,0.8)"
      hoverBackground: "#72D05E"
      hoverShadow: "6px 6px 0 rgba(16,37,13,0.85)"
      hoverColor: "#10250D"
    secondary:
      background: "#31382F"
      color: "#5FCB50"
      border: "3px solid #5FCB50"
      shadow: "4px 4px 0 rgba(16,37,13,0.8)"
      hoverBackground: "#3C4439"
      hoverShadow: "6px 6px 0 rgba(16,37,13,0.85)"
      hoverColor: "#85D873"
    ghost:
      background: "transparent"
      color: "#EDEFEC"
      border: "3px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(95,203,80,0.12)"
      hoverShadow: "none"
      hoverColor: "#5FCB50"
    danger:
      background: "#B0341F"
      color: "#F8E0DB"
      border: "3px solid #8E2A18"
      shadow: "4px 4px 0 rgba(16,37,13,0.8)"
      hoverBackground: "#8E2A18"
      hoverShadow: "6px 6px 0 rgba(16,37,13,0.85)"
      hoverColor: "#F8E0DB"
    sizes:
      sm: { height: "36px", padding: "0 16px", fontSize: "0.75rem" }
      md: { height: "48px", padding: "0 24px", fontSize: "0.875rem" }
      lg: { height: "60px", padding: "0 32px", fontSize: "1rem" }
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#2E342E"
    color: "#EDEFEC"
    border: "3px solid #4A5448"
    borderRadius: "0"
    padding: "12px 16px"
    focusBorder: "#5FCB50"
    placeholderColor: "#828D80"
  card:
    base:
      background: "#2E342E"
      border: "3px solid #3C4439"
      borderRadius: "0"
      padding: "24px"
      shadow: "4px 4px 0 rgba(16,37,13,0.8)"
    hover:
      shadow: "6px 6px 0 rgba(16,37,13,0.85)"
      transform: "translate(-2px,-2px)"
---

# Minecraft Creeper

> A mottled lime-and-grass-green voxel patchwork hissing in the dark cave gray — 16x16 texels, hard edges, zero smoothing.

## Origin

The creeper was born in 2009 from a coding accident: while building the pig model for Minecraft's public alpha, Markus "Notch" Persson swapped the length and height dimensions and produced a tall, four-legged, vertically-stretched figure. He kept it, cloaked it in a dithered green skin, and made it explode. By the game's full 1.0 release in 2011 — shepherded by lead developer Jens Bergensten at Mojang in Stockholm — the creeper had become the unofficial mascot of the entire voxel-sandbox genre.

Its visual language is inseparable from Minecraft's technical constraints: every surface is a 16x16 pixel texture (texel grid), every form is a hard-edged cube, and every shade is achieved through dithering rather than gradients. The skin itself is no single green but a mottled patchwork ramping from bright highlight lime through grass and forest tones down to near-black pits — the look of a mob spawning in the stone-shadow gray of an underground cave. This design system carries that flat, blocky, anti-anti-aliased philosophy into the interface.

## Overview

Composition cues:
- **Layout**: Strict grid on an 8px module that echoes the 16x16 texel structure — content snaps to blocky cells, never flows organically
- **Content width**: Container width with chunky bordered panels stacked like stone blocks
- **Framing**: Bordered — thick 3–6px hard-edged borders enclose every surface, like the seams between voxel cubes
- **Grid intensity**: Strong — a visible pixel-grid rhythm governs spacing; alignment to the cell is mandatory

## Colors

The palette is the creeper's skin set against the cave it spawns in. The dark stone-shadow gray (`#262B26`) is the dominant page ground — the underground where creepers appear. On top of it runs the mottled green ramp: bright highlight lime (`#5FCB50`) as the primary, grass green (`#74BB43`) and forest (`#43A047`) as the patchwork mid-tones, deep forest (`#0F800F`) and the darkest pit (`#004500`) anchoring the bottom. These greens must read *patchy and dithered*, never as a single flat fill or smooth gradient — checker, scatter, and stipple them across the 16x16 grid so the surface looks blocky and texel-stamped.

**Role usage**:
- Page background → `colors.background.page` (cave-stone gray `#262B26`, the dominant dark ground)
- Content surface → `colors.background.surface` (`#2E342E`, a slightly lifted stone block)
- Alternate blocks → `colors.background.subtle` (`#31382F`, dirt-shadow tone)
- Primary actions / highlight green → `colors.primary.500` (lime `#5FCB50`)
- Grass-green patchwork mid-tone → `colors.secondary.500` (`#74BB43`)
- Forest-green accent / deeper texels → `colors.accent.500` (`#43A047`)
- Body text on cave gray → `colors.text.primary` (`#EDEFEC`, near-white pixel ink)
- Darkest pit / inset shadows → `colors.primary.950` (`#10250D`) and forest pit `#004500`

## Typography

The type voice is pure pixel: blocky bitmap faces with no curves and no anti-aliasing, echoing Minecraft's period-accurate Minecraftia font. **Press Start 2P** carries display and headline duty — its rigid 8-bit arcade glyphs are unmistakably voxel-era. **Silkscreen** provides a slightly cleaner pixel option for tighter UI labels and weights. **VT323** — a monospace terminal pixel face that sets at smaller sizes comfortably — handles body copy and code. Everything is uppercase-friendly with generous tracking so each chunky glyph reads as its own little block. Never enable font smoothing; let the pixels stair-step.

**Text styles**:
- `display-xl` — Press Start 2P, 64px, weight 400, line-height 1.2, letter-spacing 0
- `display-lg` — Press Start 2P, 40px, weight 400, line-height 1.2, letter-spacing 0
- `heading-1` — Press Start 2P, 28px, weight 400, line-height 1.375, letter-spacing 0
- `body-lg` — VT323, 24px, weight 400, line-height 1.5, letter-spacing 0.02em
- `body-md` — VT323, 20px, weight 400, line-height 1.5, letter-spacing 0.02em
- `caption` — Silkscreen, 12px, weight 400, line-height 1.375, letter-spacing 0.05em
- `mono-md` — VT323, 20px, weight 400, line-height 1.625, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments to mirror the 16x16 texel block
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Section padding: 64px vertical (md), 96px (lg) — generous stone-block stacking room
- Grid gaps: 16px (md) to 24px (lg) — visible seams between blocks, like mortar lines

## Elevation & Depth

Depth is *blocky and hard-edged*, never atmospheric. There is no blur and no soft shadow — elevation is conveyed with offset hard drop-shadows (a solid dark pit color pushed down-right with zero spread radius), exactly like the pixel-art bevel of a Minecraft button. Surfaces are flat fills; the only "lighting" is flat dithered shading baked into the texture, never a real light source.

- Surface style: flat (solid texel fills, no glass, no layering haze)
- Blur: none (pixel art is crisply rendered; smoothing is forbidden)
- Shadow ladder: solid hard offsets in dark-pit `rgba(16,37,13,…)` — xs `2px 2px` through 2xl `12px 12px`, all with 0 blur and 0 spread
- Inner shadow: hard inset pit shadow for pressed/recessed states
- Focus ring: 3px lime glow at 60% — the one permitted soft edge, kept minimal

## Shapes

- `none`: 0 — every corner is a hard voxel edge
- `sm`: 0 — no rounding, ever
- `md`: 0 — inputs and containers stay square
- `lg`: 0 — buttons are blocky rectangles
- `xl`: 0 — cards are stone slabs
- `full`: 0 — even "pills" are squared; circles are approximated with stepped pixel corners, never `border-radius`

## Motion

Motion is playful but stepped — animation moves in discrete frames like a low-framerate sprite, never smooth interpolation. Hovers snap rather than ease; transitions use `steps()` timing so a button bevel jumps frame-to-frame the way a pixel sprite animates. The temperament is bouncy 8-bit energy held to a hard, quantized grid.

- Level: playful
- Durations: instant 0ms, fast 80ms, normal 160ms, slow 320ms, slower 500ms
- Default easing: `steps(4, end)` — quantized frame-stepping, no smooth curves
- Hover patterns: scale (snap up a texel), tint (shift green stop), stroke (border color jump)
- `reducedMotion: true` — all stepped animations respect `prefers-reduced-motion`

## Techniques

### Dithered creeper patchwork
The signature mottled green skin: a multi-stop ramp scattered as hard pixel blocks using layered repeating gradients on a 16-unit grid — patchy, never a smooth fill.
```css
.element {
  background-color: #43A047;
  background-image:
    repeating-linear-gradient(90deg,
      #5FCB50 0 16px, #74BB43 16px 32px,
      #43A047 32px 48px, #0F800F 48px 64px),
    repeating-linear-gradient(0deg,
      rgba(0,69,0,0.35) 0 16px, transparent 16px 32px);
  background-size: 64px 32px, 32px 32px;
  background-blend-mode: multiply;
  image-rendering: pixelated;
}
```

### Pixel bevel button
The hard 3D edge of a Minecraft UI button — a light top/left and dark bottom/right inset border with a solid offset drop-shadow, zero blur, zero radius.
```css
.element {
  background: #5FCB50;
  border: 3px solid #2E6A27;
  border-top-color: #85D873;
  border-left-color: #85D873;
  box-shadow: 4px 4px 0 rgba(16,37,13,0.8);
  border-radius: 0;
  image-rendering: pixelated;
  transition: transform 80ms steps(2, end);
}
.element:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 rgba(16,37,13,0.8);
}
```

### Stone-cave texel ground
The dark cave background as a faint 16x16 pixel-noise grid, giving the stone-shadow gray a blocky mottled texture instead of a flat panel.
```css
.element {
  background-color: #262B26;
  background-image:
    repeating-linear-gradient(0deg,
      rgba(255,255,255,0.02) 0 16px, transparent 16px 32px),
    repeating-linear-gradient(90deg,
      rgba(0,0,0,0.18) 0 16px, transparent 16px 32px);
  background-size: 32px 32px;
  image-rendering: pixelated;
}
```

## Iconography

Icons are custom pixel-art glyphs built on the same 16x16 texel grid as the textures — filled blocky shapes, never thin linear strokes. Draw them as hard-edged sprites (the creeper face, a TNT block, a pickaxe, a diamond) with flat color fills and `image-rendering: pixelated`. There is no stroke weight in the conventional sense; outlines, when present, are a single darker texel row.

- Treatment: filled (solid pixel sprites)
- Set: custom (16x16 pixel-art glyphs)
- Stroke: 0 (single-texel outlines only, no anti-aliased strokes)

## Do's & Don'ts

### ✓ Do
- Use cave-stone gray `#262B26` as the dominant page ground — it is the dark underground where creepers spawn
- Scatter the green ramp (`#5FCB50` / `#74BB43` / `#43A047` / `#0F800F` / `#004500`) as a dithered patchwork so the skin reads mottled, never flat
- Keep every corner square and every shadow a hard solid offset — voxel edges, no rounding
- Use Press Start 2P for headlines and VT323 for body to hold the pixel-bitmap voice
- Snap animations with `steps()` timing so motion looks like low-framerate sprite frames

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — the ground is dark cave gray
- No smooth gradients or anti-aliasing — everything is blocky 16x16 texels
- No single flat green — the creeper skin is a mottled multi-tone patchwork
- No rounded corners or soft shadows — keep hard voxel edges
- No realistic lighting — flat dithered shading only

## Applications

This system is built for gaming and creator-economy products that wear their pixel heritage proudly: indie game landing pages, Minecraft server and mod showcases, retro-gaming storefronts, Twitch/Discord community hubs, and 8-bit-styled event microsites. The blocky voxel palette and bitmap type also suit hackathon brands, NFT/voxel-art collections, and any playful tech product targeting a gamer audience that recognizes the creeper at a glance.
