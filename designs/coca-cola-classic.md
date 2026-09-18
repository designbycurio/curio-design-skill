---
version: 1

meta:
  id: coca-cola-classic
  name: Coca-Cola Classic
  description: Full-bleed Coca-Cola red, white Spencerian warmth, and a century of "open happiness" branding distilled into tokens.
  isDark: false
  tags: [bold, friendly, narrative, historical, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1886 invented; Spencerian script logo 1887; contour bottle 1915; current identity refined 1969 (Lippincott & Margulies), maintained through 2024"
  region: "Atlanta, Georgia, USA (global)"
  regionZh: "美国佐治亚州亚特兰大（全球）"
  keyFigures: [Frank Mason Robinson, Raymond Loewy, Haddon Sundblom]
  movements: [American consumer branding, mid-century advertising, global brand standardization]

introduction: |
  Coca-Cola is arguably the most recognized brand in human history. Frank Mason Robinson's 1887
  Spencerian script, the 1915 contour bottle, Haddon Sundblom's cherubic Santa, and a century of
  "happiness" advertising have welded a single red — #F40009 — to the very idea of American
  consumer culture.

  The design language is warm, celebratory, and unapologetically red. Every surface bleeds red;
  the script logo is never modernized; rounded geometry, ribbon-wave dividers, and a permanent
  smile do the emotional work. The visual says "open happiness" in a way that transcends language.
introductionZh: |
  可口可乐，可能是人类历史上辨识度最高的品牌。1887 年 Frank Mason Robinson 亲笔写下的
  Spencerian 花体字、1915 年的弧形玻璃瓶、Haddon Sundblom 1931 年画出的红衣圣诞老人，以及
  长达一个世纪的"快乐"广告，把一种红——#F40009——牢牢焊接在美国消费文化的集体记忆里。

  它的设计语言是温暖的、庆典式的、毫不掩饰的红色。页面大面积被红吞没，花体 logo 从不被
  "现代化"；圆角几何、缎带波浪线和永不收起的笑容承担起所有情绪的重量。整套视觉在说同一
  句话——"打开快乐"，而这句话不需要翻译。

colors:
  primary:
    "50":  "#FFF1F2"
    "100": "#FFD9DB"
    "200": "#FFB0B4"
    "300": "#FF7A80"
    "400": "#FB4049"
    "500": "#F40009"
    "600": "#CC0008"
    "700": "#A30006"
    "800": "#7A0005"
    "900": "#520003"
    "950": "#2E0002"
  secondary:
    "50":  "#F5F5F5"
    "100": "#E5E5E5"
    "200": "#C7C7C7"
    "300": "#9E9E9E"
    "400": "#6B6B6B"
    "500": "#000000"
    "600": "#000000"
    "700": "#000000"
    "800": "#000000"
    "900": "#000000"
    "950": "#000000"
  accent:
    "50":  "#FFFCF4"
    "100": "#FFF8E6"
    "200": "#FFF5E1"
    "300": "#FBEBC3"
    "400": "#F3D998"
    "500": "#FFF5E1"
    "600": "#E8C987"
    "700": "#BFA15E"
    "800": "#8C7340"
    "900": "#5A4828"
    "950": "#2F2414"
  neutral:
    "50":  "#FAFAFA"
    "100": "#F4F4F5"
    "200": "#E5E4E2"
    "300": "#D4D4D4"
    "400": "#A3A3A3"
    "500": "#737373"
    "600": "#525252"
    "700": "#3F3F3F"
    "800": "#262626"
    "900": "#1A1A1A"
    "950": "#0A0A0A"
  semantic:
    success: { bg: "#E8F5E9", text: "#1B5E20", light: "#F4FBF4", border: "#A5D6A7" }
    warning: { bg: "#FFF4E0", text: "#8A5A00", light: "#FFFAF0", border: "#F5C878" }
    error:   { bg: "#FFECEE", text: "#A30006", light: "#FFF5F6", border: "#F4A1A5" }
    info:    { bg: "#FFF5E1", text: "#7A4A00", light: "#FFFBF0", border: "#F3D998" }
  background:
    page:    "#F40009"
    surface: "#FFFFFF"
    subtle:  "#FFF5E1"
  text:
    primary:   "#FFFFFF"
    secondary: "#FFE4D6"
    muted:     "#FFB0B4"
    inverse:   "#1A1A1A"

typography:
  families:
    heading: "'Poppins', 'Nunito', 'Helvetica Neue', Arial, sans-serif"
    body:    "'Nunito', 'Source Sans 3', 'Helvetica Neue', Arial, sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Nunito:wght@400;500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&family=Great+Vibes&family=Dancing+Script:wght@500;700&family=JetBrains+Mono:wght@400;500&display=swap"
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
  radius: {none: "0", sm: "8px", md: "12px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "#FFFFFF", subtle: "rgba(255,255,255,0.35)", strong: "#FFFFFF", focus: "#FFF5E1"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.08)"
  sm: "0 2px 6px rgba(0,0,0,0.10)"
  md: "0 4px 12px rgba(0,0,0,0.15)"
  lg: "0 10px 24px rgba(0,0,0,0.20)"
  xl: "0 18px 40px rgba(0,0,0,0.25)"
  "2xl": "0 30px 60px rgba(0,0,0,0.32)"
  inner: "inset 0 1px 2px rgba(0,0,0,0.08)"
  focus: "0 0 0 3px rgba(255,245,225,0.65)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.55, 0, 1, 0.45)"
    out:     "cubic-bezier(0, 0.55, 0.45, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, scale, glow]
  reducedMotion: true

composition:
  layout:        stack
  contentWidth:  wide
  framing:       solid
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: filled
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.75px"

components:
  button:
    primary:
      background: "#FFFFFF"
      color: "#F40009"
      border: "1px solid #FFFFFF"
      shadow: "0 4px 12px rgba(0,0,0,0.15)"
      hoverBackground: "#FFF5E1"
      hoverShadow: "0 8px 20px rgba(0,0,0,0.22)"
      hoverColor: "#CC0008"
    secondary:
      background: "#F40009"
      color: "#FFFFFF"
      border: "2px solid #FFFFFF"
      shadow: "0 2px 6px rgba(0,0,0,0.12)"
      hoverBackground: "#CC0008"
      hoverShadow: "0 6px 16px rgba(0,0,0,0.20)"
      hoverColor: "#FFFFFF"
    ghost:
      background: "transparent"
      color: "#FFFFFF"
      border: "2px solid rgba(255,255,255,0.6)"
      shadow: "none"
      hoverBackground: "rgba(255,255,255,0.12)"
      hoverShadow: "none"
      hoverColor: "#FFFFFF"
    danger:
      background: "#1A1A1A"
      color: "#FFFFFF"
      border: "1px solid #1A1A1A"
      shadow: "0 4px 12px rgba(0,0,0,0.25)"
      hoverBackground: "#000000"
      hoverShadow: "0 8px 18px rgba(0,0,0,0.32)"
      hoverColor: "#FFF5E1"
    sizes:
      sm: { height: "36px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "44px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "56px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "12px"
    fontWeight: 700
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1A1A1A"
    border: "1px solid rgba(255,255,255,0.4)"
    borderRadius: "12px"
    padding: "12px 16px"
    focusBorder: "2px solid #FFF5E1"
    placeholderColor: "#737373"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid rgba(0,0,0,0.04)"
      borderRadius: "16px"
      padding: "24px"
      shadow: "0 4px 12px rgba(0,0,0,0.15)"
    hover:
      shadow: "0 10px 24px rgba(0,0,0,0.20)"
      transform: "translateY(-2px)"
---

# Coca-Cola Classic

> Full-bleed Coca-Cola red, a Spencerian smile, and a century of "open happiness" distilled into a design system.

## Origin

Coca-Cola was invented in Atlanta in 1886, but the brand as we know it begins a year later, when
bookkeeper Frank Mason Robinson dipped a nib and drew the Spencerian script that has been almost
untouched ever since. In 1915 the Root Glass Company delivered the contour bottle — a silhouette
recognizable even shattered in the dark — and between 1931 and 1964 Haddon Sundblom painted the
red-suited, rosy-cheeked Santa Claus that lodged the color in the collective unconscious of
consumer culture.

In 1969 Lippincott & Margulies codified the contemporary system: the Spencerian word-mark, the
"dynamic ribbon" swoosh, and a single mandated red. Through global campaigns — "I'd Like to Buy
the World a Coke" (1971), the polar bears, "Share a Coke" (2014), "Real Magic" (2021) — the kit
has barely drifted. Coca-Cola's design language is warm, celebratory, mass-market American
optimism, rendered almost entirely in one color.

## Overview
Composition cues:
- **Layout**: full-bleed red hero sections stacked vertically, broken by white or cream "happiness" cards
- **Content width**: wide, generous — never cramped, never minimalist-narrow
- **Framing**: solid, rounded, never glassy; the red IS the frame
- **Grid intensity**: soft — columns exist but are softened by ribbon dividers and curved edges
- **Rhythm**: 8px base; generous padding at every breakpoint to keep warmth

## Colors
The palette is deliberately impoverished so the red can do the work: Coca-Cola Red `#F40009` owns
the page, pure white is reserved for text and the script logo, black handles long-form reading on
white cards, and a warm cream `#FFF5E1` lets vintage surfaces breathe. No blue anywhere — blue is
Pepsi's problem. The result is a system that is legible from across a stadium and instantly
identifiable from a single pixel.

**Role usage**:
- Page background → `colors.background.page` (Coca-Cola Red `#F40009`)
- Primary text on red ground → `colors.text.primary` (`#FFFFFF`)
- Card / modal surface → `colors.background.surface` (`#FFFFFF`)
- Body text on white cards → `colors.text.inverse` (`#1A1A1A`)
- Vintage / "happiness moment" surface → `colors.background.subtle` (`#FFF5E1`)
- Secondary / editorial section → `colors.neutral.900` (`#1A1A1A`)
- Primary CTA → white button with red label (`colors.button.primary`)
- Script accent (celebratory headline) → `colors.text.primary` on red, rendered in Great Vibes

## Typography
The script word-mark is never set in live text; it lives only as the locked logo. For UI, the
voice is warm geometric sans — Poppins for headlines (rounded, friendly, slightly plump) and
Nunito for body (soft counters, generous x-height). Great Vibes appears sparingly as the
celebratory flourish — headlines like "share a Coke" or "open happiness" — to echo the Spencerian
lineage without impersonating it. Never set body in a cold grotesk like Inter or Geist; never set
body in a serif.

**Text styles**:
- `display-xl` — Poppins, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Poppins, 72px, weight 700, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Poppins, 48px, weight 700, line-height 1.15, letter-spacing -0.02em
- `heading-2` — Poppins, 36px, weight 700, line-height 1.2, letter-spacing -0.01em
- `heading-3` — Poppins, 24px, weight 600, line-height 1.3, letter-spacing 0
- `script-accent` — Great Vibes, 64px, weight 400, line-height 1.1, letter-spacing 0
- `body-lg` — Nunito, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Nunito, 16px, weight 400, line-height 1.625, letter-spacing 0
- `caption` — Nunito, 13px, weight 600, line-height 1.4, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px; rhythm: 8px multiples
- Scale: 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128 px
- Container: `xl = 1280px` for hero-and-product layouts; `lg = 1024px` for editorial
- Section padding: `lg = 96px` vertical on desktop, `md = 64px` on tablet, `sm = 32px` on mobile
- Grid gap: `lg = 24px` standard; widen to `xl = 48px` between cream "story" cards
- Never let type touch the edge — minimum 24px gutter, even inside red bleeds

## Elevation & Depth
Coca-Cola surfaces are solid and tactile, not glassy. White and cream cards float on the red
ground with a warm, softly-spread shadow; there is no blur, no translucency, no dark-mode
depth tricks. The materiality is paper-label-on-can — matte, chunky, rounded.

- Surface style: solid (matte white, matte cream, matte black)
- Blur: none
- Shadow ladder:
  - `xs` hairline lift for chips and badges (`0 1px 2px rgba(0,0,0,0.08)`)
  - `sm` product thumbnails (`0 2px 6px rgba(0,0,0,0.10)`)
  - `md` default card rest state (`0 4px 12px rgba(0,0,0,0.15)`)
  - `lg` card hover / modal (`0 10px 24px rgba(0,0,0,0.20)`)
  - `xl` marketing overlay (`0 18px 40px rgba(0,0,0,0.25)`)
  - `focus` warm cream halo (`0 0 0 3px rgba(255,245,225,0.65)`)

## Shapes
- Buttons: 12px radius — never sharp, never pill (pill belongs to Airbnb/y2k)
- Cards: 16px radius
- Modals / hero panels: 24px radius
- Avatars / badges: `full` (circle) — echoes the Coca-Cola disc seal
- Dividers: custom ribbon-wave SVG, not straight lines
- Never use 0 radius anywhere; Coca-Cola is always rounded

## Motion
Motion is lively and slightly bouncy — the temperament of a bottle cap popping, not a machine
computing. Hovers lift and warm; transitions ease out with a gentle overshoot where playful;
reduced-motion is always respected. Nothing glitches, flickers, or feels technical.

- Level: lively
- Durations: `fast 120ms` (button press), `normal 250ms` (card hover), `slow 400ms` (modal), `slower 600ms` (hero ribbon sweep)
- Easings: `out` for entrances, `spring` (cubic-bezier(.34,1.56,.64,1)) for CTA hover "pop"
- Hover patterns: lift (y = -2px), tint (cream glaze on white), scale (1.02 on product art), glow (cream shadow halo)
- Always honor `prefers-reduced-motion: reduce`

## Techniques

### Dynamic Ribbon Underlay
The signature white "swoosh" that has framed Coca-Cola since 1969, reproduced as a pure-CSS curved
accent sweeping beneath hero content.
```css
.coke-ribbon {
  position: relative;
  isolation: isolate;
  padding: 96px 32px;
  background: #F40009;
  color: #FFFFFF;
  overflow: hidden;
}
.coke-ribbon::before {
  content: "";
  position: absolute;
  inset: auto -10% -20% -10%;
  height: 60%;
  background: #FFFFFF;
  border-radius: 50% 50% 0 0 / 100% 100% 0 0;
  transform: rotate(-4deg) translateY(30%);
  box-shadow: 0 -12px 30px rgba(0, 0, 0, 0.12);
  z-index: -1;
}
```

### Contour-Bottle Card Silhouette
A pinched, double-curve card shape that nods to the 1915 contour bottle, rendered with CSS
`border-radius` shorthand for soft organic asymmetry.
```css
.contour-card {
  background: #FFF5E1;
  color: #1A1A1A;
  padding: 32px 28px;
  border-radius: 48px 48px 24px 24px / 64px 64px 28px 28px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: transform 250ms cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 250ms ease-out;
}
.contour-card:hover {
  transform: translateY(-2px) rotate(-0.5deg);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.20);
}
```

### Condensation Glass CTA
The "ice-cold" product photo effect applied to a call-to-action: a pure-white button that reads
as a frosted, sweating bottle label on the red ground.
```css
.coke-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 56px;
  padding: 0 32px;
  font: 700 18px/1 "Poppins", sans-serif;
  color: #F40009;
  background: linear-gradient(180deg, #FFFFFF 0%, #FFF5E1 100%);
  border: none;
  border-radius: 12px;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    0 4px 12px rgba(0, 0, 0, 0.15),
    0 0 0 0 rgba(255, 245, 225, 0);
  transition: box-shadow 250ms ease-out, transform 120ms ease-out;
}
.coke-cta:hover {
  transform: translateY(-1px);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    0 10px 24px rgba(0, 0, 0, 0.22),
    0 0 0 6px rgba(255, 245, 225, 0.35);
}
```

## Iconography
Icons are filled, friendly, and slightly chunky — never thin linear grotesques. Phosphor's `bold`
or `fill` weight fits the Coca-Cola warmth; custom brand icons (bottle, can, ribbon, disc seal)
are drawn to the same visual weight. Stroke-based icons, when used, sit at 1.75px with rounded
caps and joins.

- Treatment: filled (preferred), bold linear as secondary
- Set: Phosphor (`bold` / `fill`) or custom brand glyphs
- Stroke: 1.75px with round caps/joins

## Do's & Don'ts
### ✓ Do
- Use Coca-Cola Red `#F40009` as the page background — commit fully, don't apologize with white margins.
- Set primary text in white on red, and body in `#1A1A1A` on white or cream cards.
- Reach for Poppins for headlines, Nunito for body, and Great Vibes only for celebratory script accents.
- Round every corner — 12px on buttons, 16px on cards, 24px on modals.
- Frame sections with the dynamic ribbon or contour-bottle silhouette instead of straight hairline dividers.

### ✗ Don't
- Don't introduce blue in any shade — blue is Pepsi territory.
- Don't reach for cold, technical sans-serifs like Inter or Geist.
- Don't use 0px or sharp corners anywhere; Coca-Cola is always rounded.
- Don't design minimalist, sparse, negative-space layouts — Coca-Cola is warm and full.
- Don't go dark and moody, and never set body copy in a serif.

## Applications
Best for consumer-facing marketing sites, holiday and campaign landing pages, retail product
pages, loyalty programs, and any surface whose job is to feel warm, generous, and unmistakably
American-optimistic. It excels at hero-driven storytelling, product drops, and branded content;
it struggles at dense data dashboards or enterprise admin UIs, where its full-bleed red becomes
noise rather than signal.
