---
version: 1

meta:
  id: caterpillar-construction-yellow-1925
  name: Caterpillar Construction Yellow (1925)
  description: Saturated Pantone 109 industrial yellow with black slab type — heavy equipment branding at maximum visibility
  isDark: false
  tags: [bold, professional, historical, technical, modernist]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1925 founded (Holt + Best merger); Hi-Way Yellow 1931; current CAT logo 1989–present"
  region: "Peoria, Illinois, USA"
  regionZh: "美国伊利诺伊州皮奥里亚"
  keyFigures: [Benjamin Holt, C. L. Best, Lippincott (1989 rebrand)]
  movements: [American industrial design, heavy-equipment identity, ISO machinery branding]

introduction: |
  Caterpillar's Hi-Way Yellow — Pantone 109 — was chosen in 1931 so road-construction crews could spot every bulldozer and grader against dirt, dust, and fading light. Paired with a slab-bold black wordmark and the iconic yellow triangle "A," it became the most recognized color in heavy industry. This system treats that saturated yellow as the page itself: a high-visibility ground on which black type, hazard stripes, and spec-sheet white panels communicate with the directness of an engineering drawing.
introductionZh: |
  卡特彼勒的"公路黄"（Pantone 109）诞生于1931年，目的是让推土机和平地机在尘土与暮色中一公里外即可辨识。搭配粗壮的黑色字标和标志性黄色三角"A"，它成为重工业领域辨识度最高的色彩。本设计系统将这种高饱和黄色直接作为页面底色，黑色排版、危险条纹与白色规格面板在其上以工程图纸般的直接性传达信息——没有装饰，只有可见性与功能。

colors:
  primary:    {"50": "#FFFDE6", "100": "#FFF9BF", "200": "#FFF599", "300": "#FFEF66", "400": "#FFE033", "500": "#FFCD11", "600": "#E6B800", "700": "#BF9900", "800": "#997A00", "900": "#735C00", "950": "#4D3D00"}
  secondary:  {"50": "#E8E8E8", "100": "#D1D1D1", "200": "#A3A3A3", "300": "#757575", "400": "#474747", "500": "#0F0F0F", "600": "#0D0D0D", "700": "#0A0A0A", "800": "#080808", "900": "#050505", "950": "#030303"}
  accent:     {"50": "#FFF0E8", "100": "#FFD9C2", "200": "#FFB899", "300": "#FF9766", "400": "#FF7F4D", "500": "#FF6B35", "600": "#E55A25", "700": "#BF4A1E", "800": "#993B18", "900": "#732D12", "950": "#4D1E0C"}
  neutral:    {"50": "#F7F7F7", "100": "#EFEFEF", "200": "#DCDCDC", "300": "#BDBDBD", "400": "#989898", "500": "#6E6E6E", "600": "#5A5A5A", "700": "#4A4A4A", "800": "#3F4347", "900": "#2A2A2A", "950": "#1A1A1A"}
  semantic:
    success: { bg: "#1B7A3D", text: "#FFFFFF", light: "#D4EDDA", border: "#1B7A3D" }
    warning: { bg: "#FFCD11", text: "#0F0F0F", light: "#FFF9BF", border: "#E6B800" }
    error:   { bg: "#D32F2F", text: "#FFFFFF", light: "#FDECEA", border: "#D32F2F" }
    info:    { bg: "#1565C0", text: "#FFFFFF", light: "#E3F2FD", border: "#1565C0" }
  background:
    page:    "#FFCD11"
    surface: "#FFFFFF"
    subtle:  "#3F4347"
  text:
    primary:   "#0F0F0F"
    secondary: "#3F4347"
    muted:     "#4A4A4A"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Anton', sans-serif"
    body:    "'Inter', sans-serif"
    mono:    "'DM Mono', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.1, snug: 1.2, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "2px", md: "4px", lg: "6px", xl: "8px", full: "9999px"}
  color:  {default: "#0F0F0F", subtle: "#3F4347", strong: "#0F0F0F", focus: "#0F0F0F"}
  width:  {thin: "1px", default: "2px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  "2xl": "none"
  inner: "inset 0 2px 4px rgba(0,0,0,0.1)"
  focus: "0 0 0 3px rgba(15,15,15,0.4)"

motion:
  level: "minimal"
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "300ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [opacity, tint]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "full-bleed"
  framing:       "solid"
  gridIntensity: "strong"
  rhythm:        "4px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#0F0F0F", color: "#FFCD11", border: "none", shadow: "none", hoverBackground: "#3F4347", hoverShadow: "none", hoverColor: "#FFCD11"}
    secondary: {background: "transparent", color: "#0F0F0F", border: "2px solid #0F0F0F", shadow: "none", hoverBackground: "#0F0F0F", hoverShadow: "none", hoverColor: "#FFCD11"}
    ghost:     {background: "transparent", color: "#0F0F0F", border: "none", shadow: "none", hoverBackground: "rgba(15,15,15,0.08)", hoverShadow: "none", hoverColor: "#0F0F0F"}
    danger:    {background: "#D32F2F", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#B71C1C", hoverShadow: "none", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "6px 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "8px 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "12px 28px", fontSize: "1.125rem"}}
    borderRadius: "2px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFFFFF"
    color: "#0F0F0F"
    border: "2px solid #0F0F0F"
    borderRadius: "2px"
    padding: "8px 12px"
    focusBorder: "#0F0F0F"
    placeholderColor: "#4A4A4A"
  card:
    base:  {background: "#FFFFFF", border: "2px solid #0F0F0F", borderRadius: "4px", padding: "24px", shadow: "none"}
    hover: {shadow: "none", transform: "none"}
---

# Caterpillar Construction Yellow (1925)

> Pantone 109 industrial yellow as a full-bleed page ground — maximum visibility, zero decoration, engineered to read at a kilometer.

## Origin

Caterpillar Tractor Company was formed in 1925 when Benjamin Holt's track-laying tractor firm merged with C. L. Best's competing operation in Peoria, Illinois. In 1931 the company adopted "Hi-Way Yellow" — a saturated Pantone 109 — for all road-construction equipment, chosen because crews needed to spot machines against brown earth, grey dust, and fading twilight from maximum distance. The color has remained unchanged for nearly a century.

The modern CAT identity was consolidated in 1989 by Lippincott, who introduced the bold three-letter wordmark with the yellow triangle replacing the "A." The visual language is deliberately plain: slab-bold condensed type, flat matte paint, black treadmark graphics, and ISO-standard hazard markings. Every element serves visibility and legibility under harsh jobsite conditions — no ornament, no subtlety, no ambiguity.

## Overview

Composition cues:
- **Layout**: 12-column engineering grid with full-bleed yellow hero panels
- **Content width**: Full-bleed for hero sections; contained white spec-sheet panels within
- **Framing**: Solid black borders (2–4px), hard-edged rectilinear cards
- **Grid intensity**: Strong — visible structure echoing technical drawings and blueprint overlays

## Colors

The palette is binary at its core: saturated Pantone 109 yellow against pure black. White surfaces appear as inset spec-sheet panels. Concrete gray provides a secondary dark ground for technical data. Safety orange is reserved exclusively for hazard and warning states — never decorative. Every color choice traces back to ISO machinery visibility standards and jobsite safety requirements.

**Role usage**:
- Page background → `colors.background.page` (#FFCD11 — CAT yellow)
- Content panels / spec sheets → `colors.background.surface` (#FFFFFF)
- Technical data sections → `colors.background.subtle` (#3F4347 — concrete gray)
- All body text → `colors.text.primary` (#0F0F0F)
- Hazard / warning accents only → `colors.accent.500` (#FF6B35 — safety orange)
- Primary CTAs → black fill with yellow text
- Borders and structural lines → `colors.secondary.500` (#0F0F0F)

## Typography

Type is compressed, bold, and industrial — designed to read on machine panels and safety signage. Anton provides the condensed impact for headlines (evoking stamped-metal data plates). Inter handles body text with functional clarity. DM Mono serves engineering data, part numbers, and instrument-panel readouts. No serifs, no scripts, no decorative faces anywhere.

**Text styles**:
- `display-xl` — Anton, 96px, weight 400 (Anton is single-weight), line-height 1.0, letter-spacing -0.02em
- `display-lg` — Anton, 72px, weight 400, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Anton, 48px, weight 400, line-height 1.1, letter-spacing 0
- `heading-2` — Anton, 36px, weight 400, line-height 1.15, letter-spacing 0
- `body-lg` — Inter, 18px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 12px, weight 500, line-height 1.4, letter-spacing 0.05em, uppercase
- `mono-md` — DM Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px
- Scale follows 4px rhythm: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128
- Container max-width: 1280px for spec-sheet content
- Section padding: 64px vertical (md), 96px (lg) for hero panels
- Grid gap: 16px default, 24px for card grids
- Full-bleed yellow sections break out of container for maximum impact

## Elevation & Depth

Industrial surfaces are flat matte paint — no gloss, no depth illusion. Hierarchy is achieved through color contrast (yellow vs. white vs. concrete gray) and thick black borders rather than shadows. The only depth cue is the inset input field, which uses a subtle inner shadow to suggest a recessed instrument panel.

- No box-shadows on cards or buttons (flat painted surfaces)
- Depth via 2–4px solid black borders creating hard panel edges
- Inset fields use minimal inner shadow for recessed feel
- Focus states use a 3px black ring (no glow, no blur)

## Shapes

- Button border-radius: 2px (machined-metal sharpness)
- Card border-radius: 4px (slight chamfer, not rounded)
- Input border-radius: 2px
- No pill shapes, no circles for containers
- Diagonal cuts on decorative elements (45° hazard stripes)

## Motion

Motion is workmanlike and minimal — machines don't bounce or spring. Transitions exist only to confirm state changes (hover, focus, active), never for delight. Everything snaps into place like hydraulic actuators.

- Level: minimal
- Hover transitions: 100–200ms, linear or ease-out
- No spring physics, no overshoot, no playful easing
- Hover patterns: opacity reduction, background tint shift
- `prefers-reduced-motion`: respected, all transitions disabled

## Techniques

### Hazard stripe accent

Diagonal black-and-yellow repeating stripes used as a decorative border or section divider, evoking ISO 3864 safety markings.

```css
.hazard-stripe {
  background: repeating-linear-gradient(
    -45deg,
    #0F0F0F,
    #0F0F0F 10px,
    #FFCD11 10px,
    #FFCD11 20px
  );
  height: 8px;
  width: 100%;
}
```

### Machine-data panel

A concrete-gray card with monospace type and thick black border, styled like an equipment instrument readout.

```css
.machine-panel {
  background: #3F4347;
  border: 3px solid #0F0F0F;
  border-radius: 4px;
  padding: 24px;
  color: #FFFFFF;
  font-family: 'DM Mono', monospace;
  font-size: 14px;
  line-height: 1.6;
}
```

### Full-bleed yellow hero

A section that saturates the viewport with CAT yellow, using the condensed Anton headline at maximum scale against the brand ground.

```css
.hero-yellow {
  background: #FFCD11;
  padding: 96px 32px;
  text-align: left;
}
.hero-yellow h1 {
  font-family: 'Anton', sans-serif;
  font-size: clamp(3rem, 8vw, 6rem);
  color: #0F0F0F;
  line-height: 1.0;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}
```

## Iconography

Icons are linear and utilitarian — thin strokes on solid grounds, never filled or decorative. They function as technical diagram elements, not illustrations.

- Treatment: linear (outline only)
- Set: Lucide (clean geometric strokes)
- Stroke: 2px (visible at small sizes against yellow ground)

## Do's & Don'ts

### ✓ Do
- Use CAT yellow (#FFCD11) as the dominant page ground — it IS the brand
- Set headlines in Anton uppercase for maximum industrial impact
- Use thick black borders (2–4px) to define panel edges
- Reserve safety orange exclusively for warnings and hazard states
- Keep corners sharp (2–4px radius) — machined, not friendly

### ✗ Don't
- Use mustard, olive, or muted yellows — must be saturated Pantone 109
- Apply neumorphic or glossy surfaces — industrial paint is matte
- Use decorative serif type anywhere — this is engineering print
- Add cute or playful micro-animations — CAT is workmanlike
- Use pure white as page ground — yellow is the page
- Round corners beyond 8px — machine surfaces have hard chamfers
- Use pastel safety colors — proper ISO safety orange and yellow only

## Applications

Best suited for industrial product pages, equipment spec sheets, construction-company marketing sites, and technical documentation portals. The high-visibility yellow ground and condensed black type work at any scale — from mobile dashboards to trade-show displays — and the system's binary palette ensures brand recognition even in low-fidelity contexts like email or print.
