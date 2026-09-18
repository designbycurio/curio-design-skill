---
version: 1

meta:
  id: gould-hummingbird-plate-1861
  name: "Gould Hummingbird Plate"
  description: "Victorian hand-finished ornithological lithography: iridescent green plumage, gold-leaf gorgets, and magenta glints set against shadowed dark-foliage grounds"
  isDark: true
  tags: [historical, luxurious, decorative, narrative, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "pre-1900 (title pages dated 1861)"
  region: "Western Europe (British)"
  regionZh: "西欧（英国）"
  keyFigures: ["John Gould", "Henry Constantine Richter", "Hullmandel & Walton"]
  movements: ["Victorian hand-coloured lithography", "Ornithological monograph illustration"]

introduction: |
  John Gould's *A Monograph of the Trochilidae* (1861) is the high point of Victorian hand-finished bird lithography — 360 plates drawn with Henry Richter and printed by Hullmandel & Walton, with gorgets touched in actual gold leaf to mimic iridescence. Hummingbirds hover against shadowed dark-foliage vignettes.

  This system distills that jewel-like natural-history luxury: iridescent green plumage keyed to deep forest grounds, magenta gorget accents, and specular gold-leaf highlights, framed by refined old-style serifs befitting a deluxe Victorian plate book.
introductionZh: |
  约翰·古尔德的《蜂鸟科专著》（1861）是维多利亚时代手工修色鸟类石版画的巅峰之作——全书 360 幅图版由亨利·里希特协同绘制、Hullmandel & Walton 印制，喉羽更以真金箔点缀，模拟那令人目眩的金属光泽。蜂鸟成双或独立，悬停于幽暗的深林叶影之中。

  本设计系统提炼了这种珠宝般的博物学奢华：以虹彩翠绿羽色呼应深沉的森林底色，辅以洋红喉斑与金箔高光，并以精致的旧式衬线字体勾勒——一如那部华贵的维多利亚图版巨册。

colors:
  primary:
    "50": "#E8F5EE"
    "100": "#C8E8D6"
    "200": "#94D2AF"
    "300": "#5FB985"
    "400": "#369C63"
    "500": "#1F7A4D"
    "600": "#1A6841"
    "700": "#155435"
    "800": "#10412A"
    "900": "#0B2E1E"
    "950": "#061A11"
  secondary:
    "50": "#FBF6E8"
    "100": "#F5E9C7"
    "200": "#EAD295"
    "300": "#DCBA63"
    "400": "#D0AE54"
    "500": "#CAA64A"
    "600": "#AC8A3A"
    "700": "#8B6E2E"
    "800": "#6B5424"
    "900": "#4D3C19"
    "950": "#2F250F"
  accent:
    "50": "#FCEAF1"
    "100": "#F7CDDD"
    "200": "#EC9BB9"
    "300": "#DD6691"
    "400": "#C24272"
    "500": "#9B2257"
    "600": "#841D4A"
    "700": "#6C183D"
    "800": "#541330"
    "900": "#3C0D23"
    "950": "#260816"
  neutral:
    "50": "#EDF1EC"
    "100": "#D2DBD0"
    "200": "#A8B8A6"
    "300": "#7E9279"
    "400": "#5B6F57"
    "500": "#3B5A3F"
    "600": "#314C35"
    "700": "#283D2B"
    "800": "#1F2A22"
    "900": "#161F18"
    "950": "#12180F"
  semantic:
    success: { bg: "#1F7A4D", text: "#E8F5EE", light: "#C8E8D6", border: "#155435" }
    warning: { bg: "#CAA64A", text: "#2F250F", light: "#F5E9C7", border: "#AC8A3A" }
    error: { bg: "#9B2257", text: "#FCEAF1", light: "#F7CDDD", border: "#6C183D" }
    info: { bg: "#2FA56A", text: "#061A11", light: "#C8E8D6", border: "#1A6841" }
  background:
    page: "#1F2A22"
    surface: "#283D2B"
    subtle: "#12180F"
  text:
    primary: "#EDF1EC"
    secondary: "#A8B8A6"
    muted: "#7E9279"
    inverse: "#12180F"

typography:
  families:
    heading: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    body: "'EB Garamond', 'Cormorant Garamond', Georgia, serif"
    mono: "'Spectral', 'EB Garamond', Georgia, serif"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Spectral:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap"
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
    md: "4px"
    lg: "8px"
    xl: "12px"
    full: "9999px"
  color:
    default: "#CAA64A"
    subtle: "rgba(202, 166, 74, 0.28)"
    strong: "#AC8A3A"
    focus: "#DCBA63"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(6, 26, 17, 0.30)"
  sm: "0 1px 4px rgba(6, 26, 17, 0.38)"
  md: "0 2px 8px rgba(6, 26, 17, 0.45)"
  lg: "0 4px 16px rgba(6, 26, 17, 0.50)"
  xl: "0 8px 24px rgba(6, 26, 17, 0.55)"
  "2xl": "0 12px 40px rgba(6, 26, 17, 0.62)"
  inner: "inset 0 1px 2px rgba(6, 26, 17, 0.40)"
  focus: "0 0 0 3px rgba(202, 166, 74, 0.45)"

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
  hoverPatterns: [glow, tint, lift]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "duotone"
  set: "phosphor"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#1F7A4D"
      color: "#EDF1EC"
      border: "1px solid #CAA64A"
      shadow: "0 2px 8px rgba(6, 26, 17, 0.45)"
      hoverBackground: "#1A6841"
      hoverShadow: "0 4px 16px rgba(6, 26, 17, 0.55)"
      hoverColor: "#FBF6E8"
    secondary:
      background: "transparent"
      color: "#CAA64A"
      border: "1px solid #CAA64A"
      shadow: "none"
      hoverBackground: "rgba(202, 166, 74, 0.12)"
      hoverShadow: "0 2px 8px rgba(6, 26, 17, 0.40)"
      hoverColor: "#DCBA63"
    ghost:
      background: "transparent"
      color: "#EDF1EC"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(202, 166, 74, 0.10)"
      hoverShadow: "none"
      hoverColor: "#CAA64A"
    danger:
      background: "#9B2257"
      color: "#FCEAF1"
      border: "1px solid #6C183D"
      shadow: "0 2px 8px rgba(38, 8, 22, 0.45)"
      hoverBackground: "#841D4A"
      hoverShadow: "0 4px 12px rgba(38, 8, 22, 0.55)"
      hoverColor: "#FCEAF1"
    sizes:
      sm: { height: "32px", padding: "0 12px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 28px", fontSize: "1.125rem" }
    borderRadius: "8px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#283D2B"
    color: "#EDF1EC"
    border: "1px solid rgba(202, 166, 74, 0.28)"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "#CAA64A"
    placeholderColor: "#7E9279"
  card:
    base:
      background: "#283D2B"
      border: "1px solid rgba(202, 166, 74, 0.28)"
      borderRadius: "12px"
      padding: "24px"
      shadow: "0 2px 8px rgba(6, 26, 17, 0.45)"
    hover:
      shadow: "0 8px 24px rgba(6, 26, 17, 0.55)"
      transform: "translateY(-2px)"
---

# Gould Hummingbird Plate

> Jewel-like Victorian ornithology: iridescent green plumage and gold-leaf gorgets glinting against shadowed dark-foliage grounds.

## Origin

John Gould's *A Monograph of the Trochilidae* (1861) stands as the high point of Victorian hand-finished bird lithography. Across 360 plates, Gould worked with the lithographer Henry Constantine Richter to draw the hummingbirds, while the firm of Hullmandel & Walton pulled the prints. The defining innovation was material rather than graphic: each gorget — the iridescent throat patch — was touched with actual gold leaf and then hand-coloured over, so the plate would catch the light and shift colour exactly as the living bird does. No flat ink could reproduce that optical metal; only leaf and glaze could.

The result is Western European natural-history luxury at its most jewel-like. Hummingbirds are set against shadowed dark-foliage vignettes — single or paired birds perched on engraved botanical stems, iridescent green plumage rendered over deep forest grounds, magenta gorgets glinting where the gold catches. The monograph belongs to a tradition of deluxe ornithological plate books made for wealthy subscribers, and its aesthetic vocabulary — specular highlights, framed plate margins, refined old-style serif captions — defines how Victorian science could also be ornament.

## Overview

Composition cues:
- **Layout**: Plate-style grid — single or paired focal subjects framed in dark vignettes, like specimen plates bound into a monograph, with generous shadowed margins around each unit
- **Content width**: Container width with framed plate margins; content floats on deep foliage ground rather than running edge to edge
- **Framing**: Bordered — thin gold-leaf hairline frames evoke the engraved plate margins surrounding every illustration
- **Grid intensity**: Soft — the grid is a quiet plate-mounting rhythm, never a hard modernist lattice; foliage shadow does the structural work

## Colors

The palette is keyed entirely to the living bird against its shadowed habitat. The signature is iridescent green (`#1F7A4D`) — most hummingbirds key on a shade of green — supported by a brighter structural green (`#2FA56A`) for the lit edges of plumage. Against this, the gorget supplies the drama: magenta (`#9B2257`) where the throat catches at an angle, and gold-leaf gorget highlight (`#CAA64A`) for the specular metal glint that gave the originals their value. Everything sits on shadowed dark-foliage grounds — a vignette green (`#1F2A22`) deepening to the darkest shadow (`#12180F`) — with mid-foliage green (`#3B5A3F`) carrying the neutral structural tones. The register is deep, jewel-toned, and Victorian: never neon, never candy, never washed-out.

**Role usage**:
- Page background → `colors.background.page` (shadowed foliage ground `#1F2A22`, never cream)
- Content surface → `colors.background.surface` (lifted foliage `#283D2B`, the mounted plate)
- Deepest shadow / recesses → `colors.background.subtle` (`#12180F`)
- Primary plumage / primary actions → `colors.primary.500` (iridescent green `#1F7A4D`)
- Gold-leaf gorget highlight / borders → `colors.secondary.500` (gold `#CAA64A`)
- Magenta gorget accent → `colors.accent.500` (`#9B2257`)
- Mid-foliage structure / neutrals → `colors.neutral.500` (`#3B5A3F`)
- Body text on foliage ground → `colors.text.primary` (pale leaf `#EDF1EC`)

## Typography

The type voice is the refined old-style serif of a deluxe Victorian plate book, where every caption was set with the same care as the illustration. **Cormorant Garamond** carries display and headlines — a high-contrast Garamond revival with the elegant thin strokes of nineteenth-century book typography. **EB Garamond** handles body text, a faithful old-style serif sized for long-form reading. **Spectral** serves captions and the monospace role, a serif designed for screen with the steady rhythm of a specimen label beneath a plate. No modern sans chrome is permitted to compete with the old-style serif plate captions.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 600, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Cormorant Garamond, 64px, weight 600, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Cormorant Garamond, 48px, weight 500, line-height 1.2, letter-spacing 0
- `body-lg` — EB Garamond, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — EB Garamond, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Spectral, 14px, weight 400, line-height 1.375, letter-spacing 0.05em, italic
- `mono-md` — Spectral, 16px, weight 400, line-height 1.8, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Section padding: 64px vertical (md), 96px (lg) — generous shadowed margins frame each plate
- Grid gaps: 16px (md) to 24px (lg) — enough breathing room that each subject reads as a mounted plate

## Elevation & Depth

Depth comes from the vignette itself — subjects emerge from shadowed foliage rather than casting hard drop-shadows. Surfaces stack as mounted plates lifted slightly off the deepest ground, and the only true highlight is the specular gold glint of the gorget. Shadows are deep forest-dark, never neutral gray, so every recess carries the ambient green of the foliage ground.

- Surface style: layered (plates mounted over deep foliage ground)
- Blur: none (lithographic plates are crisply rendered, no atmospheric blur)
- Shadow ladder: deep-shadow rgba — xs through 2xl use `rgba(6, 26, 17, ...)` at ascending opacity, reading as forest shadow rather than gray
- Inner shadow: subtle dark inset for recessed input fields
- Focus ring: 3px gold-leaf glow at 45% opacity

## Shapes

- `none`: 0 — engraved plate edges and rules
- `sm`: 2px — tags, small UI elements (plate-margin sharpness)
- `md`: 4px — inputs, minor containers
- `lg`: 8px — buttons (restrained, befitting framed plates)
- `xl`: 12px — cards, mounted-plate containers
- `full`: 9999px — circular medallions, avatar frames

## Motion

Motion is restrained and deliberate, like turning the heavy leaves of a folio monograph. The most characteristic gesture is the iridescent shift — a slow tint from green toward magenta on hover, echoing how the gorget changes colour as the viewing angle moves. No bouncing, no playful effects; transitions feel like light catching gold leaf and sliding off.

- Level: restrained
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)` — smooth and considered
- Hover patterns: glow (gold-leaf luminance), tint (green-to-magenta iridescent shift), lift (plate raised off ground)
- `reducedMotion: true` — all animations respect `prefers-reduced-motion`

## Techniques

### Iridescent gorget shift
A green-to-magenta gradient with a gold specular highlight, simulating the angle-dependent colour shift of a hand-finished hummingbird gorget. Use on hero accents, badges, and featured cards.
```css
.element {
  background: linear-gradient(
    115deg,
    #1F7A4D 0%,
    #2FA56A 28%,
    #9B2257 72%,
    #C24272 100%
  );
  background-size: 200% 200%;
  position: relative;
  transition: background-position 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
.element:hover {
  background-position: 100% 0;
}
.element::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at 30% 25%,
    rgba(202, 166, 74, 0.55) 0%,
    transparent 45%
  );
  mix-blend-mode: screen;
  pointer-events: none;
}
```

### Gold-leaf plate frame
A thin gold hairline border with an offset rule, evoking the engraved plate margin and gold-leaf trim around every Gould illustration.
```css
.element {
  border: 1px solid #CAA64A;
  outline: 1px solid rgba(202, 166, 74, 0.28);
  outline-offset: 4px;
  background: #283D2B;
  box-shadow: 0 2px 8px rgba(6, 26, 17, 0.45),
              inset 0 0 0 1px rgba(220, 186, 99, 0.15);
}
```

### Dark-foliage vignette ground
The shadowed habitat backdrop: a deep foliage green radiating to near-black at the edges, so the subject is lit at center and swallowed by shadow at the margins.
```css
.element {
  background:
    radial-gradient(
      ellipse 80% 70% at 50% 42%,
      #2A3A2E 0%,
      #1F2A22 45%,
      #12180F 100%
    );
  color: #EDF1EC;
}
```

## Iconography

Icons should feel like engraved natural-history marks rather than utilitarian glyphs, drawing on the vocabulary of the plate book: botanical perches, leaf sprays, feather barbs, and the long curved bill of the hummingbird. Where functional icons are needed, use Phosphor duotone at 1.5px stroke — the duotone treatment allows a gold-leaf accent fill (`#CAA64A`) layered over an iridescent-green base, mimicking the gold-on-pigment finishing of the originals.

- Treatment: duotone (gold-leaf accent layer over green base)
- Set: Phosphor
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use shadowed foliage green `#1F2A22` as the page ground — it is the dark vignette habitat, never cream
- Reserve iridescent green `#1F7A4D` for the primary plumage and primary actions — it is the signature
- Apply the green-to-magenta gorget shift with a gold-leaf highlight for hero accents and featured surfaces
- Frame cards and panels with thin gold-leaf hairlines (`#CAA64A`) to evoke engraved plate margins
- Set all display and caption text in old-style serifs — Cormorant Garamond, EB Garamond, Spectral

### ✗ Don't
- Use cream, ivory, or plain-white backgrounds — grounds are dark, shadowed foliage
- Use flat green fills for gorgets — they need the iridescent green-to-magenta shift and a gold highlight
- Reach for a neon or candy palette — keep the deep, jewel-toned Victorian register
- Introduce modern sans-serif chrome that competes with the old-style serif plate captions
- Render shadows as neutral gray — use deep forest-dark `rgba(6, 26, 17, …)` so recesses carry the foliage tone

## Applications

This system is ideal for natural-history museum catalogues, rare-book and archive microsites, premium botanical or ornithological storytelling, and luxury heritage brand pages where craft provenance matters. It excels wherever a deep, jewel-toned ground and gold-leaf detailing lend authority and richness — exhibition companions, collector portfolios, illustrated science editorial, and high-end conservation or wildlife campaigns. The iridescent gorget accent gives a single, memorable signature gesture for hero moments and calls to action.
