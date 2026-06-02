---
version: 1

meta:
  id: the-matrix-green-code-1999
  name: The Matrix (Green-Code)
  description: Saturated CRT-green falling-character code rain on deep black, terminal-monospace cyberpunk discipline.
  isDark: true
  tags: [bold, futuristic, narrative, experimental, subcultural]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1999 (Warner Bros. release); cultural-impact ongoing through Matrix Reloaded / Revolutions (2003) and Resurrections (2021)"
  region: "USA — Hollywood (production), Sydney (principal photography)"
  regionZh: "美国好莱坞（出品）·澳大利亚悉尼（拍摄地）"
  keyFigures: ["The Wachowskis", "Bill Pope", "Owen Paterson", "Don Davis"]
  movements: ["late-1990s cyberpunk cinema", "post-Ghost-in-the-Shell digital mythology", "terminal aesthetic"]

introduction: |
  The Matrix (1999) crystallised cyberpunk for a mainstream audience: saturated CRT-green katakana raining down a deep-black terminal, monospace text as the very fabric of reality, and a philosophy of waking up from simulation. The look is austere, technical, and mythic — a desktop pretending to be a cathedral.

  This system bottles that aesthetic for product use: two-tone Matrix-green and near-black, monospace typography as headline voice, hairline rules, zero-radius CTAs, and a phosphor glow that suggests the screen itself is leaking light. It is restrained, not decorative — every element earns its place on the grid.

introductionZh: |
  1999 年华纳兄弟发行的《黑客帝国》是赛博朋克美学的世俗化里程碑：沃卓斯基姐妹把日文片假名做成绿色雨水从黑色终端上落下，让等宽字体本身成为现实的肌理，把"从模拟中觉醒"这件事讲成了现代神话。整个视觉只有两种东西在工作——饱和的 CRT 矩阵绿，以及近乎纯黑的底色。

  这套系统把那种克制又神秘的气质装进产品里：双色严守、等宽字体担当标题、1 像素发光绿色细线作为分隔、按钮零圆角、阴影是从屏幕里渗出的磷光晕。不做装饰，不堆元素，每一寸像素都要回答"它在终端里出现的理由"。整体气场像一台被供奉起来的旧 CRT 显示器，冷峻、虔诚，又有点危险。

colors:
  primary:
    "50":  "#E6FFEE"
    "100": "#B8FFCE"
    "200": "#80FFA8"
    "300": "#4DFF82"
    "400": "#26FF61"
    "500": "#00FF41"
    "600": "#00E63A"
    "700": "#00CC34"
    "800": "#009926"
    "900": "#006619"
    "950": "#00330D"
  secondary:
    "50":  "#E6E6E6"
    "100": "#C2C2C2"
    "200": "#9E9E9E"
    "300": "#7A7A7A"
    "400": "#4F4F4F"
    "500": "#0A0A0A"
    "600": "#080808"
    "700": "#060606"
    "800": "#040404"
    "900": "#020202"
    "950": "#000000"
  accent:
    "50":  "#EDEDED"
    "100": "#D6D6D6"
    "200": "#B3B3B3"
    "300": "#8A8A8A"
    "400": "#5C5C5C"
    "500": "#3A3A3A"
    "600": "#2F2F2F"
    "700": "#252525"
    "800": "#1B1B1B"
    "900": "#121212"
    "950": "#0A0A0A"
  neutral:
    "50":  "#F5F5F5"
    "100": "#E0E0E0"
    "200": "#BDBDBD"
    "300": "#9E9E9E"
    "400": "#8A8A8A"
    "500": "#6F6F6F"
    "600": "#5A5A5A"
    "700": "#3F3F3F"
    "800": "#2A2A2A"
    "900": "#1A1A1A"
    "950": "#0A0A0A"
  semantic:
    success: { bg: "#00330D", text: "#00FF41", light: "#006619", border: "#00CC34" }
    warning: { bg: "#332600", text: "#FFC400", light: "#664D00", border: "#CC9D00" }
    error:   { bg: "#330505", text: "#FF3B3B", light: "#660A0A", border: "#CC2929" }
    info:    { bg: "#001A33", text: "#4DA6FF", light: "#003366", border: "#1A8CFF" }
  background:
    page:    "#0A0A0A"
    surface: "#1A1A1A"
    subtle:  "#121212"
  text:
    primary:   "#00FF41"
    secondary: "#9E9E9E"
    muted:     "#6F6F6F"
    inverse:   "#0A0A0A"

typography:
  families:
    heading: "'Source Code Pro', 'JetBrains Mono', 'Roboto Mono', 'Fira Code', ui-monospace, monospace"
    body:    "'Inter', 'Helvetica', system-ui, -apple-system, Arial, sans-serif"
    mono:    "'Source Code Pro', 'Roboto Mono', 'JetBrains Mono', 'Fira Code', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Roboto+Mono:wght@400;500;700&family=Fira+Code:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
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
  radius: {none: "0", sm: "2px", md: "2px", lg: "4px", xl: "6px", full: "9999px"}
  color:  {default: "#00CC34", subtle: "#1A1A1A", strong: "#00FF41", focus: "#00FF41"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0, 255, 65, 0.08)"
  sm: "0 2px 6px rgba(0, 255, 65, 0.12)"
  md: "0 6px 20px rgba(0, 255, 65, 0.20)"
  lg: "0 10px 32px rgba(0, 255, 65, 0.28)"
  xl: "0 18px 48px rgba(0, 255, 65, 0.32)"
  "2xl": "0 28px 72px rgba(0, 255, 65, 0.40)"
  inner: "inset 0 1px 2px rgba(0, 0, 0, 0.65)"
  focus: "0 0 0 3px rgba(0, 255, 65, 0.45)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.7, 0, 1, 0.4)"
    out:     "cubic-bezier(0, 0.6, 0.3, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [glow, stroke, opacity, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        "8px"

surfaceStyle: solid
blur:         "none"

iconography:
  treatment: linear
  set:       lucide
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "#00FF41"
      color: "#0A0A0A"
      border: "1px solid #00FF41"
      shadow: "0 0 0 0 rgba(0, 255, 65, 0)"
      hoverBackground: "#26FF61"
      hoverShadow: "0 6px 20px rgba(0, 255, 65, 0.32)"
      hoverColor: "#0A0A0A"
    secondary:
      background: "transparent"
      color: "#00FF41"
      border: "1px solid #00FF41"
      shadow: "none"
      hoverBackground: "rgba(0, 255, 65, 0.08)"
      hoverShadow: "inset 0 0 0 1px #00FF41"
      hoverColor: "#00FF41"
    ghost:
      background: "transparent"
      color: "#9E9E9E"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(0, 255, 65, 0.06)"
      hoverShadow: "none"
      hoverColor: "#00FF41"
    danger:
      background: "#330505"
      color: "#FF3B3B"
      border: "1px solid #CC2929"
      shadow: "none"
      hoverBackground: "#4D0808"
      hoverShadow: "0 0 0 1px #FF3B3B"
      hoverColor: "#FF3B3B"
    sizes:
      sm: {height: "28px", padding: "0 12px", fontSize: "0.75rem"}
      md: {height: "36px", padding: "0 16px", fontSize: "0.875rem"}
      lg: {height: "44px", padding: "0 24px", fontSize: "1rem"}
    borderRadius: "0"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#0A0A0A"
    color: "#00FF41"
    border: "1px solid #00CC34"
    borderRadius: "2px"
    padding: "10px 12px"
    focusBorder: "1px solid #00FF41"
    placeholderColor: "#6F6F6F"
  card:
    base:
      background: "#1A1A1A"
      border: "1px solid rgba(0, 255, 65, 0.20)"
      borderRadius: "2px"
      padding: "24px"
      shadow: "0 1px 2px rgba(0, 255, 65, 0.08)"
    hover:
      shadow: "0 6px 20px rgba(0, 255, 65, 0.20)"
      transform: "translateY(-1px)"
---

# The Matrix (Green-Code)

> A two-tone terminal cathedral: Matrix-green katakana rain on deep black, monospace as scripture.

## Origin

In March 1999, the Wachowskis released *The Matrix* through Warner Bros., shot largely on Sydney soundstages by cinematographer Bill Pope with production designer Owen Paterson. The film's instantly-iconic title sequence — vertical streams of green half-width katakana falling down a black screen — was assembled by visual-effects supervisor Lynne Cartwright's team from kanji scanned out of a sushi cookbook, then run through a custom particle system. Don Davis's brass-heavy score fixed the mood: monastic, alarming, vast.

The two follow-ups (Reloaded and Revolutions, both 2003) and the 2021 Resurrections extended the look, but the look itself never moved: phosphor-green code rain, deep-black terminals, monospace text as the seam of reality. Within five years it had become the default visual shorthand for "computer code" worldwide and the anchor of late-1990s cyberpunk cinema alongside Ghost in the Shell (1995) and Akira (1988). Every "wake up" trailer since owes it tax.

## Overview
Composition cues:
- **Layout**: bordered grid with strong column rhythm, like a terminal window
- **Content width**: `container` (1280px max) — never full-bleed bodies of text
- **Framing**: bordered (1px Matrix-green hairlines) on solid black surfaces
- **Grid intensity**: strong — visible 8px rhythm, optional ASCII-style rules

## Colors
Two saturated tones do all the heavy lifting: Matrix CRT-green `#00FF41` against deep-black `#0A0A0A`, with slate-grey `#3A3A3A` reserved for non-active chrome. No pastels, no tints, no warm greys — the discipline is the brand.

**Role usage**:
- Page background → `colors.background.page` (`#0A0A0A`)
- Card / panel surface → `colors.background.surface` (`#1A1A1A`)
- Primary text + key marks → `colors.text.primary` (`#00FF41`)
- Inactive / metadata text → `colors.text.muted` (`#6F6F6F`)
- Primary CTA fill → `colors.primary.500` (`#00FF41`)
- Hairlines and dividers → `rgba(0, 255, 65, 0.20)` over black
- Inert chrome / stroke icons → `colors.accent.500` (`#3A3A3A`)

## Typography
Monospace is the headline voice — Source Code Pro carries display weight, with JetBrains Mono, Roboto Mono, and Fira Code as ladder fallbacks. Body copy switches to Inter / Helvetica only where reading volume demands it. Letter-spacing stays tight in monospace and widens slightly in uppercase CTAs.

**Text styles**:
- `display-xl` — Source Code Pro, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Source Code Pro, 64px, weight 700, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Source Code Pro, 36px, weight 600, line-height 1.15, letter-spacing -0.02em
- `heading-2` — Source Code Pro, 24px, weight 600, line-height 1.2, letter-spacing -0.01em
- `body-lg` — Inter, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.55, letter-spacing 0
- `caption` — Source Code Pro, 12px, weight 500, line-height 1.4, letter-spacing 0.05em (UPPERCASE)
- `mono-md` — Source Code Pro, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px; rhythm: 8px
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max: 1280px; never full-bleed for prose
- Section padding: 32 / 64 / 96 / 128 by viewport size
- Grid gap: 8 / 16 / 24 / 48 px tiers — prefer 24 for card grids

## Elevation & Depth
Surfaces are flat-solid black panels separated by 1px Matrix-green hairlines. Where shadow appears, it is **phosphor glow** — never a soft grey drop. The light source is the green itself, leaking out of the panel.

- Surface style: solid (no glass, no gradients)
- Blur: none
- Shadow ladder: all shadows use `rgba(0, 255, 65, α)` — `xs` 8%, `sm` 12%, `md` 20%, `lg` 28%, `xl` 32%, `2xl` 40%
- Inner shadow is **black** (`rgba(0,0,0,0.65)`) to deepen recessed surfaces

## Shapes
- Buttons: 0px radius (terminal-precision)
- Cards / inputs / panels: 2px radius
- Larger containers: 4–6px max
- Pills / avatars: `9999px` reserved for status dots and avatar frames only — use sparingly

## Motion
Restrained and exact. Things glow, fade, and snap; they do not bounce or arc. Hover states pulse a phosphor halo for ~250ms and settle. Reduced-motion is honoured everywhere — no scanlines or rain for those who opt out.

- Level: restrained
- Durations: 0 / 120 / 250 / 400 / 600 ms
- Easings: default `cubic-bezier(0.4, 0, 0.2, 1)`, sharp `in (0.7, 0, 1, 0.4)`, ease-out `(0, 0.6, 0.3, 1)`, spring `(0.34, 1.56, 0.64, 1)` (used rarely)
- Hover patterns: glow (primary), stroke, opacity, tint
- Reduced motion: respected — code rain and pulses pause

## Techniques

### Falling katakana code-rain background
A pure-CSS column rain that drifts behind hero content. Use sparingly — one section, one rain layer.
```css
.code-rain {
  position: absolute; inset: 0;
  background:
    repeating-linear-gradient(
      to bottom,
      transparent 0 14px,
      rgba(0, 255, 65, 0.85) 14px 16px,
      rgba(0, 255, 65, 0.35) 16px 22px,
      transparent 22px 34px),
    repeating-linear-gradient(to right,
      transparent 0 11px,
      rgba(0, 0, 0, 0.92) 11px 12px);
  mix-blend-mode: screen;
  animation: rain 8s linear infinite;
  pointer-events: none;
  mask-image: linear-gradient(to bottom, transparent, #000 18%, #000 70%, transparent);
}
@keyframes rain { from { background-position-y: 0; } to { background-position-y: 220px; } }
```

### Phosphor glow CTA
Buttons sit flat on black until hover, then leak phosphor light from below.
```css
.btn-matrix {
  background: #00FF41; color: #0A0A0A;
  border: 1px solid #00FF41; border-radius: 0;
  font-family: 'Source Code Pro', monospace;
  font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
  padding: 0 16px; height: 36px;
  transition: box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1),
              background-color 120ms ease-out;
}
.btn-matrix:hover {
  background: #26FF61;
  box-shadow: 0 6px 20px rgba(0, 255, 65, 0.32),
              0 0 0 1px rgba(0, 255, 65, 0.6);
}
.btn-matrix:focus-visible { outline: none; box-shadow: 0 0 0 3px rgba(0, 255, 65, 0.45); }
```

### Terminal-prompt heading
H1s wear a blinking caret, like a prompt waiting for the next command.
```css
.h-prompt {
  font-family: 'Source Code Pro', monospace;
  color: #00FF41;
  font-weight: 600;
  letter-spacing: -0.02em;
}
.h-prompt::before { content: '> '; color: rgba(0, 255, 65, 0.55); }
.h-prompt::after {
  content: '_';
  display: inline-block;
  margin-left: 0.15em;
  animation: caret 1.05s steps(1) infinite;
}
@keyframes caret { 50% { opacity: 0; } }
```

## Iconography
Linear stroke icons (Lucide set) at 1.5px stroke, always rendered in `#00FF41` or `#6F6F6F` (inactive). Custom glyphs follow the same stroke and pixel-snap to the 8px grid. Avoid filled or duotone treatments — they break the terminal logic.

- Treatment: linear / outline
- Set: Lucide
- Stroke: 1.5px

## Do's & Don'ts
### ✓ Do
- Use Matrix-green `#00FF41` for primary actions, key text, and active state — nothing else competes for accent.
- Set headings in Source Code Pro (or its monospace fallbacks); reserve Inter for body copy only.
- Keep button radius at 0 and card radius at 2px — terminal-precision is the shape language.
- Render shadows as Matrix-green phosphor glow (`rgba(0, 255, 65, α)`), never as grey drop shadows.
- Hold the two-tone discipline: deep-black surfaces, Matrix-green ink, slate-grey for inert chrome only.

### ✗ Don't
- Don't ship a light-mode variant — this system is dark-mode Matrix-cyberpunk only.
- Don't introduce pastels or washed tints; the saturated green + black duo is the brand.
- Don't dress this in refined-luxury chrome (no gold, no serifs, no marble) — the gravity is late-1990s cyberpunk.
- Don't reach for generic cyberpunk tropes (neon-pink + neon-cyan, glitch text); stay inside Matrix vocabulary: falling-character-code, CRT-green, terminal-monospace.
- Don't set headings in a serif — monospace and sans-serif only.

## Applications
Best fit for developer tools, security / hacking products, cyberpunk-themed games, terminal launchers, and any product whose narrative leans on "waking up from the consumer web." Works strongly for landing pages, dashboards, and CLI documentation; works poorly for warm, friendly, or family-oriented surfaces. Use it where the product wants to feel technical, austere, and slightly dangerous.
