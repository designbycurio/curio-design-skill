---
version: 1

meta:
  id: shaker-furniture-1850-minimalist
  name: Shaker Furniture 1850
  description: "Bone-plaster and ironwork minimalism drawn from the 1830–1900 Shaker communal furniture canon"
  isDark: false
  tags: [minimal, modernist, handmade, professional, editorial]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1830–1900 peak Shaker craft production; community founded 1747"
  region: "New York (Mount Lebanon), Massachusetts (Hancock), Kentucky (Pleasant Hill), Maine (Sabbathday Lake)"
  regionZh: "美国纽约州新黎巴嫩、马萨诸塞州汉考克、肯塔基州愉悦山、缅因州安息日湖"
  keyFigures: [Ann Lee, Mother Lucy Wright, Brother Robert Wagan, Eldress Bertha Lindsay]
  movements: [Shaker communal craft tradition, oval-box finger-joint canon, milk-paint pigment system]

introduction: |
  The Shaker furniture canon — stabilized between 1830 and 1900 across Mount Lebanon, Hancock, and Pleasant Hill — represents the purest American expression of form following function as theological principle. Every dowel joint, wall-peg rail, and oval-box finger existed to serve a purpose, and beauty emerged as a consequence of that discipline.

  This design system distills the Shaker visual register into digital form: smoke-pine warm wood, bone wall plaster, true ironwork black, and a single smoke-teal milk-paint accent. No sentimentality, no distressing — just the plain clarity that later inspired Scandinavian modernism.
introductionZh: |
  震教徒家具体系——1830至1900年间在纽约新黎巴嫩、马萨诸塞汉考克和肯塔基愉悦山等社区定型——是美国工艺史上"功能即美"最纯粹的表达。每一根榫卯、每一条挂钉横栏、每一只椭圆盒的指接缝都因实用而存在，美感是信仰纪律的自然结果。

  本设计系统将震教徒视觉语言转化为数字界面：烟松暖木色、骨白灰泥墙、锻铁纯黑，以及一抹烟青牛奶漆点缀。没有做旧、没有田园感伤——只有那份启发了整个北欧现代主义运动的素朴理性。

colors:
  primary:    {"50": "#f5f5f5", "100": "#e8e8e8", "200": "#d4d4d4", "300": "#a3a3a3", "400": "#6b6b6b", "500": "#1A1A1A", "600": "#171717", "700": "#141414", "800": "#0f0f0f", "900": "#0a0a0a", "950": "#050505"}
  secondary:  {"50": "#f9f5f0", "100": "#f0e8dc", "200": "#e2d2ba", "300": "#d4bb98", "400": "#bea17d", "500": "#A88863", "600": "#8f7252", "700": "#755c42", "800": "#5c4834", "900": "#4a3a2b", "950": "#2d2319"}
  accent:     {"50": "#f0f5f6", "100": "#dce8ea", "200": "#b8d0d4", "300": "#8fb3b9", "400": "#66969e", "500": "#3D5A60", "600": "#354e53", "700": "#2d4246", "800": "#253639", "900": "#1e2c2f", "950": "#121c1e"}
  neutral:    {"50": "#fafaf9", "100": "#f5f4f2", "200": "#ebe9e5", "300": "#dedad4", "400": "#b8b3ab", "500": "#8a847c", "600": "#6b6560", "700": "#524e4a", "800": "#3a3735", "900": "#262423", "950": "#141312"}
  semantic:
    success: { bg: "#2d5a3a", text: "#ffffff", light: "#e8f5ec", border: "#3d7a4f" }
    warning: { bg: "#8a6b2a", text: "#ffffff", light: "#faf3e0", border: "#a88832" }
    error:   { bg: "#6A2A2A", text: "#ffffff", light: "#f9e8e8", border: "#8a3a3a" }
    info:    { bg: "#3D5A60", text: "#ffffff", light: "#e8f0f2", border: "#4d6a70" }
  background:
    page:    "#EDE9DF"
    surface: "#FFFFFF"
    subtle:  "#F5F3EE"
  text:
    primary:   "#1A1A1A"
    secondary: "#524E4A"
    muted:     "#8A847C"
    inverse:   "#EDE9DF"

typography:
  families:
    heading: "'Cormorant Garamond', 'Georgia', serif"
    body:    "'Inter', -apple-system, sans-serif"
    mono:    "'JetBrains Mono', 'Menlo', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&display=swap"
  scale: {"2xs": "0.625rem", "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
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
  radius: {none: "0", sm: "2px", md: "3px", lg: "4px", xl: "6px", full: "9999px"}
  color:  {default: "#1A1A1A", subtle: "#DED AD4", strong: "#1A1A1A", focus: "#3D5A60"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(26,26,26,0.04)"
  sm: "0 1px 3px rgba(26,26,26,0.06)"
  md: "0 1px 4px rgba(26,26,26,0.08)"
  lg: "0 4px 12px rgba(26,26,26,0.10)"
  xl: "0 8px 24px rgba(26,26,26,0.12)"
  "2xl": "0 16px 48px rgba(26,26,26,0.14)"
  inner: "inset 0 1px 2px rgba(26,26,26,0.04)"
  focus: "0 0 0 3px rgba(61,90,96,0.25)"

motion:
  level: "minimal"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [opacity, lift]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "minimal"
  gridIntensity: "subtle"
  rhythm:        "8px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#1A1A1A", color: "#EDE9DF", border: "none", shadow: "none", hoverBackground: "#3D5A60", hoverShadow: "0 1px 4px rgba(26,26,26,0.08)", hoverColor: "#EDE9DF"}
    secondary: {background: "transparent", color: "#1A1A1A", border: "2px solid #1A1A1A", shadow: "none", hoverBackground: "#1A1A1A", hoverShadow: "none", hoverColor: "#EDE9DF"}
    ghost:     {background: "transparent", color: "#1A1A1A", border: "none", shadow: "none", hoverBackground: "rgba(26,26,26,0.06)", hoverShadow: "none", hoverColor: "#1A1A1A"}
    danger:    {background: "#6A2A2A", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#8a3a3a", hoverShadow: "none", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "6px 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "8px 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "12px 28px", fontSize: "1.125rem"}}
    borderRadius: "3px"
    fontWeight: 500
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1A1A1A"
    border: "none"
    borderRadius: "0"
    padding: "10px 0"
    focusBorder: "2px solid #1A1A1A"
    placeholderColor: "#8A847C"
  card:
    base:  {background: "#FFFFFF", border: "1px solid #DEDAD4", borderRadius: "4px", padding: "24px", shadow: "none"}
    hover: {shadow: "0 1px 4px rgba(26,26,26,0.08)", transform: "translateY(-1px)"}
---

# Shaker Furniture 1850

> Bone-plaster walls, ironwork black, and smoke-pine warmth — the theological minimalism that became America's first design language.

## Origin

The Shaker furniture canon emerged from the United Society of Believers communities between 1830 and 1900, principally at Mount Lebanon (New York), Hancock (Massachusetts), Pleasant Hill (Kentucky), and Sabbathday Lake (Maine). Under the doctrinal principle that "beauty rests on utility," craftsmen like Brother Robert Wagan and Brother Orren Haskins produced ladder-back chairs, oval boxes, trestle tables, and wall-peg rail systems whose forms were dictated entirely by function. The Mount Lebanon chair shop sold commercially nationwide by the 1860s, making Shaker design America's first mass-distributed aesthetic.

This visual language — smoke-tinted pine, bone-white plaster interiors, hand-forged iron hardware, and rare milk-paint accents in teal and oxblood — directly influenced Hans Wegner, Børge Mogensen, and the entire Scandinavian modern movement. The Shaker register is not a precursor to minimalism; it is minimalism's original theological argument made physical in wood and iron.

## Overview

Composition cues:
- **Layout**: Vertical stack with generous negative space between sections, echoing the post-and-rail proportions of Shaker wall-peg rails
- **Content width**: Container (max 1024px–1280px), never full-bleed — the composition breathes like a Shaker interior
- **Framing**: Minimal — content stands on its own merit without decorative containers
- **Grid intensity**: Subtle — horizontal rule lines divide sections like the rail-and-stile joinery of a Shaker cupboard door

## Colors

The palette is drawn directly from Shaker material culture: the cool-tinted pine and maple of sanded furniture, the bone-white lime plaster of meeting-house walls, the true black of hand-forged iron hardware, and the rare smoke-teal of historic milk paint. There is no cream, no beige, no warm yellow — Shaker wood has a cool mineral undertone from decades of indoor aging. The oxblood `#6A2A2A` appears only in semantic error states, referencing the deep-red cupboard interiors found at Pleasant Hill.

**Role usage**:
- Page background → `colors.background.page` (bone plaster `#EDE9DF`)
- Surface panels → `colors.background.surface` (white interior `#FFFFFF`)
- Primary actions & text → `colors.primary.500` (ironwork black `#1A1A1A`)
- Warm accents & secondary elements → `colors.secondary.500` (smoke pine `#A88863`)
- Feature accent & dark blocks → `colors.accent.500` (smoke teal `#3D5A60`)
- Muted text → `colors.text.muted` (worn iron grey `#8A847C`)
- Inverse text on dark blocks → `colors.text.inverse` (bone `#EDE9DF`)

## Typography

The type voice pairs a historical serif with a clean contemporary body face. Cormorant Garamond for headlines evokes the 1830s–1840s broadside printing of New Lebanon community notices — it has the weight and proportion of hand-set type without affectation. Inter for body text provides the quiet legibility that Shaker craft demands: nothing decorative, nothing that calls attention to itself over the content it carries.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Cormorant Garamond, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Cormorant Garamond, 48px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Inter, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 14px, weight 400, line-height 1.5, letter-spacing 0
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm at 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-width: 1024px (lg), 1280px (xl)
- Section padding: 64px (md) to 96px (lg) vertical — generous, unhurried
- Grid gap: 16px (md) to 24px (lg) — the breathing room of a Shaker interior

## Elevation & Depth

Shaker interiors are flat and honest — no false depth, no theatrical shadow. Surfaces sit directly on the bone-plaster ground with at most a hairline shadow suggesting physical presence. The material metaphor is a wooden panel resting on a plaster wall: real, tangible, but not floating.

- Surface style: flat — no glass, no blur, no layering tricks
- Blur: none
- Shadow ladder: xs (barely perceptible) → md (the standard `0 1px 4px rgba(26,26,26,0.08)`) → lg (reserved for modals/overlays only)
- Cards use no shadow at rest; on hover, a single `md` shadow appears like a panel lifting slightly from the wall

## Shapes

- Button radius: 3px (almost square — ironwork precision)
- Card radius: 4px (the slight softening of a hand-planed edge)
- Input radius: 0px (underline-only inputs — no rounded fields)
- Full radius: 9999px (reserved for avatar circles and badges only)

## Motion

Shaker craft is still. A chair does not animate into position; it is placed there with intention. Motion in this system is minimal and purposeful — only to confirm interaction, never to entertain.

- Level: minimal
- Hover: opacity fade (0.85) or subtle 1px lift — never scale, never glow
- Durations: fast (120ms) for micro-interactions, normal (250ms) for transitions
- Easing: ease-out for exits, default cubic-bezier for entrances
- Reduced motion: always respected; all animation is optional

## Techniques

### Ironwork underline input
A text input styled as a bone-plaster inset field with only a bottom border — referencing the hand-forged iron strap hinge.
```css
.input-ironwork {
  background: transparent;
  border: none;
  border-bottom: 2px solid #1A1A1A;
  padding: 10px 0;
  color: #1A1A1A;
  font-family: 'Inter', sans-serif;
  transition: border-color 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.input-ironwork:focus {
  outline: none;
  border-bottom-color: #3D5A60;
}
```

### Wall-peg rail divider
A horizontal rule that echoes the Shaker wall-peg rail — a thin black line with periodic dot markers suggesting peg positions.
```css
.divider-peg-rail {
  border: none;
  height: 1px;
  background: repeating-linear-gradient(
    90deg,
    #1A1A1A 0px,
    #1A1A1A 48px,
    transparent 48px,
    transparent 52px
  );
  position: relative;
}
.divider-peg-rail::before {
  content: '';
  position: absolute;
  top: -2px;
  left: 0;
  right: 0;
  height: 5px;
  background: repeating-linear-gradient(
    90deg,
    transparent 0px,
    transparent 46px,
    #1A1A1A 46px,
    #1A1A1A 54px,
    transparent 54px
  );
  mask: repeating-linear-gradient(
    90deg,
    transparent 0px,
    transparent 47px,
    black 47px,
    black 53px,
    transparent 53px
  );
  border-radius: 50%;
}
```

### Oval-box card border
A card with a subtle warm-wood border that references the graduated finger-joint of a Shaker oval box — using a layered border with a slight wood-tone inset.
```css
.card-oval-box {
  background: #FFFFFF;
  border: 1px solid #A88863;
  border-radius: 4px;
  padding: 24px;
  box-shadow: inset 0 0 0 3px #EDE9DF;
  transition: box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.card-oval-box:hover {
  box-shadow:
    inset 0 0 0 3px #EDE9DF,
    0 1px 4px rgba(26, 26, 26, 0.08);
}
```

## Iconography

Icons follow the Shaker principle of honest construction — linear strokes with no fill, no decoration, no ambiguity. Each icon should read as clearly as a hand-forged iron latch: one continuous gesture, immediately understood.

- Treatment: linear (outline only)
- Set: Lucide (closest to the single-stroke Shaker sensibility)
- Stroke: 1.5px — the weight of a fine iron wire

## Do's & Don'ts

### ✓ Do
- Use ironwork black `#1A1A1A` for all primary actions and text — it is the structural material
- Maintain generous negative space between elements — a Shaker room is never crowded
- Let Cormorant Garamond headlines breathe at large sizes with tight letter-spacing
- Use the smoke-teal accent `#3D5A60` sparingly — it is the rare milk-paint moment
- Favor horizontal rule dividers over boxed containers — the wall-peg rail, not the picture frame

### ✗ Don't
- Use cream or beige page backgrounds — bone plaster `#EDE9DF` has a cool mineral tint
- Apply "farmhouse" or "modern farmhouse" Pinterest aesthetics
- Conflate with Scandinavian modern — Shaker is the source, not the copy
- Use distressed or weathered wood textures — Shaker craft is clean, not aged
- Set headlines in sans-serif geometric typefaces
- Create cluttered compositions — Shaker demands generous negative space
- Add cottagecore floral ornament or folk-craft kitsch
- Use warm yellow-cream wood tones — the pine is cool-tinted

## Applications

This system suits editorial platforms, portfolio sites, and product pages where content quality speaks for itself. It excels in contexts that demand quiet authority — publishing tools, craft documentation, architectural project pages — anywhere the interface should recede and let the work be seen plainly.
