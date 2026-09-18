---
version: 1

meta:
  id: apple-fitness-rings-closed-2024
  name: Apple Fitness Rings Closed (2024)
  description: Three saturated concentric rings on matte OLED black — Apple's gamified wellness data-viz distilled into a design system.
  isDark: true
  tags: [tech, bold, professional, minimal, futuristic]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2015–present (Apple Watch S0 launched April 2015; Fitness+ launched December 2020; visual language consolidated 2020–2024)"
  region: "Cupertino, California"
  regionZh: "美国加利福尼亚州库比蒂诺"
  keyFigures: [Jay Blahnik, Jeff Williams, Jony Ive, Kevin Lynch]
  movements: [wearable health-tracking, gamification-of-fitness, Apple ecosystem health-services]

introduction: |
  Apple's three-rings Activity system — Move magenta, Exercise green, Stand cyan on pure OLED black — is the defining wellness data-visualization of the 2010s. Launched with Apple Watch in 2015 and refined through Fitness+, it fuses industrial-design minimalism with gamified urgency: dense metric dashboards, SF Pro caps-locked stats, and the singular emotional hook of closing all three rings before midnight.

  This design system captures that 11:47 PM adrenaline — saturated ring arcs against matte black, tabular figures ticking upward, and the restrained confidence of Apple's hardware-grade typography. Every surface is OLED-optimized, every component earns its pixel density.
introductionZh: |
  苹果三环活动系统——洋红色"活动"环、绿色"锻炼"环、青色"站立"环在纯黑OLED背景上发光——是2010年代最具标志性的健康数据可视化语言。自2015年Apple Watch首发以来，经Fitness+服务不断打磨，它将工业设计极简主义与游戏化健身完美融合：密集的指标仪表盘、大写无衬线字体的运动数据、以及午夜前"合环"的紧迫感。

  这套设计系统捕捉的正是深夜11:47的肾上腺素——饱和弧线在哑光黑底上跃动，等宽数字逐帧跳动，一切都带着苹果硬件级排版的克制自信。每个表面为OLED优化，每个组件都配得上它的像素密度。

colors:
  primary:    {"50": "#FFF0F3", "100": "#FFD6DE", "200": "#FFB0C2", "300": "#FF7A9A", "400": "#FF3D6B", "500": "#FA114F", "600": "#D90E43", "700": "#B30B37", "800": "#8C082B", "900": "#66051F", "950": "#400313"}
  secondary:  {"50": "#F4FFE6", "100": "#E4FFC2", "200": "#CCFF8A", "300": "#B2F85C", "400": "#9EF03A", "500": "#92E82A", "600": "#74C41E", "700": "#579A16", "800": "#3D700F", "900": "#264809", "950": "#152B05"}
  accent:     {"50": "#E6FFFE", "100": "#B8FFFC", "200": "#80FFF9", "300": "#4DFFF6", "400": "#26F5F2", "500": "#1EEAEF", "600": "#17BFC4", "700": "#119499", "800": "#0B6A6E", "900": "#074143", "950": "#032526"}
  neutral:    {"50": "#F4F4F4", "100": "#E5E5E5", "200": "#C6C6C8", "300": "#AEAEB2", "400": "#8E8E93", "500": "#636366", "600": "#48484A", "700": "#3A3A3C", "800": "#2C2C2E", "900": "#1C1C1E", "950": "#0A0A0A"}
  semantic:
    success: { bg: "#92E82A", text: "#152B05", light: "#1A3D0A", border: "#579A16" }
    warning: { bg: "#FF9F0A", text: "#1C1C1E", light: "#3D2800", border: "#CC7F08" }
    error:   { bg: "#FA114F", text: "#FFFFFF", light: "#3D0515", border: "#D90E43" }
    info:    { bg: "#1EEAEF", text: "#032526", light: "#0B3A3C", border: "#119499" }
  background:
    page:    "#000000"
    surface: "#1C1C1E"
    subtle:  "#2C2C2E"
  text:
    primary:   "#F4F4F4"
    secondary: "#AEAEB2"
    muted:     "#636366"
    inverse:   "#000000"

typography:
  families:
    heading: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    body:    "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    mono:    "'IBM Plex Mono', 'SF Mono', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600;700;800&display=swap"
  scale: {"2xs": "0.625rem", "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.1, snug: 1.25, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "8px", md: "12px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "rgba(255,255,255,0.08)", subtle: "rgba(255,255,255,0.04)", strong: "rgba(255,255,255,0.16)", focus: "#1EEAEF"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 0 0 1px rgba(255,255,255,0.04)"
  sm: "0 0 0 1px rgba(255,255,255,0.06)"
  md: "0 0 0 1px rgba(255,255,255,0.08)"
  lg: "0 0 0 1px rgba(255,255,255,0.10), 0 4px 16px rgba(0,0,0,0.4)"
  xl: "0 0 0 1px rgba(255,255,255,0.12), 0 8px 32px rgba(0,0,0,0.5)"
  "2xl": "0 0 0 1px rgba(255,255,255,0.14), 0 16px 48px rgba(0,0,0,0.6)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.3)"
  focus: "0 0 0 3px rgba(30,234,239,0.4)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.25, 0.1, 0.25, 1)"
    in:      "cubic-bezier(0.42, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.58, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [opacity, scale, tint]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "solid"
  gridIntensity: "strong"
  rhythm:        "4px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#FA114F", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#D90E43", hoverShadow: "none", hoverColor: "#FFFFFF"}
    secondary: {background: "#2C2C2E", color: "#F4F4F4", border: "1px solid rgba(255,255,255,0.08)", shadow: "none", hoverBackground: "#3A3A3C", hoverShadow: "none", hoverColor: "#FFFFFF"}
    ghost:     {background: "transparent", color: "#F4F4F4", border: "none", shadow: "none", hoverBackground: "rgba(255,255,255,0.06)", hoverShadow: "none", hoverColor: "#FFFFFF"}
    danger:    {background: "#FA114F", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#B30B37", hoverShadow: "none", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "0 12px", fontSize: "0.75rem"}, md: {height: "40px", padding: "0 20px", fontSize: "0.875rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1rem"}}
    borderRadius: "12px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#1C1C1E"
    color: "#F4F4F4"
    border: "1px solid rgba(255,255,255,0.08)"
    borderRadius: "12px"
    padding: "12px 16px"
    focusBorder: "#1EEAEF"
    placeholderColor: "#636366"
  card:
    base:  {background: "#1C1C1E", border: "1px solid rgba(255,255,255,0.08)", borderRadius: "16px", padding: "24px", shadow: "none"}
    hover: {shadow: "0 0 0 1px rgba(255,255,255,0.12)", transform: "none"}
---

# Apple Fitness Rings Closed (2024)

> Three saturated concentric rings on OLED black — the gamified urgency of closing Move, Exercise, and Stand before midnight.

## Origin

Apple's three-rings Activity system debuted with Apple Watch Series 0 on 24 April 2015, designed under Jony Ive's hardware team with Jay Blahnik leading fitness technologies. The concept — Move (magenta), Exercise (green), Stand (cyan) arcs filling clockwise from 12 o'clock on pure black — became the most replicated wellness data-visualization of the decade. The visual language consolidated when Fitness+ launched in December 2020, extending the ring metaphor from a 44mm watch face to full-screen iPhone, iPad, and Apple TV dashboards.

The system's power lies in its constraint: three colors, one background, one typeface family, and a single interaction model (fill the arc). Every refinement from watchOS 2 through watchOS 11 has tightened density rather than adding decoration — more metrics per square centimeter, sharper tabular figures, denser stat grids. It is industrial-design minimalism applied to biometric data.

## Overview

Composition cues:
- **Layout**: 12-column grid; asymmetric "ring hero + metric-grid sidebar" composition
- **Content width**: Container (1024–1280px), dense 16px padding rhythm
- **Framing**: Solid matte-charcoal cards on pure-black page, zero elevation
- **Grid intensity**: Strong — stat-dense dashboards with tight gutters

## Colors

The palette is deliberately limited to three saturated ring colors against absolute black. Move-pink magenta `#FA114F` dominates as the primary action color — it's the ring you're most anxious to close. Exercise-green `#92E82A` signals completion and active states. Stand-cyan `#1EEAEF` provides accent and focus indicators. Everything else is grayscale: pure black `#000000` page (OLED-optimized, never charcoal), `#1C1C1E` card surfaces, and warm-white `#F4F4F4` type. The dim-grey `#3A3A3C` represents unfilled ring track. Warning amber `#FF9F0A` appears only for calorie-burn alerts.

**Role usage**:
- Page background → `colors.background.page` (#000000, pure OLED black)
- Card / surface → `colors.background.surface` (#1C1C1E)
- Primary actions / CTA → `colors.primary.500` (Move magenta)
- Success / completion → `colors.secondary.500` (Exercise green)
- Focus / accent / links → `colors.accent.500` (Stand cyan)
- Body text → `colors.text.primary` (#F4F4F4)
- Muted / secondary text → `colors.text.secondary` (#AEAEB2)
- Ring empty track → `colors.neutral.700` (#3A3A3C)

## Typography

All type is Inter — the Google Fonts analog of Apple's SF Pro. Heavy use of bold and semibold weights in uppercase for metric labels and stat headings creates the industrial-instrument-panel density of the Activity app. IBM Plex Mono appears sparingly for pace, cadence, and technical readouts where tabular alignment is critical. No serif anywhere — this is hardware-grade sans-only typography. Tabular figures (`font-variant-numeric: tabular-nums`) are mandatory for all numeric data.

**Text styles**:
- `display-xl` — Inter, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Inter, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Inter, 48px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-2` — Inter, 32px, weight 600, line-height 1.2, letter-spacing 0
- `body-lg` — Inter, 18px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 12px, weight 600, line-height 1.25, letter-spacing 0.05em, uppercase
- `mono-md` — IBM Plex Mono, 14px, weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px
- Grid: 12-column, 16px gap default, 24px at large breakpoints
- Section padding: 64px vertical (md), 96px (lg)
- Card internal padding: 24px
- Dense metric grids use 8px gap for stat-table tightness

## Elevation & Depth

Apple Fitness uses a zero-elevation aesthetic. There are no drop shadows — depth is communicated exclusively through surface color stepping (black → #1C1C1E → #2C2C2E) and 1px hairline borders at `rgba(255,255,255,0.08)`. This mirrors Apple's OLED-first philosophy where true black pixels are literally off, creating physical depth between lit surfaces and the void.

- Surfaces: flat matte charcoal cards, no blur, no glass
- Borders: 1px `rgba(255,255,255,0.08)` hairlines as sole elevation cue
- Shadow ladder: all levels use inset hairline borders, not box-shadow blur
- Focus state: 3px cyan ring (`0 0 0 3px rgba(30,234,239,0.4)`)

## Shapes

- Button radius: 12px (Apple-industrial-product round)
- Card radius: 16px
- Input radius: 12px
- Small elements (tags, badges): 8px
- Pill / toggle: 9999px (full)
- No sharp corners anywhere — minimum 8px

## Motion

Motion is restrained and purposeful — the only animated element that matters is the ring-fill arc. Everything else uses quick, imperceptible transitions that don't compete with data updates. Apple's Activity app animates ring progress at ~400ms with a decelerating ease, while UI transitions are 120–250ms. No bouncy springs, no playful overshoots — this is instrument-panel precision.

- Level: restrained
- Ring-fill animation: 400ms, ease-out
- UI transitions: 120ms (hover), 250ms (state change)
- Easing: `cubic-bezier(0.25, 0.1, 0.25, 1)` — Apple's system curve
- Hover patterns: opacity fade, subtle scale (1.02), tint shift
- Reduced motion: respected — ring fills snap to final state

## Techniques

### Ring-fill arc (SVG/CSS)
The canonical three-rings hero motif — concentric circular progress arcs with rounded stroke caps on pure black.
```css
.ring {
  fill: none;
  stroke-linecap: round;
  stroke-width: 18px;
  transform: rotate(-90deg);
  transform-origin: center;
  transition: stroke-dashoffset 400ms cubic-bezier(0.25, 0.1, 0.25, 1);
}
.ring--move { stroke: #FA114F; }
.ring--exercise { stroke: #92E82A; }
.ring--stand { stroke: #1EEAEF; }
.ring-track { stroke: #3A3A3C; stroke-width: 18px; fill: none; }
```

### Metric stat card
Dense calorie/step/distance readout card with uppercase caption labels and tabular mono figures.
```css
.stat-card {
  background: #1C1C1E;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 20px 24px;
}
.stat-card__label {
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #AEAEB2;
}
.stat-card__value {
  font-family: 'Inter', sans-serif;
  font-size: 2.25rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #F4F4F4;
  line-height: 1.1;
}
```

### Sweat-glow radial vignette
Subtle radial gradient vignette behind athlete portraits or ring heroes — the only gradient permitted in the system.
```css
.sweat-glow {
  position: relative;
}
.sweat-glow::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at 50% 40%,
    rgba(250, 17, 79, 0.15) 0%,
    transparent 70%
  );
  pointer-events: none;
}
```

## Iconography

Icons are linear/outline style at 1.5px stroke weight, matching Inter's geometric precision. Lucide icons are preferred for their clean geometry and consistent optical sizing. Icons appear in `#AEAEB2` (secondary text) by default, shifting to ring colors for active/selected states.

- Treatment: linear outline
- Set: Lucide
- Stroke: 1.5px, round caps and joins

## Do's & Don'ts

### ✓ Do
- Use pure OLED black (#000000) as the page background — never charcoal or dark grey
- Apply Move magenta (#FA114F) for all primary actions and CTAs
- Use uppercase + letter-spacing for metric labels and captions
- Maintain tabular-nums on all numeric data for alignment
- Compose asymmetric layouts: ring hero on one side, stat grid on the other

### ✗ Don't
- Use beige, cream, or parchment backgrounds — page is pure OLED black
- Apply generic neon-rainbow fitness palettes — only the three ring colors
- Use stock smiling-gym-person photography that doesn't earn the sweat
- Add Material-Design elevation drop shadows — Apple uses hairline borders only
- Soften into pastel "wellness" register — Apple Fitness is high-intensity
- Center hero compositions symmetrically — always asymmetric ring + stat-grid
- Include cute fitness mascot illustrations
- Substitute Helvetica or Geist for Inter
- Apply skeuomorphic 3D-bevel effects to rings — they are flat saturated arcs
- Use bright-white-page register — this is dark-mode-first, always

## Applications

This system is ideal for fitness dashboards, health-tracking apps, wearable companion interfaces, and training-day stat-dense UIs. It excels at presenting dense biometric data (calories, heart rate, distance, pace) in a way that feels urgent and rewarding rather than clinical. Best suited for dark-mode-first products where data visualization is the hero element.
