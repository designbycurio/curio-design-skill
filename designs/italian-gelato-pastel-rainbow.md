---
version: 1

meta:
  id: italian-gelato-pastel-rainbow
  name: Italian Gelato Shop
  description: Pastel-rainbow artisanal gelateria aesthetic with hand-chalked warmth and cobblestone charm
  isDark: false
  tags: [warm, playful, friendly, handmade, decorative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "16th-century Florentine origins; modern boutique-gelateria revival 2000s–present"
  region: "Italy — Rome, Bologna, Florence, Turin"
  regionZh: "意大利——罗马、博洛尼亚、佛罗伦萨、都灵"
  keyFigures: [Bernardo Buontalenti, Stefano Ferrara, Federico Grom, Procopio Cutò]
  movements: [artigianale Italian food revival, slow-food movement, modern Italian boutique branding]

introduction: |
  The Italian gelato-shop aesthetic draws from the artisanal gelateria revival — metal trays of pastel-hued tubs glowing under counter lights, hand-chalked flavor boards in Italian script, and the warm terracotta tones of Roman cobblestones at dusk. It layers milky pistachio greens, strawberry pinks, and lemon yellows over chocolate-brown groundwork.

  This system captures Trastevere at 9 PM in July: generous warmth, handmade texture, and the quiet confidence of a craft perfected over centuries. Every element feels scooped by hand, never factory-pressed.
introductionZh: |
  意大利手工冰淇淋店美学源自千禧年后的精品冰淇淋复兴浪潮——罗马剧院冰淇淋店的十七世纪庭院、博洛尼亚La Romana自1947年延续至今的品牌传承、以及Grom对单一产地原料的执着追求。金属展示盘中一排排粉彩色调的冰淇淋，手写黑板上的意大利语风味名，构成了这一视觉语言的核心。

  整套设计如同七月傍晚的罗马特拉斯提弗列区：脚下鹅卵石尚存白日余温，开心果绿与草莓粉在柜台灯光下柔和发光，巧克力棕色为所有甜蜜色彩提供沉稳的锚点。质感温润如手工纸张，绝非工业化的光滑糖果。

colors:
  primary:    {"50": "#fef2f5", "100": "#fde6ec", "200": "#fbd0db", "300": "#f8b8c9", "400": "#f4b4c4", "500": "#F4B4C4", "600": "#e08da3", "700": "#c46a83", "800": "#a34d66", "900": "#7d3a4e", "950": "#5a2537"}
  secondary:  {"50": "#f7f1ec", "100": "#ede0d5", "200": "#d9bfab", "300": "#c19a7e", "400": "#a07254", "500": "#5C3D2A", "600": "#523626", "700": "#452d20", "800": "#38241a", "900": "#2c1c14", "950": "#1e120d"}
  accent:     {"50": "#fef8eb", "100": "#fcefc9", "200": "#f9e09e", "300": "#f5cf6e", "400": "#f1be47", "500": "#E9A93C", "600": "#d08e28", "700": "#ab6f1f", "800": "#875620", "900": "#6b4520", "950": "#4a2d12"}
  neutral:    {"50": "#faf8f4", "100": "#f5f0e8", "200": "#ebe3d6", "300": "#ddd3c1", "400": "#c4b69f", "500": "#a89880", "600": "#8a7a63", "700": "#6d5f4c", "800": "#544839", "900": "#3d342a", "950": "#2A1F1A"}
  semantic:
    success: { bg: "#d4edda", text: "#2d5a3a", light: "#e8f5ec", border: "#a8d89c" }
    warning: { bg: "#fff3cd", text: "#7a5c00", light: "#fff9e6", border: "#f5e186" }
    error:   { bg: "#f8d7da", text: "#842029", light: "#fdebed", border: "#e4a0a8" }
    info:    { bg: "#d6e9f8", text: "#2a5a7a", light: "#e8f2fb", border: "#a3cde6" }
  background:
    page:    "#A8D89C"
    surface: "#F8F0DC"
    subtle:  "#C8E4BE"
  text:
    primary:   "#2A1F1A"
    secondary: "#5C3D2A"
    muted:     "#8a7a63"
    inverse:   "#F8F0DC"

typography:
  families:
    heading: "'Playfair Display', Georgia, serif"
    body:    "'Lora', 'Times New Roman', serif"
    mono:    "'Caveat', cursive"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Playfair+Display:wght@400;500;600;700;800&display=swap"
  scale: {"2xs": "0.625rem", "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "8px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "4px", md: "8px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "#C97A5A", subtle: "#ddd3c1", strong: "#5C3D2A", focus: "#E9A93C"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(92, 61, 42, 0.04)"
  sm: "0 2px 4px rgba(92, 61, 42, 0.08)"
  md: "0 4px 8px rgba(92, 61, 42, 0.12)"
  lg: "0 8px 16px rgba(92, 61, 42, 0.14)"
  xl: "0 12px 24px rgba(92, 61, 42, 0.16)"
  "2xl": "0 20px 40px rgba(92, 61, 42, 0.20)"
  inner: "inset 0 1px 2px rgba(92, 61, 42, 0.06)"
  focus: "0 0 0 3px rgba(233, 169, 60, 0.35)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, scale]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "solid"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#5C3D2A", color: "#F8F0DC", border: "none", shadow: "0 2px 4px rgba(92, 61, 42, 0.08)", hoverBackground: "#452d20", hoverShadow: "0 4px 8px rgba(92, 61, 42, 0.12)", hoverColor: "#F8F0DC"}
    secondary: {background: "#F8F0DC", color: "#5C3D2A", border: "1px solid #C97A5A", shadow: "none", hoverBackground: "#f5e8d0", hoverShadow: "0 2px 4px rgba(92, 61, 42, 0.08)", hoverColor: "#5C3D2A"}
    ghost:     {background: "transparent", color: "#5C3D2A", border: "none", shadow: "none", hoverBackground: "rgba(92, 61, 42, 0.06)", hoverShadow: "none", hoverColor: "#2A1F1A"}
    danger:    {background: "#c0392b", color: "#ffffff", border: "none", shadow: "none", hoverBackground: "#a33025", hoverShadow: "0 2px 4px rgba(192, 57, 43, 0.2)", hoverColor: "#ffffff"}
    sizes:     {sm: {height: "32px", padding: "6px 14px", fontSize: "0.875rem"}, md: {height: "40px", padding: "8px 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "12px 28px", fontSize: "1.125rem"}}
    borderRadius: "16px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#F8F0DC"
    color: "#2A1F1A"
    border: "1px solid #C97A5A"
    borderRadius: "8px"
    padding: "10px 14px"
    focusBorder: "#E9A93C"
    placeholderColor: "#8a7a63"
  card:
    base:  {background: "#F8F0DC", border: "1px solid #C97A5A", borderRadius: "8px", padding: "24px", shadow: "0 4px 8px rgba(92, 61, 42, 0.12)"}
    hover: {shadow: "0 8px 16px rgba(92, 61, 42, 0.14)", transform: "translateY(-2px)"}
---

# Italian Gelato Shop

> Pastel-rainbow artisanal gelateria warmth — pistachio green, strawberry pink, and hand-chalked Italian script over cobblestone charm.

## Origin

The Italian gelato tradition traces to 16th-century Florence, where Bernardo Buontalenti is credited with creating the first frozen dessert for the Medici court. Procopio Cutò, a Sicilian, later brought gelato to Paris in the 1680s. But the modern visual language of the gelateria emerged from the artisanal revival of the 2000s — boutique shops like Gelateria del Teatro (housed in a 17th-century Roman courtyard), Gelateria La Romana (operating since 1947 in Bologna), and Grom (founded 2003 in Turin with single-origin ingredient sourcing).

These gelaterias built an entire aesthetic from one iconic image: the metal counter display of tubs, each a different milky pastel — pistachio green, strawberry pink, lemon yellow, hazelnut cream. Layered with hand-chalked Italian menus, warm terracotta tones from Roman cobblestones, and chocolate-brown grounding, the look captures the slow-food movement's reverence for craft. It is Trastevere at dusk: warm stone, open doors, and the soft glow of pastel gelato under counter lights.

## Overview

Composition cues:
- **Layout**: Vertical stack with generous breathing room, mimicking tall narrow chalkboard menus
- **Content width**: Container (max 1024px), centered with ample side margins
- **Framing**: Solid cream-paper cards on a pistachio-green page — layered surfaces, not floating glass
- **Grid intensity**: Soft — horizontal rows of pastel circles (gelato-tub motif) for decorative rhythm, not rigid Swiss grids

## Colors

The palette is drawn directly from the gelato counter: milky pistachio green dominates the page like the most popular tub, strawberry pink provides primary accents, and chocolate brown grounds everything with warmth and legibility. Lemon yellow and saffron gold appear as highlights — the chalkboard-script and price-label moments. Rome-terracotta (`#C97A5A`) warms borders and rule lines. Cream (`#F8F0DC`) is reserved exclusively for card surfaces, never the page background. Every color is milky and matte, never neon or glossy — these are gelato tones, not candy colors.

**Role usage**:
- Page background → `colors.background.page` (#A8D89C pistachio green)
- Card / menu-panel surface → `colors.background.surface` (#F8F0DC cream)
- Softer green sections → `colors.background.subtle` (#C8E4BE)
- Primary text → `colors.text.primary` (#2A1F1A espresso-bean ink)
- Secondary text / labels → `colors.text.secondary` (#5C3D2A chocolate brown)
- Accent highlights / prices → `colors.accent.500` (#E9A93C saffron)
- Border / rule lines → `borders.color.default` (#C97A5A terracotta)
- Button backgrounds → `colors.secondary.500` (#5C3D2A chocolate brown)

## Typography

The type voice is warm Italian elegance — Playfair Display brings Didone sophistication to menu headlines (the same high-contrast serif tradition seen in Italian fashion and food publishing), while Lora provides a readable, warm serif for body text and flavor descriptions. Caveat supplies the hand-chalked-blackboard script moment — used sparingly for accent labels, prices, and decorative flourishes. Italian diacritics (à, è, ò, ù) are treated with care; flavor names remain in Italian (pistacchio di Bronte, fior di latte, stracciatella).

**Text styles**:
- `display-xl` — Playfair Display, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Playfair Display, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Playfair Display, 48px, weight 600, line-height 1.2, letter-spacing -0.02em
- `heading-2` — Playfair Display, 36px, weight 600, line-height 1.2, letter-spacing 0
- `body-lg` — Lora, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Lora, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Lora, 14px, weight 500, line-height 1.5, letter-spacing 0
- `mono-md` — Caveat, 20px, weight 400, line-height 1.4, letter-spacing 0

## Spacing & Layout

- Base unit: 8px — all spacing derives from multiples of 8
- Generous padding around imagery: 24px minimum
- Card internal padding: 24px
- Section padding: 64px vertical (md), 96px (lg)
- Container max-width: 1024px centered
- Grid gap: 16px (md) between cards, 24px (lg) for gallery layouts
- Tall narrow card proportions mimicking restaurant chalkboard menus

## Elevation & Depth

Surfaces are layered like a gelateria interior: the pistachio-green page is the painted wall, cream cards are paper menus pinned to it, and subtle chocolate-brown shadows provide just enough depth to separate layers. No glossy gradients — gelato is matte-creamy. Shadows use warm brown tones (rgba 92, 61, 42) rather than cold black, maintaining the warmth throughout the depth stack.

- Cards float with `shadow.md` (0 4px 8px rgba(92,61,42,0.12)) — soft and warm
- Hover lifts cards to `shadow.lg` with a subtle -2px translateY
- No blur/glass effects — surfaces are opaque and paper-like
- Shadow ladder: xs → sm → md → lg → xl → 2xl, all in warm chocolate-brown alpha

## Shapes

- Card border-radius: 8px (friendly but not bubbly)
- Button border-radius: 16px (gelato-scoop-shaped, inviting)
- Input border-radius: 8px (matching cards)
- Tag / badge radius: full (9999px pill shape)
- Image containers: 8px radius
- No sharp 0px corners anywhere — everything has at least 4px softness

## Motion

Motion is restrained and warm — like a hand placing a cone on the counter, not a carnival ride. Transitions are smooth and unhurried, reflecting the slow-food philosophy. Hover states lift gently or warm in tint. Nothing bounces or overshoots aggressively.

- Level: restrained
- Default duration: 250ms for most interactions
- Fast: 120ms for micro-feedback (button press)
- Slow: 400ms for card reveals and page transitions
- Default easing: cubic-bezier(0.4, 0, 0.2, 1) — smooth deceleration
- Spring easing available for playful moments: cubic-bezier(0.34, 1.56, 0.64, 1)
- Hover patterns: lift (translateY -2px), tint (background warmth shift), scale (1.02 on images)
- Reduced motion respected: all animations collapse to instant

## Techniques

### Creamy paper-grain texture
A subtle noise overlay on cream surfaces that evokes hand-made paper menus and artisanal packaging.
```css
.surface-grain {
  background-color: #F8F0DC;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='grain'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23grain)' opacity='0.02'/%3E%3C/svg%3E");
}
```

### Gelato-tub pastel row
Horizontal row of pastel circles evoking the overhead view of a gelato counter display — used as decorative section dividers.
```css
.gelato-tub-row {
  display: flex;
  justify-content: center;
  gap: 12px;
  padding: 24px 0;
}
.gelato-tub-row span {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(92, 61, 42, 0.1);
}
.gelato-tub-row span:nth-child(1) { background: #A8D89C; }
.gelato-tub-row span:nth-child(2) { background: #F4B4C4; }
.gelato-tub-row span:nth-child(3) { background: #F5E186; }
.gelato-tub-row span:nth-child(4) { background: #C97A5A; }
.gelato-tub-row span:nth-child(5) { background: #E9A93C; }
.gelato-tub-row span:nth-child(6) { background: #F8F0DC; }
```

### Hand-chalked script accent
Caveat-font labels styled to feel like hand-written chalkboard annotations — used for prices, flavor callouts, and decorative asides.
```css
.chalk-accent {
  font-family: 'Caveat', cursive;
  font-size: 1.25rem;
  color: #E9A93C;
  transform: rotate(-2deg);
  display: inline-block;
  letter-spacing: 0.02em;
}
```

## Iconography

Icons are linear and lightweight — thin strokes that complement the serif typography without competing for attention. They evoke hand-drawn menu illustrations (a cone, a spoon, a leaf) rather than heavy UI chrome.

- Treatment: linear (outline only)
- Set: Lucide (clean, friendly, pairs well with serif type)
- Stroke: 1.5px — delicate but legible at small sizes

## Do's & Don'ts

### ✓ Do
- Use pistachio green (#A8D89C) as the dominant page background — it IS the brand
- Ground all sweetness with chocolate brown (#5C3D2A) text and buttons
- Reserve cream (#F8F0DC) exclusively for card surfaces and menu panels
- Use Caveat script sparingly — for prices, callouts, and decorative moments only
- Preserve Italian flavor names in their original language (pistacchio, stracciatella, fior di latte)

### ✗ Don't
- Use beige or cream as page background — cream is card surface only
- Apply Italian-flag red-white-green tourist kitsch color schemes
- Use bright neon candy colors — all pastels must be milky and matte
- Mimic American ice-cream-parlor pink-and-chrome diner aesthetics
- Include stock pizza or pasta tourism photography
- Fall into cold Scandinavian minimalism — this system is warm and handmade
- Set type in all-caps screaming retail style
- Add cartoon mascot characters

## Applications

This system is ideal for artisanal food brands, restaurant and café websites, menu design, food-delivery landing pages, and boutique retail experiences that want to feel handmade, warm, and Italian-inflected. It works beautifully for editorial food content, recipe platforms, and any product that benefits from the slow-food ethos of craft over speed.
