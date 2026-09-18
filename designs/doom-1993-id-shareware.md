---
version: 1

meta:
  id: doom-1993-id-shareware
  name: "Doom 1993 Toxic Green"
  description: "Techno-gothic shareware FPS look: glowing radioactive nukage green over rust-brown and near-black pixelated techbase metal"
  isDark: true
  tags: [retro, subcultural, bold, tech, decorative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1993 (Doom release); North American PC-shareware FPS era (1990–2010 window)"
  region: "North America (id Software, Mesquite, Texas)"
  regionZh: "北美（id Software，美国得克萨斯州梅斯基特）"
  keyFigures: ["John Carmack", "John Romero", "Adrian Carmack", "Tom Hall", "Sandy Petersen"]
  movements: ["early-'90s PC FPS / shareware distribution", "techno-gothic game art", "demoscene-adjacent pixel craft"]

introduction: |
  Doom (1993) is id Software's techno-gothic first-person shooter, the title that fused industrial techbase metal with hellfire and radioactive waste. Its look is built from glowing nukage green pools, rust-brown plating, and near-black pixelated floors lit by saturated nuclear light.

  This design system distills that shareware-era artifact: embossed grungy titling, beveled HUD panels, scanline grain, and toxic-green readouts glowing off oily metal. Every surface reads as STARTAN plating under radioactive illumination.
introductionZh: |
  《毁灭战士》（Doom，1993）是 id Software 的技术哥特式第一人称射击游戏，把工业科技基地金属与地狱火、放射性废料熔为一体。它的视觉由发光的"核浆"绿色水池、锈褐色装甲板，以及被饱和核光照亮的近黑色像素化地面构成。

  本设计系统提炼这种共享软件时代的质感：浮雕做旧的标题字、斜切立体的 HUD 面板、扫描线颗粒，以及在油腻金属上发光的剧毒绿色读数。每一处表面都像放射光下的 STARTAN 装甲板，硬朗、做旧、技术哥特。

colors:
  primary:
    "50": "#EAFFE4"
    "100": "#CCFFC0"
    "200": "#9DFF8A"
    "300": "#6DFF54"
    "400": "#52FF34"
    "500": "#39FF14"
    "600": "#26D406"
    "700": "#1CA305"
    "800": "#157A05"
    "900": "#0D5204"
    "950": "#072E02"
  secondary:
    "50": "#E6FFE6"
    "100": "#C2FFC2"
    "200": "#85FF85"
    "300": "#47FF47"
    "400": "#1FFF1F"
    "500": "#00FC00"
    "600": "#00D000"
    "700": "#00A000"
    "800": "#007A00"
    "900": "#005200"
    "950": "#002E00"
  accent:
    "50": "#FBEBE6"
    "100": "#F6CFC6"
    "200": "#EC9C8C"
    "300": "#E16A52"
    "400": "#D14428"
    "500": "#A8200D"
    "600": "#8C1B0B"
    "700": "#6F1609"
    "800": "#531007"
    "900": "#380B05"
    "950": "#220603"
  neutral:
    "50": "#F2EFEC"
    "100": "#D9D3CD"
    "200": "#B4ABA2"
    "300": "#8E8378"
    "400": "#6B6056"
    "500": "#7A4B2A"
    "600": "#5C3920"
    "700": "#42291A"
    "800": "#2B2622"
    "900": "#1D1815"
    "950": "#161210"
  semantic:
    success: { bg: "#39FF14", text: "#072E02", light: "#CCFFC0", border: "#26D406" }
    warning: { bg: "#7A4B2A", text: "#F2EFEC", light: "#F6CFC6", border: "#5C3920" }
    error: { bg: "#A8200D", text: "#FBEBE6", light: "#F6CFC6", border: "#8C1B0B" }
    info: { bg: "#00FC00", text: "#002E00", light: "#C2FFC2", border: "#00D000" }
  background:
    page: "#161210"
    surface: "#2B2622"
    subtle: "#1D1815"
  text:
    primary: "#E8FFE0"
    secondary: "#9DFF8A"
    muted: "#8E8378"
    inverse: "#161210"

typography:
  families:
    heading: "'Pirata One', 'Metamorphous', 'Cinzel', serif"
    body: "'Metamorphous', 'Cinzel', Georgia, serif"
    mono: "'VT323', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=Metamorphous&family=Pirata+One&family=VT323&display=swap"
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
    sm: "2px"
    md: "3px"
    lg: "4px"
    xl: "6px"
    full: "9999px"
  color:
    default: "#7A4B2A"
    subtle: "rgba(122, 75, 42, 0.4)"
    strong: "#39FF14"
    focus: "#50FF00"
  width:
    thin: "1px"
    default: "2px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.6)"
  sm: "0 2px 4px rgba(0,0,0,0.7), inset 0 1px 0 rgba(122,75,42,0.4)"
  md: "0 3px 8px rgba(0,0,0,0.75), inset 0 1px 0 rgba(122,75,42,0.5), inset 0 -2px 4px rgba(0,0,0,0.6)"
  lg: "0 6px 16px rgba(0,0,0,0.8), 0 0 12px rgba(57,255,20,0.25)"
  xl: "0 10px 28px rgba(0,0,0,0.85), 0 0 20px rgba(57,255,20,0.35)"
  "2xl": "0 16px 44px rgba(0,0,0,0.9), 0 0 32px rgba(57,255,20,0.45)"
  inner: "inset 0 2px 6px rgba(0,0,0,0.7)"
  focus: "0 0 0 3px rgba(57,255,20,0.45)"

motion:
  level: "lively"
  durations:
    instant: "0ms"
    fast: "120ms"
    normal: "250ms"
    slow: "400ms"
    slower: "600ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.55, 0, 1, 0.45)"
    out: "cubic-bezier(0, 0.55, 0.45, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [glow, tint, stroke]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "strong"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "filled"
  set: "custom"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "2px"

components:
  button:
    primary:
      background: "#1D1815"
      color: "#39FF14"
      border: "2px solid #7A4B2A"
      shadow: "inset 0 1px 0 rgba(122,75,42,0.5), inset 0 -2px 4px rgba(0,0,0,0.6), 0 0 10px rgba(57,255,20,0.25)"
      hoverBackground: "#2B2622"
      hoverShadow: "inset 0 1px 0 rgba(122,75,42,0.6), 0 0 18px rgba(57,255,20,0.5)"
      hoverColor: "#50FF00"
    secondary:
      background: "transparent"
      color: "#7A4B2A"
      border: "2px solid #7A4B2A"
      shadow: "inset 0 1px 0 rgba(122,75,42,0.4)"
      hoverBackground: "rgba(122,75,42,0.18)"
      hoverShadow: "inset 0 1px 0 rgba(122,75,42,0.6)"
      hoverColor: "#B4ABA2"
    ghost:
      background: "transparent"
      color: "#9DFF8A"
      border: "2px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(57,255,20,0.1)"
      hoverShadow: "none"
      hoverColor: "#39FF14"
    danger:
      background: "#A8200D"
      color: "#FBEBE6"
      border: "2px solid #6F1609"
      shadow: "inset 0 1px 0 rgba(225,106,82,0.4), 0 0 10px rgba(168,32,13,0.4)"
      hoverBackground: "#8C1B0B"
      hoverShadow: "0 0 18px rgba(168,32,13,0.6)"
      hoverColor: "#FBEBE6"
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "1rem" }
      md: { height: "42px", padding: "0 22px", fontSize: "1.125rem" }
      lg: { height: "52px", padding: "0 30px", fontSize: "1.25rem" }
    borderRadius: "3px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#1D1815"
    color: "#39FF14"
    border: "2px solid #7A4B2A"
    borderRadius: "3px"
    padding: "10px 14px"
    focusBorder: "#39FF14"
    placeholderColor: "#6B6056"
  card:
    base:
      background: "#2B2622"
      border: "2px solid #7A4B2A"
      borderRadius: "4px"
      padding: "24px"
      shadow: "inset 0 1px 0 rgba(122,75,42,0.5), inset 0 -2px 6px rgba(0,0,0,0.6), 0 4px 14px rgba(0,0,0,0.7)"
    hover:
      shadow: "inset 0 1px 0 rgba(122,75,42,0.6), 0 0 18px rgba(57,255,20,0.35), 0 6px 18px rgba(0,0,0,0.8)"
      transform: "translateY(-2px)"
---

# Doom 1993 Toxic Green

> Techno-gothic shareware FPS: glowing nukage green bleeding across rust-brown plating and near-black pixelated techbase metal.

## Origin

Doom shipped on December 10, 1993, distributed as shareware by id Software out of Mesquite, Texas — the first episode free, the rest sold by mail. John Carmack's binary-space-partition renderer let the team paint claustrophobic 3D corridors at speed, while John Romero designed the level pacing and Adrian Carmack authored the art and the 256-color PLAYPAL palette that defined the look. Tom Hall and Sandy Petersen shaped the bestiary and the descent from clean UAC techbase into hellscape.

The visual signature is techno-gothic industrial: rust-brown STARTAN and GSTONE wall plates, oily near-black metal floors, and pools of glowing radioactive "nukage" — toxic-waste green so saturated it reads as a light source. The HUD layered chunky beveled panels and pixelated green digits over this grime. Spread peer-to-peer through the shareware era, Doom's saturated-green-on-rust-metal aesthetic became a foundational reference for the whole '90s PC FPS movement.

## Overview

Composition cues:
- **Layout**: Beveled HUD-panel grid — chunky plated blocks butted together like techbase wall segments, each framed by rust-brown bezels
- **Content width**: Container width, dense and modular, like stacked status readouts and inventory panels
- **Framing**: Bordered — hard 2px rust-brown bevels with embossed inner highlights and recessed shadows on every surface
- **Grid intensity**: Strong — pixel-tight panel plating and hex/scanline texture govern the rhythm; nothing floats freely

## Colors

The palette comes straight from Doom's PLAYPAL: glowing nukage green (`#39FF14`) as the radioactive hero, pushed by pure nuclear green (`#00FC00`) and bright nukage (`#50FF00`) for HUD readouts and toxic-pool surfaces. Grounds are rust-brown techbase tan (`#7A4B2A`, the STARTAN/GSTONE family), dark metal (`#2B2622`), and near-black plating (`#161210`). Hellfire red (`#A8200D`) marks damage and danger. The greens must stay loud and radioactive — never desaturated, never minty — glowing against grime like waste pools under reactor light.

**Role usage**:
- Page background → `colors.background.page` (near-black techbase metal `#161210`, never cream/white)
- Content surface → `colors.background.surface` (dark metal plating `#2B2622`)
- Recessed / alternate blocks → `colors.background.subtle` (deeper metal `#1D1815`)
- Primary actions / nukage glow / HUD digits → `colors.primary.500` (`#39FF14`)
- Pure nuclear-green readouts / live indicators → `colors.secondary.500` (`#00FC00`)
- Damage / danger / hellfire → `colors.accent.500` (`#A8200D`)
- Rust-brown bezels & borders → `colors.neutral.500` (`#7A4B2A`)
- Body text on metal → `colors.text.primary` (toxic-tinted off-white `#E8FFE0`)

## Typography

The type voice is embossed and techno-gothic, approximating Doom's carved metal title art. **Pirata One** drives display headlines — a blackletter-derived gothic face that reads as engraved hell-typography. **Metamorphous** carries subheads and body, a sturdy gothic serif with the same chiseled stone feel at smaller sizes. **VT323** handles the HUD and all monospace digits — a pixel-bitmap terminal font that mirrors the in-game ammo/health readouts. **Cinzel** is the carved-Roman-capital accent for inscriptions and labels. Uppercase tracking stays wide (`0.05em`) so titling reads as embossed plating.

**Text styles**:
- `display-xl` — Pirata One, 96px, weight 400, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Pirata One, 64px, weight 400, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Metamorphous, 48px, weight 400, line-height 1.2, letter-spacing 0
- `body-lg` — Metamorphous, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Metamorphous, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Cinzel, 14px, weight 600, line-height 1.375, letter-spacing 0.05em
- `mono-md` — VT323, 18px, weight 400, line-height 1.4, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments — tight, modular like HUD plating
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Section padding: 64px vertical (md), 96px (lg) — breathing room around dense plated panels
- Grid gaps: 16px (md) to 24px (lg) — panels butt close like wall segments

## Elevation & Depth

Depth is *embossed and recessed*, not soft. Surfaces are beveled metal plates: a bright rust-brown highlight along the top inner edge, a dark recess along the bottom, like extruded HUD panels. Outer drop shadows are near-opaque black (the grime is deep), and elevation is conveyed by adding a radioactive green glow rather than a soft blur — luminance, not softness.

- Surface style: layered (stacked beveled metal plates)
- Blur: none (Doom is crisp pixel art, no atmospheric blur)
- Shadow ladder: deep black drops (`rgba(0,0,0,...)` 0.6→0.9) with inset bevel highlights; lg and up add a `rgba(57,255,20,...)` nukage glow
- Inner shadow: dark recess `inset 0 2px 6px rgba(0,0,0,0.7)` for sunken inputs and pools
- Focus ring: 3px nukage-green glow at 45% opacity

## Shapes

- `none`: 0 — raw plating edges, scanline bands
- `sm`: 2px — tags, chips, small HUD readouts
- `md`: 3px — buttons and inputs (hard, barely-rounded bevels)
- `lg`: 4px — cards and plated panels
- `xl`: 6px — large containers, status modules
- `full`: 9999px — circular gauges, reactor dials, radiation icons

## Motion

Motion is lively but mechanical, not playful — flickering CRT readouts, pulsing nukage glow, and the snap of a HUD element activating. Transitions feel electric and slightly unstable, like a scanline display under radioactive light, never bouncy or soft.

- Level: lively
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)`
- Hover patterns: glow (nukage luminance ramps up), tint (color shift toward pure nuclear green), stroke (bezel border brightens to green)
- `reducedMotion: true` — flicker and pulse animations respect `prefers-reduced-motion`

## Techniques

### Embossed techbase bevel
The chunky beveled HUD-panel look: a rust-brown plate with a bright top inner highlight and a dark recessed bottom, like extruded metal.
```css
.element {
  background: linear-gradient(180deg, #2B2622 0%, #1D1815 100%);
  border: 2px solid #7A4B2A;
  border-radius: 3px;
  box-shadow:
    inset 0 1px 0 rgba(122, 75, 42, 0.6),
    inset 0 -2px 5px rgba(0, 0, 0, 0.65),
    0 4px 14px rgba(0, 0, 0, 0.7);
}
```

### Glowing nukage pool
The radioactive toxic-waste accent surface: a saturated green field with a pulsing outer glow, used for active indicators and accent panels.
```css
.element {
  background: radial-gradient(ellipse at 50% 40%, #50FF00 0%, #26D406 55%, #157A05 100%);
  color: #072E02;
  box-shadow:
    0 0 16px rgba(57, 255, 20, 0.55),
    inset 0 0 12px rgba(0, 252, 0, 0.4);
  animation: nukage-pulse 1.6s ease-in-out infinite;
}
@keyframes nukage-pulse {
  0%, 100% { box-shadow: 0 0 14px rgba(57,255,20,0.45), inset 0 0 10px rgba(0,252,0,0.35); }
  50%      { box-shadow: 0 0 26px rgba(57,255,20,0.7),  inset 0 0 16px rgba(0,252,0,0.55); }
}
```

### Scanline + dither grain overlay
The shareware-era CRT texture: horizontal scanlines layered over a faint pixel-dither grain, draped across dark metal surfaces.
```css
.element {
  position: relative;
  background-color: #161210;
}
.element::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    repeating-linear-gradient(0deg, rgba(0,0,0,0.28) 0px, rgba(0,0,0,0.28) 1px, transparent 1px, transparent 3px),
    repeating-linear-gradient(90deg, rgba(57,255,20,0.04) 0px, rgba(57,255,20,0.04) 1px, transparent 1px, transparent 2px);
  mix-blend-mode: overlay;
}
```

## Iconography

Icons should read as in-game HUD glyphs and pickup sprites: hard-edged, filled, slightly pixelated, never thin or airy. Draw from Doom's own vocabulary — radiation trefoils, barrels, keycards, skulls, ammo and health crosses — rendered as chunky filled silhouettes with a 2px hard edge. Where functional icons are needed, use a custom filled set tinted nukage green over the rust-brown metal, so they glow like active readouts.

- Treatment: filled (hard-edged silhouettes, no thin linework)
- Set: custom (Doom HUD / pickup-sprite vocabulary)
- Stroke: 2px

## Do's & Don'ts

### ✓ Do
- Use near-black techbase metal `#161210` as the page ground — the artifact lives on grungy oily metal
- Make nukage green `#39FF14` glow — back it with green box-shadow halos on active and primary elements
- Emboss every panel with a rust-brown bevel (`#7A4B2A`) top-highlight and dark bottom recess — surfaces are plated, not flat
- Set HUD digits and stats in VT323 and titles in Pirata One to channel the carved, pixelated in-game type
- Layer scanline and dither grain over dark surfaces to carry the shareware-CRT texture

### ✗ Don't
- Use cream/ivory or plain-white backgrounds — the ground is near-black grungy metal
- Apply clean modern flat design — surfaces must be embossed, pixelated, and grungy
- Desaturate the nukage green — it is a glowing, radioactive saturated green, never minty or muted
- Use pastel or soft-rounded UI — keep it hard, beveled, and techno-gothic

## Applications

This system fits game-adjacent products, retro-FPS fan sites, modding hubs, and esports or speedrun dashboards where the HUD-panel language reads as native. It excels at status-dense layouts — leaderboards, build pages, patch notes, server browsers — where beveled plating and glowing green readouts make data feel like a live in-game display. It also suits dark-mode landing pages and event microsites for horror, sci-fi, and synthwave-adjacent brands that want loud, techno-gothic energy.
