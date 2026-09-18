---
version: 1

meta:
  id: solarpunk-greenhouse-2020
  name: Solarpunk Greenhouse
  description: An optimistic ecological futurism of glass conservatories, climbing vines, and patinated brass under a deep planted canopy.
  isDark: true
  tags: [organic, futuristic, friendly, warm, decorative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2010s–present (term crystallized c. 2008, flourishing ~2020)"
  region: "Global / internet-native movement"
  regionZh: "全球 / 互联网原生运动"
  keyFigures: [Alphonse Mucha, Hector Guimard]
  movements: [Solarpunk, Art Nouveau revival, Eco-utopianism, Appropriate technology]

introduction: |
  Solarpunk imagines a hopeful, hand-built green future: glass greenhouses
  laced with climbing vines, brass and copper fixtures gone soft with verdigris,
  and Art-Nouveau curves that refuse the cold rectangle. The Greenhouse cut
  reads from inside a sunlit planted conservatory.
  Deep foliage canopy sits in shade rather than open sky, layering pine, leaf,
  and moss against patinated metal and solar-gold light. It is a future you
  could grow yourself—warm, lush, and optimistic, never sterile or dystopian.
introductionZh: |
  太阳朋克是一种乐观的生态未来主义：玻璃温室爬满藤蔓，黄铜与紫铜配件
  覆着青绿色铜锈，新艺术运动的有机曲线拒绝冰冷的直角。这个「温室」切片
  从一座洒满阳光的种植暖房内部望出去——不是开阔的天空，而是层叠的浓密
  树冠投下的荫影，松绿、叶绿与苔黄交织在做旧金属与日照金光之间。
  这是一个你可以亲手种出来的未来：温暖、葱郁、充满希望，绝不冰冷或反乌托邦。
  圆润的人文字体带来手工感的乐观，新艺术衬线则点出植物纹样的优雅曲线。

colors:
  primary:    {"50": "#EAF6EC", "100": "#D2EBD7", "200": "#A8D6B2", "300": "#7EC18C", "400": "#66B076", "500": "#4E9F5B", "600": "#3F8A4C", "700": "#33713E", "800": "#285930", "900": "#1E4324", "950": "#122B17"}
  secondary:  {"50": "#F2F7E6", "100": "#E4EFCB", "200": "#CFE2A4", "300": "#B6D177", "400": "#A2C55B", "500": "#8FB339", "600": "#769430", "700": "#5C7426", "800": "#46591E", "900": "#344216", "950": "#1F2A0D"}
  accent:     {"50": "#FBF3DE", "100": "#F6E6BC", "200": "#EFD389", "300": "#E9C25B", "400": "#E6B94B", "500": "#E3B23C", "600": "#C2942C", "700": "#9A7322", "800": "#73561A", "900": "#534013", "950": "#33270B"}
  neutral:    {"50": "#EDF3EE", "100": "#D6E2D8", "200": "#AFC4B3", "300": "#84A18B", "400": "#5C7C64", "500": "#3F5E47", "600": "#2E6E4E", "700": "#27523A", "800": "#1F3F2D", "900": "#1B3A2B", "950": "#102219"}
  semantic:
    success: { bg: "#1E4324", text: "#A8D6B2", light: "#285930", border: "#3F8A4C" }
    warning: { bg: "#534013", text: "#EFD389", light: "#73561A", border: "#C2942C" }
    error:   { bg: "#4A1F1B", text: "#E7A79E", light: "#6B2C25", border: "#B5524A" }
    info:    { bg: "#123E3C", text: "#8FD6D2", light: "#1A5755", border: "#43B3AE" }
  background:
    page:    "#1B3A2B"
    surface: "#234A37"
    subtle:  "#2E6E4E"
  text:
    primary:   "#EDF3EE"
    secondary: "#B6D177"
    muted:     "#84A18B"
    inverse:   "#102219"

typography:
  families:
    heading: "'Quicksand', 'Comfortaa', sans-serif"
    body:    "'Philosopher', 'Cormorant Garamond', serif"
    mono:    "'IBM Plex Mono', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&family=Comfortaa:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Philosopher:ital,wght@0,400;0,700;1,400&display=swap"
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
  radius: {none: "0", sm: "8px", md: "16px", lg: "24px", xl: "40px", full: "9999px"}
  color:  {default: "#43B3AE", subtle: "#2E6E4E", strong: "#B5A642", focus: "#E3B23C"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(8,24,16,0.20)"
  sm: "0 2px 6px rgba(8,24,16,0.28)"
  md: "0 6px 18px rgba(8,24,16,0.34)"
  lg: "0 14px 36px rgba(8,24,16,0.40)"
  xl: "0 24px 60px rgba(8,24,16,0.46)"
  "2xl": "0 40px 90px rgba(8,24,16,0.52)"
  inner: "inset 0 1px 2px rgba(8,24,16,0.30)"
  focus: "0 0 0 3px rgba(227,178,60,0.45)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, glow, tint, scale]
  reducedMotion: true

composition:
  layout:        flex
  contentWidth:  container
  framing:       glassy
  gridIntensity: soft
  rhythm:        "4px"

surfaceStyle: glass
blur:         12px

iconography:
  treatment: linear
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#4E9F5B", color: "#102219", border: "1px solid #3F8A4C", shadow: "0 6px 18px rgba(8,24,16,0.34)", hoverBackground: "#66B076", hoverShadow: "0 0 0 3px rgba(78,159,91,0.35), 0 8px 22px rgba(8,24,16,0.40)", hoverColor: "#102219"}
    secondary: {background: "rgba(181,166,66,0.14)", color: "#E3B23C", border: "1px solid #B5A642", shadow: "none", hoverBackground: "rgba(181,166,66,0.24)", hoverShadow: "0 0 18px rgba(227,178,60,0.30)", hoverColor: "#F6E6BC"}
    ghost:     {background: "transparent", color: "#B6D177", border: "1px solid transparent", shadow: "none", hoverBackground: "rgba(143,179,57,0.14)", hoverShadow: "none", hoverColor: "#CFE2A4"}
    danger:    {background: "#B5524A", color: "#FBF3DE", border: "1px solid #6B2C25", shadow: "0 6px 18px rgba(8,24,16,0.34)", hoverBackground: "#C5645B", hoverShadow: "0 8px 22px rgba(8,24,16,0.40)", hoverColor: "#FBF3DE"}
    sizes:     {sm: {height: "36px", padding: "0 16px", fontSize: "0.875rem"}, md: {height: "44px", padding: "0 24px", fontSize: "1rem"}, lg: {height: "54px", padding: "0 32px", fontSize: "1.125rem"}}
    borderRadius: "9999px"
    fontWeight: 600
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "rgba(16,34,25,0.55)"
    color: "#EDF3EE"
    border: "1px solid #2E6E4E"
    borderRadius: "16px"
    padding: "12px 16px"
    focusBorder: "1px solid #E3B23C"
    placeholderColor: "#84A18B"
  card:
    base:  {background: "rgba(35,74,55,0.62)", border: "1px solid rgba(67,179,174,0.28)", borderRadius: "24px", padding: "28px", shadow: "0 14px 36px rgba(8,24,16,0.40)"}
    hover: {shadow: "0 24px 60px rgba(8,24,16,0.46)", transform: "translateY(-4px)"}
---

# Solarpunk Greenhouse

> An optimistic ecological future read from inside a sunlit, vine-laced glass conservatory.

## Origin

Solarpunk emerged as an internet-native literary and visual movement, with the term crystallizing around 2008 and flourishing in online collectives, climate-fiction anthologies, and aesthetic communities by ~2020. Against the grime and fatalism of cyberpunk, it proposed a hopeful counter-image: cities re-wilded with climbing greenery, energy gathered gently from the sun, and technology that is appropriate, repairable, and hand-built. Its visual DNA reaches back to Art Nouveau—the whiplash tendrils of Hector Guimard's Métro entrances and the floral panels of Alphonse Mucha—reinterpreted for an age of solar collectors and living architecture.

The Greenhouse cut narrows that vision to a single interior: a planted conservatory of hexagonal glass panes, brass fittings softened by verdigris, and a deep foliage canopy overhead. Light filters through leaves rather than open sky, so the palette layers pine, leaf, and moss against patinated metal and solar gold. The mood is warm and grown, never sterile—a future you could cultivate with your own hands.

## Overview

Composition cues:
- **Layout**: Flowing flex arrangements that let organic curves and vine borders weave between blocks rather than locking to a rigid grid.
- **Content width**: Centered container (~1024–1280px) so foliage framing can breathe at the margins.
- **Framing**: Glassy conservatory panels—translucent surfaces with 12px blur over the canopy-green page.
- **Grid intensity**: Soft—hexagonal glass-pane lattices and solar grids are present but always softened by overgrowth.

## Colors

The palette layers a living greenhouse: a deep planted-canopy green page in shade, healthy leaf green for action, moss-yellow and pine for foliage depth, brass and verdigris for patinated metal fittings, and solar-gold for warm light. Nothing reads cold or corporate—warmth and growth govern every value.

**Role usage**:
- Page background → `colors.background.page` (#1B3A2B deep canopy green)
- Glass panel / card surface → `colors.background.surface` (#234A37)
- Primary action & healthy growth → `colors.primary.500` (#4E9F5B leaf green)
- Foliage accent / moss highlight → `colors.secondary.500` (#8FB339)
- Solar-gold highlight & focus glow → `colors.accent.500` (#E3B23C)
- Verdigris border / patina detail → `borders.color.default` (#43B3AE)
- Brass fitting / strong border → `borders.color.strong` (#B5A642)
- Body text on canopy → `colors.text.primary` (#EDF3EE)

## Typography

The type voice pairs rounded humanist optimism with an Art-Nouveau serif streak. Quicksand and Comfortaa give headings a soft, hand-built warmth; Cormorant Garamond lends an elegant botanical-serif flourish for display moments; Philosopher carries supporting and body text with quiet character.

**Text styles**:
- `display-xl` — Comfortaa, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Quicksand, 64px, weight 700, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Quicksand, 36px, weight 600, line-height 1.2, letter-spacing -0.01em
- `heading-2` — Cormorant Garamond, 30px, weight 600, line-height 1.25, letter-spacing 0
- `body-lg` — Philosopher, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Philosopher, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Quicksand, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — IBM Plex Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit 4px; scale runs 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container caps at 1280px (xl), with 1024px the comfortable reading width.
- Section padding generous (md 64px, lg 96px) so foliage framing has room to climb.
- Grid gaps stay soft (md 16px, lg 24px), letting vine borders bridge gaps.

## Elevation & Depth

Surfaces behave like glass conservatory panels: translucent green-tinted planes with a 12px backdrop blur, floating over the shaded canopy. Shadows are deep and warm-dark (toward #081810) rather than neutral gray, and a solar-gold focus glow signals interactivity.

- Surface style: glass panels with `rgba(35,74,55,0.62)` fill over the page.
- Blur: 12px backdrop blur on framed surfaces.
- Shadow ladder: xs hairline → md panel lift → xl floating conservatory pane → 2xl hero glass.
- Focus glow: `0 0 0 3px rgba(227,178,60,0.45)` solar-gold ring.

## Shapes

- Corner radii lean generous and rounded: sm 8px, md 16px, lg 24px, xl 40px—echoing leaf and pane curvature.
- Buttons and pills go fully round (9999px) for a soft, hand-built feel.
- Hexagonal lattices supply the only angular motif, always softened by overgrowth.

## Motion

Motion is lively but gentle—growth, not mechanics. Things ease in like a plant turning toward light, with a spring on playful elements and a soft solar glow on hover. Reduced-motion is honored.

- Level: lively.
- Durations: fast 120ms, normal 250ms, slow 400ms, slower 600ms.
- Easings: default ease, spring `cubic-bezier(0.34, 1.56, 0.64, 1)` for organic bounce.
- Hover patterns: lift, glow, tint, scale.

## Techniques

### Climbing-vine border
A tendril border that wraps a panel using a layered radial-gradient "leaf node" pattern along an organically curved edge.
```css
.vine-panel {
  position: relative;
  border: 1px solid rgba(67, 179, 174, 0.28);
  border-radius: 24px;
  background: rgba(35, 74, 55, 0.62);
  backdrop-filter: blur(12px);
}
.vine-panel::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: 26px;
  padding: 2px;
  background:
    radial-gradient(circle at 12% 0%, #8FB339 0 4px, transparent 5px),
    radial-gradient(circle at 40% 100%, #4E9F5B 0 4px, transparent 5px),
    radial-gradient(circle at 88% 8%, #2E6E4E 0 5px, transparent 6px),
    linear-gradient(120deg, #2E6E4E, #43B3AE, #8FB339);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  pointer-events: none;
}
```

### Verdigris brass fitting
A patinated metal surface—brass base bleeding into verdigris—for fixtures, dividers, and metal accents.
```css
.brass-fitting {
  background:
    linear-gradient(135deg, #B5A642 0%, #8FB339 38%, #43B3AE 100%);
  box-shadow:
    inset 0 1px 1px rgba(251, 243, 222, 0.35),
    inset 0 -2px 4px rgba(8, 24, 16, 0.45);
  border-radius: 9999px;
}
```

### Hexagonal glass-pane lattice
A soft conservatory backdrop of hexagonal panes, dimmed so foliage and content read on top.
```css
.glass-lattice {
  background-color: #1B3A2B;
  background-image:
    repeating-linear-gradient(60deg, rgba(67,179,174,0.10) 0 1px, transparent 1px 28px),
    repeating-linear-gradient(-60deg, rgba(67,179,174,0.10) 0 1px, transparent 1px 28px),
    repeating-linear-gradient(0deg, rgba(67,179,174,0.06) 0 1px, transparent 1px 28px);
}
```

## Iconography

Use linear, even-stroke icons (Phosphor) at 1.5px stroke for a clean, hand-drawn warmth that matches the rounded headings. Favor botanical and ecological glyphs—leaf, sun, sprout, droplet—rendered with gently rounded terminals. Tint icons in leaf green or solar gold over the canopy ground.

- Treatment: linear outline.
- Set: phosphor.
- Stroke: 1.5px with rounded caps.

## Do's & Don'ts

### ✓ Do
- Anchor every layout on the deep planted-canopy green (#1B3A2B) background.
- Use leaf green (#4E9F5B) for primary actions and healthy, growing states.
- Let organic curves, vine borders, and rounded radii soften any geometry.
- Layer brass (#B5A642) and verdigris (#43B3AE) for patinated metal warmth.
- Reach for solar-gold (#E3B23C) as the optimistic highlight and focus glow.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds.
- Avoid cold corporate grays, chrome, and sterile minimalism—this future is warm and grown.
- Avoid hard mechanical rectangles only; let organic curves and vines soften the geometry.
- Avoid dystopian neon/grime; the mood is hopeful, lush, and sunlit, not cyberpunk.

## Applications

Best for climate and sustainability brands, eco-product launches, community-garden and regenerative-tech sites, hopeful manifestos, and conference decks that want a warm, living-future feel. Excels wherever optimism, growth, and craft should read instantly—and poorly suited to austere corporate dashboards or cold high-tech minimalism.
