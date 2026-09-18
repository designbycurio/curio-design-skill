---
version: 1

meta:
  id: squid-game-2021
  name: Squid Game (2021)
  description: Candy-pastel playground palette staged inside panopticon geometry — fuchsia guards, teal tracksuits, and a shape-based iconographic grammar.
  isDark: false
  tags: [bold, narrative, geometric, playful, subcultural]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2021 (Season 1, September 2021; Seasons 2–3, 2024–2025)"
  region: "Seoul, South Korea (Netflix global release)"
  regionZh: "韩国首尔"
  keyFigures: [Hwang Dong-hyuk, Chae Kyoung-sun, Jung Jae-il, Lee Jung-jae]
  movements: [Korean New Wave TV, graphic minimalism, dystopian pop design]

introduction: |
  Squid Game turns the palette of childhood into an instrument of dread. Fuchsia
  guard suits, teal tracksuits, and candy-pastel Escher stairways stay relentlessly
  cheerful while the layout underneath turns menacing — playground colors, panopticon
  logic. The three masked-guard glyphs — circle, triangle, square — become a whole
  iconographic grammar.

  Everything is flat, graphic, oversized, and a little too clean. Numbers stencil
  across chests, surfaces hold poster-paint blocks with zero bevels, and a single
  tilted plane interrupts hard right-angle grids. The tension is the point: smile for
  the guards, the exit is only a shape away.

introductionZh: |
  《鱿鱼游戏》把童年游戏的甜美配色变成一台制造恐惧的机器。粉红卫兵服、青绿运动服、
  糖果色的埃舍尔楼梯——画面越是欢快明亮，底下的秩序就越发冷酷。这是游乐场的颜色，
  却是圆形监狱的逻辑。三个蒙面卫兵的符号——圆、三角、方——被拆解成一整套图形语法：
  作为项目符号、徽章、章节标记、加载状态。

  一切都是平涂的、图形化的、放大的，干净得有点过头。数字像模板漆印在胸前，色块之间
  没有任何斜面与渐变，硬直角网格里只斜插一块倾斜平面。张力就是全部意义所在：对着
  卫兵微笑吧——出口不过是一个形状的距离。

colors:
  primary:    {"50": "#FEE6F1", "100": "#FDC0DC", "200": "#FA8FC1", "300": "#F65BA3", "400": "#F23A8E", "500": "#ED1B76", "600": "#C71563", "700": "#9E1050", "800": "#760B3C", "900": "#4E0728", "950": "#2C0417"}
  secondary:  {"50": "#E4F7F5", "100": "#BDEBE6", "200": "#8ADCD3", "300": "#54CBBF", "400": "#31B6A8", "500": "#1BA098", "600": "#16847D", "700": "#116762", "800": "#0C4B47", "900": "#08302D", "950": "#041917"}
  accent:     {"50": "#FDF8E4", "100": "#FBEEBB", "200": "#F7E08C", "300": "#F3D26B", "400": "#F0CB56", "500": "#EEC643", "600": "#D3A824", "700": "#A6821B", "800": "#785D13", "900": "#4C3B0B", "950": "#2A2006"}
  neutral:    {"50": "#F7F5F6", "100": "#EDEAEC", "200": "#D6D1D4", "300": "#B6AEB3", "400": "#8B8188", "500": "#655C62", "600": "#4E464C", "700": "#3B343A", "800": "#2A242A", "900": "#201A22", "950": "#161217"}
  semantic:
    success: { bg: "#E4F7F5", text: "#116762", light: "#BDEBE6", border: "#54CBBF" }
    warning: { bg: "#FDF8E4", text: "#A6821B", light: "#FBEEBB", border: "#F0CB56" }
    error:   { bg: "#FEE6F1", text: "#C71563", light: "#FDC0DC", border: "#F65BA3" }
    info:    { bg: "#E7F5FB", text: "#2A7CA6", light: "#C3E6F6", border: "#6EC1E4" }
  background:
    page:    "#FCE1EA"
    surface: "#FFFFFF"
    subtle:  "#F9C0D0"
  text:
    primary:   "#201A22"
    secondary: "#4E464C"
    muted:     "#8B8188"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Space Grotesk', 'Helvetica Neue', Arial, sans-serif"
    body:    "'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif"
    mono:    "'Space Mono', 'SFMono-Regular', Menlo, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap"
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
  radius: {none: "0", sm: "4px", md: "6px", lg: "10px", xl: "16px", full: "9999px"}
  color:  {default: "#F9C0D0", subtle: "#FDC0DC", strong: "#1BA098", focus: "#ED1B76"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(32,26,34,0.05)"
  sm: "0 2px 6px rgba(237,27,118,0.10)"
  md: "0 6px 20px rgba(237,27,118,0.18)"
  lg: "0 12px 32px rgba(237,27,118,0.22)"
  xl: "0 20px 48px rgba(237,27,118,0.26)"
  "2xl": "0 28px 64px rgba(237,27,118,0.30)"
  inner: "inset 0 2px 4px rgba(32,26,34,0.06)"
  focus: "0 0 0 3px rgba(237,27,118,0.35)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, scale]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  wide
  framing:       solid
  gridIntensity: strong
  rhythm:        "4px"

surfaceStyle: flat
blur:         none

iconography:
  treatment: filled
  set:       custom
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#ED1B76", color: "#FFFFFF", border: "none", shadow: "0 6px 20px rgba(237,27,118,0.18)", hoverBackground: "#C71563", hoverShadow: "0 12px 32px rgba(237,27,118,0.22)", hoverColor: "#FFFFFF"}
    secondary: {background: "#1BA098", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#16847D", hoverShadow: "0 8px 24px rgba(27,160,152,0.20)", hoverColor: "#FFFFFF"}
    ghost:     {background: "transparent", color: "#ED1B76", border: "2px solid #ED1B76", shadow: "none", hoverBackground: "#FEE6F1", hoverShadow: "none", hoverColor: "#C71563"}
    danger:    {background: "#C71563", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#9E1050", hoverShadow: "0 8px 24px rgba(199,21,99,0.24)", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "42px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "52px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "6px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#FFFFFF"
    color: "#201A22"
    border: "2px solid #F9C0D0"
    borderRadius: "6px"
    padding: "10px 14px"
    focusBorder: "2px solid #ED1B76"
    placeholderColor: "#8B8188"
  card:
    base:  {background: "#FFFFFF", border: "2px solid #1BA098", borderRadius: "10px", padding: "24px", shadow: "0 6px 20px rgba(237,27,118,0.18)"}
    hover: {shadow: "0 12px 32px rgba(237,27,118,0.22)", transform: "translateY(-4px)"}
---

# Squid Game (2021)

> Playground palette, panopticon logic — candy hues staged over menacing geometry.

## Origin

Squid Game premiered on Netflix in September 2021, written and directed by Hwang Dong-hyuk after more than a decade shopping the script. Its look was authored by production designer Chae Kyoung-sun, whose life-size sets — the fuchsia-lit Escher stairway corridor, the pastel bunk-bed arena, the Young-hee "Red Light, Green Light" doll field — became as recognizable as the plot. Composer Jung Jae-il scored the sugar-and-dread contrast, and a principal cast led by Lee Jung-jae carried the human cost.

The design grammar is deliberately regressive: costumes reduce people to a fuchsia guard suit or a teal tracksuit stamped with a stencil number, and the three guard-mask glyphs — circle, triangle, square — echo Bauhaus shape pedagogy and Korean playground-game traditions like ddakji and gonu. The palette stays flat, saturated, and childlike — poster paint, never gradient-soft — so the cheerfulness of the surfaces keeps colliding with the cruelty of the rules. That collision is the entire aesthetic thesis.

## Overview

Composition cues:
- **Layout**: Hard right-angle grids, occasionally interrupted by a single tilted plane; numbered lockers and bunk stacks as list metaphors.
- **Content width**: Wide — oversized graphic blocks that dominate the viewport.
- **Framing**: Solid flat color-field blocks with crisp 2px borders, zero bevels.
- **Grid intensity**: Strong — the grid is a visible, load-bearing structure.

## Colors

The palette is the coldest, sweetest pairing on television: bubblegum guard-suit fuchsia against tracksuit teal, cut by near-black masks and stark white numerals. Every hue stays flat and confident — no gradient softening, no muddy neutrals. Pastel pink is the page, teal is the contrast band, and piggy-bank gold is rationed for reward emphasis only.

**Role usage**:
- Page background → `colors.background.page` (#FCE1EA soft bubblegum pink stairway wall)
- Card ground → `colors.background.surface` (#FFFFFF clean white)
- Contrast bands → `colors.secondary.500` (#1BA098 teal tracksuit block)
- Primary actions / guard emphasis → `colors.primary.500` (#ED1B76 guard-suit fuchsia)
- Prize / reward emphasis → `colors.accent.500` (#EEC643 piggy-bank gold)
- Primary text → `colors.text.primary` (#201A22 near-black plum)
- Numerals / inverse text → `colors.text.inverse` (#FFFFFF)

## Typography

Type is split between geometric display and clinical institution. Space Grotesk headings carry a slight quirk that echoes the stencil chest tags; IBM Plex Sans keeps body copy neutral and administrative; Space Mono handles player IDs, timers, and subtitle-like captions. Display tracks tight, labels track wide and uppercase like a numbered badge.

**Text styles**:
- `display-xl` — Space Grotesk, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Space Grotesk, 64px, weight 700, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Space Grotesk, 36px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — IBM Plex Sans, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — IBM Plex Sans, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Space Mono, 12px, weight 400, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Space Mono, 14px, weight 400, line-height 1.5, letter-spacing 0.02em

## Spacing & Layout

- Base unit: 4px; scale 2/4/6/8/12/16/24/32/48/64/96/128.
- Container: capped at 1280px (xl) for wide graphic layouts.
- Section padding: 64–96px vertical for arena-scale breathing room.
- Grid gap: 16–24px default, 48px between major blocks.

## Elevation & Depth

Materiality is matte printed-vinyl flatness — no glossy chrome, no drop-shadow soup. The only depth cue is a soft fuchsia set-light glow, as if lit by the corridor's pink floods. Shadows tint toward fuchsia rather than neutral gray.

- Surface style: flat poster-paint blocks with crisp borders.
- Blur: none.
- Shadow ladder: xs hairline → md soft fuchsia set-light (0 6px 20px rgba(237,27,118,0.18)) → xl for lifted heroes.

## Shapes

- Button radius: 6px (sharp, stencil-like).
- Card radius: 10px.
- Larger surfaces: 16px max — nothing pill-round.
- The circle/triangle/square trinity supplies badges, bullets, and markers; keep corners crisp.

## Motion

Motion is lively but disciplined: shapes snap and lift, tints flip like a green-light / red-light switch. Nothing floats or drifts — movement reads as game-show cueing, not ambient drift. A gentle spring adds a toy-like bounce on emphasis.

- Level: lively.
- Durations: fast 120ms, normal 250ms, slow 400ms.
- Easings: default cubic-bezier(0.4,0,0.2,1); spring cubic-bezier(0.34,1.56,0.64,1).
- Hover patterns: lift, tint, scale.

## Techniques

### Guard-glyph shape markers

The circle/triangle/square guard trinity rendered as pure CSS shapes for badges and section markers.

```css
.glyph { display: inline-flex; gap: 8px; }
.glyph--circle {
  width: 20px; height: 20px; border-radius: 9999px;
  background: #ED1B76;
}
.glyph--triangle {
  width: 0; height: 0;
  border-left: 11px solid transparent;
  border-right: 11px solid transparent;
  border-bottom: 20px solid #ED1B76;
}
.glyph--square {
  width: 20px; height: 20px; background: #ED1B76;
}
```

### Stencil player-number tag

Cards styled as numbered player tags — teal border with an oversized white numeral in the corner.

```css
.player-tag {
  position: relative;
  background: #1BA098;
  color: #FFFFFF;
  border-radius: 10px;
  padding: 24px;
  font-family: 'Space Mono', monospace;
}
.player-tag::before {
  content: attr(data-number);
  position: absolute; top: 12px; right: 16px;
  font-size: 3rem; font-weight: 700;
  color: rgba(255,255,255,0.85);
  letter-spacing: -0.04em;
}
```

### Fuchsia set-light glow

The single depth cue — a soft pink glow on hero blocks mimicking the corridor's stage lighting, no drop shadow.

```css
.set-lit {
  background: #ED1B76;
  color: #FFFFFF;
  box-shadow: 0 6px 20px rgba(237, 27, 118, 0.18);
}
.set-lit:hover {
  box-shadow: 0 12px 32px rgba(237, 27, 118, 0.22);
  transform: translateY(-4px);
}
```

## Iconography

Icons are custom filled shapes drawn from the circle/triangle/square guard grammar rather than a standard line-icon set. They read as solid graphic marks — no thin outlines, no duotone. Where a UI icon is unavoidable, use a bold 2px-weight filled glyph so it matches the stencil confidence of the numerals.

- Treatment: filled, custom.
- Set: custom guard-shape grammar (circle/triangle/square).
- Stroke: 2px on any structural outlines.

## Do's & Don'ts

### ✓ Do
- Use guard-suit fuchsia (#ED1B76) for primary actions and the loudest emphasis.
- Keep every color a flat, confident block — poster paint, never gradient-soft.
- Deploy the circle/triangle/square trinity as bullets, badges, and section markers.
- Reserve piggy-bank gold (#EEC643) for prize and reward emphasis only.
- Set player IDs, timers, and captions in Space Mono for the institutional feel.

### ✗ Don't
- Use cream, ivory, or parchment backgrounds — the page is pastel pink.
- Add gradients or glossy 3D bevels — keep color blocks flat.
- Mute or desaturate the palette — the candy hues must stay loud.
- Use ornate serifs or handwritten scripts — geometric sans only.
- Reproduce show dialogue, subtitles, or logotype verbatim.
- Let blue dominate — pink and teal lead; blue is a stair accent only.

## Applications

Best fit for bold event landing pages, game or entertainment product UI, poster-scale social cards, and any interface that wants a graphic, high-contrast, slightly unsettling personality. The shape grammar and stencil numerals make it especially strong for leaderboards, countdown timers, and numbered-list layouts.
