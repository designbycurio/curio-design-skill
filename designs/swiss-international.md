---
version: 1

meta:
  id: swiss-international
  name: Swiss International Style
  description: Objective modernist clarity built on mathematical grids, sans-serif type, and radical restraint
  isDark: false
  tags: [modernist, editorial, historical, minimal, professional]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1950s–1970s (peaked 1955–1965); visual principles still foundational today"
  region: "Zürich and Basel, Switzerland"
  regionZh: "瑞士苏黎世与巴塞尔"
  keyFigures: [Josef Müller-Brockmann, Armin Hofmann, Max Bill, Emil Ruder, Adrian Frutiger]
  movements: [Modernism, New Typography, Constructivism]

introduction: |
  The Swiss International Typographic Style emerged from Zürich and Basel in the 1950s as a radical commitment to objectivity: information should communicate through structure, not decoration. Mathematical grids, sans-serif type, asymmetric composition, and disciplined use of white space became the vocabulary of an entire generation of corporate and editorial design.

  Its influence is inescapable — from Lufthansa's identity to the New York subway signage — and its core principles (hierarchy through scale and weight, not ornament) remain the bedrock of modern UI and editorial design sixty years later.
introductionZh: |
  瑞士国际排版风格于 1950 年代在苏黎世与巴塞尔兴起，是一场对"客观传达"的激进承诺：信息应当通过结构而非装饰来沟通。数学网格、无衬线字体、不对称构图以及对留白的严格控制，成为整整一代企业与编辑设计的共同语言。

  从汉莎航空的企业标识到纽约地铁导视系统，其影响无处不在。六十年后的今天，其核心原则——通过字号与字重而非装饰建立层级——仍然是现代界面与编辑设计的基石。

colors:
  primary:
    "50": "#fdf2f2"
    "100": "#f9dada"
    "200": "#f0a8a8"
    "300": "#e67676"
    "400": "#da3b3b"
    "500": "#cc0000"
    "600": "#b80000"
    "700": "#a30000"
    "800": "#850000"
    "900": "#660000"
    "950": "#4d0000"
  secondary:
    "50": "#f5f5f5"
    "100": "#e8e8e8"
    "200": "#d1d1d1"
    "300": "#b0b0b0"
    "400": "#8a8a8a"
    "500": "#666666"
    "600": "#555555"
    "700": "#444444"
    "800": "#333333"
    "900": "#222222"
    "950": "#111111"
  accent:
    "50": "#fdf2f2"
    "100": "#f9dada"
    "200": "#f0a8a8"
    "300": "#e67676"
    "400": "#da3b3b"
    "500": "#cc0000"
    "600": "#b80000"
    "700": "#a30000"
    "800": "#850000"
    "900": "#660000"
    "950": "#4d0000"
  neutral:
    "50": "#fafafa"
    "100": "#f5f5f5"
    "200": "#e5e5e5"
    "300": "#d4d4d4"
    "400": "#a3a3a3"
    "500": "#737373"
    "600": "#525252"
    "700": "#404040"
    "800": "#262626"
    "900": "#171717"
    "950": "#0a0a0a"
  semantic:
    success: { bg: "#1a7a2e", text: "#ffffff", light: "#e8f5e9", border: "#1a7a2e" }
    warning: { bg: "#e6a800", text: "#171717", light: "#fff8e1", border: "#e6a800" }
    error:   { bg: "#cc0000", text: "#ffffff", light: "#fdf2f2", border: "#cc0000" }
    info:    { bg: "#262626", text: "#ffffff", light: "#f5f5f5", border: "#525252" }
  background:
    page:    "#ffffff"
    surface: "#ffffff"
    subtle:  "#f5f5f5"
  text:
    primary:   "#171717"
    secondary: "#525252"
    muted:     "#737373"
    inverse:   "#ffffff"

typography:
  families:
    heading: "'Inter', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif"
    body:    "'Inter', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap"
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
    lg: "4px"
    xl: "4px"
    full: "9999px"
  color:
    default: "#e5e5e5"
    subtle: "#f5f5f5"
    strong: "#171717"
    focus: "#cc0000"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.03)"
  sm: "0 1px 3px rgba(0,0,0,0.04)"
  md: "0 2px 4px rgba(0,0,0,0.05)"
  lg: "0 4px 8px rgba(0,0,0,0.05)"
  xl: "0 6px 12px rgba(0,0,0,0.06)"
  "2xl": "0 8px 16px rgba(0,0,0,0.06)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.04)"
  focus: "0 0 0 3px rgba(204,0,0,0.20)"

motion:
  level: "minimal"
  durations:
    instant: "0ms"
    fast: "120ms"
    normal: "200ms"
    slow: "300ms"
    slower: "500ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.25, 0.46, 0.45, 0.94)"
  hoverPatterns: [opacity, underline]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "minimal"
  gridIntensity: "strong"
  rhythm:        "4px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#171717"
      color: "#ffffff"
      border: "none"
      shadow: "none"
      hoverBackground: "#cc0000"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    secondary:
      background: "#ffffff"
      color: "#171717"
      border: "2px solid #171717"
      shadow: "none"
      hoverBackground: "#171717"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    ghost:
      background: "transparent"
      color: "#171717"
      border: "none"
      shadow: "none"
      hoverBackground: "#f5f5f5"
      hoverShadow: "none"
      hoverColor: "#171717"
    danger:
      background: "#cc0000"
      color: "#ffffff"
      border: "none"
      shadow: "none"
      hoverBackground: "#a30000"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    sizes:
      sm: { height: "32px", padding: "0 16px", fontSize: "0.75rem" }
      md: { height: "40px", padding: "0 24px", fontSize: "0.875rem" }
      lg: { height: "48px", padding: "0 32px", fontSize: "1rem" }
    borderRadius: "2px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#ffffff"
    color: "#171717"
    border: "1px solid #e5e5e5"
    borderRadius: "2px"
    padding: "10px 12px"
    focusBorder: "2px solid #171717"
    placeholderColor: "#737373"
  card:
    base:
      background: "#ffffff"
      border: "1px solid #e5e5e5"
      borderRadius: "0"
      padding: "24px"
      shadow: "none"
    hover:
      shadow: "none"
      transform: "none"
---

# Swiss International Style

> Objective communication through mathematical grids, sans-serif discipline, and the eloquence of white space.

## Origin

The Swiss International Typographic Style crystallized in the mid-1950s at two Swiss design schools — the Zürich School of Applied Arts and the Basel School of Design — though its roots reach back to Jan Tschichold's *Die neue Typographie* (1928) and the Constructivist experiments of the 1920s. Josef Müller-Brockmann in Zürich and Armin Hofmann and Emil Ruder in Basel independently arrived at overlapping principles: design should serve objective communication, not personal expression. Their students and colleagues — Max Bill, Adrian Frutiger, Karl Gerstner — codified these ideas into a coherent movement.

The defining artifacts of the style include *Neue Grafik* magazine (1958–1965), which became its manifesto in print; the Helvetica typeface designed by Max Miedinger and Eduard Hoffmann in 1957; and landmark corporate identities for Lufthansa, Swiss Federal Railways, and later IBM (through the Swiss-influenced Paul Rand). By the 1960s, what began as a regional school had become the global default for serious graphic design — the "International Style" in name and practice.

## Overview

Composition cues:
- **Layout**: Strict column grids (8, 12, or 16 columns) with asymmetric placement of elements along grid lines
- **Content width**: Container (max 1024–1280px) with generous margins; content rarely fills the full width
- **Framing**: Minimal — no decorative borders, no cards with shadows; hierarchy through typography and whitespace alone
- **Grid intensity**: Strong — the grid is not merely structural but a visible organizing principle; elements snap to grid lines with mathematical precision

## Colors

The Swiss palette is an exercise in severity. Black ink on white paper is the default; color is not decoration but information. When a single accent appears — historically, a saturated red (#cc0000) — it carries enormous weight precisely because everything else is monochromatic. Greys serve as intermediaries between the absolute poles of black and white. This restraint is the point: by removing chromatic noise, the designer forces the viewer to engage with structure, hierarchy, and content.

**Role usage**:
- Page background → `colors.background.page` (#ffffff)
- Surface background → `colors.background.surface` (#ffffff)
- Subtle background (section dividers) → `colors.background.subtle` (#f5f5f5)
- Primary text → `colors.text.primary` (#171717)
- Secondary text → `colors.text.secondary` (#525252)
- Accent for emphasis → `colors.primary.500` (#cc0000) — used sparingly
- Borders and rules → `colors.neutral.200` (#e5e5e5)
- Strong dividers → `colors.neutral.900` (#171717)

## Typography

Inter serves as the digital heir to Helvetica: a neutral, highly legible grotesque sans-serif with an extensive weight range and optical sizing. The Swiss approach to typography is architectural — hierarchy is built through size, weight, and spatial position, never through decorative variation. Headings are set in bold or semibold with tight tracking; body text in regular weight with comfortable line-height for extended reading. Uppercase with wide letter-spacing appears in labels and navigation, echoing the poster tradition of Müller-Brockmann. There is one typeface family; variation comes from the scale, not the font.

**Text styles**:
- `display-xl` — Inter, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Inter, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Inter, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `heading-2` — Inter, 32px, weight 600, line-height 1.25, letter-spacing 0
- `body-lg` — Inter, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 12px, weight 500, line-height 1.5, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px rhythm (all spacing values are multiples of 4)
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-width: 1024–1280px, left-aligned or centred with generous margins
- Section vertical padding: 64–96px on desktop, 32–48px on mobile
- Grid: 12-column with 24px gutters; content placed asymmetrically along grid lines
- Elements align to baseline grids where possible

## Elevation & Depth

The Swiss style is fundamentally flat — a direct descendant of ink on paper. There are no shadows, no gradients, no glass effects. Depth is expressed through spatial hierarchy: larger elements are more important, not closer. When subtle elevation is unavoidable in digital contexts (e.g., dropdowns), shadows are extremely minimal and near-invisible. The materiality is high-quality matte paper: crisp, clean, and unambiguously two-dimensional.

- Default surface: no shadow, no border or a single 1px rule
- If shadow is unavoidable: `0 1px 3px rgba(0,0,0,0.04)` maximum
- No backdrop blur, no frosted glass, no translucency
- Focus ring: `0 0 0 3px rgba(204,0,0,0.20)` — red accent

## Shapes

- Card/container corners: 0 (sharp rectangles are canonical)
- Button corners: 2px (barely perceptible, functional only)
- Input corners: 2px
- No rounded corners beyond functional minimum — the rectangle is the fundamental Swiss unit

## Motion

Swiss design is static by heritage — its masters worked in print, where nothing moves. In digital translation, motion should be invisible: instant enough to feel responsive, restrained enough to never distract. Transitions exist only to prevent jarring state changes, not to delight or entertain. No bounces, no overshoots, no playful easing. Elements appear, shift, and disappear with the precision of a railway timetable.

- Level: minimal
- Default transition: 200ms, `cubic-bezier(0.4, 0, 0.2, 1)`
- Micro-interactions: 120ms (button press, input focus)
- No spring or bounce easings
- Hover patterns: opacity change, underline reveal
- Reduced motion: always respected; transitions collapse to instant

## Techniques

### Grid-ruled section divider

A visible grid line used as a section divider — the grid itself becomes the design element, not merely the invisible scaffolding. Thin horizontal rules at full container width create the rhythm of a well-set page.

```css
.grid-rule {
  border: none;
  border-top: 1px solid #171717;
  margin: 64px 0;
  width: 100%;
}
.grid-rule--subtle {
  border-top-color: #e5e5e5;
}
```

### Typographic scale poster block

The signature Swiss composition: a single oversized word or number anchors the layout, with smaller supporting text aligned to the same grid. Size contrast does the work that color and decoration do in other systems.

```css
.poster-block {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  align-items: baseline;
}
.poster-block__headline {
  grid-column: 1 / 9;
  font-family: 'Inter', 'Helvetica Neue', sans-serif;
  font-size: clamp(4rem, 8vw, 8rem);
  font-weight: 700;
  line-height: 1.0;
  letter-spacing: -0.04em;
  color: #171717;
}
.poster-block__meta {
  grid-column: 9 / 13;
  font-family: 'Inter', 'Helvetica Neue', sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #525252;
  align-self: end;
}
```

### Red accent marker

A single block of pure red used as a typographic accent or navigational indicator — the only color in a black-and-white composition, carrying maximum visual weight through contrast with its monochrome surroundings.

```css
.accent-marker {
  display: inline-block;
  width: 24px;
  height: 4px;
  background: #cc0000;
  margin-bottom: 16px;
}
.accent-marker--vertical {
  width: 4px;
  height: 24px;
  margin-right: 12px;
  margin-bottom: 0;
  vertical-align: middle;
}
.accent-marker--dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
```

## Iconography

Icons in the Swiss tradition are reduced to their most essential geometric form — every unnecessary stroke is removed until only the minimum information remains. Linear treatment with consistent stroke weight mirrors the typographic discipline of the system. Icons inform; they do not illustrate or decorate.

- Treatment: linear with square joins and flat caps
- Set: Lucide (clean geometric construction closest to Swiss principles)
- Stroke: 1.5px consistent weight

## Do's & Don'ts

### ✓ Do
- Use the mathematical grid as the primary compositional tool — every element snaps to grid lines
- Build hierarchy through type size and weight alone; let scale do the expressive work
- Embrace generous white space as an active design element, not empty filler
- Restrict color to black, white, and greys; deploy red #cc0000 only for deliberate emphasis
- Align text flush-left with ragged-right edges (asymmetric composition is doctrine)

### ✗ Don't
- Use serif fonts of any kind
- Add decorative ornaments, frames, or flourishes
- Apply gradients, glows, or any non-flat treatment
- Center layouts symmetrically (asymmetry is doctrine)
- Introduce multiple accent colors — one saturated hue or none

## Applications

The Swiss International Style is ideal for editorial platforms, corporate identities, data-heavy dashboards, documentation systems, and any interface where clarity and information density are paramount. Its grid-first, type-driven approach scales cleanly from business cards to annual reports to complex web applications. The style works best when content — text, data, photography — is strong enough to stand without decorative support.
