---
version: 1

meta:
  id: mexican-day-of-dead-marigold
  name: Mexican Día de Muertos (Marigold Ofrenda)
  description: Fluorescent-marigold altar aesthetic on velvet-night purple — papel picado, calaveras, and cempasúchil in loud joyful color
  isDark: true
  tags: [historical, bold, decorative, narrative, handmade]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "pre-Hispanic Aztec roots; Catholic syncretism post-1521; codified 19th c.; UNESCO ICH 2008"
  region: "Mexico (Oaxaca, Michoacán, Mexico City, Puebla)"
  regionZh: "墨西哥（瓦哈卡、米却肯、墨西哥城、普埃布拉）"
  keyFigures: [José Guadalupe Posada, Diego Rivera, Frida Kahlo, Octavio Paz]
  movements: [pre-Hispanic Aztec death ritual, Catholic All Saints syncretism, Posada engraving revival, post-1970s national identity codification]

introduction: |
  Día de Muertos wraps death in fluorescent marigold petals. Every November, Mexican families build multi-tiered ofrendas — velvet-draped altars stacked with cempasúchil flowers, papel picado banners, sugar skulls, candles, and photographs of the departed — turning grief into a chromatic celebration that has no visual peer in the Americas.

  This design system captures midnight at the ofrenda: deep velvet-purple grounds, blazing marigold-orange accents, hot-magenta cut-paper lattice, and candle-flame yellow warmth. Typography pairs Posada-era condensed impact with literary serif elegance, and every surface carries the crisp stencil-edge of papel picado and the soft fluorescence of cempasúchil petals.
introductionZh: |
  亡灵节用荧光万寿菊花瓣拥抱死亡。每年十一月，墨西哥家庭搭建多层祭坛（ofrenda）：丝绒紫夜幕为底，堆满万寿菊、剪纸旗、糖骷髅、蜡烛和逝者照片——把哀思化作美洲最浓烈的色彩庆典。

  本设计体系捕捉午夜祭坛的氛围：深邃的丝绒紫夜底色、炽烈的万寿菊橙、灼热的洋红剪纸花边、烛光金黄的温暖辉映。排版将波萨达时代的窄体冲击力与文学衬线字体优雅结合，每个界面都带着剪纸的锐利镂花轮廓和万寿菊花瓣的柔和荧光。

colors:
  primary:    {"50": "#FFF5E6", "100": "#FFE4BF", "200": "#FFD199", "300": "#FFBC66", "400": "#FFA440", "500": "#FF8C20", "600": "#E67A10", "700": "#BF6200", "800": "#994E00", "900": "#733A00", "950": "#4D2600"}
  secondary:  {"50": "#FDE8F1", "100": "#FACBDF", "200": "#F5A0C8", "300": "#EF6EAD", "400": "#E84993", "500": "#E0287A", "600": "#C01E66", "700": "#9E1652", "800": "#7D103F", "900": "#5C0B2E", "950": "#3D0720"}
  accent:     {"50": "#FEF8E6", "100": "#FDF0C8", "200": "#FCE59E", "300": "#FBD976", "400": "#F9D05E", "500": "#F8C84A", "600": "#E5B530", "700": "#C49820", "800": "#9E7A18", "900": "#785C12", "950": "#52400D"}
  neutral:    {"50": "#F0E5D8", "100": "#E6D8C8", "200": "#D4C4B0", "300": "#B8A898", "400": "#9A8C80", "500": "#7A6E64", "600": "#5E544C", "700": "#463E38", "800": "#3A2A5A", "900": "#2A1A4A", "950": "#1A0E30"}
  semantic:
    success: { bg: "#2A6B3A", text: "#D4F5DC", light: "#3A8A4E", border: "#4AA862" }
    warning: { bg: "#F8C84A", text: "#2A1A4A", light: "#FBD976", border: "#E5B530" }
    error:   { bg: "#C8281A", text: "#FDE8E6", light: "#E04030", border: "#D83428" }
    info:    { bg: "#2A4AB8", text: "#E0E8FF", light: "#3A5CD0", border: "#4A6CE0" }
  background:
    page:    "#2A1A4A"
    surface: "#3A2A5A"
    subtle:  "#4A3A6A"
  text:
    primary:   "#F0E5D8"
    secondary: "#D4C4B0"
    muted:     "#9A8C80"
    inverse:   "#2A1A4A"

typography:
  families:
    heading: "'Bebas Neue', Impact, sans-serif"
    body:    "'Cormorant Garamond', 'Times New Roman', serif"
    mono:    "'JetBrains Mono', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Caveat:wght@400;700&family=Marcellus&display=swap"
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
  radius: {none: "0", sm: "4px", md: "8px", lg: "12px", xl: "20px", full: "9999px"}
  color:  {default: "#FF8C20", subtle: "#4A3A6A", strong: "#E0287A", focus: "#F8C84A"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(42, 26, 74, 0.25)"
  sm: "0 2px 6px rgba(42, 26, 74, 0.30)"
  md: "0 4px 16px rgba(255, 140, 32, 0.30)"
  lg: "0 8px 24px rgba(255, 140, 32, 0.35)"
  xl: "0 12px 32px rgba(255, 140, 32, 0.40)"
  "2xl": "0 20px 48px rgba(255, 140, 32, 0.45)"
  inner: "inset 0 1px 3px rgba(42, 26, 74, 0.30)"
  focus: "0 0 0 3px rgba(248, 200, 74, 0.50)"

motion:
  level: "playful"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [glow, scale, tint, lift]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "12px"

iconography:
  treatment: "duotone"
  set:       "phosphor"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#FF8C20", color: "#2A1A4A", border: "2px solid #FF8C20", shadow: "0 4px 16px rgba(255, 140, 32, 0.30)", hoverBackground: "#E67A10", hoverShadow: "0 6px 20px rgba(255, 140, 32, 0.45)", hoverColor: "#2A1A4A"}
    secondary: {background: "transparent", color: "#F0E5D8", border: "2px solid #E0287A", shadow: "none", hoverBackground: "#E0287A", hoverShadow: "0 4px 12px rgba(224, 40, 122, 0.30)", hoverColor: "#F0E5D8"}
    ghost:     {background: "transparent", color: "#F0E5D8", border: "2px solid transparent", shadow: "none", hoverBackground: "rgba(255, 140, 32, 0.12)", hoverShadow: "none", hoverColor: "#FF8C20"}
    danger:    {background: "#C8281A", color: "#FDE8E6", border: "2px solid #C8281A", shadow: "none", hoverBackground: "#A82010", hoverShadow: "0 4px 12px rgba(200, 40, 26, 0.30)", hoverColor: "#FDE8E6"}
    sizes:     {sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "8px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#3A2A5A"
    color: "#F0E5D8"
    border: "2px solid #4A3A6A"
    borderRadius: "8px"
    padding: "10px 14px"
    focusBorder: "#F8C84A"
    placeholderColor: "#9A8C80"
  card:
    base:  {background: "#3A2A5A", border: "3px solid #FF8C20", borderRadius: "12px", padding: "24px", shadow: "0 4px 16px rgba(255, 140, 32, 0.30)"}
    hover: {shadow: "0 8px 24px rgba(255, 140, 32, 0.40)", transform: "translateY(-2px)"}
---

# Mexican Día de Muertos (Marigold Ofrenda)

> A fluorescent-marigold altar on velvet-night purple — papel picado lattice, calavera cartouches, and cempasúchil glow turned into a design system.

## Origin

Día de Muertos descends from the Aztec festival of Mictecacíhuatl, goddess of the dead, syncretized with Catholic All Saints and All Souls Day after the Spanish conquest in 1521. Over five centuries the tradition crystallized into the multi-tiered ofrenda — a domestic altar stacked with cempasúchil marigolds, photographs, candles, sugar skulls, copal incense, pan de muerto, and papel picado banners — that Mexican families construct each November 1–2 to welcome the returning dead.

The visual language we know today owes its sharpest lines to José Guadalupe Posada, whose calavera engravings (1900–1913) gave death its sardonic grin, and to Diego Rivera, who elevated Posada's "La Catrina" into a national icon. UNESCO inscribed the festival as Intangible Cultural Heritage in 2008, recognizing it as a living practice spanning Oaxaca, Michoacán, Mexico City, Puebla, and the Mexican-American diaspora. The aesthetic is folk-altar handmade: loud, layered, saturated, and defiantly joyful.

## Overview

Composition cues:
- **Layout**: Vertical stack compositions echoing the three-tier ofrenda — content stacks upward from a velvet-purple ground, each tier framed by marigold borders and papel-picado lattice dividers.
- **Content width**: Container (max ~1024–1280 px) — the altar is framed, not infinite.
- **Framing**: Bordered — every card and panel gets a visible 3 px marigold or magenta papel-picado border, evoking cut-paper stencil edges.
- **Grid intensity**: Soft — the ofrenda is arranged but organic; items overlap and crowd together rather than snapping to a rigid grid.

## Colors

The palette is a midnight vigil: the dominant ground is deep velvet-night purple (`#2A1A4A`), the color of the sky above an Oaxacan cemetery at midnight. Against this darkness, fluorescent marigold orange (`#FF8C20`) blazes as the primary accent — the cempasúchil petal that guides the dead home. Hot magenta (`#E0287A`) cuts through like papel picado banners strung across a courtyard. Candle-flame yellow (`#F8C84A`) provides warm glow highlights. Bone-white (`#F0E5D8`) grounds text surfaces like sugar-skull icing. The palette is deliberately loud, saturated, and festival-bright — Día de Muertos is chromatic joy, not muted mourning.

**Role usage**:
- Page background → `colors.background.page` (velvet-night purple)
- Card / surface backgrounds → `colors.background.surface` (lighter velvet)
- Primary actions, key accents → `colors.primary.500` (marigold orange)
- Secondary accents, borders, tags → `colors.secondary.500` (hot magenta)
- Warm highlights, focus rings, badges → `colors.accent.500` (candle-flame yellow)
- Body text on dark → `colors.text.primary` (bone-white)
- Body text on light surfaces → `colors.text.inverse` (velvet-night purple)
- Muted labels, captions → `colors.text.muted`
- Semantic feedback → `colors.semantic.*`

## Typography

The type voice pairs Posada-era engraving impact with literary serif elegance. **Bebas Neue** — tall, condensed, all-caps — shouts headlines like a broadside calavera print nailed to a plaza wall; it carries the blunt directness of 1900s Mexican printmaking. **Cormorant Garamond** provides the body text with the cultured warmth of Octavio Paz's prose — a serif with calligraphic soul that reads comfortably at length against dark or light grounds. **Caveat** adds a hand-lettered voice for calavera-literaria poetry captions. **Marcellus** serves cartouche labels and secondary headings with restrained classical elegance. The contrast between condensed sans display and literary serif body creates the festival's own tension: irreverent spectacle meeting sincere remembrance.

**Text styles**:
- `display-xl` — Bebas Neue, 96px, weight 400, line-height 1.0, letter-spacing 0.05em
- `display-lg` — Bebas Neue, 64px, weight 400, line-height 1.05, letter-spacing 0.05em
- `heading-1` — Bebas Neue, 48px, weight 400, line-height 1.1, letter-spacing 0.05em
- `heading-2` — Marcellus, 32px, weight 400, line-height 1.2, letter-spacing 0
- `body-lg` — Cormorant Garamond, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Cormorant Garamond, 18px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Caveat, 16px, weight 400, line-height 1.375, letter-spacing 0
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8 px (ofrenda items are densely packed but rhythmic)
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-width: 1280 px (xl), narrower tiers at 1024 / 768 / 640 px
- Section padding: 64–128 px vertical — generous breathing room between altar tiers
- Grid gap: 16–24 px — items crowd together like ofrenda objects, not spaced apart

## Elevation & Depth

Surfaces are layered like an ofrenda's stacked tiers. The base page is the deepest velvet-night; surfaces rise through progressively lighter purples. Shadows carry a warm marigold-orange tint rather than neutral black, creating the impression that every elevated element is lit from below by candle flame. Blur is moderate (12 px) — enough to suggest incense haze without losing the crisp stencil-cut edges of papel picado borders.

- Surface layers: page (#2A1A4A) → surface (#3A2A5A) → subtle (#4A3A6A) → bone-white (#F0E5D8) for content blocks
- Shadow color: rgba(255, 140, 32, 0.30) — marigold-tinted candle glow
- Shadow ladder: xs (subtle) → sm → md (default card) → lg (elevated) → xl (hero) → 2xl (modal)
- Inner shadow: inset purple for recessed fields
- Focus ring: candle-flame yellow at 50% opacity

## Shapes

- Button radius: 8 px — slightly rounded cartouche, not pill-shaped
- Card radius: 12 px — soft ofrenda-panel corners
- Input radius: 8 px — matches buttons
- Badge / tag radius: 9999 px (full pill) — sugar-skull roundel
- No radius (0): dividers, full-bleed sections

## Motion

Motion is playful and warm — candle flames flicker, papel picado flutters, marigold petals drift. Transitions lean into spring easings that overshoot slightly, giving UI elements the buoyant energy of a festival celebration rather than clinical precision. Nothing is sluggish; the dead have only two days to visit, so the interface feels alive and immediate.

- Level: playful
- Durations: instant 0 ms, fast 120 ms, normal 250 ms, slow 400 ms, slower 600 ms
- Default easing: cubic-bezier(0.4, 0, 0.2, 1)
- Spring easing: cubic-bezier(0.34, 1.56, 0.64, 1) — for enter/scale animations
- Hover patterns: glow (marigold shadow intensifies), scale (slight grow), tint (marigold wash), lift (translateY)
- Reduced motion: respected — falls back to opacity-only transitions

## Techniques

### Papel picado border lattice
A repeating cut-paper stencil border using CSS clip-path and a pseudo-element, evoking the scalloped/perforated edges of papel picado banners.
```css
.papel-picado-border {
  position: relative;
  border: 3px solid #FF8C20;
  border-radius: 12px;
  overflow: visible;
}
.papel-picado-border::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 5%;
  right: 5%;
  height: 8px;
  background: repeating-linear-gradient(
    90deg,
    #E0287A 0px, #E0287A 12px,
    transparent 12px, transparent 16px,
    #FF8C20 16px, #FF8C20 28px,
    transparent 28px, transparent 32px,
    #F8C84A 32px, #F8C84A 44px,
    transparent 44px, transparent 48px
  );
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 8'%3E%3Cpath d='M0 0h8l4 8h-4L4 4 0 8z M16 0h8l4 8h-4l-4-4-4 4z M32 0h8l4 8h-4l-4-4-4 4z' fill='black'/%3E%3C/svg%3E");
  mask-size: 48px 8px;
  mask-repeat: repeat-x;
}
```

### Cempasúchil candle glow
A radial marigold-orange glow behind hero elements, simulating candle-lit cempasúchil petal fluorescence on the velvet-night ground.
```css
.cempasuchil-glow {
  position: relative;
}
.cempasuchil-glow::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 160%;
  height: 160%;
  transform: translate(-50%, -50%);
  background: radial-gradient(
    ellipse at center,
    rgba(255, 140, 32, 0.25) 0%,
    rgba(248, 200, 74, 0.10) 40%,
    transparent 70%
  );
  pointer-events: none;
  z-index: -1;
  border-radius: 50%;
  filter: blur(20px);
}
```

### Calavera cartouche frame
An ornate oval portrait frame with marigold and magenta layered borders, used for avatar or portrait containers — evoking the framed photographs placed on ofrendas.
```css
.calavera-cartouche {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 3px solid #FF8C20;
  box-shadow:
    0 0 0 6px #2A1A4A,
    0 0 0 9px #E0287A,
    0 0 0 12px #2A1A4A,
    0 0 20px rgba(255, 140, 32, 0.35);
  overflow: hidden;
}
```

## Iconography

Icons use duotone treatment from the Phosphor set — the dual-tone rendering echoes the two-color woodcut prints of Posada's calavera engravings, where a solid fill and a lighter accent layer coexist. The primary tone is bone-white or marigold; the secondary tone is a translucent magenta or candle-yellow.

- Treatment: duotone (primary fill + translucent accent)
- Set: Phosphor
- Stroke width: 1.5 px
- Sizes: 16 / 20 / 24 px (sm / md / lg)

## Do's & Don'ts

### ✓ Do
- Use fluorescent marigold (#FF8C20) as the dominant accent — it is the cempasúchil, the signature of the festival
- Layer borders and frames like papel picado — multi-color, stencil-crisp, and festive
- Keep the velvet-night purple (#2A1A4A) as the page ground to maintain the midnight-vigil atmosphere
- Mix Bebas Neue headlines with Cormorant Garamond body for the Posada-broadside-meets-literary-prose tension
- Let surfaces feel handmade, layered, and altar-like — not slick or corporate

### ✗ Don't
- Use a white page — velvet-night purple is the correct ground
- Use cream or beige page backgrounds — the drama demands dark
- Use modern sans-serif body text (Inter is forbidden)
- Mimic Pixar's Coco corporate palette — this must feel folk-altar handmade
- Restrict the palette to orange-and-black Halloween — Mexican Día de Muertos is multi-color rainbow
- Use generic sugar-skull clip art — skulls should feel hand-decorated with rainbow icing detail
- Mute or subdue the palette for "taste" — Día de Muertos is loud chromatic joy
- Fall into tourist sombrero kitsch

## Applications

This system is built for cultural festival platforms, event landing pages, memorial and tribute sites, Day of the Dead community pages, Mexican folk-art marketplaces, and any interface that needs to channel the layered, saturated, handmade energy of a midnight ofrenda. It pairs especially well with editorial longform, gallery showcases, and celebration-themed dashboards where the bold palette and ornate framing create an immersive, reverent-yet-joyful atmosphere.
