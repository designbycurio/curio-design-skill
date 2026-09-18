---
version: 1

meta:
  id: pokemon-game-boy-1996
  name: Pokémon Game Boy
  description: "Saturated kawaii pixel art meets Ken Sugimori's hand-watercolored pocket monsters on a chunky Game Boy grid"
  isDark: false
  tags: [retro, playful, friendly, bold, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1996 (Pocket Monsters Red/Green, Japan); 1998 international; ongoing 30-year franchise"
  region: "Japan (Tokyo / Kyoto)"
  regionZh: "日本（东京／京都）"
  keyFigures: [Satoshi Tajiri, Ken Sugimori, Junichi Masuda, Atsuko Nishida]
  movements: [8-bit Game Boy pixel art, 90s Japanese kawaii illustration, transmedia franchise design]

introduction: |
  The original 1996 Pokémon Red/Green fused two unlikely aesthetics into one of the most recognizable visual identities ever created: Ken Sugimori's delicate hand-watercolored creature portraits and Game Freak's grid-precise 4-shade monochrome pixel sprites. The result is a design language that feels simultaneously handmade and systematic.

  This system captures that duality — Pokeball red, Pikachu yellow, and Game Boy LCD green anchored by thick black manga contours, chunky 8px-radius buttons, and comic-book offset shadows. Every surface says "catch 'em all" with saturated kawaii confidence.
introductionZh: |
  1996年的初代《精灵宝可梦 红/绿》将杉森建的手绘水彩宝可梦肖像与Game Freak工程师的四色Game Boy像素精灵融为一体，创造出游戏史上最具辨识度的视觉语言。精灵球的红白配色、皮卡丘的纯黄、Game Boy液晶屏的绿色调——每一个元素都承载着90年代日本卡哇伊文化的饱和活力。

  本设计系统复刻了那份像素与水彩共存的独特质感：厚实的黑色漫画轮廓线、8像素圆角的复古按钮、漫画风格的偏移投影，以及密集而欢快的画面构成。

colors:
  primary:    {"50": "#FEE8EA", "100": "#FDD1D5", "200": "#FBA3AB", "300": "#F87581", "400": "#F54757", "500": "#E63946", "600": "#C42E39", "700": "#A3242F", "800": "#821A24", "900": "#61101A", "950": "#400A11"}
  secondary:  {"50": "#FFFBE5", "100": "#FFF7CC", "200": "#FFEF99", "300": "#FFE766", "400": "#FFDF33", "500": "#FFD60A", "600": "#D4B100", "700": "#A88C00", "800": "#7D6800", "900": "#524400", "950": "#3D3300"}
  accent:     {"50": "#EBF6FD", "100": "#D7EDFB", "200": "#AFDCF7", "300": "#87CAF3", "400": "#5FB9EF", "500": "#5DADE2", "600": "#3A95D1", "700": "#2D74A4", "800": "#205477", "900": "#14344A", "950": "#0C2030"}
  neutral:    {"50": "#FAFAFA", "100": "#F5F5F5", "200": "#E5E5E5", "300": "#D4D4D4", "400": "#A3A3A3", "500": "#737373", "600": "#525252", "700": "#404040", "800": "#262626", "900": "#171717", "950": "#0A0A0A"}
  semantic:
    success: { bg: "#27AE60", text: "#FFFFFF", light: "#D4EFDF", border: "#1E8449" }
    warning: { bg: "#FFD60A", text: "#0A0A0A", light: "#FFF7CC", border: "#D4B100" }
    error:   { bg: "#E63946", text: "#FFFFFF", light: "#FDD1D5", border: "#C42E39" }
    info:    { bg: "#5DADE2", text: "#FFFFFF", light: "#D7EDFB", border: "#3A95D1" }
  background:
    page:    "#FFFFFF"
    surface: "#FAFAFA"
    subtle:  "#9BBC0F"
  text:
    primary:   "#0A0A0A"
    secondary: "#404040"
    muted:     "#737373"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Anton', sans-serif"
    body:    "'Cabin', 'Inter', sans-serif"
    mono:    "'Press Start 2P', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Anton&family=Cabin:wght@400;500;600;700&family=Press+Start+2P&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "8px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "4px", md: "8px", lg: "12px", xl: "16px", full: "9999px"}
  color:  {default: "#0A0A0A", subtle: "#D4D4D4", strong: "#0A0A0A", focus: "#5DADE2"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "2px 2px 0 #0A0A0A"
  sm: "3px 3px 0 #0A0A0A"
  md: "4px 4px 0 #0A0A0A"
  lg: "6px 6px 0 #0A0A0A"
  xl: "8px 8px 0 #0A0A0A"
  "2xl": "12px 12px 0 #0A0A0A"
  inner: "inset 0 2px 0 rgba(0,0,0,0.1)"
  focus: "0 0 0 3px rgba(93,173,226,0.5)"

motion:
  level: "playful"
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "350ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, scale, tint]
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
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#E63946", color: "#FFFFFF", border: "2px solid #0A0A0A", shadow: "4px 4px 0 #0A0A0A", hoverBackground: "#C42E39", hoverShadow: "2px 2px 0 #0A0A0A", hoverColor: "#FFFFFF"}
    secondary: {background: "#FFD60A", color: "#0A0A0A", border: "2px solid #0A0A0A", shadow: "4px 4px 0 #0A0A0A", hoverBackground: "#D4B100", hoverShadow: "2px 2px 0 #0A0A0A", hoverColor: "#0A0A0A"}
    ghost:     {background: "transparent", color: "#0A0A0A", border: "2px solid #0A0A0A", shadow: "none", hoverBackground: "#F5F5F5", hoverShadow: "2px 2px 0 #0A0A0A", hoverColor: "#0A0A0A"}
    danger:    {background: "#E63946", color: "#FFFFFF", border: "2px solid #0A0A0A", shadow: "4px 4px 0 #0A0A0A", hoverBackground: "#A3242F", hoverShadow: "2px 2px 0 #0A0A0A", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "4px 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "8px 16px", fontSize: "1rem"}, lg: {height: "48px", padding: "12px 24px", fontSize: "1.125rem"}}
    borderRadius: "8px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#9BBC0F"
    color: "#0F380F"
    border: "2px solid #0A0A0A"
    borderRadius: "8px"
    padding: "8px 12px"
    focusBorder: "#5DADE2"
    placeholderColor: "#306230"
  card:
    base:  {background: "#FFFFFF", border: "2px solid #0A0A0A", borderRadius: "12px", padding: "16px", shadow: "4px 4px 0 #0A0A0A"}
    hover: {shadow: "6px 6px 0 #0A0A0A", transform: "translate(-2px, -2px)"}
---

# Pokémon Game Boy

> Saturated kawaii pixel art meets Ken Sugimori's hand-watercolored pocket monsters — chunky, bold, and bursting with 1996 Game Boy charm.

## Origin

Pokémon Red and Green launched in Japan on February 27, 1996, developed by Game Freak under Satoshi Tajiri's vision of collecting creatures inspired by his childhood insect-hunting. Ken Sugimori hand-watercolored all 151 original Pokémon — each portrait rendered with visible pigment pooling and thin black contour lines — establishing an art direction that would define the franchise for three decades. The Game Boy's 4-shade green LCD (palette: `#9BBC0F` to `#0F380F`) constrained the in-game sprites to pure pixel grid precision.

The resulting visual identity is a collision of handmade warmth and digital rigor: Sugimori's watercolors for marketing and packaging, Game Freak's 56×56 pixel sprites for gameplay, and a saturated kawaii color system (Pokeball red, Pikachu yellow, elemental blues and greens) that became the most commercially successful palette in entertainment history. Atsuko Nishida's Pikachu design — round, yellow, lightning-bolt-tailed — became the single most recognized character silhouette worldwide.

## Overview

Composition cues:
- **Layout**: Dense grid-based panels echoing Game Boy menu screens; no empty space — kawaii compositions feel populated and energetic
- **Content width**: Container (1024–1280px) with chunky internal padding
- **Framing**: Thick 2–3px black-bordered panels with comic-book offset shadows
- **Grid intensity**: Strong — 8px modular grid with visible structure

## Colors

The palette is pure saturated kawaii — no pastels, no muted tones. Pokeball red and white form the iconic dual base visible on every logo and capsule. Pikachu yellow provides the franchise's most famous accent. Game Boy LCD green (`#9BBC0F` → `#0F380F`) serves as a retro-nostalgia surface for special panels. Water blue and grass green round out the elemental type system. Every color is outlined in thick black contour, manga-style.

**Role usage**:
- Page background → `colors.background.page` (pure white `#FFFFFF`)
- Card / panel surface → `colors.background.surface` (`#FAFAFA`)
- Retro Game Boy panels → `colors.background.subtle` (`#9BBC0F`)
- Primary actions (CTAs, Pokeball buttons) → `colors.primary.500` (`#E63946`)
- Highlight / badge / star → `colors.secondary.500` (`#FFD60A`)
- Water-type accents / links → `colors.accent.500` (`#5DADE2`)
- Body text / outlines → `colors.text.primary` (`#0A0A0A`)
- Muted labels → `colors.text.muted` (`#737373`)

## Typography

Type voice splits between retro pixel nostalgia and modern anime-merchandise boldness. Headers use Anton — a condensed impact sans that echoes the chunky uppercase energy of Pokémon merchandise and anime title cards. Body text uses Cabin for friendly readability. Pixel-font moments (retro panels, stat displays, Game Boy screen UI) use Press Start 2P, the authentic 8-bit bitmap aesthetic.

**Text styles**:
- `display-xl` — Anton, 96px, weight 400, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Anton, 64px, weight 400, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Anton, 48px, weight 400, line-height 1.2, letter-spacing 0
- `heading-2` — Anton, 36px, weight 400, line-height 1.2, letter-spacing 0
- `body-lg` — Cabin, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — Cabin, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Cabin, 14px, weight 500, line-height 1.4, letter-spacing 0
- `mono-md` — Press Start 2P, 12px, weight 400, line-height 1.8, letter-spacing 0

## Spacing & Layout

- Base unit: 8px (pixel-grid modular)
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px with 24px gutter
- Section padding: 64–96px vertical
- Card internal padding: 16–24px
- Dense compositions — minimize whitespace, fill panels with content

## Elevation & Depth

Materiality is flat and comic-book-inspired. No soft diffused shadows — only hard-offset black drop shadows that feel like manga panel borders or sticker edges. Surfaces are opaque solids (white or Game Boy green), never translucent. Depth is communicated through stacking offset shadows rather than blur.

- Surfaces: opaque solid fills, no glass or blur
- Shadow style: hard pixel-offset (`Xpx Xpx 0 #0A0A0A`)
- Shadow ladder: xs (2px) → sm (3px) → md (4px) → lg (6px) → xl (8px) → 2xl (12px)
- Hover: shadow shrinks + element translates toward shadow origin (press-in effect)

## Shapes

- Button radius: 8px (chunky retro pill)
- Card radius: 12px
- Input radius: 8px
- Badge / tag radius: 4px
- Pokeball circle motifs: `border-radius: 9999px` with red/white split
- All shapes outlined with 2px solid black minimum

## Motion

Motion is playful and bouncy — echoing the energetic feel of Pokémon battle animations and menu transitions. Elements pop in with spring easing, buttons press down on click, cards lift on hover. Nothing is subtle or restrained.

- Level: playful
- Fast interactions: 100ms (button press feedback)
- Normal transitions: 200ms (panel reveals, hover states)
- Slow animations: 350ms (page transitions, card entrances)
- Spring easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` for bouncy overshoots
- Hover patterns: lift (translate-Y + shadow grow), scale (1.02–1.05), tint (background color shift)
- Reduced motion: respects `prefers-reduced-motion`

## Techniques

### Comic-book offset shadow press
Buttons and cards use hard-offset black shadows that shrink on interaction, creating a tactile "press into the page" effect.
```css
.element {
  border: 2px solid #0A0A0A;
  box-shadow: 4px 4px 0 #0A0A0A;
  transition: box-shadow 100ms cubic-bezier(0.34, 1.56, 0.64, 1),
              transform 100ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.element:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #0A0A0A;
}
.element:active {
  transform: translate(2px, 2px);
  box-shadow: 1px 1px 0 #0A0A0A;
}
```

### Game Boy LCD retro panel
Input fields and stat displays rendered in the authentic 4-shade Game Boy green palette with pixel font.
```css
.gameboy-panel {
  background: #9BBC0F;
  border: 2px solid #0F380F;
  border-radius: 8px;
  padding: 12px 16px;
  font-family: 'Press Start 2P', monospace;
  font-size: 12px;
  color: #0F380F;
  box-shadow: inset 0 2px 0 rgba(15, 56, 15, 0.1);
}
```

### Pokeball split-circle motif
Decorative Pokeball circles used as section dividers, avatar frames, or loading indicators.
```css
.pokeball-motif {
  width: 48px;
  height: 48px;
  border-radius: 9999px;
  border: 3px solid #0A0A0A;
  background: linear-gradient(to bottom, #E63946 50%, #FFFFFF 50%);
  position: relative;
}
.pokeball-motif::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
  border-radius: 9999px;
  border: 3px solid #0A0A0A;
  background: #FFFFFF;
}
```

## Iconography

Icons should feel chunky and bold to match the thick-outlined manga aesthetic. Filled treatment at 2px stroke ensures visibility against busy kawaii compositions. Pokeball circles, lightning bolts, and star shapes are preferred decorative motifs over generic geometric icons.

- Treatment: filled with 2px stroke
- Set: Lucide (rounded, friendly geometry)
- Stroke: 2px

## Do's & Don'ts

### ✓ Do
- Use Pokeball red `#E63946` for all primary actions and CTAs
- Apply 2–3px black outlines on every interactive element and card
- Use hard-offset black shadows (no blur) for comic-book depth
- Fill compositions densely — kawaii layouts avoid empty space
- Use Press Start 2P for retro Game Boy screen moments

### ✗ Don't
- Use pastel or muted palettes — the kawaii palette is always saturated
- Apply modern minimalism or Bauhaus restraint
- Use thin outlines below 2px
- Use photographic imagery — hand-watercolored Sugimori-style portraits only
- Place content on pure dark backgrounds (white ground is primary; Game Boy green is accent only)
- Use smooth digital gradients (watercolor pooling for character art)
- Substitute generic geometric icons for Pokeball circles and lightning bolts
- Use decorative serifs as primary typeface

## Applications

This system is ideal for fan community sites, Pokémon collection trackers, retro gaming dashboards, TCG deck builders, and nostalgic 90s-themed landing pages. The dense kawaii composition and chunky comic-book styling works especially well for content-rich interfaces that need to feel energetic and collectible rather than corporate.
