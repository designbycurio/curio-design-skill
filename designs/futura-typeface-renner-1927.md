---
version: 1

meta:
  id: futura-typeface-renner-1927
  name: "Futura Typeface (Renner, 1927)"
  description: "Geometric sans-serif purity — circle, triangle, square distilled into typographic modernism"
  isDark: false
  tags: [modernist, minimal, professional, historical, futuristic]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1924–1927 design; 1927 commercial release; continuous adoption through 2024"
  region: "Frankfurt, Germany"
  regionZh: "德国法兰克福"
  keyFigures: ["Paul Renner", "Heinrich Jost", "Edwin Jost", "Tobias Frere-Jones"]
  movements: ["Bauhaus typography", "German New Typography", "Geometric sans-serif tradition"]

introduction: |
  Futura is geometry made legible. Paul Renner's 1927 masterpiece for the Bauer Type Foundry reduced the Latin alphabet to its Platonic essentials — the circle, the equilateral triangle, the square — producing a typeface so forward-looking it traveled to the Moon on the Apollo 11 plaque.

  This system channels that radical clarity: pure white fields, black geometric type, and strategic Bauhaus primary-color accents deployed with the discipline Renner demanded. Every element earns its place through geometric logic, not decoration.
introductionZh: |
  Futura 是几何学的可读化身。保罗·伦纳 1927 年为法兰克福鲍尔铸字厂设计的这款字体，将拉丁字母还原为圆形、等边三角形与正方形的柏拉图本质，创造出一款前瞻性如此之强的字体，以至于它随阿波罗 11 号登月纪念牌抵达了月球表面。

  本设计系统承袭那份激进的清晰：纯白底色、黑色几何排版，以及包豪斯三原色作为战略性点缀——以伦纳所要求的纪律性精准部署。每一个元素都通过几何逻辑而非装饰来证明自身存在的合理性。

colors:
  primary:
    "50": "#FEF0F2"
    "100": "#FDD8DC"
    "200": "#FBB0B9"
    "300": "#F87A8A"
    "400": "#F24058"
    "500": "#D70026"
    "600": "#B8001F"
    "700": "#93001A"
    "800": "#6E0013"
    "900": "#4A000D"
    "950": "#2D0008"
  secondary:
    "50": "#EEF3FA"
    "100": "#D4E1F3"
    "200": "#A9C3E7"
    "300": "#7BA2D8"
    "400": "#4D7FC6"
    "500": "#1A4A8C"
    "600": "#153D74"
    "700": "#10305C"
    "800": "#0C2344"
    "900": "#08172D"
    "950": "#040C18"
  accent:
    "50": "#FFFCEB"
    "100": "#FFF7CC"
    "200": "#FFEF99"
    "300": "#FFE566"
    "400": "#FFD933"
    "500": "#FFCC00"
    "600": "#D4AA00"
    "700": "#AA8800"
    "800": "#806600"
    "900": "#554400"
    "950": "#2B2200"
  neutral:
    "50": "#FAFAFA"
    "100": "#F5F5F5"
    "200": "#E8E8E8"
    "300": "#D4D4D4"
    "400": "#A8A8A8"
    "500": "#737373"
    "600": "#6A6A6A"
    "700": "#525252"
    "800": "#333333"
    "900": "#1A1A1A"
    "950": "#0A0A0A"
  semantic:
    success: { bg: "#E8F5E9", text: "#1B5E20", light: "#C8E6C9", border: "#4CAF50" }
    warning: { bg: "#FFF8E1", text: "#E65100", light: "#FFECB3", border: "#FF9800" }
    error: { bg: "#FEF0F2", text: "#B8001F", light: "#FDD8DC", border: "#D70026" }
    info: { bg: "#EEF3FA", text: "#153D74", light: "#D4E1F3", border: "#1A4A8C" }
  background:
    page: "#FFFFFF"
    surface: "#F8F8F8"
    subtle: "#F0F0F0"
  text:
    primary: "#0A0A0A"
    secondary: "#525252"
    muted: "#6A6A6A"
    inverse: "#FFFFFF"

typography:
  families:
    heading: "'Jost', 'Futura', sans-serif"
    body: "'Jost', 'Inter', sans-serif"
    mono: "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500&display=swap"
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
  scale: ["2px", "4px", "6px", "8px", "12px", "16px", "24px", "32px", "48px", "64px", "96px", "128px"]
  container: { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap: { sm: "8px", md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "0", md: "2px", lg: "2px", xl: "4px", full: "9999px" }
  color: { default: "#0A0A0A", subtle: "#E8E8E8", strong: "#0A0A0A", focus: "#D70026" }
  width: { thin: "1px", default: "1px", thick: "2px" }
  style: "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  "2xl": "none"
  inner: "none"
  focus: "0 0 0 2px #D70026"

motion:
  level: "minimal"
  durations: { instant: "0ms", fast: "100ms", normal: "200ms", slow: "300ms", slower: "500ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [opacity, stroke, underline]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "strong"
  rhythm: "4px"

surfaceStyle: "flat"
blur: "none"

iconography:
  treatment: "linear"
  set: "lucide"
  size: { sm: "16px", md: "20px", lg: "24px" }
  stroke: "1.5px"

components:
  button:
    primary: { background: "#0A0A0A", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#333333", hoverShadow: "none", hoverColor: "#FFFFFF" }
    secondary: { background: "transparent", color: "#0A0A0A", border: "2px solid #0A0A0A", shadow: "none", hoverBackground: "#0A0A0A", hoverShadow: "none", hoverColor: "#FFFFFF" }
    ghost: { background: "transparent", color: "#0A0A0A", border: "none", shadow: "none", hoverBackground: "#F0F0F0", hoverShadow: "none", hoverColor: "#0A0A0A" }
    danger: { background: "#D70026", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#B8001F", hoverShadow: "none", hoverColor: "#FFFFFF" }
    sizes:
      sm: { height: "32px", padding: "0 12px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 28px", fontSize: "1.125rem" }
    borderRadius: "0"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFFFFF"
    color: "#0A0A0A"
    border: "1px solid #E8E8E8"
    borderRadius: "0"
    padding: "10px 12px"
    focusBorder: "2px solid #0A0A0A"
    placeholderColor: "#A8A8A8"
  card:
    base: { background: "#FFFFFF", border: "1px solid #0A0A0A", borderRadius: "0", padding: "24px", shadow: "none" }
    hover: { shadow: "none", transform: "none" }
---

# Futura Typeface (Renner, 1927)

> Geometry is the alphabet — circle, triangle, square rendered as typographic modernism on pure white clarity.

## Origin

Paul Renner began designing Futura in 1924 at the Bauer Type Foundry in Frankfurt, Germany, releasing it commercially in 1927. The typeface distilled Bauhaus geometric principles — the circle, the equilateral triangle, the square — into a functional alphabet. Its perfectly circular O, isoceles triangular A, and single-story g represented a radical break from calligraphic tradition, declaring that the letter *is* geometry and everything else is ornament.

Futura became one of the most widely adopted typefaces of the 20th century. Nike's "Just Do It" wordmark (1988), Volkswagen's advertising campaigns, IKEA's corporate identity (until 2009), and most iconically the Apollo 11 lunar plaque (1969) all employed Futura. The typeface's influence spawned an entire geometric sans-serif lineage including Avant Garde, Avenir, and the open-source Jost* by Owen Earl — the most faithful digital revival available without licensing restrictions.

## Overview

Composition cues:
- **Layout**: 12-column geometric grid with rigorous alignment
- **Content width**: Container (1024–1280px) with generous margins
- **Framing**: Bordered — thin black 1px rules define panels and sections
- **Grid intensity**: Strong — visible structural logic throughout

## Colors

The palette is Bauhaus-canonical: pure white dominates as the field of clarity, pure black carries all typographic weight, and the three Bauhaus primaries (red, blue, yellow) serve as strategic geometric accents — never decorative, always structural. Color is deployed sparingly: one or two primaries per composition, used as solid blocks or hairline rules, never as gradients or atmospheric effects.

**Role usage**:
- Page background → `colors.background.page` (#FFFFFF)
- Card / panel surface → `colors.background.surface` (#F8F8F8)
- Primary text → `colors.text.primary` (#0A0A0A)
- Muted / secondary text → `colors.text.muted` (#6A6A6A)
- Primary accent (CTA, emphasis) → `colors.primary.500` (#D70026 Bauhaus red)
- Structural accent → `colors.secondary.500` (#1A4A8C Bauhaus blue)
- Highlight / tertiary → `colors.accent.500` (#FFCC00 Bauhaus yellow)
- Hairline borders → `colors.neutral.400` (#A8A8A8)

## Typography

All type is geometric sans-serif — Jost* (the open-source Futura clone by Owen Earl / indestructible type) for headings and body, with no exceptions. The voice is authoritative, clean, and forward-looking. Display sizes use bold/extrabold weights with tight tracking to emphasize geometric letterforms; body uses book weight with comfortable line-height for sustained reading. Uppercase is used for buttons and labels to reinforce geometric uniformity.

**Text styles**:
- `display-xl` — Jost, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Jost, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Jost, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `heading-2` — Jost, 36px, weight 600, line-height 1.2, letter-spacing -0.01em
- `body-lg` — Jost, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — Jost, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Jost, 12px, weight 500, line-height 1.4, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px (Bauhaus modular rhythm)
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px centered
- Section padding: 64–96px vertical for breathing room
- Grid: 12-column with 24px gutters
- Generous whitespace between elements — Renner's clarity principle

## Elevation & Depth

There is no elevation. Futura's world is rigorously flat — depth is created through contrast (black on white), scale hierarchy, and geometric color blocks, never through shadows or blur. Surfaces are differentiated by border and background tone only.

- No box-shadows on any element
- Panels defined by 1px solid black borders
- Depth hierarchy through type scale and color weight
- Focus states use 2px solid red outline, not glow

## Shapes

- Button radius: 0 (perfectly rectilinear)
- Card radius: 0
- Input radius: 0
- Maximum radius anywhere: 4px (only for small pills/badges if needed)
- Circle used only as a geometric motif, not as UI rounding

## Motion

Motion is minimal and purposeful — Renner's modernism has no room for playful animation. Transitions exist only to confirm interaction, never to entertain. Hover states change opacity or add underlines; no lifts, no bounces, no scaling.

- Level: minimal
- Hover transition: 200ms ease
- Page transitions: none (instant)
- Hover patterns: opacity fade, underline reveal, stroke weight change
- Reduced motion: respected by default
- No spring or bounce easings

## Techniques

### Bauhaus Primary-Color Block Accent
A geometric color block (circle, triangle, or rectangle) in one Bauhaus primary, positioned as a compositional anchor.
```css
.color-block-accent {
  position: absolute;
  width: 120px;
  height: 120px;
  background: #D70026;
  clip-path: circle(50%);
  z-index: -1;
  opacity: 0.9;
}
```

### Geometric Grid Overlay
A visible structural grid rendered as hairline rules to reinforce the system's geometric logic.
```css
.geometric-grid {
  background-image:
    linear-gradient(to right, #E8E8E8 1px, transparent 1px),
    linear-gradient(to bottom, #E8E8E8 1px, transparent 1px);
  background-size: 64px 64px;
}
```

### Black-Field Inversion Section
A full-width section inverted to black background with white geometric type — the Bauhaus contrast principle.
```css
.inversion-section {
  background: #0A0A0A;
  color: #FFFFFF;
  padding: 96px 0;
}
.inversion-section .accent {
  color: #FFCC00;
}
```

## Iconography

Icons follow the same geometric reduction as the typeface — linear strokes at consistent weight, no fills, no decorative flourishes. Every icon should feel like it could be a Futura glyph.

- Treatment: linear (stroke only)
- Set: Lucide (geometric, consistent stroke weight)
- Stroke: 1.5px uniform weight

## Do's & Don'ts

### ✓ Do
- Use Jost* (or Futura) exclusively for all typographic elements
- Deploy Bauhaus primaries as solid geometric blocks, one or two per composition
- Maintain rigorous rectilinear geometry (0px radius on all interactive elements)
- Use generous whitespace to let geometric forms breathe
- Treat the 12-column grid as visible structural logic

### ✗ Don't
- Use non-geometric typography anywhere (no serifs, no humanist sans)
- Apply rounded soft corners (Bauhaus rectilinearity is non-negotiable)
- Use photographic naturalistic imagery (geometric / architectural / abstract only)
- Apply saturated gradient backgrounds (flat solid colors only)
- Add faux-vintage or textured surfaces (Futura is modernist clarity)
- Mix more than two primary colors in a single composition
- Use decorative shadows or depth effects

## Applications

This system is ideal for portfolios, architecture studios, design agencies, editorial layouts, and any brand that wants to project intellectual rigor and modernist confidence. It excels at typography-forward presentations, manifesto-style landing pages, and minimal product showcases where the content's geometry speaks louder than decoration.
