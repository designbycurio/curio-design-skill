---
version: 1

meta:
  id: star-trek-lcars-1987
  name: Star Trek LCARS
  description: Okudagram capsule buttons and sweeping elbow frames — golden-orange and violet color blocks glowing on true black.
  isDark: true
  tags: [tech, futuristic, retro, bold, geometric]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1987 onward (TNG era); within the 1950–1990 design window"
  region: "Los Angeles, California (Paramount Studios)"
  regionZh: "美国洛杉矶 / 派拉蒙影业"
  keyFigures: [Michael Okuda, Denise Okuda, Rick Sternbach]
  movements: [Television production design, speculative interface design, flat color-block graphic systems]

introduction: |
  LCARS — the Library Computer Access and Retrieval System — is the touchscreen
  interface Michael Okuda designed for Star Trek: The Next Generation in 1987.
  Built from softly-rounded color blocks and sweeping curved "elbow" frames, it
  reads from a pure-black backlit console: warm orange and tan capsules glowing
  beside cool violet and blue ones, with thin colored rails and right-aligned
  numeric tags threading between them.

  The system is resolutely flat — no gradients, no bevels, no skeuomorphic chrome.
  Its identity lives in the geometry: pill-shaped Okudagram buttons, generous black
  negative space, and the iconic elbow that bends a header bar down into a sidebar
  in one continuous radius. It is a fictional UI that became one of the most
  recognizable graphic languages in television.
introductionZh: |
  LCARS（图书馆计算机访问与检索系统）是 Michael Okuda 在 1987 年为《星际迷航：
  下一代》设计的触控界面。整套语言由柔和的圆角色块与大弧度的「弯肘」框架构成，
  从一块纯黑的背光控制台读起：暖橙与沙色的胶囊按钮和冷紫、冷蓝的色块并排发光，
  细细的彩色分隔轨与右对齐的数字标签在其间穿行。

  它彻底是平面的——没有渐变，没有斜面，没有拟物质感的光泽。它的辨识度全在几何：
  药丸形的 Okuda 色块、慷慨的黑色留白，以及那条标志性的「弯肘」——把顶部横条用
  一段连续半径折下来接到侧栏。它是一套虚构的界面，却成了电视史上最易辨认的图形
  语言之一。

colors:
  primary:    {"50": "#FFF4E0", "100": "#FFE6BF", "200": "#FFD699", "300": "#FFC266", "400": "#FFAB33", "500": "#FF9900", "600": "#DB8000", "700": "#B36800", "800": "#8A5000", "900": "#5E3700", "950": "#3D2400"}
  secondary:  {"50": "#F2EBFF", "100": "#E0D1FF", "200": "#C9AEFF", "300": "#B088FF", "400": "#9D77FF", "500": "#9966FF", "600": "#7E4FDB", "700": "#633BB3", "800": "#4A2B89", "900": "#321C5E", "950": "#1F113D"}
  accent:     {"50": "#EBEFFF", "100": "#D1D9FF", "200": "#AEBBFF", "300": "#889AFF", "400": "#6E80FF", "500": "#5566FF", "600": "#3F4FDB", "700": "#2E3BB3", "800": "#202B89", "900": "#151D5E", "950": "#0C113D"}
  neutral:    {"50": "#F5F5F7", "100": "#E2E2E6", "200": "#C2C2C9", "300": "#9A9AA3", "400": "#73737D", "500": "#54545C", "600": "#3D3D44", "700": "#2A2A30", "800": "#1A1A1E", "900": "#0D0D0F", "950": "#000000"}
  semantic:
    success: { bg: "#1F113D", text: "#99CCFF", light: "#321C5E", border: "#5566FF" }
    warning: { bg: "#3D2400", text: "#FFCC99", light: "#5E3700", border: "#FF9900" }
    error:   { bg: "#3D0F1A", text: "#FF6680", light: "#5E1426", border: "#FF334D" }
    info:    { bg: "#0C113D", text: "#99CCFF", light: "#151D5E", border: "#5566FF" }
  background:
    page:    "#000000"
    surface: "#0D0D0F"
    subtle:  "#1A1A1E"
  text:
    primary:   "#FFCC99"
    secondary: "#FF9900"
    muted:     "#9A9AA3"
    inverse:   "#000000"

typography:
  families:
    heading: "'Antonio', 'Oswald', sans-serif"
    body:    "'Oswald', 'Antonio', sans-serif"
    mono:    "'Jura', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Antonio:wght@400;500;600;700&family=Oswald:wght@300;400;500;600;700&family=Jura:wght@400;500;600;700&display=swap"
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
  radius: {none: "0", sm: "8px", md: "16px", lg: "28px", xl: "48px", full: "9999px"}
  color:  {default: "#2A2A30", subtle: "#1A1A1E", strong: "#FF9900", focus: "#FF9900"}
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
  inner: "none"
  focus: "0 0 0 3px rgba(255,153,0,0.5)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [tint, opacity]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  full-bleed
  framing:       solid
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: flat
blur:         none

iconography:
  treatment: filled
  set:       custom
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "0px"

components:
  button:
    primary:   {background: "#FF9900", color: "#000000", border: "none", shadow: "none", hoverBackground: "#FFCC99", hoverShadow: "none", hoverColor: "#000000"}
    secondary: {background: "#9966FF", color: "#000000", border: "none", shadow: "none", hoverBackground: "#B088FF", hoverShadow: "none", hoverColor: "#000000"}
    ghost:     {background: "#1A1A1E", color: "#FF9900", border: "none", shadow: "none", hoverBackground: "#2A2A30", hoverShadow: "none", hoverColor: "#FFCC99"}
    danger:    {background: "#FF334D", color: "#000000", border: "none", shadow: "none", hoverBackground: "#FF6680", hoverShadow: "none", hoverColor: "#000000"}
    sizes:     {sm: {height: "32px", padding: "0 18px", fontSize: "0.875rem"}, md: {height: "44px", padding: "0 28px", fontSize: "1rem"}, lg: {height: "56px", padding: "0 40px", fontSize: "1.25rem"}}
    borderRadius: "9999px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#1A1A1E"
    color: "#FFCC99"
    border: "2px solid #FF9900"
    borderRadius: "9999px"
    padding: "10px 22px"
    focusBorder: "2px solid #FFCC99"
    placeholderColor: "#9A9AA3"
  card:
    base:  {background: "#0D0D0F", border: "none", borderRadius: "28px", padding: "24px", shadow: "none"}
    hover: {shadow: "none", transform: "none"}
---

# Star Trek LCARS

> Okudagram capsule buttons and sweeping elbow frames — golden-orange and violet color blocks glowing on true black.

## Origin
LCARS — the Library Computer Access and Retrieval System — was designed by scenic art supervisor Michael Okuda for *Star Trek: The Next Generation*, which premiered in 1987. Tasked with making the Enterprise-D's consoles look advanced yet cheap to build, Okuda devised a flat, frameless graphic language of softly-rounded color blocks on backlit black acrylic. The fan nickname "Okudagram" honors him directly. His wife Denise Okuda and illustrator Rick Sternbach helped develop the wider technical-manual visual world that LCARS anchored.

The look was practical fiction: real consoles were printed gels lit from behind, so the interface had to be pure flat color with no rendering, no depth, no photographic texture. That constraint became the style — saturated orange, tan, lilac, violet, and blue capsules arranged around sweeping "elbow" frames over generous black space. Across decades of Trek and an enormous fan-CSS ecosystem, it remains one of the most instantly recognizable interface aesthetics ever made for screen.

## Overview
Composition cues:
- **Layout**: Asymmetric grid framed by elbow bars — a curved header rail bends down into a left sidebar of stacked capsule buttons, content filling the right field.
- **Content width**: Full-bleed — the interface owns the entire black screen edge to edge, like a console.
- **Framing**: Solid flat color blocks; no borders, no glass — shape and color do all the framing.
- **Grid intensity**: Soft — alignment is strict but lattices are implied by block edges and divider rails, not drawn grids.

## Colors
The palette is a fixed cast of saturated capsule hues glowing on true black: warm golden-orange and sand/tan on one side, cool lilac, moonlit-violet, electric blue, and sky blue on the other. Nothing is muted, nothing is grey-corporate — color blocks are the entire interface. Black is not a background so much as the lit field the capsules float in, and color carries every functional meaning.

**Role usage**:
- Page background → `colors.background.page` (#000000 true black console field)
- Panel / card surface → `colors.background.surface` (#0D0D0F near-black)
- Primary capsules, CTAs, headers → `colors.primary.500` (#FF9900 signature golden-orange)
- Sand / tan secondary blocks → #FFCC99 (`colors.primary.200` family)
- Violet / lilac capsules → `colors.secondary.500` (#9966FF moonlit-violet)
- Electric-blue accent rails → `colors.accent.500` (#5566FF)
- Sky-blue data labels / info → #99CCFF (`colors.semantic.info.text`)
- Primary text on black → `colors.text.primary` (#FFCC99 sand)

## Typography
Condensed and engineered. Antonio carries headings and capsule labels — a tall, ultra-condensed sans that echoes the on-set Helvetica / Swiss-911 lettering — while Oswald handles body text in the same condensed family. Jura, with its rounded technical geometry, sets numeric tags, timestamps, and the right-aligned reference numbers that decorate every LCARS panel. Labels run uppercase with open letter-spacing.

**Text styles**:
- `display-xl` — Antonio, 96px, weight 700, line-height 1.0, letter-spacing 0.02em
- `display-lg` — Antonio, 64px, weight 600, line-height 1.05, letter-spacing 0.02em
- `heading-1` — Antonio, 36px, weight 600, line-height 1.15, letter-spacing 0.05em
- `body-lg` — Oswald, 18px, weight 400, line-height 1.5, letter-spacing 0.02em
- `body-md` — Oswald, 16px, weight 400, line-height 1.5, letter-spacing 0.02em
- `caption` — Jura, 12px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Jura, 16px, weight 500, line-height 1.5, letter-spacing 0.05em

## Spacing & Layout
- Base unit: 4px, but rhythm reads on an 8px beat; scale climbs 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container: full-bleed by default (the console owns the screen); 1280px (xl) when constrained.
- Section padding: 64px (md) standard, 96–128px around hero elbow frames.
- Grid gap: tight 8px between stacked sidebar capsules, 16–24px between major panels; generous black gutters everywhere.

## Elevation & Depth
There is no elevation. LCARS is resolutely flat — backlit gels have no shadow, no bevel, no gloss. Every shadow token is `none` on purpose; depth and grouping come entirely from color, the black gutter, and the radius of the elbow frames. The only ring in the system is a focus outline for accessibility.
- Surface style: flat solid color blocks on black, zero blur.
- Shadow ladder: all `none` — never add drop shadows or inner shadows.
- Focus ring: 3px golden-orange alpha outline (the one permitted glow, for keyboard accessibility).

## Shapes
- Capsule radius rules everything: `full` (9999px) for buttons, pills, and end-caps.
- Block radii: sm 8px, md 16px, lg 28px (panels/cards), xl 48px (elbow frame corners).
- Never square — every interactive block and frame corner is softly rounded; the elbow is a large quarter-radius bend.

## Motion
Restrained and instant, like a touch console responding. Buttons tint or shift opacity on press rather than animating; panels swap rather than slide. Any movement is short and linear — no bounce, no parallax, no decorative flourish. The interface should feel like flat lit acrylic that simply changes color under a fingertip.
- Level: restrained.
- Durations: 120ms fast / 250ms normal for tint changes; avoid slow transitions.
- Easings: standard cubic default and linear out; spring reserved and rarely used.
- Hover patterns: tint, opacity.
- `prefers-reduced-motion`: respected — color changes are instant, no transitions.

## Techniques
Brand-specific CSS recipes that carry the Okudagram console look.

### Elbow frame
The signature LCARS corner — a header bar bending down into a sidebar in one continuous radius.
```css
.lcars-elbow {
  display: grid;
  grid-template-columns: 160px 1fr;
  grid-template-rows: 60px 1fr;
  gap: 8px;
  background: #000000;
}
.lcars-elbow__corner {
  grid-row: 1 / 3;
  background: #FF9900;
  border-top-left-radius: 48px;
  border-bottom-left-radius: 48px;
}
.lcars-elbow__header {
  background: #9966FF;
  border-top-right-radius: 28px;
}
```

### Capsule button
The rounded Okudagram block — flat color, end-cap radius, uppercase condensed label.
```css
.lcars-capsule {
  display: inline-flex;
  align-items: center;
  justify-content: flex-end;
  height: 44px;
  padding: 0 28px;
  background: #FF9900;
  color: #000000;
  font-family: 'Antonio', sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: none;
  border-radius: 9999px;
  transition: background 120ms linear;
}
.lcars-capsule:hover { background: #FFCC99; }
.lcars-capsule--violet { background: #9966FF; }
.lcars-capsule--blue { background: #5566FF; }
```

### Numeric reference tag
The right-aligned Jura number that labels every panel, padded to a fixed digit count.
```css
.lcars-tag {
  font-family: 'Jura', monospace;
  font-weight: 500;
  letter-spacing: 0.05em;
  color: #99CCFF;
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

## Iconography
LCARS rarely uses pictographic icons — meaning is carried by color, capsule shape, and numeric tags. When symbols appear, keep them flat and filled (the Star Trek delta, simple solid glyphs), matched to the capsule palette, never outlined line-art with shadows. Treat any icon as another flat color block, not a decorated illustration.
- Treatment: filled / solid.
- Set: custom (flat geometric glyphs; no stock line-icon library).
- Stroke: 0px — solid fills only.

## Do's & Don'ts
### ✓ Do
- Keep the page floor pure black (#000000) — the canonical backlit console field.
- Use golden-orange (#FF9900) for primary capsules, headers, and CTAs.
- Round every interactive block to a full capsule and bend frame corners with the elbow radius.
- Carry meaning through saturated orange + violet + blue color blocks, not borders.
- Right-align numeric reference tags in Jura on every panel.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — the ground is true black.
- No drop shadows, bevels, or glossy/skeuomorphic chrome — LCARS is resolutely flat.
- No square hard-cornered buttons — every interactive block is capsule-rounded.
- No cool minimalist gray "dashboard" palette; commit to the saturated orange + purple + blue capsule set.

## Applications
Best for sci-fi and gaming brands, dashboard and control-panel UIs, event microsites, fan projects, and any product that wants a confident retro-future console identity. It shines in full-bleed dark layouts with stacked capsule navigation and live data tags — less suited to long-form print, photography-heavy editorial, or muted corporate contexts.
