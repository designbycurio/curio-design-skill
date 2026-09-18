---
version: 1

meta:
  id: ukrainian-pysanka-wax-egg
  name: "Ukrainian Pysanka Wax-Resist Egg"
  description: "Deep indigo dye-bath ground carrying precise white wax-reserved line-work — ruzha stars, wheat bands, and red-gold folk motifs"
  isDark: true
  tags: [historical, decorative, handmade, narrative, bold]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Centuries-old folk tradition; 19th-century aniline-dye revival"
  region: "Ukraine (Carpathian and central regions)"
  regionZh: "乌克兰（喀尔巴阡山区及中部地区）"
  keyFigures: ["Village pysankarky (egg-writing women)", "Folk-craft revivalists"]
  movements: ["Ukrainian folk ritual art", "Slavic Easter egg-writing (pysankarstvo)"]

introduction: |
  The pysanka is Ukraine's wax-resist Easter egg: a design is written in molten beeswax with a kistka stylus, then the egg passes through successive dye baths from lightest to darkest, each wax layer reserving the color beneath. The final ground is the darkest bath — in the 19th-century aniline revival, a deep indigo or purple joined the traditional black.

  This design system translates that shell into interface: a saturated indigo field carrying crisp white reserved lines, eight-pointed ruzha sun-stars, wheat-sheaf bands, and measured red and gold accents — geometry drawn by hand, precise as wax.
introductionZh: |
  皮桑卡（pysanka）是乌克兰的蜡染复活节彩蛋：以称作 kistka 的细笔尖蘸熔化的蜂蜡在蛋壳上"书写"纹样，再由浅至深逐层浸染，蜡线封存下层颜色。最终的底色即是最深的一道染浴——在十九世纪苯胺染料复兴时期，深靛蓝与紫色底与传统黑色并列登场。

  本设计系统将这枚染就的蛋壳译为界面语言：饱和的深靛蓝底色上，白色留蜡线条勾出精确的几何纹样——八角"鲁扎"太阳星、麦穗丰收纹带，辅以克制的洋红与金黄点缀。线条出自乡村写蛋妇人（pysankarky）之手，却如蜡刻般利落精准。

colors:
  primary:
    "50": "#EAECF8"
    "100": "#C9CEED"
    "200": "#A3ABDE"
    "300": "#7A85CC"
    "400": "#4A55A8"
    "500": "#1A237E"
    "600": "#161E6C"
    "700": "#12185A"
    "800": "#101448"
    "900": "#0F1235"
    "950": "#080A20"
  secondary:
    "50": "#FCEDED"
    "100": "#F6D1D1"
    "200": "#EEA8A8"
    "300": "#E17A7A"
    "400": "#CC4A4A"
    "500": "#B22222"
    "600": "#9A1D1D"
    "700": "#7E1818"
    "800": "#611212"
    "900": "#450D0D"
    "950": "#2C0808"
  accent:
    "50": "#FBF5E4"
    "100": "#F5E6BE"
    "200": "#EDD48F"
    "300": "#E2BD5C"
    "400": "#D6AA38"
    "500": "#C9971C"
    "600": "#AC8017"
    "700": "#8C6813"
    "800": "#6C500E"
    "900": "#4C380A"
    "950": "#302306"
  neutral:
    "50": "#F8F4E9"
    "100": "#F3ECDC"
    "200": "#E1D9C6"
    "300": "#C3BCB0"
    "400": "#9A97A3"
    "500": "#6E6C86"
    "600": "#55536E"
    "700": "#3F3E57"
    "800": "#2B2A41"
    "900": "#1A192E"
    "950": "#0F0E1D"
  semantic:
    success: { bg: "#2E7D4F", text: "#E9F7EE", light: "#CBEBD8", border: "#256A42" }
    warning: { bg: "#C9971C", text: "#302306", light: "#F5E6BE", border: "#7A4A1E" }
    error: { bg: "#B22222", text: "#FCEDED", light: "#F6D1D1", border: "#7E1818" }
    info: { bg: "#4A55A8", text: "#EAECF8", light: "#C9CEED", border: "#1A237E" }
  background:
    page: "#1A237E"
    surface: "#141A5E"
    subtle: "#0F1235"
  text:
    primary: "#F3ECDC"
    secondary: "#DCD3BC"
    muted: "#9BA3D9"
    inverse: "#0F1235"

typography:
  families:
    heading: "'Marcellus', 'Philosopher', Georgia, serif"
    body: "'EB Garamond', 'Noto Serif', Georgia, serif"
    mono: "'Noto Serif', 'EB Garamond', Georgia, serif"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Marcellus&family=Noto+Serif:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Philosopher:ital,wght@0,400;0,700;1,400&display=swap"
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
    md: "6px"
    lg: "12px"
    xl: "24px"
    full: "9999px"
  color:
    default: "rgba(243, 236, 220, 0.4)"
    subtle: "rgba(243, 236, 220, 0.18)"
    strong: "#F3ECDC"
    focus: "#C9971C"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(8, 10, 32, 0.3)"
  sm: "0 1px 4px rgba(8, 10, 32, 0.35)"
  md: "0 2px 8px rgba(8, 10, 32, 0.4)"
  lg: "0 4px 16px rgba(8, 10, 32, 0.45)"
  xl: "0 8px 24px rgba(8, 10, 32, 0.5)"
  "2xl": "0 12px 40px rgba(8, 10, 32, 0.6)"
  inner: "inset 0 1px 3px rgba(8, 10, 32, 0.4)"
  focus: "0 0 0 3px rgba(201, 151, 28, 0.4)"

motion:
  level: "restrained"
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
  hoverPatterns: [stroke, glow, tint]
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
  set: "phosphor"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#B22222"
      color: "#F3ECDC"
      border: "1px solid rgba(243, 236, 220, 0.6)"
      shadow: "0 2px 8px rgba(8, 10, 32, 0.4)"
      hoverBackground: "#9A1D1D"
      hoverShadow: "0 4px 16px rgba(8, 10, 32, 0.5)"
      hoverColor: "#F8F4E9"
    secondary:
      background: "transparent"
      color: "#F3ECDC"
      border: "1px solid rgba(243, 236, 220, 0.5)"
      shadow: "none"
      hoverBackground: "rgba(243, 236, 220, 0.08)"
      hoverShadow: "none"
      hoverColor: "#F8F4E9"
    ghost:
      background: "transparent"
      color: "#F3ECDC"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(243, 236, 220, 0.06)"
      hoverShadow: "none"
      hoverColor: "#C9971C"
    danger:
      background: "#B22222"
      color: "#FCEDED"
      border: "1px solid #7E1818"
      shadow: "0 2px 8px rgba(178, 34, 34, 0.3)"
      hoverBackground: "#7E1818"
      hoverShadow: "0 4px 12px rgba(178, 34, 34, 0.4)"
      hoverColor: "#FCEDED"
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 22px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 30px", fontSize: "1.125rem" }
    borderRadius: "9999px"
    fontWeight: 500
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#0F1235"
    color: "#F3ECDC"
    border: "1px solid rgba(243, 236, 220, 0.35)"
    borderRadius: "6px"
    padding: "10px 14px"
    focusBorder: "#C9971C"
    placeholderColor: "#9BA3D9"
  card:
    base:
      background: "#141A5E"
      border: "1px solid rgba(243, 236, 220, 0.35)"
      borderRadius: "12px"
      padding: "24px"
      shadow: "0 2px 8px rgba(8, 10, 32, 0.4)"
    hover:
      shadow: "0 8px 24px rgba(8, 10, 32, 0.5)"
      transform: "translateY(-2px)"
---

# Ukrainian Pysanka Wax-Resist Egg

> A deep indigo dye-bath shell carrying wax-crisp white line-work: ruzha sun-stars, wheat bands, and red-gold folk geometry written by hand.

## Origin

The pysanka (from *pysaty*, "to write") is the Ukrainian wax-resist Easter egg, a ritual art older than written record in the Carpathian and central regions. The pysankarka — the village egg-writing woman — draws molten beeswax onto the shell with a kistka stylus, then submerges the egg in successive dye baths ordered strictly from light to dark. Each wax pass reserves the color beneath it, so the design is built in negatives: white lines are the untouched shell, yellows and reds are early baths sealed under wax, and the final ground is the darkest bath of all. The motifs are inherited, not invented — eight-pointed ruzha stars for the sun, wheat sheaves for harvest, endless meander lines for eternity.

In the nineteenth century, imported aniline dyes triggered a revival: deep blue, indigo, and purple grounds joined the traditional black, giving the classic revival-era look — saturated indigo shells divided into registers by fine reserved-white geometry. Collections such as the Ukrainian Museum in New York preserve thousands of these eggs, each a hand-written record of village pattern vocabularies.

## Overview

Composition cues:
- **Layout**: Banded, register-based grid wrapping content the way pysanka ornament wraps a curved shell — horizontal bands and radial medallions, symmetrical about a central axis
- **Content width**: Container width with ornamental band borders top and bottom; sections read as dye registers stacked on the shell
- **Framing**: Bordered — every card and panel carries a fine reserved-white hairline, the wax line that divides color fields
- **Grid intensity**: Strong — radial and banded symmetry govern placement; motifs repeat on strict geometric rhythm

## Colors

The palette is a literal dye-bath sequence read in reverse. The ground is the final, darkest bath: deep aniline indigo `#1A237E`, deepening to near-black indigo `#0F1235` for recessed depth. Against it sits `#F3ECDC` — not a background but the *reserved line*, the untouched eggshell preserved under wax, used exclusively for line-work and text. Earlier baths supply the accents: onion-skin and cochineal red `#B22222`, gold-yellow `#C9971C`, and warm motif brown `#7A4A1E` for wheat and branch details. Everything is matte and saturated — dyed shell, not glaze — and white never spreads into a field; it stays a line.

**Role usage**:
- Page background → `colors.background.page` (deep indigo `#1A237E`, the final dye bath)
- Raised/recessed panels → `colors.background.surface` (`#141A5E`) and `colors.background.subtle` (near-black indigo `#0F1235`, the deepest bath)
- Reserved line-work, borders, and body text → `colors.text.primary` (wax-preserved white `#F3ECDC`)
- Primary actions / ritual accents → `colors.secondary.500` (cochineal red `#B22222`)
- Highlights, focus rings, sun-star centers → `colors.accent.500` (gold `#C9971C`)
- Wheat and branch motif details → motif brown `#7A4A1E` (semantic warning border)
- Muted captions on indigo → `colors.text.muted` (indigo-tinted `#9BA3D9`)
- Text on light chips/badges → `colors.text.inverse` (`#0F1235`)

## Typography

The type voice is a folk-book serif: the printed prayer books and pattern albums of the revival era, not a modern grotesque. **Marcellus** leads display work — its inscribed, lapidary capitals carry a Slavic epigraphic character — with **Philosopher** as a display alternate for warmer, slightly curved headings. Body text is **EB Garamond**, the folk-book workhorse, with **Noto Serif** as the sturdier companion for captions and the mono role. Display settings breathe with wide letter-spacing, like letters spaced around an egg's circumference; body text stays quiet and book-like.

**Text styles**:
- `display-xl` — Marcellus, 96px, weight 400, line-height 1.0, letter-spacing 0.02em
- `display-lg` — Marcellus, 64px, weight 400, line-height 1.1, letter-spacing 0.02em
- `heading-1` — Marcellus, 48px, weight 400, line-height 1.2, letter-spacing 0.01em
- `heading-2` — Philosopher, 30px, weight 700, line-height 1.25, letter-spacing 0.01em
- `body-lg` — EB Garamond, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — EB Garamond, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Noto Serif, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Noto Serif, 16px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments — bands align like dye registers
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Section padding: 64px (md) to 96px (lg) vertical — each section is a distinct register on the shell
- Grid gaps: 16px (md), 24px (lg); ornamental band dividers between major sections consume 8–12px of their own

## Elevation & Depth

A pysanka has no gloss and no cast shadows — it is a matte dyed shell whose depth comes from the dye sequence itself: deeper color reads as deeper layer. Elevation here follows that logic. Recessed areas darken toward the near-black `#0F1235` bath; raised elements are separated by reserved-white hairlines, not by blur or glass. Drop shadows exist only as soft indigo-black ambience to lift cards off the ground, never as glossy highlights.

- Surface style: solid — matte, opaque dyed surfaces
- Blur: none — wax lines are crisp; nothing is frosted
- Shadow ladder: deep indigo-black rgba(8, 10, 32, …) at rising opacity, xs → 2xl
- Depth direction: darker = deeper (dye-bath logic); lighter lines = nearer (wax-reserved)
- Focus ring: 3px gold glow `rgba(201, 151, 28, 0.4)` — the kistka's gold bath

## Shapes

- `none`: 0 — straight band dividers and register rules
- `sm`: 2px — tags, small chips
- `md`: 6px — inputs, minor panels
- `lg`: 12px — cards and content panels
- `xl`: 24px — hero medallions, feature panels echoing the shell's curvature
- `full`: 9999px — buttons, rosette medallions, avatar frames (the egg's own geometry)

## Motion

Motion is restrained and ceremonial — the slow rotation of an egg in the hand as its bands come into view, the deliberate pull of a wax line. Transitions favor gentle fades and small translations; nothing bounces or spins. Line-reveal effects (a border drawing itself in) are the one signature flourish, echoing the kistka writing wax.

- Level: restrained
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)`; spring reserved for medallion hover only
- Hover patterns: stroke (white hairline brightens), glow (soft gold halo), tint (indigo lightens one bath)
- `reducedMotion: true` — all animations respect `prefers-reduced-motion`

## Techniques

### Wax-reserved double line
The signature pysanka edge: a crisp reserved-white hairline with a second, fainter line offset outside it, like two passes of the kistka dividing color fields.
```css
.element {
  border: 1px solid rgba(243, 236, 220, 0.85);
  outline: 1px solid rgba(243, 236, 220, 0.25);
  outline-offset: 4px;
  background: #141A5E;
  border-radius: 12px;
}
```

### Ruzha eight-point star medallion
A radial sun-star built from two rotated squares of conic gradient — the ruzha motif — used as a hero medallion or section marker on the indigo ground.
```css
.element {
  width: 160px;
  height: 160px;
  border-radius: 9999px;
  background:
    conic-gradient(
      from 22.5deg,
      #C9971C 0deg 45deg, transparent 45deg 90deg,
      #B22222 90deg 135deg, transparent 135deg 180deg,
      #C9971C 180deg 225deg, transparent 225deg 270deg,
      #B22222 270deg 315deg, transparent 315deg 360deg
    ),
    radial-gradient(circle at center, #F3ECDC 0 18%, transparent 18%),
    #0F1235;
  border: 1px solid rgba(243, 236, 220, 0.85);
  box-shadow: 0 0 0 6px #1A237E, 0 0 0 7px rgba(243, 236, 220, 0.4);
}
```

### Wheat-band register divider
A horizontal ornamental band between sections: repeating diagonal red-and-gold strokes fenced by reserved-white hairlines, the wheat-sheaf harvest register.
```css
.element {
  height: 14px;
  border-top: 1px solid rgba(243, 236, 220, 0.85);
  border-bottom: 1px solid rgba(243, 236, 220, 0.85);
  background: repeating-linear-gradient(
    -55deg,
    #C9971C 0 4px,
    #0F1235 4px 8px,
    #B22222 8px 12px,
    #0F1235 12px 16px
  );
}
```

## Iconography

Icons should read as motifs written in a single reserved line — sun-stars, wheat sheaves, rams' horns, endless meanders — not as utilitarian UI glyphs. Where functional icons are required, use Phosphor in its linear treatment at 1.5px stroke, colored in reserved white `#F3ECDC` so every icon reads as wax line-work on the dyed shell; gold `#C9971C` marks the active state.

- Treatment: linear (single-weight line, wax-crisp)
- Set: Phosphor (thin/regular), supplemented by custom pysanka motif SVGs where possible
- Stroke: 1.5px, reserved white on indigo

## Do's & Don'ts

### ✓ Do
- Keep deep indigo `#1A237E` as the page ground everywhere — the darkest bath is the field
- Draw every border and divider in reserved white `#F3ECDC` — white is a line, never a fill
- Build layouts in bands and radial medallions with strict symmetry, like registers wrapping a shell
- Spend red `#B22222` and gold `#C9971C` as small, deliberate motif accents — early baths, used sparingly
- Set display type in Marcellus or Philosopher and body in EB Garamond or Noto Serif for the folk-book voice

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — white is the reserved line, not the field
- No pale pastel egg-shell tints; the final bath is deep and saturated
- No loose, painterly, or brush-textured motifs — line-work is geometric, precise, and wax-crisp
- No modern sans display faces (Inter, Helvetica, Geist) — keep the inscribed folk-book character
- Don't add gloss, glass blur, or heavy photographic shadows — the shell is matte dyed material

## Applications

This system suits cultural-heritage and museum microsites, folk-craft archives, and festival or holiday campaign pages where ritual gravity and handmade precision must coexist. It also serves editorial storytelling on Ukrainian and Slavic culture, artisan e-commerce (dyes, textiles, ceramics), and event identities for spring or Easter programming. The deep indigo ground with jewel-line accents reads premium in dark-mode-first products that want ornament with discipline rather than minimalist austerity.
