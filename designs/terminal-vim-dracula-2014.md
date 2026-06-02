---
version: 1

meta:
  id: terminal-vim-dracula-2014
  name: Terminal Vim Dracula (2014)
  description: "Saturated six-color syntax palette over near-black blue-gray — the terminal is the interface"
  isDark: true
  tags: [tech, subcultural, minimal, professional, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2014 created; explosive adoption 2015–2024; v3.0+ active through 2024"
  region: "Online / open-source — São Paulo, Brazil origin"
  regionZh: "线上开源社区 / 巴西圣保罗"
  keyFigures: [Zeno Rocha, Derek Sivers, Pranesh Prakash]
  movements: [developer-tool dark-mode normalization, open-source-theme-as-brand, terminal-aesthetics-as-lifestyle]

introduction: |
  Dracula is the dark color scheme Zeno Rocha released in 2014 that became the most-installed dark theme across developer tools — six saturated accent colors (purple, pink, green, cyan, orange, yellow) floating over a slightly purple-shifted near-black background. Its vocabulary is monospace type, syntax highlighting, terminal prompts, and Powerline glyphs.

  The design system treats the screen as an editor pane: everything is monospaced, colors signal semantic meaning like syntax tokens, and surfaces stack like split terminal panels. It is rigorously flat, rectilinear, and unapologetically dark.
introductionZh: |
  Dracula 是巴西开发者 Zeno Rocha 于 2014 年发布的暗色配色方案，凭借六种高饱和度强调色（紫、粉、绿、青、橙、黄）覆盖在略带紫调的近黑背景上，迅速成为全球开发者工具中安装量最大的暗色主题，已移植至 300 余款编辑器与终端。

  该设计系统将屏幕视为编辑器窗格：一切皆等宽字体，色彩如语法高亮般承载语义，面板如终端分屏般层叠排列。风格极度扁平、直角、纯粹暗色——属于终端美学的生活方式宣言。

colors:
  primary:
    "50": "#f3ecfe"
    "100": "#e5d6fd"
    "200": "#ccaefb"
    "300": "#b285f9"
    "400": "#BD93F9"
    "500": "#BD93F9"
    "600": "#a06ef7"
    "700": "#8349f0"
    "800": "#6625e0"
    "900": "#4c1aab"
    "950": "#2e1066"
  secondary:
    "50": "#fff0f7"
    "100": "#ffe0ef"
    "200": "#ffc2df"
    "300": "#ff99c8"
    "400": "#FF79C6"
    "500": "#FF79C6"
    "600": "#e04da3"
    "700": "#bf2d80"
    "800": "#991a62"
    "900": "#731248"
    "950": "#4a0a2e"
  accent:
    "50": "#edfff3"
    "100": "#d5ffe4"
    "200": "#a8ffca"
    "300": "#78fda8"
    "400": "#50FA7B"
    "500": "#50FA7B"
    "600": "#30d95c"
    "700": "#1fb347"
    "800": "#168c36"
    "900": "#10662a"
    "950": "#083d19"
  neutral:
    "50": "#f8f8f2"
    "100": "#e8e8e0"
    "200": "#c8c8c0"
    "300": "#9999a0"
    "400": "#6272A4"
    "500": "#6272A4"
    "600": "#515e85"
    "700": "#44475A"
    "800": "#343648"
    "900": "#282A36"
    "950": "#21222C"
  semantic:
    success: { bg: "#50FA7B", text: "#282A36", light: "#2a4a35", border: "#50FA7B" }
    warning: { bg: "#F1FA8C", text: "#282A36", light: "#3a3a28", border: "#F1FA8C" }
    error:   { bg: "#FF5555", text: "#F8F8F2", light: "#4a2020", border: "#FF5555" }
    info:    { bg: "#8BE9FD", text: "#282A36", light: "#1e3a40", border: "#8BE9FD" }
  background:
    page:    "#282A36"
    surface: "#44475A"
    subtle:  "#21222C"
  text:
    primary:   "#F8F8F2"
    secondary: "#BD93F9"
    muted:     "#6272A4"
    inverse:   "#282A36"

typography:
  families:
    heading: "'JetBrains Mono', 'Fira Code', monospace"
    body:    "'JetBrains Mono', 'Fira Code', monospace"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Fira+Code:wght@300;400;500;600;700&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,400&display=swap"
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
  radius: {none: "0", sm: "2px", md: "4px", lg: "6px", xl: "8px", full: "9999px"}
  color:  {default: "#44475A", subtle: "#343648", strong: "#6272A4", focus: "#BD93F9"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0, 0, 0, 0.3)"
  sm: "0 2px 4px rgba(0, 0, 0, 0.35)"
  md: "0 4px 12px rgba(0, 0, 0, 0.4)"
  lg: "0 8px 24px rgba(0, 0, 0, 0.45)"
  xl: "0 12px 36px rgba(0, 0, 0, 0.5)"
  "2xl": "0 20px 48px rgba(0, 0, 0, 0.6)"
  inner: "inset 0 1px 2px rgba(0, 0, 0, 0.3)"
  focus: "0 0 0 3px rgba(189, 147, 249, 0.4)"

motion:
  level: "minimal"
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "350ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [tint, opacity, glow]
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
    primary:   {background: "#BD93F9", color: "#282A36", border: "none", shadow: "none", hoverBackground: "#a06ef7", hoverShadow: "0 0 0 3px rgba(189, 147, 249, 0.3)", hoverColor: "#282A36"}
    secondary: {background: "transparent", color: "#FF79C6", border: "1px solid #FF79C6", shadow: "none", hoverBackground: "rgba(255, 121, 198, 0.1)", hoverShadow: "none", hoverColor: "#FF79C6"}
    ghost:     {background: "transparent", color: "#F8F8F2", border: "none", shadow: "none", hoverBackground: "#44475A", hoverShadow: "none", hoverColor: "#F8F8F2"}
    danger:    {background: "#FF5555", color: "#F8F8F2", border: "none", shadow: "none", hoverBackground: "#e03030", hoverShadow: "none", hoverColor: "#F8F8F2"}
    sizes:     {sm: {height: "28px", padding: "4px 12px", fontSize: "0.75rem"}, md: {height: "36px", padding: "6px 16px", fontSize: "0.875rem"}, lg: {height: "44px", padding: "8px 24px", fontSize: "1rem"}}
    borderRadius: "4px"
    fontWeight: 500
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#21222C"
    color: "#F8F8F2"
    border: "1px solid #44475A"
    borderRadius: "4px"
    padding: "8px 12px"
    focusBorder: "#BD93F9"
    placeholderColor: "#6272A4"
  card:
    base:  {background: "#44475A", border: "1px solid #6272A4", borderRadius: "6px", padding: "16px", shadow: "0 4px 12px rgba(0, 0, 0, 0.4)"}
    hover: {shadow: "0 8px 24px rgba(0, 0, 0, 0.45)", transform: "translateY(-1px)"}
---

# Terminal Vim Dracula (2014)

> The screen is the page; the page is the editor; the editor is the terminal — everything is monospace and the colors are the syntax.

## Origin

Dracula was created by Brazilian developer Zeno Rocha in August 2014 as a dark color scheme for Vim and terminal emulators. Its six saturated accent colors — purple, pink, green, cyan, orange, yellow — over a distinctive blue-gray-near-black background (#282A36, 6.5% luminance) proved so visually coherent that the community ported it to over 300 developer tools within a decade. By 2024 the VSCode extension alone had surpassed 10 million installs, making Dracula the most widely adopted dark theme in software development.

The scheme emerged from the 2010s wave of developer-tool dark-mode normalization and the r/unixporn community's elevation of terminal aesthetics into lifestyle expression. Dracula's success as open-source-theme-as-brand — with a consistent spec, a PRO tier, and hundreds of volunteer port-maintainers — established a template for how color schemes could become recognizable design identities beyond any single application.

## Overview

Composition cues:
- **Layout**: Split-pane grid mimicking terminal/editor window tiling — vertical and horizontal divisions
- **Content width**: Container (88ch optimal line-length, reflecting code-column conventions)
- **Framing**: Solid flat panels with hairline dividers (tab-bar / panel-divider aesthetic)
- **Grid intensity**: Strong — 16-column code-grid with visible structural rhythm

## Colors

The Dracula palette is a six-color syntax system designed for maximum readability on a near-black surface. Each hue carries semantic weight borrowed from code highlighting: purple for primary actions (functions/keywords), pink for secondary emphasis (tags/syntax), green for success/confirmation (strings), cyan for informational (built-ins), orange for caution (parameters), and yellow for warnings (variables). The background is not pure black but a slightly purple-shifted blue-gray that reduces eye strain during extended sessions.

**Role usage**:
- Page background → `colors.background.page` (#282A36)
- Panel / card surfaces → `colors.background.surface` (#44475A)
- Nested / deeper panels → `colors.background.subtle` (#21222C)
- Primary text → `colors.text.primary` (#F8F8F2)
- Muted / comment text → `colors.text.muted` (#6272A4)
- Primary accent / CTA → `colors.primary.500` (#BD93F9)
- Secondary accent → `colors.secondary.500` (#FF79C6)
- Success / confirmation → `colors.accent.500` (#50FA7B)

## Typography

All typography is monospaced — this is a mono-religion system. JetBrains Mono serves as the universal typeface for headings, body, and code, with ligature support enabled. DM Mono provides a lighter editorial accent for non-code display moments. No proportional typefaces appear anywhere in the system; the fixed-width grid IS the typographic identity.

**Text styles**:
- `display-xl` — JetBrains Mono, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — JetBrains Mono, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — JetBrains Mono, 48px, weight 600, line-height 1.2, letter-spacing -0.02em
- `heading-2` — JetBrains Mono, 36px, weight 600, line-height 1.2, letter-spacing 0
- `body-lg` — JetBrains Mono, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — JetBrains Mono, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — JetBrains Mono, 12px, weight 400, line-height 1.5, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1024px (lg) for content; 1280px (xl) for dashboards
- Section padding: 64px vertical (md), 96px (lg) for hero sections
- Grid gap: 16px default between panes; 8px for tight panel splits
- Optimal line-length: 88 characters (monospace column convention)

## Elevation & Depth

Dracula is rigorously flat. There is no material depth metaphor — surfaces are distinguished by background color steps (#21222C → #282A36 → #44475A) rather than shadows. Shadows exist only for floating elements (dropdowns, modals) and are dark, tight, and functional rather than decorative. The focus ring (purple glow) is the primary depth signal for interactive states.

- Surfaces stack via background-color differentiation, not blur or shadow
- Shadow ladder reserved for overlays: `0 4px 12px rgba(0,0,0,0.4)` for cards, `0 8px 24px` for modals
- No blur, no glass, no gradients on surfaces
- Focus state: `0 0 0 3px rgba(189, 147, 249, 0.4)` purple ring

## Shapes

- Button radius: 4px (editor-pane sharpness)
- Card radius: 6px
- Input radius: 4px
- Maximum radius: 8px (no pill shapes, no heavy rounding)
- Panel dividers: 1px hairlines in `#44475A`

## Motion

Motion is minimal and functional — matching the instantaneous feedback of a terminal cursor. Transitions exist only to confirm state changes (hover, focus, selection), never for decoration or delight. The cursor-blink cadence and selection-highlight flash are the only ornamental motion patterns.

- Level: minimal
- Hover transitions: 100–200ms
- Easing: `cubic-bezier(0.4, 0, 0.2, 1)` (standard ease-out)
- Hover patterns: tint (background color shift), opacity fade, purple glow on focus
- No entrance animations, no scroll-triggered motion
- `prefers-reduced-motion` respected — disables all transitions

## Techniques

### Syntax-highlight accent bar
A left-border color accent on panels that mimics the gutter-highlight pattern in code editors.
```css
.element {
  border-left: 3px solid #BD93F9;
  background: #44475A;
  padding: 16px 16px 16px 20px;
}
```

### Terminal prompt badge
Inline badge styled as a terminal prompt prefix with Dracula colors.
```css
.element {
  display: inline-flex;
  align-items: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  background: #21222C;
  color: #50FA7B;
  padding: 2px 8px;
  border-radius: 2px;
  border: 1px solid #44475A;
}
.element::before {
  content: '❯ ';
  color: #BD93F9;
}
```

### Selection highlight row
Full-width current-line highlight for active/selected list items, mimicking editor cursor-line.
```css
.element {
  background: #44475A;
  box-shadow: inset 3px 0 0 #BD93F9;
  padding: 8px 16px 8px 20px;
  border-radius: 0;
  transition: background 100ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Iconography

Icons follow the linear/outline treatment at 1.5px stroke weight, matching the monospace grid's precision. Lucide icons are preferred for their geometric clarity and consistent optical weight at small sizes.

- Treatment: linear (outline only)
- Set: Lucide
- Stroke: 1.5px, square line-caps

## Do's & Don'ts

### ✓ Do
- Use JetBrains Mono for ALL text — headings, body, labels, everything
- Apply Dracula purple (#BD93F9) for primary interactive elements and focus states
- Treat accent colors as syntax tokens: each hue carries consistent semantic meaning
- Build layouts as split-pane grids mimicking terminal window tiling
- Use background-color steps (#21222C → #282A36 → #44475A) for depth, not shadows

### ✗ Don't
- Use non-monospace typography anywhere (rigorously mono)
- Apply light-mode backgrounds (Dracula is forever dark)
- Soften or pastel-ify the six accent colors (must be saturated official spec values)
- Add decorative ornament (sharp editor minimalism only)
- Use photographic imagery (use code listings, terminal screenshots, schematic diagrams)
- Apply drop shadows on text (flat editor surfaces)
- Use curve-heavy 16px+ rounded corners (editor panels are rectilinear)

## Applications

This system is ideal for developer tools, CLI documentation sites, code-focused portfolios, and technical dashboards. It excels anywhere the audience expects a terminal-native aesthetic — package registry pages, API documentation, open-source project landing pages, and developer blog themes where monospace typography and syntax-color semantics feel native rather than affected.
