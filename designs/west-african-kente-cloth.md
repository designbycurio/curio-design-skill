---
version: 1

meta:
  id: west-african-kente-cloth
  name: "West African Kente Cloth"
  description: "Gold, crimson, jade, and purple loom strips woven on deep coffee-brown ground — ceremonial textile geometry as interface language"
  isDark: true
  tags: [decorative, bold, narrative, historical, organic]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "17th century origin; modern ceremonial peak; diaspora reinterpretation since 1960s"
  region: "Asante kingdom (Bonwire, Ghana) and Ewe people of Togo"
  regionZh: "加纳阿散蒂王国（邦维雷村）及多哥埃维族地区"
  keyFigures: [Asantehene Osei Tutu, Bonwire master weavers, Christie Brown, Studio 189]
  movements: [Asante royal textile tradition, Adinkra symbol system, African diaspora identity revival]

introduction: |
  Kente cloth is the most semiotically loaded woven textile tradition in West Africa — every color is a proverb, every strip a name. Originally reserved for Asante royalty, kente's narrow loom strips lock together in mirror-symmetric repeats of gold, crimson, jade, and purple on a deep coffee-brown ground.

  This design system translates kente's rectilinear geometry and royal palette into digital interfaces: vertical strip panels, weft accent lines, and Adinkra symbol ornaments replace generic cards and icons, creating surfaces that feel woven rather than rendered.
introductionZh: |
  肯特布是西非最具符号意义的织物传统——每一种颜色都是一句谚语，每一条织带都有名字。这种源自加纳阿散蒂王国的皇家织物，以金、朱红、翡翠绿和紫色在深咖啡色底布上编织出镜像对称的几何图案。

  本设计系统将肯特布的直线几何与皇家配色转化为数字界面语言：垂直条带面板、纬线装饰线与阿丁克拉符号取代通用卡片和图标，让界面呈现织物般的质感与仪式感。

colors:
  primary:
    "50": "#fdf8eb"
    "100": "#f9ebc3"
    "200": "#f5de9b"
    "300": "#f1d173"
    "400": "#edc44e"
    "500": "#EAB308"
    "600": "#c89807"
    "700": "#a67e06"
    "800": "#846405"
    "900": "#624a04"
    "950": "#3e2f02"
  secondary:
    "50": "#e8faf4"
    "100": "#bbf0dd"
    "200": "#8ee6c6"
    "300": "#61dcaf"
    "400": "#38d29b"
    "500": "#10B981"
    "600": "#0e9e6e"
    "700": "#0b835b"
    "800": "#096848"
    "900": "#074d35"
    "950": "#043222"
  accent:
    "50": "#f7e8e8"
    "100": "#e8bbbb"
    "200": "#d98e8e"
    "300": "#ca6161"
    "400": "#b43e3e"
    "500": "#991B1B"
    "600": "#831717"
    "700": "#6d1313"
    "800": "#570f0f"
    "900": "#410b0b"
    "950": "#2b0808"
  neutral:
    "50": "#f5e8c9"
    "100": "#e8d4a8"
    "200": "#d4bb88"
    "300": "#bfa068"
    "400": "#a38550"
    "500": "#876a3a"
    "600": "#6b5430"
    "700": "#503f24"
    "800": "#3D1F0F"
    "900": "#1F0F0A"
    "950": "#100806"
  semantic:
    success:
      bg: "#10B981"
      text: "#1F0F0A"
      light: "#0b835b"
      border: "#10B981"
    warning:
      bg: "#EAB308"
      text: "#1F0F0A"
      light: "#a67e06"
      border: "#EAB308"
    error:
      bg: "#991B1B"
      text: "#F5E8C9"
      light: "#6d1313"
      border: "#991B1B"
    info:
      bg: "#1E40AF"
      text: "#F5E8C9"
      light: "#162f80"
      border: "#1E40AF"
  background:
    page: "#3D1F0F"
    surface: "#1F0F0A"
    subtle: "#4D2A16"
  text:
    primary: "#F5E8C9"
    secondary: "#D4BB88"
    muted: "#A38550"
    inverse: "#1F0F0A"

typography:
  families:
    heading: "'Sora', 'Futura', sans-serif"
    body: "'Public Sans', 'Spartan', sans-serif"
    mono: "'IBM Plex Mono', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Anton&family=IBM+Plex+Mono:wght@400;500&display=swap"
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
    lg: "6px"
    xl: "8px"
    full: "9999px"
  color:
    default: "#EAB308"
    subtle: "#503f24"
    strong: "#F5E8C9"
    focus: "#EAB308"
  width:
    thin: "1px"
    default: "2px"
    thick: "3px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(31,15,10,0.15)"
  sm: "0 1px 3px rgba(31,15,10,0.20)"
  md: "0 4px 6px rgba(31,15,10,0.18)"
  lg: "0 10px 15px rgba(31,15,10,0.16)"
  xl: "0 20px 25px rgba(31,15,10,0.20)"
  "2xl": "0 25px 50px rgba(31,15,10,0.28)"
  inner: "inset 0 1px 2px rgba(31,15,10,0.10)"
  focus: "0 0 0 3px rgba(234,179,8,0.35)"

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
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [tint, opacity, stroke]
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
  treatment: "linear"
  set: "custom"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "2px"

components:
  button:
    primary:
      background: "#EAB308"
      color: "#1F0F0A"
      border: "2px solid #EAB308"
      shadow: "none"
      hoverBackground: "#c89807"
      hoverShadow: "none"
      hoverColor: "#1F0F0A"
    secondary:
      background: "#10B981"
      color: "#1F0F0A"
      border: "2px solid #10B981"
      shadow: "none"
      hoverBackground: "#0e9e6e"
      hoverShadow: "none"
      hoverColor: "#1F0F0A"
    ghost:
      background: "transparent"
      color: "#EAB308"
      border: "2px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(234,179,8,0.10)"
      hoverShadow: "none"
      hoverColor: "#f1d173"
    danger:
      background: "#991B1B"
      color: "#F5E8C9"
      border: "2px solid #991B1B"
      shadow: "none"
      hoverBackground: "#6d1313"
      hoverShadow: "none"
      hoverColor: "#F5E8C9"
    sizes:
      sm:
        height: "32px"
        padding: "0 12px"
        fontSize: "0.875rem"
      md:
        height: "40px"
        padding: "0 16px"
        fontSize: "1rem"
      lg:
        height: "48px"
        padding: "0 24px"
        fontSize: "1.125rem"
    borderRadius: "4px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "transparent"
    color: "#F5E8C9"
    border: "2px solid #503f24"
    borderRadius: "4px"
    padding: "8px 12px"
    focusBorder: "#EAB308"
    placeholderColor: "#A38550"
  card:
    base:
      background: "#1F0F0A"
      border: "2px solid #503f24"
      borderRadius: "4px"
      padding: "24px"
      shadow: "none"
    hover:
      shadow: "0 4px 6px rgba(31,15,10,0.18)"
      transform: "translateY(-1px)"
---

# West African Kente Cloth

> Gold, crimson, jade, and purple loom strips woven on deep coffee-brown — ceremonial textile geometry as digital interface.

## Origin

Kente cloth originates from the Asante kingdom of modern-day Ghana, with Bonwire village as its most celebrated weaving center. Legend credits the Asantehene Osei Tutu with commissioning the first royal kente cloths in the early 18th century. Each cloth is woven on a narrow horizontal loom — strips roughly four inches wide — then sewn edge-to-edge into a full garment. Every pattern carries a name and a proverb: "Adwene asa" ("ideas are finished") declares the weaver's exhaustive creativity; "Sika fre mogya" ("gold calls blood") speaks to the bond between wealth and kinship.

The Ewe people of Togo developed a parallel kente tradition with finer weft patterning and figural motifs. In the 1960s, kente crossed the Atlantic as a symbol of Pan-African identity — adopted by the Black Power movement, woven into Kwanzaa celebrations, and draped across HBCU graduation stages. Contemporary Ghanaian designers like Christie Brown and Studio 189 have reimagined kente geometry for global fashion, proving the tradition's visual grammar is as legible on a runway as it is on a chief's shoulder.

## Overview

Composition cues:
- **Layout**: Grid-based, echoing the vertical loom-strip structure — narrow columns side by side
- **Content width**: Container-bound, reflecting the finite width of a kente cloth panel
- **Framing**: Bordered with 2px solid edges, evoking strip-edge joins and weft boundaries
- **Grid intensity**: Strong — dense vertical rhythm with visible column gutters, like strips on a loom

## Colors

Kente colors are never decorative — they are semantic. Gold signifies royalty and wealth; crimson speaks of blood and strength; jade green represents vegetation and growth; royal blue embodies harmony and peace; ink purple denotes wealth accumulated through trade. The deep coffee-brown ground (`#3D1F0F`) is the color of undyed cotton dipped in the first dye-bath, the starting point from which every strip is woven. Bone white (`#F5E8C9`) represents divine purity and appears as the primary text color against the dark ground.

**Role usage**:
- Page background → `colors.background.page` (coffee brown `#3D1F0F`)
- Card / panel surface → `colors.background.surface` (deeper brown `#1F0F0A`)
- Primary accent / royalty → `colors.primary.500` (gold `#EAB308`)
- Growth / confirmation → `colors.secondary.500` (jade `#10B981`)
- Strength / warning → `colors.accent.500` (crimson `#991B1B`)
- Body text → `colors.text.primary` (bone white `#F5E8C9`)
- Muted text → `colors.text.muted` (warm sand `#A38550`)
- Info / harmony → semantic info (royal blue `#1E40AF`)

## Typography

The type voice is geometric and upright — kente's rectilinear weave demands letterforms built from clear angles, not calligraphic flourish. Sora provides the heading face: a geometric sans-serif with a slightly humanist touch that pairs naturally with West African geometric pattern work. Anton serves as the condensed display face for ceremonial titles and hero text — tall, narrow, and commanding like a vertical loom strip. Public Sans handles body text with neutral clarity that lets the color palette and geometry do the talking. IBM Plex Mono provides the technical voice. Letter-spacing runs wider on display text, echoing the deliberate spacing between weft pattern repeats.

**Text styles**:
- `display-xl` — Anton, 96px, weight 400, line-height 1.0, letter-spacing 0.05em
- `display-lg` — Anton, 72px, weight 400, line-height 1.05, letter-spacing 0.05em
- `heading-1` — Sora, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Public Sans, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Public Sans, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Public Sans, 12px, weight 500, line-height 1.5, letter-spacing 0.05em
- `mono-md` — IBM Plex Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px (half a weave thread)
- Scale: 2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128px
- Container max-widths: 640 · 768 · 1024 · 1280px
- Grid gap: 8px (sm) → 16px (md) → 24px (lg) → 48px (xl) — tighter gutters at small sizes echo the close join of loom strips
- Section padding: 32px (sm) → 64px (md) → 96px (lg) → 128px (xl)

## Elevation & Depth

Kente is a flat textile — thread on thread, no glossy finish. Surfaces are layered by color difference, not by shadow. The deeper brown `#1F0F0A` lifts a card panel above the page ground `#3D1F0F` through value contrast alone. Shadows are minimal and warm-toned (`rgba(31,15,10,...)`) for the rare cases where interactive states need depth feedback. The focus ring glows gold (`rgba(234,179,8,0.35)`) — a thread of royal gold pulled taut around the active element.

- Surfaces separate by color value, not shadow
- Shadow ladder: none → xs → sm → md → lg → xl → 2xl (all warm brown alpha)
- Focus ring: 3px gold glow
- Inner shadow: subtle inset for pressed states

## Shapes

- Corner radii: 0–4px throughout (loom geometry is rectilinear)
- Buttons: 4px radius
- Cards: 4px radius
- Inputs: 4px radius
- Pills/tags: 4px radius (not full-round — kente has no curves)
- No rounded corners beyond 8px; full-round (`9999px`) reserved only for avatar circles

## Motion

Motion is restrained and deliberate — a weaver's hand moves with intention, never with flourish. Transitions honor the rhythm of the loom: steady, measured, and purposeful. Hover states shift color tint rather than adding spatial effects, keeping the surface flat as cloth on a frame.

- Level: restrained
- Durations: instant 0ms · fast 120ms · normal 250ms · slow 400ms · slower 600ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)` (ease-out dominant)
- Spring easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` (reserved for toggle snaps)
- Hover patterns: tint shift (gold warmth), opacity fade, border stroke reveal
- `prefers-reduced-motion` respected

## Techniques

### Kente strip panel

Vertical loom-strip panels — narrow colored columns side by side with a 2px weft accent line running horizontally across, evoking the structure of woven kente cloth.

```css
.kente-strip-panel {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0;
  position: relative;
}
.kente-strip-panel > * {
  border-left: 2px solid var(--color-neutral-700);
  padding: 24px 16px;
}
.kente-strip-panel > *:first-child {
  border-left: none;
}
.kente-strip-panel::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 2px;
  background: repeating-linear-gradient(
    90deg,
    var(--color-primary-500) 0 12px,
    var(--color-accent-500) 12px 24px,
    var(--color-secondary-500) 24px 36px
  );
}
```

### Weft thread border

A repeating color-segment border that simulates the alternating weft threads of a kente loom — gold, crimson, jade, purple segments cycling along the edge.

```css
.weft-border {
  border: 2px solid transparent;
  border-image: repeating-linear-gradient(
    90deg,
    #EAB308 0 16px,
    #991B1B 16px 32px,
    #10B981 32px 48px,
    #7C3AED 48px 64px
  ) 2;
}
```

### Adinkra symbol accent

Decorative Adinkra-symbol-inspired SVG used as section dividers or card ornaments — rendered in royal gold on the coffee ground, keeping geometry abstract to respect cultural context.

```css
.adinkra-accent {
  display: flex;
  align-items: center;
  gap: 16px;
  color: #EAB308;
  opacity: 0.6;
}
.adinkra-accent::before,
.adinkra-accent::after {
  content: '';
  flex: 1;
  height: 2px;
  background: currentColor;
}
.adinkra-accent svg {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2px;
}
```

## Iconography

Icons follow the linear treatment with a 2px stroke — thicker than typical UI icon sets to match kente's bold 2px border language. The icon set is custom: Adinkra symbols (Gye Nyame for supremacy, Sankofa for reflection, Dwennimmen for strength) serve as decorative accents, while functional icons use geometric linear forms consistent with the rectilinear textile aesthetic.

- Treatment: linear, 2px stroke
- Set: custom (Adinkra symbols for decorative; geometric linear for functional)
- Sizes: 16px (sm) · 20px (md) · 24px (lg)

## Do's & Don'ts

### ✓ Do
- Use royal gold `#EAB308` for primary actions and emphasis — it is the color of the Asantehene
- Build layouts with vertical strip columns (narrow grid columns side by side)
- Apply the weft-thread repeating border for section dividers and card edges
- Keep corners rectilinear (0–4px radius) — kente is woven on a right-angle loom
- Use dense, full compositions — kente cloth has no empty ground

### ✗ Don't
- Use curves or large border-radius — kente geometry is strictly rectilinear
- Choose Inter, Geist, or cool-toned sans-serifs — use Sora/Futura geometric faces
- Apply pastel or desaturated colors — kente demands fully saturated royal hues
- Use cream or white page backgrounds — the coffee-brown `#3D1F0F` ground is essential
- Apply SaaS-style gradients or glassmorphism — kente is flat textile, not glossy surface
- Introduce modernist minimalism or excessive whitespace — kente is densely woven, emptiness is wrong
- Use specific named kente patterns without attribution context — keep geometry abstracted

## Applications

This system is ideal for cultural heritage platforms, Pan-African brand identities, HBCU event sites, Afrocentric e-commerce, museum exhibition microsites, and any project celebrating West African craft traditions. The dense geometric grid and bold saturated palette work especially well for editorial layouts, event landing pages, and community platforms where visual richness and cultural depth are assets rather than distractions.
