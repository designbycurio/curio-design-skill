---
version: 1

meta:
  id: maori-koru-aotearoa
  name: "Māori Koru (Aotearoa)"
  description: "Dark paua-shell depths with koru spirals, kowhaiwhai scroll borders, and kokowai crimson — a Polynesian design language from Aotearoa"
  isDark: true
  tags: [organic, decorative, historical, bold, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "pre-1769 to present; contemporary revival from 1970s onwards"
  region: "Aotearoa / New Zealand"
  regionZh: "新西兰（奥特亚罗瓦）"
  keyFigures: [Cliff Whiting, Robyn Kahukiwa, Shane Cotton, Lisa Reihana]
  movements: [Māori traditional art (toi Māori), kowhaiwhai rafter painting, tukutuku weaving, contemporary Māori art]

introduction: |
  Māori visual culture is a Polynesian design language built on the koru spiral, woven raranga patterns, and carved meeting-house interiors. The koru — the unfurling silver fern frond — represents new life, growth, and harmony, spiralling outward from ancestral memory into living form.

  This system translates those forms into a dark, immersive digital palette: deep paua-shell purple-blue grounds, pitch-black koru line work, kokowai crimson accents, and silver iridescence that shifts like abalone shell. Every spiral remembers the ancestor it came from.

introductionZh: |
  毛利视觉文化是一套来自奥特亚罗瓦（新西兰）的波利尼西亚设计语言，以银蕨嫩芽卷曲的「科鲁」螺旋为核心图腾，融合了考怀怀楣梁彩绘与图库图库编织板的纹理体系。科鲁象征新生、成长与和谐——每一道螺旋都承载着祖先的记忆。

  这套设计系统将毛利会堂（法雷努伊）的内部空间转译为数字界面：以�的深蓝紫�的鲍鱼壳色为基底，漆黑螺旋线条勾勒轮廓，赭红大地颜料点燃重点，银色珍珠光泽如潮水般流转。

colors:
  primary:
    "50": "#F7E8E6"
    "100": "#EDCCC8"
    "200": "#DB9A91"
    "300": "#C9685A"
    "400": "#B74A3C"
    "500": "#8B2A1F"
    "600": "#76231A"
    "700": "#5E1C14"
    "800": "#46150F"
    "900": "#2E0E0A"
    "950": "#170705"
  secondary:
    "50": "#EEF2EB"
    "100": "#DCE4D6"
    "200": "#BACAAD"
    "300": "#97AF84"
    "400": "#79926A"
    "500": "#5B6F4A"
    "600": "#4D5E3F"
    "700": "#3E4C32"
    "800": "#2F3926"
    "900": "#202719"
    "950": "#10130D"
  accent:
    "50": "#F5F5F5"
    "100": "#ECECEC"
    "200": "#D8D8D8"
    "300": "#C0C0C0"
    "400": "#B0B0B0"
    "500": "#C0C0C0"
    "600": "#909090"
    "700": "#707070"
    "800": "#505050"
    "900": "#303030"
    "950": "#181818"
  neutral:
    "50": "#F5EFDF"
    "100": "#E8DFC8"
    "200": "#D0C5A8"
    "300": "#B8AB88"
    "400": "#A89E8A"
    "500": "#8A8070"
    "600": "#6C6458"
    "700": "#4E4840"
    "800": "#302C28"
    "900": "#1A1714"
    "950": "#0D0B0A"
  semantic:
    success: { bg: "#5B6F4A", text: "#F5EFDF", light: "#3E4C32", border: "#79926A" }
    warning: { bg: "#B8860B", text: "#F5EFDF", light: "#8B6508", border: "#DAA520" }
    error:   { bg: "#8B2A1F", text: "#F5EFDF", light: "#5E1C14", border: "#C9685A" }
    info:    { bg: "#2A1A4A", text: "#F5EFDF", light: "#1F1438", border: "#6B4FA0" }
  background:
    page:    "#2A1A4A"
    surface: "#1F1438"
    subtle:  "#0A0A0A"
  text:
    primary:   "#F5EFDF"
    secondary: "#D0C5A8"
    muted:     "#A89E8A"
    inverse:   "#0A0A0A"

typography:
  families:
    heading: "'Cinzel', 'Trajan Pro', Georgia, serif"
    body:    "'Spartan', 'League Spartan', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=League+Spartan:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap"
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
  weights: { light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800 }
  lineHeights: { tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px", md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "2px", md: "4px", lg: "8px", xl: "12px", full: "9999px" }
  color:  { default: "#3D2A66", subtle: "#2E1F50", strong: "#C0C0C0", focus: "#8B2A1F" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(10, 10, 10, 0.3)"
  sm: "0 2px 4px rgba(42, 26, 74, 0.4)"
  md: "0 4px 16px rgba(42, 26, 74, 0.6)"
  lg: "0 8px 32px rgba(42, 26, 74, 0.7)"
  xl: "0 16px 48px rgba(10, 10, 10, 0.6)"
  "2xl": "0 24px 64px rgba(10, 10, 10, 0.8)"
  inner: "inset 0 1px 2px rgba(10, 10, 10, 0.3)"
  focus: "0 0 0 3px rgba(139, 42, 31, 0.5)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [glow, opacity, tint]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "subtle"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "8px"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "#8B2A1F"
      color: "#F5EFDF"
      border: "1px solid #8B2A1F"
      shadow: "0 2px 4px rgba(42, 26, 74, 0.4)"
      hoverBackground: "#76231A"
      hoverShadow: "0 4px 16px rgba(139, 42, 31, 0.5)"
      hoverColor: "#F5EFDF"
    secondary:
      background: "#1F1438"
      color: "#F5EFDF"
      border: "1px solid #3D2A66"
      shadow: "none"
      hoverBackground: "#2A1A4A"
      hoverShadow: "0 2px 4px rgba(42, 26, 74, 0.4)"
      hoverColor: "#F5EFDF"
    ghost:
      background: "transparent"
      color: "#C0C0C0"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(192, 192, 192, 0.08)"
      hoverShadow: "none"
      hoverColor: "#F5EFDF"
    danger:
      background: "#8B2A1F"
      color: "#F5EFDF"
      border: "1px solid #5E1C14"
      shadow: "0 2px 4px rgba(139, 42, 31, 0.4)"
      hoverBackground: "#5E1C14"
      hoverShadow: "0 4px 16px rgba(139, 42, 31, 0.5)"
      hoverColor: "#F5EFDF"
    sizes:
      sm: { height: "32px", padding: "0 12px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 28px", fontSize: "1.125rem" }
    borderRadius: "4px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#1F1438"
    color: "#F5EFDF"
    border: "1px solid #3D2A66"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "#8B2A1F"
    placeholderColor: "#A89E8A"
  card:
    base:
      background: "#1F1438"
      border: "1px solid #3D2A66"
      borderRadius: "8px"
      padding: "24px"
      shadow: "0 4px 16px rgba(42, 26, 74, 0.6)"
    hover:
      shadow: "0 8px 32px rgba(42, 26, 74, 0.7)"
      transform: "translateY(-2px)"
---

# Māori Koru (Aotearoa)

> A dark Polynesian design language built on koru spirals, paua-shell iridescence, and kokowai crimson — every spiral remembers the ancestor it came from.

## Origin

Māori visual art forms one of the most coherent design systems in the Pacific — a vocabulary forged over centuries in Aotearoa (New Zealand) from the koru spiral (the unfurling silver fern frond), kowhaiwhai painted rafter patterns, tukutuku woven wall panels, and tā moko (tattoo) line work. Before European contact in 1769 and continuing through a powerful cultural revival from the 1970s onwards, these motifs encoded genealogy, narrative, and cosmology into physical space. The carved meeting house (wharenui) is the ultimate expression: an ancestor's body rendered in wood, its interior dark, spiralling, alive with meaning.

In the contemporary era, artists like Cliff Whiting, Robyn Kahukiwa, Shane Cotton, and Lisa Reihana have translated these ancestral forms into modernist murals, digital panoramas, and institutional identities — most iconically the Air New Zealand koru logo (1973) and Te Papa Tongarewa museum's visual language. The landmark *Te Maori* exhibition (1984) brought Māori art to international attention, revealing it not as ethnographic artefact but as a living, evolving design tradition that speaks in spirals.

## Overview

Composition cues:
- **Layout**: Stack-based vertical compositions echoing the carved pou (posts) of a wharenui — content flows downward through layered panels, not across horizontal grids
- **Content width**: Container width (1024–1280px), with generous section padding creating the reverent interior spacing of a meeting house
- **Framing**: Bordered panels with curvilinear koru ornament at edges — sharp rectangular content framed by organic spiral decoration
- **Grid intensity**: Subtle — tukutuku weaving provides implicit background rhythm, but content sits in stacked blocks rather than rigid columns

## Colors

The palette draws from the interior of a Māori meeting house: deep paua-shell blue-purple grounds like the inside of an abalone shell, pitch-black koru spirals carved into space, kokowai (red ochre earth pigment) crimson for ceremonial emphasis, silver iridescence that shimmers like paua shell catching light, and fern green from the native bush. Bone white appears only as text on dark surfaces, never as background — this is a night-sky, cave-interior, carved-wood palette.

**Role usage**:
- Page background → `colors.background.page` (paua deep blue-purple `#2A1A4A`)
- Card / surface background → `colors.background.surface` (deeper paua `#1F1438`)
- Alternate dark panels → `colors.background.subtle` (pitch black `#0A0A0A`)
- Primary actions, crimson accents → `colors.primary.500` (kokowai `#8B2A1F`)
- Nature / growth contexts → `colors.secondary.500` (fern green `#5B6F4A`)
- Silver highlights, iridescent borders → `colors.accent.500` (`#C0C0C0`)
- Body text on dark → `colors.text.primary` (bone white `#F5EFDF`)
- Muted captions → `colors.text.muted` (`#A89E8A`)

## Typography

The type voice is monumental and carved — Cinzel's geometric serifs echo the chisel marks of tohunga whakairo (master carvers) cutting into totara and kauri wood. Headlines are uppercase, widely tracked, carrying the gravity of ancestral names inscribed on meeting house lintels. Body text in League Spartan is clean and geometric, a modern sans that doesn't compete with the ornamental weight of the heading face but maintains the bold, structured clarity of Māori design.

**Text styles**:
- `display-xl` — Cinzel, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Cinzel, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Cinzel, 48px, weight 700, line-height 1.2, letter-spacing 0
- `body-lg` — League Spartan, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — League Spartan, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — League Spartan, 12px, weight 500, line-height 1.5, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px rhythm (matching the precision of tukutuku grid weaving)
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px with auto margins
- Section padding: 64–96px vertical, creating the spacious interior feeling of a wharenui
- Grid gap: 16–24px between stacked panels, with 48px between major sections

## Elevation & Depth

Surfaces are layered like the carved and painted panels of a meeting house interior — the deepest layer is pitch black (`#0A0A0A`), mid-ground is dark paua (`#1F1438`), and the main surface is deep blue-purple (`#2A1A4A`). Shadows cast in the paua colour family, creating depth that feels like looking into the iridescent interior of an abalone shell rather than generic drop shadows.

- Surface style: layered dark panels on darker grounds
- Blur: 8px for subtle glass effects on elevated surfaces
- Shadow ladder: xs (subtle floor contact) → sm (resting card) → md (paua glow, `0 4px 16px rgba(42,26,74,0.6)`) → lg (lifted panel) → xl (modal overlay) → 2xl (dramatic hero)
- Inner shadow for recessed fields (input wells, carved-in panels)

## Shapes

- No radius (`none: 0`): reserved for divider lines and full-bleed panels
- Small radius (`sm: 2px`): subtle softening on inline elements
- Medium radius (`md: 4px`): buttons, inputs, small interactive elements — rectilinear like carved wood
- Large radius (`lg: 8px`): cards, panels — the sharpest-cornered card system
- Extra large (`xl: 12px`): modals, hero containers
- Full (`9999px`): avatar circles, badges only
- **No large rounded corners** — Māori carving tradition uses sharp rectilinear frames with curvilinear ornament applied on top, not baked into the shape itself

## Motion

Motion is restrained and deliberate — like the slow unfurling of a koru frond or the measured gestures of a haka. Nothing bounces or wiggles. Transitions are smooth and purposeful, with elements emerging into view rather than snapping. Hover states use a subtle paua-shell glow rather than spatial movement.

- Level: restrained
- Fast interactions: 120ms (button press, toggle)
- Normal transitions: 250ms (panel reveal, card hover)
- Slow ceremonies: 400ms (page transitions, hero reveals)
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)` — smooth deceleration
- Hover patterns: glow (paua iridescent shimmer), opacity (fade-in reveals), tint (kokowai warmth on hover)
- `prefers-reduced-motion`: respected, all animations collapse to instant

## Techniques

### Paua-shell iridescent border
A CSS gradient border that mimics the colour-shifting surface of New Zealand paua (abalone) shell, cycling through the deep purple, fern green, and silver of the palette.
```css
.element {
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
}
.element::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  background: linear-gradient(135deg, #2A1A4A, #5B6F4A, #C0C0C0, #2A1A4A);
  z-index: -1;
}
```

### Koru spiral accent
A CSS-drawn koru spiral used as a decorative corner accent on hero sections and feature panels — the unfurling fern frond rendered in kokowai crimson.
```css
.element::after {
  content: '';
  position: absolute;
  bottom: -24px;
  right: -24px;
  width: 96px;
  height: 96px;
  border: 3px solid #8B2A1F;
  border-radius: 0 0 50% 0;
  border-top: none;
  border-left: none;
  opacity: 0.6;
}
```

### Tukutuku grid weave background
A repeating CSS pattern inspired by tukutuku woven wall panels, creating a subtle diamond-lattice texture on dark surfaces.
```css
.element {
  background-color: #1F1438;
  background-image:
    linear-gradient(45deg, rgba(192, 192, 192, 0.04) 25%, transparent 25%),
    linear-gradient(-45deg, rgba(192, 192, 192, 0.04) 25%, transparent 25%),
    linear-gradient(45deg, transparent 75%, rgba(192, 192, 192, 0.04) 75%),
    linear-gradient(-45deg, transparent 75%, rgba(192, 192, 192, 0.04) 75%);
  background-size: 24px 24px;
  background-position: 0 0, 0 12px, 12px -12px, -12px 0;
}
```

## Iconography

Icons follow the linear treatment — clean strokes at 1.5px weight that echo the incised lines of tā moko and kowhaiwhai without appropriating sacred imagery. The Lucide set provides the geometric clarity needed, with icons rendered in silver (`#C0C0C0`) on dark grounds or bone white (`#F5EFDF`) for high-emphasis contexts.

- Treatment: linear (stroke-only, matching carved line traditions)
- Set: Lucide
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use paua deep blue-purple (`#2A1A4A`) as the dominant page ground — every screen should feel like stepping inside a wharenui
- Apply kokowai crimson (`#8B2A1F`) for primary actions and ceremonial emphasis only — it is a sacred pigment, use it sparingly
- Frame rectangular content panels with curvilinear koru ornament at corners and borders
- Use uppercase Cinzel headings with wide tracking for monumental, carved-stone authority
- Layer surfaces from pitch black through deep paua to create carved-depth spatial hierarchy

### ✗ Don't
- Use white or cream page backgrounds — the palette must remain dark paua
- Use Inter, Geist, or Manrope — these generic sans-serifs erase the carved-monumental voice
- Apply large rounded "friendly" corners — Māori carving is rectilinear with curvilinear ornament, not soft bubbles
- Use pastel colours of any kind — the palette is earth pigment, shell, and shadow
- Fall into generic Western SaaS layouts — compose vertically like carved meeting house posts, not horizontally like dashboard grids
- Generate moko (facial tattoo) imagery — tā moko is sacred and identity-specific; stick to koru, kowhaiwhai, and tukutuku as the safe decorative vocabulary

## Applications

This system is best suited for cultural institutions, heritage projects, indigenous media platforms, and Aotearoa-based brands that want to honour Māori visual traditions in digital form. It works powerfully for museum exhibition sites, documentary storytelling, educational platforms about Pacific culture, and any context where dark, layered, narrative-rich design serves the content. The monumental typography and restrained motion also make it effective for keynote presentations and editorial longform.
