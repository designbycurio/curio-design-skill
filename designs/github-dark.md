---
version: 1

meta:
  id: github-dark
  name: GitHub Dark
  description: "GitHub's signature cool-blue-tinted dark interface — the most-used dark UI on the web for technical users"
  isDark: true
  tags: [tech, modernist, editorial, minimal, professional]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2008 founded; dark mode launched September 2020; stable through 2024"
  region: "San Francisco, California"
  regionZh: "美国旧金山，加利福尼亚"
  keyFigures: ["Diana Mounter", "Tom Preston-Werner", "Mona the Octocat"]
  movements: ["Primer Design System", "Developer tool aesthetic", "Terminal-inspired UI"]

introduction: |
  GitHub Dark is the canonical dark interface for the world's largest code hosting platform. Launched in September 2020, it rapidly became the most widely used dark UI among technical users, setting the visual standard for modern developer tools. Its design language centers on a distinctive cool-blue-tinted canvas (#0d1117) — neither pure black nor neutral grey — paired with semantic colors that communicate code review states at a glance.

  Built on the open-source Primer Design System, GitHub Dark prioritizes information density and readability over decoration. Every choice serves the code: tight grids, monospace-friendly layouts, crisp 1px borders instead of shadows, and a restrained palette where green means merge and red means conflict. It is utilitarian design elevated to an aesthetic.
introductionZh: |
  GitHub Dark 是全球最大代码托管平台的标志性暗色界面。自2020年9月推出以来，它迅速成为技术用户中使用最广泛的暗色 UI，为现代开发者工具定义了视觉标准。其设计语言以独特的冷蓝色调画布（#0d1117）为核心——既非纯黑也非中性灰——搭配在代码审查中一目了然的语义色彩体系。

  GitHub Dark 基于开源的 Primer 设计系统构建，优先考虑信息密度与可读性而非装饰。每一个设计决策都服务于代码本身：紧凑的网格、等宽字体友好的排版、以清晰的1像素边框替代阴影，以及克制的调色板——绿色代表合并，红色代表冲突。这是将实用主义设计提升至美学高度的典范。

colors:
  primary:
    "50": "#e6f3ff"
    "100": "#c0dfff"
    "200": "#94c8ff"
    "300": "#6db1ff"
    "400": "#58a6ff"
    "500": "#58a6ff"
    "600": "#4090e0"
    "700": "#2d7ac4"
    "800": "#1b5fa0"
    "900": "#0e4480"
    "950": "#072a5c"
  secondary:
    "50": "#e6fbe8"
    "100": "#b8f0be"
    "200": "#86e490"
    "300": "#56d864"
    "400": "#3fb950"
    "500": "#3fb950"
    "600": "#2ea043"
    "700": "#238636"
    "800": "#196c2e"
    "900": "#0f5323"
    "950": "#083b17"
  accent:
    "50": "#f1eafe"
    "100": "#dacbfc"
    "200": "#c2a9fa"
    "300": "#a882f7"
    "400": "#8b5cf6"
    "500": "#8b5cf6"
    "600": "#7c3aed"
    "700": "#6d28d9"
    "800": "#5b21b6"
    "900": "#4c1d95"
    "950": "#3b0f7a"
  neutral:
    "50": "#f0f6fc"
    "100": "#c9d1d9"
    "200": "#b1bac4"
    "300": "#8b949e"
    "400": "#6e7681"
    "500": "#484f58"
    "600": "#30363d"
    "700": "#21262d"
    "800": "#161b22"
    "900": "#0d1117"
    "950": "#010409"
  semantic:
    success: { bg: "#238636", text: "#3fb950", light: "#0f5323", border: "#2ea043" }
    warning: { bg: "#9e6a03", text: "#d29922", light: "#4b2900", border: "#bb8009" }
    error:   { bg: "#da3633", text: "#f85149", light: "#490202", border: "#f85149" }
    info:    { bg: "#1f6feb", text: "#58a6ff", light: "#0c2d6b", border: "#388bfd" }
  background:
    page:    "#0d1117"
    surface: "#161b22"
    subtle:  "#21262d"
  text:
    primary:   "#c9d1d9"
    secondary: "#8b949e"
    muted:     "#484f58"
    inverse:   "#0d1117"

typography:
  families:
    heading: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    body:    "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    mono:    "'JetBrains Mono', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap"
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
  radius: { none: "0", sm: "4px", md: "6px", lg: "8px", xl: "12px", full: "9999px" }
  color:  { default: "#30363d", subtle: "#21262d", strong: "#484f58", focus: "#58a6ff" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(1,4,9,0.3)"
  sm: "0 2px 4px rgba(1,4,9,0.3)"
  md: "0 4px 8px rgba(1,4,9,0.3)"
  lg: "0 8px 16px rgba(1,4,9,0.35)"
  xl: "0 12px 24px rgba(1,4,9,0.4)"
  "2xl": "0 24px 48px rgba(1,4,9,0.5)"
  inner: "inset 0 1px 2px rgba(1,4,9,0.2)"
  focus: "0 0 0 3px rgba(88,166,255,0.4)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "120ms", normal: "200ms", slow: "300ms", slower: "450ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.16, 1, 0.3, 1)"
  hoverPatterns: [tint, opacity, underline]
  reducedMotion: true

composition:
  layout:        "flex"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "subtle"
  rhythm:        "4px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "outline"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:   { background: "#238636", color: "#ffffff", border: "1px solid rgba(240,246,252,0.1)", shadow: "none", hoverBackground: "#2ea043", hoverShadow: "none", hoverColor: "#ffffff" }
    secondary: { background: "#21262d", color: "#c9d1d9", border: "1px solid #30363d", shadow: "none", hoverBackground: "#30363d", hoverShadow: "none", hoverColor: "#c9d1d9" }
    ghost:     { background: "transparent", color: "#58a6ff", border: "1px solid transparent", shadow: "none", hoverBackground: "rgba(88,166,255,0.1)", hoverShadow: "none", hoverColor: "#58a6ff" }
    danger:    { background: "#da3633", color: "#ffffff", border: "1px solid rgba(240,246,252,0.1)", shadow: "none", hoverBackground: "#f85149", hoverShadow: "none", hoverColor: "#ffffff" }
    sizes:
      sm: { height: "28px", padding: "0 12px", fontSize: "0.75rem" }
      md: { height: "32px", padding: "0 16px", fontSize: "0.875rem" }
      lg: { height: "40px", padding: "0 20px", fontSize: "1rem" }
    borderRadius: "6px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#0d1117"
    color: "#c9d1d9"
    border: "1px solid #30363d"
    borderRadius: "6px"
    padding: "5px 12px"
    focusBorder: "#58a6ff"
    placeholderColor: "#484f58"
  card:
    base:  { background: "#0d1117", border: "1px solid #30363d", borderRadius: "6px", padding: "16px", shadow: "none" }
    hover: { shadow: "none", transform: "none" }
---

# GitHub Dark

> The web's canonical dark interface for code — cool-blue canvas, semantic diff colors, and zero decoration.

## Origin

GitHub was founded in 2008 by Tom Preston-Werner, Chris Wanstrath, PJ Hyett, and Scott Chacon as a hosting platform for Git repositories. It rapidly became the world's largest code collaboration platform, acquired by Microsoft in 2018. GitHub's dark mode launched in September 2020 to massive demand, built by the Primer design systems team led by Diana Mounter.

The visual language of GitHub Dark draws from terminal aesthetics — the cool-blue tones of Solarized Dark, the information density of Atom editor (GitHub's own text editor), and the utilitarian tradition of UNIX interfaces. The Primer Design System (primer.style) codifies these choices as open-source design tokens, making GitHub's aesthetic one of the most-imitated in modern developer tooling. Linear, Vercel, and Resend all descend from this lineage.

## Overview
Composition cues:
- **Layout**: flex-based, predominantly vertical stacking with horizontal nav bars and sidebar layouts
- **Content width**: container (max ~1280px) with generous padding
- **Framing**: bordered — crisp 1px borders define every surface; shadows are nearly absent
- **Grid intensity**: subtle — 4px base unit, tight spacing, high information density

## Colors
GitHub Dark's palette is built on a single principle: cool-blue-tinted neutrals, never warm, never pure black. The canvas (#0d1117) sits halfway between charcoal and navy, creating a surface that reduces eye strain during extended coding sessions while maintaining high contrast for syntax highlighting. Semantic colors are paramount — green (#3fb950) and red (#f85149) carry the weight of code review, while accent blue (#58a6ff) serves as the primary interactive color. Mona purple (#8b5cf6) appears sparingly for special features and brand moments.

**Role usage**:
- Page background → `colors.background.page` (#0d1117)
- Card/surface background → `colors.background.surface` (#161b22)
- Primary actions & links → `colors.primary.500` (#58a6ff)
- Merge/success actions → `colors.secondary.500` (#3fb950)
- Danger/destructive → `colors.semantic.error.text` (#f85149)
- Borders & dividers → `borders.color.default` (#30363d)
- Body text → `colors.text.primary` (#c9d1d9)
- Muted text → `colors.text.secondary` (#8b949e)

## Typography
GitHub's type voice is neutral and invisible — the interface disappears so the code can speak. Inter at semibold serves headings with just enough weight to establish hierarchy without shouting. Body text in Inter regular at 14-16px prioritizes scanability across dense lists of repositories, issues, and pull requests. JetBrains Mono handles all code display, chosen for its clear glyph differentiation at small sizes and ligature support.

**Text styles**:
- `display-xl` — Inter, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Inter, 64px, weight 700, line-height 1.05, letter-spacing -0.04em
- `heading-1` — Inter, 32px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Inter, 18px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — Inter, 14px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 12px, weight 400, line-height 1.375, letter-spacing 0
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container widths: sm 640 / md 768 / lg 1024 / xl 1280px
- Section padding: 32 / 64 / 96 / 128px vertical
- Grid gap: 8 / 16 / 24 / 48px
- Component internal padding: 12-16px horizontal, 4-8px vertical (compact)

## Elevation & Depth
GitHub Dark is radically flat. There is no elevation hierarchy through shadows — surfaces are differentiated purely through background color steps (page → surface → subtle) and 1px borders. This creates a map-like reading experience where every element sits on the same plane, connected by visible edges rather than implied depth.

- Surface style: flat — no gradients, no glass, no blur
- Blur: none
- Shadow ladder: virtually unused; focus ring (0 0 0 3px rgba(88,166,255,0.4)) is the only common shadow
- Elevation is communicated through border prominence and background color shifts

## Shapes
- Card/button radius: 6px (GitHub's signature radius)
- Input radius: 6px
- Pill/tag radius: 9999px (full)
- Avatar radius: 9999px (circle)
- No radius: 0 for inline code blocks and table cells

## Motion
GitHub's motion is restrained and functional — transitions exist to confirm interaction, not to entertain. Most state changes (hover, focus) resolve in under 200ms. Page-level animations are essentially absent; navigation is instant. This telegraphs reliability and speed, core values for a tool developers use 8+ hours daily.

- Level: restrained
- Hover transitions: 120-200ms
- Easings: default cubic-bezier(0.4, 0, 0.2, 1) for most transitions
- Hover patterns: tint (background lightens one neutral step), opacity (icons fade in), underline (text links)
- No entrance animations, no parallax, no decorative motion
- Reduced motion: fully supported

## Techniques

### Diff-line color coding
GitHub's iconic code review coloring — addition lines get a green-tinted background, deletions get red-tinted, with the specific changed characters highlighted more intensely.
```css
.diff-line-add {
  background-color: rgba(63, 185, 80, 0.15);
  border-left: 3px solid #3fb950;
}
.diff-line-add .highlight {
  background-color: rgba(63, 185, 80, 0.4);
}
.diff-line-remove {
  background-color: rgba(248, 81, 73, 0.15);
  border-left: 3px solid #f85149;
}
.diff-line-remove .highlight {
  background-color: rgba(248, 81, 73, 0.4);
}
```

### One-pixel border card
GitHub's universal container pattern — no shadow, just a crisp 1px border on the cool-blue-grey #30363d, with a slightly elevated surface fill.
```css
.gh-card {
  background: #0d1117;
  border: 1px solid #30363d;
  border-radius: 6px;
  padding: 16px;
  transition: border-color 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.gh-card:hover {
  border-color: #484f58;
}
```

### Merge button gradient
GitHub's primary action button for merging pull requests — a solid green that lightens on hover, with a subtle inner border for dimension against the dark canvas.
```css
.merge-button {
  background-color: #238636;
  color: #ffffff;
  border: 1px solid rgba(240, 246, 252, 0.1);
  border-radius: 6px;
  padding: 5px 16px;
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;
  transition: background-color 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.merge-button:hover {
  background-color: #2ea043;
}
.merge-button:focus {
  box-shadow: 0 0 0 3px rgba(46, 160, 67, 0.4);
  outline: none;
}
```

## Iconography
GitHub uses Octicons, its own open-source icon set, characterized by clean outlined strokes at 16px and 24px sizes. For this system, Lucide serves as the closest general-purpose equivalent — both share the same 1.5px stroke weight, rounded joins, and preference for geometric simplicity over decorative detail.

- Treatment: outline
- Set: Lucide (standing in for Octicons)
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use the cool-blue canvas #0d1117 as the base — it defines the GitHub Dark identity
- Use 1px borders (#30363d) as the primary means of visual separation
- Reserve green (#238636 / #3fb950) for positive and merge-related actions
- Keep typography in Inter at 14px base for high-density information display
- Use JetBrains Mono for all code presentation, diffs, and terminal output

### ✗ Don't
- Use warm or sepia-tinted dark backgrounds — GitHub is distinctly cool-toned
- Use pure black #000000 anywhere in the palette
- Apply decorative gradients to surfaces or backgrounds
- Use serif fonts — GitHub's identity is entirely sans-serif and monospace
- Rely on heavy shadows for depth — use borders and background color steps instead

## Applications
GitHub Dark is purpose-built for developer-facing interfaces: code editors, repository browsers, CI/CD dashboards, documentation sites, and API consoles. Its high information density and semantic color system make it ideal for any application where users spend extended hours reading structured data. It translates naturally to admin panels, analytics dashboards, and technical documentation platforms where clarity and scanability outweigh visual flair.
