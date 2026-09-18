---
version: 1

meta:
  id: tiffany-blue
  name: "Tiffany & Co"
  description: "Robin's-egg blue luxury with serif elegance and Audrey Hepburn romance"
  isDark: false
  tags: [luxurious, editorial, friendly, professional, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1837 founded; Tiffany Blue trademarked 1998; LVMH acquired 2021"
  region: "New York, United States / Paris, France"
  regionZh: "美国纽约 / 法国巴黎"
  keyFigures: ["Charles Lewis Tiffany", "Elsa Peretti", "Paloma Picasso", "Audrey Hepburn"]
  movements: ["American luxury jewelry", "branded color as IP", "mass-market-luxury crossover"]

introduction: |
  Tiffany & Co is the rare brand whose identity lives in a single color. The robin's-egg blue — Pantone 1837, trademarked and unmistakable — transforms every surface it touches into a promise of romance and occasion. Paired with classical serif typography and restrained luxury, the Tiffany visual language says elegance without ever raising its voice.

  This design system captures that spirit: Tiffany Blue as the singular chromatic anchor, warm cream for editorial depth, and serif type that echoes the brand's nearly two-century heritage. Every component is polished, romantic, and unmistakably Tiffany — from the blue-filled call-to-action to the delicate focus ring that recalls the color of the box itself.

introductionZh: |
  蒂芙尼是少数以一种颜色定义整个品牌的传奇。那抹知更鸟蛋蓝——Pantone 1837，注册商标，独一无二——将每一个触及它的表面都化为浪漫与珍贵的承诺。搭配古典衬线字体与克制的奢华感，蒂芙尼的视觉语言在无声中传递优雅。

  这套设计系统以蒂芙尼蓝为唯一的色彩锚点，温暖的奶油色赋予编辑页面以深度，衬线字体呼应品牌近两个世纪的传承。从蓝色实心按钮到令人联想到经典蓝盒子的聚焦光环，每一个组件都精致、浪漫，且毫无疑问地属于蒂芙尼。

colors:
  primary:
    "50": "#E6F9F8"
    "100": "#B3EEEC"
    "200": "#80E3E0"
    "300": "#4DD8D4"
    "400": "#26CEC9"
    "500": "#0ABAB5"
    "600": "#089A96"
    "700": "#067A77"
    "800": "#045A58"
    "900": "#033B39"
    "950": "#012221"
  secondary:
    "50": "#FDFBF7"
    "100": "#FAF5EC"
    "200": "#F5F0E8"
    "300": "#EBE3D5"
    "400": "#DDD2BE"
    "500": "#C9B99A"
    "600": "#B09D78"
    "700": "#967F5A"
    "800": "#756341"
    "900": "#564A31"
    "950": "#3A3121"
  accent:
    "50": "#FDF8E8"
    "100": "#FAEFC5"
    "200": "#F5E09E"
    "300": "#F0D177"
    "400": "#EBC250"
    "500": "#D4A932"
    "600": "#B08B24"
    "700": "#8C6D1A"
    "800": "#685112"
    "900": "#4A390D"
    "950": "#2E2308"
  neutral:
    "50": "#F7F7F7"
    "100": "#EFEFEF"
    "200": "#E0E0E0"
    "300": "#C8C8C8"
    "400": "#A0A0A0"
    "500": "#6B6B6B"
    "600": "#545454"
    "700": "#3D3D3D"
    "800": "#2A2A2A"
    "900": "#1A1A1A"
    "950": "#0D0D0D"
  semantic:
    success: { bg: "#0ABAB5", text: "#FFFFFF", light: "#E6F9F8", border: "#089A96" }
    warning: { bg: "#D4A932", text: "#FFFFFF", light: "#FDF8E8", border: "#B08B24" }
    error:   { bg: "#C53030", text: "#FFFFFF", light: "#FFF5F5", border: "#9B2C2C" }
    info:    { bg: "#0ABAB5", text: "#FFFFFF", light: "#E6F9F8", border: "#067A77" }
  background:
    page:    "#FFFFFF"
    surface: "#FFFFFF"
    subtle:  "#F5F0E8"
  text:
    primary:   "#1A1A1A"
    secondary: "#545454"
    muted:     "#6B6B6B"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Cormorant Garamond', 'Georgia', serif"
    body:    "'Spectral', 'Georgia', serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&family=Spectral:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap"
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
  lineHeights: { tight: 1.15, snug: 1.35, normal: 1.5, relaxed: 1.65, loose: 1.8 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.02em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px",  md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "4px", md: "6px", lg: "8px", xl: "12px", full: "9999px" }
  color:  { default: "#E0E0E0", subtle: "#EFEFEF", strong: "#1A1A1A", focus: "#0ABAB5" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.04)"
  sm: "0 1px 3px rgba(0,0,0,0.05)"
  md: "0 2px 8px rgba(0,0,0,0.06)"
  lg: "0 4px 16px rgba(0,0,0,0.08)"
  xl: "0 8px 24px rgba(0,0,0,0.10)"
  "2xl": "0 12px 40px rgba(0,0,0,0.12)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.04)"
  focus: "0 0 0 3px rgba(10,186,181,0.30)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: ["lift", "opacity", "underline"]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "solid"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "solid"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:   { background: "#0ABAB5", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#089A96", hoverShadow: "0 2px 8px rgba(10,186,181,0.25)", hoverColor: "#FFFFFF" }
    secondary: { background: "transparent", color: "#1A1A1A", border: "1px solid #1A1A1A", shadow: "none", hoverBackground: "#1A1A1A", hoverShadow: "none", hoverColor: "#FFFFFF" }
    ghost:     { background: "transparent", color: "#0ABAB5", border: "none", shadow: "none", hoverBackground: "rgba(10,186,181,0.08)", hoverShadow: "none", hoverColor: "#089A96" }
    danger:    { background: "#C53030", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#9B2C2C", hoverShadow: "none", hoverColor: "#FFFFFF" }
    sizes:
      sm: { height: "32px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "6px"
    fontWeight: 600
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1A1A1A"
    border: "1px solid #E0E0E0"
    borderRadius: "6px"
    padding: "10px 14px"
    focusBorder: "#0ABAB5"
    placeholderColor: "#A0A0A0"
  card:
    base:  { background: "#FFFFFF", border: "1px solid #EFEFEF", borderRadius: "8px", padding: "24px", shadow: "0 2px 8px rgba(0,0,0,0.06)" }
    hover: { shadow: "0 4px 16px rgba(0,0,0,0.08)", transform: "translateY(-2px)" }
---

# Tiffany & Co

> The robin's-egg blue box that means you matter — Pantone 1837 luxury meets serif romance.

## Origin

Tiffany & Co was founded in 1837 by Charles Lewis Tiffany in New York City, originally as a stationery and fancy goods emporium before pivoting to fine jewelry. The brand's signature blue — adopted for its first Blue Book catalogue cover — became so iconic that it was trademarked as Pantone 1837 (the founding year). Audrey Hepburn cemented the brand's romantic identity in the 1961 film *Breakfast at Tiffany's*, transforming a jeweler into a cultural symbol.

The visual language matured through decades of restraint: always the blue, always serif elegance, always white space as a frame for precious objects. Designers Elsa Peretti and Paloma Picasso brought modernist sensibility to the product line while the brand identity remained classical. After LVMH's 2021 acquisition, Tiffany's digital presence was polished with e-commerce sophistication, but the blue box — and the promise it carries — remains the immovable center of gravity.

## Overview

Composition cues:
- **Layout**: Grid-based editorial layouts with generous whitespace, alternating full-bleed Tiffany Blue panels and white sections
- **Content width**: Container (max ~1280px) for text content; full-bleed for hero and brand-color panels
- **Framing**: Solid, clean frames — photography presented as precious objects in white or cream mounts
- **Grid intensity**: Soft — visible structure without heavy lines, letting whitespace do the work

## Colors

Tiffany's palette is radically simple: one proprietary blue dominates, supported by pure white, warm cream, and deep black. The trademark Tiffany Blue `#0ABAB5` is used as a confident accent — for primary actions, hero panels, and brand moments — never diluted with competing chromatic hues. The cream `#F5F0E8` provides editorial warmth, evoking the tactile quality of Tiffany catalogues and tissue paper. Gold appears only as a subtle accent nod to the Tiffany Yellow Diamond and the brand's jewelry heritage.

**Role usage**:
- Page background → `colors.background.page` (pure white `#FFFFFF`)
- Editorial/catalogue sections → `colors.background.subtle` (cream `#F5F0E8`)
- Brand hero panels → `colors.primary.500` (Tiffany Blue `#0ABAB5`)
- Primary text → `colors.text.primary` (deep ink `#1A1A1A`)
- Muted captions and metadata → `colors.text.muted` (`#6B6B6B`)
- Primary buttons and focus rings → `colors.primary.500`
- Secondary/ghost button borders → `colors.neutral.900` (`#1A1A1A`)

## Typography

Tiffany's type voice is classical and assured — serif fonts that carry the weight of nearly two centuries of heritage without feeling heavy or antiquated. Display headlines in Cormorant Garamond are set large and airy with wide letter-spacing, channeling the elegance of engraved jewelry box lettering. Body text in Spectral reads at 16–17px with generous 1.65 line-height, creating the comfortable reading rhythm of a luxury editorial publication.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 300, line-height 1.0, letter-spacing 0.02em
- `display-lg` — Cormorant Garamond, 72px, weight 300, line-height 1.05, letter-spacing 0.02em
- `heading-1` — Cormorant Garamond, 48px, weight 500, line-height 1.15, letter-spacing 0.02em
- `heading-2` — Cormorant Garamond, 36px, weight 500, line-height 1.2, letter-spacing 0.02em
- `body-lg` — Spectral, 18px, weight 400, line-height 1.65, letter-spacing 0
- `body-md` — Spectral, 16px, weight 400, line-height 1.65, letter-spacing 0
- `caption` — Spectral, 13px, weight 400, line-height 1.5, letter-spacing 0.02em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px, with an 8px rhythm for component spacing
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px centered, with 24px side padding on mobile
- Section padding: 64–128px vertical, creating the "breathing room" that luxury editorial demands
- Grid gap: 16–24px between content cards; 48px between major grid sections

## Elevation & Depth

Tiffany's surfaces are decidedly flat and solid — luxury prefers the confidence of material presence over atmospheric blur or layered translucency. Shadows are used sparingly: a soft 2px-offset shadow on product cards suggests the gentle lift of a jewelry tray, while hover states add slightly more depth. There is no glassmorphism, no backdrop-blur, no gradient — just honest surfaces that let the blue and the photography speak.

- Surface style: Solid white or cream, no transparency
- Blur: None — surfaces are opaque
- Shadow ladder: `xs` for subtle card lift → `md` for default cards (`0 2px 8px rgba(0,0,0,0.06)`) → `lg` for hover states → focus ring uses `0 0 0 3px rgba(10,186,181,0.30)`
- No elevation stacking — surfaces sit on the page, not above it

## Shapes

- Default corner radius: 6px for interactive elements (buttons, inputs)
- Card radius: 8px for content cards and image frames
- Small elements (tags, badges): 4px
- Pill shapes: `9999px` for chips and toggle indicators
- No sharp corners (0px) on interactive elements — the 6px minimum maintains Tiffany's polished, approachable feel

## Motion

Tiffany's motion is restrained and graceful — movements should feel like a velvet-lined drawer sliding open, never bouncy or playful. Transitions serve function (confirming interactions, directing attention) but never call attention to themselves. The brand's confidence means things simply appear where they should be.

- Level: Restrained
- Default transition: 250ms ease-out for most state changes
- Fast transitions: 120ms for hover color shifts and focus states
- Slow transitions: 400ms for panel reveals and page-level transitions
- Easing: `cubic-bezier(0.4, 0, 0.2, 1)` default; `ease-out` for exits
- Hover patterns: gentle lift (`translateY(-2px)`), opacity fade, serif underline reveals
- Reduced motion: fully supported — all animations collapse to instant

## Techniques

### Tiffany Blue Full-Bleed Panel

A signature brand moment: full-viewport-width sections in solid Tiffany Blue with white serif typography, creating the digital equivalent of opening the blue box.

```css
.tiffany-panel {
  background-color: #0ABAB5;
  color: #FFFFFF;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  padding: 96px 24px;
  text-align: center;
}
.tiffany-panel h2 {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 3rem;
  font-weight: 300;
  letter-spacing: 0.02em;
  margin-bottom: 16px;
}
```

### Jewelry Card Frame

Product cards that present items like precious objects in a shadowbox — minimal border, soft shadow, generous internal padding, with serif overlay text.

```css
.jewelry-card {
  background: #FFFFFF;
  border: 1px solid #EFEFEF;
  border-radius: 8px;
  padding: 0;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.jewelry-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}
.jewelry-card .card-body {
  padding: 24px;
  font-family: 'Spectral', Georgia, serif;
}
.jewelry-card .card-title {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 1.25rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: #1A1A1A;
}
```

### Tiffany Focus Ring

A distinctive focus indicator using the brand's trademark blue — subtle enough for luxury polish, visible enough for accessibility.

```css
.tiffany-focus:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(10, 186, 181, 0.30);
  border-color: #0ABAB5;
  transition: box-shadow 120ms ease-out, border-color 120ms ease-out;
}
```

## Iconography

Icons in the Tiffany system are linear and refined — thin strokes that complement the serif typography without competing with it. They function as quiet wayfinding elements, never as decorative illustrations. The treatment mirrors the brand's restraint: precise, elegant, and never heavy.

- Treatment: Linear with 1.5px stroke
- Set: Lucide (clean geometric lines suit the classical aesthetic)
- Stroke: 1.5px consistent weight

## Do's & Don'ts

### Do
- Use Tiffany Blue `#0ABAB5` exclusively for primary actions, hero panels, and brand moments
- Pair serif display type with generous whitespace to create editorial luxury
- Use cream `#F5F0E8` backgrounds for catalogue-style editorial sections
- Present photography as the centerpiece — jewelry and lifestyle imagery should breathe
- Maintain the 6px border-radius on interactive elements for polished consistency

### Don't
- Use any teal or turquoise that isn't exactly `#0ABAB5` — the color is a trademark
- Apply modern sans-serif minimalism — Tiffany is classical serif territory
- Introduce multiple chromatic accents — the blue stands alone
- Add SaaS-style gradients or glassmorphism to surfaces
- Use playful, friendly illustrations — the brand voice is romantic and assured, not whimsical

## Applications

This system is ideal for luxury e-commerce, editorial brand storytelling, and high-end product showcases. It suits any interface that needs to convey heritage, romance, and premium quality — from jewelry catalogues and wedding registries to invitation platforms and lifestyle editorial magazines. The restrained palette and serif typography also work well for cultural institution websites and upscale hospitality booking experiences.
