---
version: 1

meta:
  id: brutalist-web-2014
  name: Brutalist Web 2014
  description: Raw HTML aesthetic — no decoration, no rounded corners, pure structural honesty
  isDark: false
  tags: [bold, editorial, modernist, experimental]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2014–2020; brutalistwebsites.com launched 2014"
  region: "International web design discourse; Berlin / NYC nexus"
  regionZh: "国际网页设计圈；柏林/纽约交汇"
  keyFigures: [Pascal Deville, Balenciaga, Matt Drudge, Tim Berners-Lee]
  movements: [anti-design, post-digital, architectural Brutalism]

introduction: |
  Brutalist web design strips the browser back to its defaults — Times New Roman, electric blue links, solid black borders, and nothing else. Emerging around 2014 as a conscious rejection of polished SaaS aesthetics, it treats raw HTML structure as both medium and message.

  The movement draws its name from béton brut (raw concrete) and channels the same confrontational honesty into digital form. Sites like brutalistwebsites.com, Drudge Report, and Balenciaga's 2015 redesign proved that refusing decoration could itself be a powerful design statement.
introductionZh: |
  粗野主义网页设计将浏览器还原到最原始的状态——Times New Roman 字体、电蓝色超链接、纯黑实线边框，别无他物。它在2014年前后兴起，是对千篇一律的 SaaS 视觉风格的一次有意识的反叛，将未经修饰的 HTML 结构本身视为表达的媒介与信息。

  这一运动的名称源自建筑学中的"清水混凝土"（béton brut），并将同样毫不妥协的诚实态度注入数字世界。brutalistwebsites.com、Drudge Report 以及巴黎世家2015年的官网改版证明了：拒绝装饰本身，也可以成为一种强有力的设计宣言。

colors:
  primary:
    "50": "#e6e6ff"
    "100": "#bfbfff"
    "200": "#9999ff"
    "300": "#7373ff"
    "400": "#4d4dff"
    "500": "#0000ee"
    "600": "#0000cc"
    "700": "#0000aa"
    "800": "#000088"
    "900": "#000066"
    "950": "#000044"
  secondary:
    "50": "#f2f2f2"
    "100": "#e6e6e6"
    "200": "#cccccc"
    "300": "#b3b3b3"
    "400": "#999999"
    "500": "#666666"
    "600": "#555555"
    "700": "#444444"
    "800": "#333333"
    "900": "#222222"
    "950": "#111111"
  accent:
    "50": "#fff0ff"
    "100": "#ffe0ff"
    "200": "#ffc0ff"
    "300": "#ffa0ff"
    "400": "#ff80ff"
    "500": "#ff00ff"
    "600": "#dd00dd"
    "700": "#bb00bb"
    "800": "#990099"
    "900": "#770077"
    "950": "#440044"
  neutral:
    "50": "#ffffff"
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
    success: { bg: "#008000", text: "#ffffff", light: "#e6f5e6", border: "#008000" }
    warning: { bg: "#ff8c00", text: "#000000", light: "#fff5e6", border: "#ff8c00" }
    error:   { bg: "#ff0000", text: "#ffffff", light: "#ffe6e6", border: "#ff0000" }
    info:    { bg: "#0000ee", text: "#ffffff", light: "#e6e6ff", border: "#0000ee" }
  background:
    page:    "#ffffff"
    surface: "#ffffff"
    subtle:  "#f5f5f5"
  text:
    primary:   "#000000"
    secondary: "#333333"
    muted:     "#666666"
    inverse:   "#ffffff"

typography:
  families:
    heading: "'EB Garamond', 'Times New Roman', Times, serif"
    body:    "'EB Garamond', 'Times New Roman', Times, serif"
    mono:    "'Cutive Mono', 'Courier New', Courier, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,700&family=Cutive+Mono&display=swap"
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
    sm: "0"
    md: "0"
    lg: "0"
    xl: "0"
    full: "0"
  color:
    default: "#000000"
    subtle: "#666666"
    strong: "#000000"
    focus: "#0000ee"
  width:
    thin: "1px"
    default: "2px"
    thick: "3px"
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
  focus: "0 0 0 3px rgba(0, 0, 238, 0.3)"

motion:
  level: "minimal"
  durations:
    instant: "0ms"
    fast: "0ms"
    normal: "0ms"
    slow: "100ms"
    slower: "200ms"
  easings:
    default: "linear"
    in: "linear"
    out: "linear"
    spring: "linear"
  hoverPatterns: [underline, opacity]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "narrow"
  framing: "minimal"
  gridIntensity: "none"
  rhythm: "4px"

surfaceStyle: "flat"
blur: "none"

iconography:
  treatment: "outline"
  set: "feather"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#000000"
      color: "#ffffff"
      border: "2px solid #000000"
      shadow: "none"
      hoverBackground: "#ffffff"
      hoverShadow: "none"
      hoverColor: "#000000"
    secondary:
      background: "#ffffff"
      color: "#000000"
      border: "2px solid #000000"
      shadow: "none"
      hoverBackground: "#000000"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    ghost:
      background: "transparent"
      color: "#0000ee"
      border: "none"
      shadow: "none"
      hoverBackground: "transparent"
      hoverShadow: "none"
      hoverColor: "#000000"
    danger:
      background: "#ff0000"
      color: "#ffffff"
      border: "2px solid #ff0000"
      shadow: "none"
      hoverBackground: "#cc0000"
      hoverShadow: "none"
      hoverColor: "#ffffff"
    sizes:
      sm: { height: "32px", padding: "4px 12px", fontSize: "0.75rem" }
      md: { height: "40px", padding: "8px 20px", fontSize: "0.875rem" }
      lg: { height: "48px", padding: "12px 28px", fontSize: "1rem" }
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#ffffff"
    color: "#000000"
    border: "2px solid #000000"
    borderRadius: "0"
    padding: "8px 12px"
    focusBorder: "2px solid #0000ee"
    placeholderColor: "#666666"
  card:
    base:
      background: "#ffffff"
      border: "1px solid #000000"
      borderRadius: "0"
      padding: "16px"
      shadow: "none"
    hover:
      shadow: "none"
      transform: "none"
---

# Brutalist Web 2014

> Raw HTML as ideology — no decoration, no compromise, no rounded corners.

## Origin

Brutalist web design surfaced around 2014 as a deliberate provocation against the polished uniformity of consumer-tech interfaces. Pascal Deville's brutalistwebsites.com became the movement's gallery, cataloguing sites that looked "broken" by conventional UX standards — yet were fully intentional. The aesthetic drew openly from architectural Brutalism, where Le Corbusier and Ernő Goldfinger celebrated exposed concrete over decorative facades.

The movement found unlikely allies: Balenciaga stripped its fashion site to raw HTML in 2015, Bloomberg Businessweek ran experimental long-form layouts that defied grid norms, and the Drudge Report — running essentially the same layout since 1997 — was retroactively canonized as a brutalist ancestor. This was anti-design as critical practice: if every SaaS landing page looked the same, brutalism proved that refusal itself could be a brand.

## Overview
Composition cues:
- **Layout**: Vertical stack — long, uninterrupted text columns with aggressive whitespace
- **Content width**: Narrow, single-column reading measure
- **Framing**: Minimal — no cards, no containers, just content and occasional hard borders
- **Grid intensity**: None — brutalism rejects grid systems as a design crutch

## Colors
Color in brutalist web design is not a palette — it is an accident of browser defaults made deliberate. Pure white (#ffffff) background, pure black (#000000) text, and the electric blue of an unvisited hyperlink (#0000ee) form the entire working vocabulary. If an accent appears at all, it is a single, screaming hue — fuchsia (#ff00ff) or chartreuse — chosen for maximum disruption, never for harmony.

**Role usage**:
- Page background → `colors.background.page` (#ffffff, non-negotiable)
- Body text → `colors.text.primary` (#000000, maximum contrast)
- Links and interactive elements → `colors.primary.500` (#0000ee, browser-default blue)
- Accent / disruption highlights → `colors.accent.500` (#ff00ff, sparingly)
- Secondary text → `colors.text.muted` (#666666, minimal hierarchy)
- Borders → `colors.borders.default` (#000000, always solid)
- Hover states → text color inversion only
- Semantic states → raw, unstyled browser-default colors (pure red, pure green)

## Typography
Typography in brutalist web design is an act of refusal. Where modern design selects typefaces for brand expression, brutalism uses whatever the browser ships with. The canonical choice is Times New Roman — the serif that every operating system includes and no designer would choose voluntarily. EB Garamond serves as the web-font equivalent: recognizably "default serif" while being properly hinted for screens. Cutive Mono stands in for Courier New when monospace is needed. There is no typographic hierarchy beyond size — headings and body share the same family, the same weight. The message is the content, not its styling.

**Text styles**:
- `display-xl` — EB Garamond, 96px, weight 400, line-height 1.0, letter-spacing -0.04em
- `display-lg` — EB Garamond, 64px, weight 400, line-height 1.1, letter-spacing -0.02em
- `heading-1` — EB Garamond, 48px, weight 700, line-height 1.2, letter-spacing 0
- `body-lg` — EB Garamond, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — EB Garamond, 18px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — EB Garamond, 14px, weight 400, line-height 1.5, letter-spacing 0
- `mono-md` — Cutive Mono, 16px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px
- Scale follows default browser rhythm: 8px, 16px, 24px, 32px, 48px, 64px
- Container max-width: 640px (narrow single-column, like a printed page)
- Section padding: generous vertical space (64px–128px) to let content breathe against the bare white page
- No grid gaps — elements stack vertically with simple margins
- Horizontal padding: minimal (16px on mobile, 0 on desktop within container)

## Elevation & Depth
There is no elevation. Brutalist web design is deliberately flat — not "flat design" flat, but actually flat, like a sheet of paper. No shadows exist in the system. No blur. No layering. Elements sit directly on the white page. If something needs visual separation, it gets a black border. The Z-axis does not exist here. This is a conscious rejection of skeuomorphism, Material Design's elevation model, and any metaphor that pretends a screen is three-dimensional.

- Surface style: flat — no background differentiation between surface levels
- Blur: none (0px, always)
- Shadow ladder: entirely "none" — shadows are forbidden by principle
- Separation method: 1–2px solid black borders only

## Shapes
- All corner radii: 0 — this is the single most non-negotiable rule
- `border-radius: 0` on every element: buttons, inputs, cards, images, modals
- No rounded corners, no pill shapes, no circles (except text content like bullet points)
- Rectangles only — the native shape of the HTML box model

## Motion
Brutalism is suspicious of animation. Motion in web design typically exists to smooth transitions, guide attention, and make interfaces feel "polished" — all things brutalism explicitly rejects. The default is no motion at all. If absolutely necessary, transitions are instant or near-instant. Hover states change properties immediately, without easing. Scroll is native. Loading states are a plain text string ("Loading..."), not a spinner.

- Level: minimal (approaching zero)
- Durations: 0ms for most interactions; 100ms maximum for state changes
- Easings: linear only — no ease-in-out, no springs, no bounce
- Hover patterns: underline (for links), opacity (for interactive elements)
- Reduced motion: always on by default — the baseline IS reduced motion
- No scroll animations, no parallax, no fade-ins

## Techniques

### Raw HTML Link Wall
A dense, undecorated list of hyperlinks in browser-default blue with underlines — the fundamental navigation pattern of the early web, reclaimed as an aesthetic choice.
```css
.link-wall {
  font-family: 'EB Garamond', 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.8;
  max-width: 640px;
}
.link-wall a {
  color: #0000ee;
  text-decoration: underline;
}
.link-wall a:visited {
  color: #551a8b;
}
.link-wall a:hover {
  color: #ff00ff;
}
```

### Black-Border Content Block
A content container that uses only a solid black border for separation — no shadow, no background, no radius. The border weight communicates hierarchy.
```css
.content-block {
  border: 2px solid #000000;
  padding: 24px;
  margin: 32px 0;
  background: #ffffff;
  border-radius: 0;
  box-shadow: none;
}
.content-block--heavy {
  border-width: 4px;
}
.content-block--ruled {
  border: none;
  border-top: 2px solid #000000;
  border-bottom: 1px solid #000000;
  padding: 24px 0;
}
```

### Monospace Code Aesthetic
Passages set in monospace to evoke terminal output or source code — used for emphasis where other systems might use bold or color, reinforcing the "view source" ethos.
```css
.mono-emphasis {
  font-family: 'Cutive Mono', 'Courier New', monospace;
  font-size: 0.875rem;
  line-height: 1.6;
  letter-spacing: 0.02em;
  background: #f5f5f5;
  border: 1px solid #000000;
  padding: 16px;
  border-radius: 0;
  overflow-x: auto;
  white-space: pre-wrap;
}
```

## Iconography
Brutalist web design is fundamentally skeptical of icons. The early web used text labels, not pictograms, and brutalism follows suit. When icons are absolutely necessary (close buttons, external link indicators), they should be the simplest possible outline stroke — Feather icons at their thinnest setting. Icons should never replace text labels, only supplement them.

- Treatment: outline, minimal — icons are functional signals, not decorative
- Set: Feather (simplest available line icons)
- Stroke: 1.5px — thin enough to feel like punctuation, not illustration

## Do's & Don'ts

### ✓ Do
- Use browser-default blue (#0000ee) for all links — respect the convention brutalism is built on
- Keep all border-radius at exactly 0 — rectangles are the only permitted shape
- Let long-form text run in a single narrow column with generous line-height
- Use solid black borders as the primary (and only) method of visual separation
- Embrace white space as a structural element, not empty space to be filled

### ✗ Don't
- Use rounded corners of any kind — this is the cardinal sin of brutalist design
- Apply gradients or shadows — elevation does not exist in this system
- Reach for modern sans-serif typefaces — Helvetica, Inter, and SF Pro are the enemy
- Make anything feel "designed" or polished — the aesthetic should feel like raw HTML
- Use pastel colors — if color appears at all, it must be at full saturation

## Applications
Brutalist web design is best suited for editorial platforms, personal blogs, manifestos, portfolios, and any context where the content must speak louder than its container. It works exceptionally well for text-heavy sites, link aggregators, reading lists, and documentation that values clarity over comfort. It is a natural fit for art galleries, independent publishers, and anyone who wants their web presence to feel like a deliberate statement rather than a template.
