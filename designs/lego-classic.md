---
version: 1

meta:
  id: lego-classic
  name: LEGO Classic
  description: Primary-color bricks on a warm baseplate — cheerful engineering that says "build anything."
  isDark: false
  tags: [bold, friendly, playful, modernist]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1949 first plastic bricks; current logo since 1998; visual identity mature 1970s–present"
  region: "Billund, Denmark"
  regionZh: "丹麦比隆"
  keyFigures: [Ole Kirk Christiansen, Godtfred Kirk Christiansen, Jørgen Vig Knudstorp]
  movements: [Scandinavian toy design, construction play, instruction-based visual communication]

introduction: |
  LEGO is primary colors snapped together — the most intuitive visual language of construction ever created. Red, yellow, blue, and green sit on a medium-gray baseplate beside the rounded stud grid and instruction-manual line art. The brand says "build anything" and means it.

  The design language is cheerful engineering: a precise 8mm stud grid, bold saturated primaries, chunky rounded forms, and the satisfying click of things fitting together. Nothing is elegant, nothing is moody — everything is toybox bright, matte plastic, and snap-together confident.
introductionZh: |
  乐高是一种被卡扣咬合的原色语言——或许是人类发明过最直观的"搭建"视觉系统。红、黄、蓝、绿四色块落在中灰色底板之上，圆形凸点整齐排列，说明书式的线描图清晰到连小朋友都能照着拼。它用最简单的色彩说出最自信的一句话：Build anything——什么都能搭。

  乐高的视觉哲学是"快乐的工程学"：8 毫米凸点网格作为底层秩序，饱和度拉满的原色作为情绪，圆角方块（砖块本身的形状）作为基础语汇。没有柔和粉彩，没有优雅衬线，没有玻璃质感——一切都是磨砂塑料的手感、鲜亮的配色，以及两块砖咔哒扣上时那一声令人上瘾的清脆。

colors:
  primary:
    "50":  "#FDE8E9"
    "100": "#FACFD0"
    "200": "#F39FA1"
    "300": "#EC6F72"
    "400": "#E24042"
    "500": "#D11013"
    "600": "#B00D10"
    "700": "#8D0A0D"
    "800": "#69070A"
    "900": "#470406"
    "950": "#280203"
  secondary:
    "50":  "#FEFAE6"
    "100": "#FDF4CC"
    "200": "#FBE99A"
    "300": "#F9DE67"
    "400": "#F7D449"
    "500": "#F5CD2F"
    "600": "#D9B21D"
    "700": "#AE8E14"
    "800": "#826A0E"
    "900": "#584708"
    "950": "#2F2604"
  accent:
    "50":  "#E6EEF9"
    "100": "#CCDCF2"
    "200": "#99B9E5"
    "300": "#6697D9"
    "400": "#3376CC"
    "500": "#0055BF"
    "600": "#00489F"
    "700": "#003A80"
    "800": "#002B60"
    "900": "#001D40"
    "950": "#001024"
  neutral:
    "50":  "#F4F4F0"
    "100": "#E8E9E5"
    "200": "#D6D8D5"
    "300": "#C1C4C2"
    "400": "#A0A5A9"
    "500": "#7E8389"
    "600": "#60666B"
    "700": "#474D52"
    "800": "#2F3439"
    "900": "#1B2A34"
    "950": "#0C141B"
  semantic:
    success: { bg: "#E3F1E9", text: "#19532E", light: "#F1F8F3", border: "#237841" }
    warning: { bg: "#FEF4D1", text: "#6B560A", light: "#FEF9E4", border: "#F5CD2F" }
    error:   { bg: "#FBE0E0", text: "#7A0A0D", light: "#FDEDED", border: "#D11013" }
    info:    { bg: "#D9E5F3", text: "#003A80", light: "#EDF2FA", border: "#0055BF" }
  background:
    page:    "#F4F4F0"
    surface: "#FFFFFF"
    subtle:  "#E8E9E5"
  text:
    primary:   "#1B2A34"
    secondary: "#474D52"
    muted:     "#7E8389"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Nunito', 'Varela Round', system-ui, sans-serif"
    body:    "'Nunito', system-ui, sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Varela+Round&family=JetBrains+Mono:wght@400;500&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.1, snug: 1.25, normal: 1.5, relaxed: 1.625, loose: 1.8}
  letterSpacing: {tighter: "-0.02em", tight: "-0.01em", normal: "0", wide: "0.04em"}

spacing:
  base: "4px"
  scale: ["2px","4px","8px","12px","16px","24px","32px","48px","64px","96px","128px","160px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "32px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "6px", md: "12px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "#D6D8D5", subtle: "#E8E9E5", strong: "#1B2A34", focus: "#F5CD2F"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 0 rgba(0,0,0,0.08)"
  sm: "0 2px 0 rgba(0,0,0,0.10)"
  md: "0 4px 0 rgba(0,0,0,0.12)"
  lg: "0 6px 0 rgba(0,0,0,0.14)"
  xl: "0 8px 0 rgba(0,0,0,0.16)"
  "2xl": "0 12px 0 rgba(0,0,0,0.18)"
  inner: "inset 0 2px 0 rgba(255,255,255,0.20)"
  focus: "0 0 0 4px rgba(245,205,47,0.55)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "200ms", slow: "320ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.34, 1.56, 0.64, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.5, 1.6, 0.4, 1)"
  hoverPatterns: [lift, scale, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       solid
  gridIntensity: strong
  rhythm:        "8px"

surfaceStyle: solid
blur:         "none"

iconography:
  treatment: filled
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:
      background: "#D11013"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 4px 0 rgba(122,10,13,1)"
      hoverBackground: "#E24042"
      hoverShadow: "0 6px 0 rgba(122,10,13,1)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "#F5CD2F"
      color: "#1B2A34"
      border: "none"
      shadow: "0 4px 0 rgba(107,86,10,1)"
      hoverBackground: "#F7D449"
      hoverShadow: "0 6px 0 rgba(107,86,10,1)"
      hoverColor: "#1B2A34"
    ghost:
      background: "transparent"
      color: "#1B2A34"
      border: "2px solid #1B2A34"
      shadow: "none"
      hoverBackground: "#E8E9E5"
      hoverShadow: "none"
      hoverColor: "#1B2A34"
    danger:
      background: "#1B2A34"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 4px 0 rgba(0,0,0,0.4)"
      hoverBackground: "#2F3439"
      hoverShadow: "0 6px 0 rgba(0,0,0,0.4)"
      hoverColor: "#FFFFFF"
    sizes:
      sm: { height: "36px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "48px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "60px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "12px"
    fontWeight: 800
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1B2A34"
    border: "2px solid #D6D8D5"
    borderRadius: "12px"
    padding: "12px 16px"
    focusBorder: "2px solid #F5CD2F"
    placeholderColor: "#7E8389"
  card:
    base:
      background: "#FFFFFF"
      border: "2px solid #E8E9E5"
      borderRadius: "12px"
      padding: "24px"
      shadow: "0 4px 0 rgba(0,0,0,0.12)"
    hover:
      shadow: "0 6px 0 rgba(0,0,0,0.14)"
      transform: "translateY(-2px)"
---

# LEGO Classic

> Primary-color bricks snap onto a warm baseplate — cheerful engineering that says "build anything."

## Origin

LEGO began in 1949 in the small Danish town of Billund, where carpenter Ole Kirk Christiansen started molding small plastic "Automatic Binding Bricks." His son Godtfred Kirk Christiansen patented the stud-and-tube coupling system in 1958 — the moment a toy became a platform. Through the 1970s and 1980s the visual identity matured: the red wordmark with its yellow and black outline (current form since 1998), the saturated primary palette borrowed straight from a paint-mixing set, and the obsessive instruction-manual illustrations where every piece was numbered and every step drawn in clean isometric line art.

The design language belongs to a Scandinavian tradition of modernist toy design — functional, optimistic, and engineered for children — but LEGO pushed further into construction-play and instruction-based visual communication. Under Jørgen Vig Knudstorp's 2000s turnaround, the brand doubled down on its core system: the 8mm stud grid, the rounded brick silhouette, and the primary-color discipline that made *The LEGO Movie* (2014) feel instantly legible to a global audience.

## Overview
Composition cues:
- **Layout**: Strong orthogonal grid — everything snaps to an 8px rhythm like studs on a baseplate.
- **Content width**: Container-bounded blocks sitting on a generous warm-gray surround.
- **Framing**: Solid, chunky 2px borders and hard-edged shadows — no glass, no translucency.
- **Grid intensity**: Strong and visible. The grid is a feature, not a guide.

## Colors
LEGO's palette is unapologetic primaries drawn from a child's paint set — red, yellow, blue, green — placed on a medium-warm baseplate gray with near-black ink. Nothing is muted, nothing is pastel; saturation is held at its toybox maximum and the four hues are allowed to clash in adjacent blocks the same way bricks do in a build.

**Role usage**:
- Page background → `colors.background.page` (`#F4F4F0`, baseplate warm gray)
- Surface / card → `colors.background.surface` (`#FFFFFF`)
- Primary CTA → `colors.primary.500` (LEGO red `#D11013`)
- Secondary / highlight → `colors.secondary.500` (LEGO yellow `#F5CD2F`)
- Links / structural trust → `colors.accent.500` (LEGO blue `#0055BF`)
- Success / nature sets → LEGO green `#237841` (via `semantic.success.border`)
- Body text → `colors.text.primary` (`#1B2A34`, near-black ink)
- Muted captions → `colors.text.muted` (`#7E8389`, medium stone gray)

## Typography
LEGO's type voice is friendly, rounded, and confident — never sharp, never elegant. Letterforms have soft terminals and heavy weight, reading like words stamped on a brick rather than printed in a book. Headlines push to weight 800 and often go title-case or uppercase for product names, while body text stays comfortably rounded at 400–600.

**Text styles**:
- `display-xl` — Nunito, 96px, weight 900, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Nunito, 64px, weight 800, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Nunito, 48px, weight 800, line-height 1.1, letter-spacing -0.01em
- `heading-2` — Nunito, 36px, weight 800, line-height 1.15, letter-spacing -0.01em
- `heading-3` — Nunito, 24px, weight 700, line-height 1.25, letter-spacing 0
- `body-lg` — Nunito, 18px, weight 500, line-height 1.625, letter-spacing 0
- `body-md` — Nunito, 16px, weight 400, line-height 1.625, letter-spacing 0
- `caption` — Nunito, 12px, weight 700, line-height 1.5, letter-spacing 0.04em, uppercase
- `mono-md` — JetBrains Mono, 14px, weight 500, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: **4px**, but the functional rhythm is **8px** — the stud grid.
- Scale: 2, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160 px.
- Container max-width: 1280px, centered with generous side padding.
- Section padding: 64–128px vertical on desktop, 32–48px on mobile.
- Grid gaps: 16–24px standard; 32px for hero-row card grids.

## Elevation & Depth
Surfaces are solid, matte, and physical — closer to colored ABS plastic than to glass. Depth comes from flat hard-edged offset shadows (no blur, or very little) that mimic the rim of a raised brick catching overhead light. Never use blur-heavy glassmorphism; never use translucency.

- Surface style: **solid** matte fills, 2px crisp borders.
- Blur: **none**. No backdrop-filter.
- Shadow ladder: `sm` 0 2px 0, `md` 0 4px 0, `lg` 0 6px 0, `xl` 0 8px 0 — all hard-edged, black at 8–18% alpha.
- Hover on cards/buttons: shadow grows from 4px to 6px and the element rises 2px (the "click" feeling reversed).

## Shapes
- Corner radii follow the brick silhouette — never zero, never pill (except for tags and avatars).
- `sm`: 6px — tight chips, tags.
- `md`: 12px — buttons, inputs, cards (the core brick radius).
- `lg`: 16px — large cards, modals.
- `xl`: 24px — hero panels.
- `full`: 9999px — avatars, dots, stud circles.

## Motion
Motion is bouncy and satisfying — things click into place. Every interaction should feel like a brick snapping onto a baseplate: a confident overshoot, a tiny settle, then stillness. Never linear-slow; never subtle-drift.

- Level: **lively** (occasionally **playful** for marketing surfaces).
- Durations: `fast` 120ms, `normal` 200ms, `slow` 320ms.
- Easings: default is a mild spring `cubic-bezier(0.34, 1.56, 0.64, 1)` — the overshoot is the brand.
- Hover patterns: `lift` (−2px + shadow grow), `scale` (1.02–1.04 on images), `tint` (button color lightens one step).
- Reduced motion honored: disables overshoot, keeps instant state changes.

## Techniques

### Brick-shadow button
Flat offset shadow beneath a solid-fill button so pressing it feels like pushing a real brick — the shadow shortens on `:active` as if the brick sinks onto the baseplate.

```css
.brick-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  padding: 0 24px;
  background: #D11013;
  color: #fff;
  font-family: 'Nunito', sans-serif;
  font-weight: 800;
  font-size: 1rem;
  border: none;
  border-radius: 12px;
  box-shadow: 0 4px 0 #7A0A0D;
  transition: transform 120ms cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 120ms ease-out,
              background 120ms ease-out;
  cursor: pointer;
}
.brick-button:hover {
  background: #E24042;
  box-shadow: 0 6px 0 #7A0A0D;
  transform: translateY(-2px);
}
.brick-button:active {
  box-shadow: 0 1px 0 #7A0A0D;
  transform: translateY(3px);
}
```

### Stud-grid baseplate background
Recreates the iconic LEGO baseplate with a radial-gradient stud repeated on an 8mm-ish grid. Use as a page or hero background behind content cards.

```css
.stud-baseplate {
  background-color: #F4F4F0;
  background-image:
    radial-gradient(circle at center,
      rgba(27, 42, 52, 0.10) 0 3px,
      transparent 3.5px),
    radial-gradient(circle at center,
      rgba(255, 255, 255, 0.8) 0 1.5px,
      transparent 2px);
  background-size: 32px 32px, 32px 32px;
  background-position: 0 0, 0 -1px;
}
```

### Primary-color block header
Four solid color blocks stacked edge-to-edge with zero gap — the LEGO-Movie opening sequence, reduced to a CSS header. Drop over any section break or category divider.

```css
.lego-stripe {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  height: 8px;
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
}
.lego-stripe > span:nth-child(1) { background: #D11013; }
.lego-stripe > span:nth-child(2) { background: #F5CD2F; }
.lego-stripe > span:nth-child(3) { background: #0055BF; }
.lego-stripe > span:nth-child(4) { background: #237841; }
```

## Iconography
Icons are filled, chunky, and friendly — not wire-thin outlines. Use Phosphor's `-fill` weight or a custom matte set. Stroke when used (for outline variants) is a confident 2px. Pair icons with decorative stud-dot circles for navigation chips.

- Treatment: filled (occasionally thick-outline 2px)
- Set: phosphor (`-fill` style preferred)
- Stroke: 2px for any outline variants

## Do's & Don'ts
### ✓ Do
- Use LEGO red `#D11013` for the primary call-to-action and brand anchor on every page.
- Pair LEGO yellow `#F5CD2F`, blue `#0055BF`, and green `#237841` as full-saturation accents — let them clash like bricks, not blend.
- Snap every layout to an 8px rhythm so spacing reads like a stud grid.
- Round every container to 12px and give it a flat offset shadow for that raised-brick feel.
- Set headings in Nunito 800 with tight leading, lean into the rounded terminals.

### ✗ Don't
- Don't use pastel or muted palettes — LEGO lives on saturated primaries.
- Don't use serif fonts anywhere in the system.
- Don't use sharp 0px corners; every brick is rounded.
- Don't drift into dark or moody aesthetics.
- Don't leave layouts minimalist or sparse — LEGO is colorful and full.
- Don't use glassmorphism, translucency, or blurred depth.

## Applications
Best-fit for kids' and family product marketing, educational platforms, construction/maker tools, toy e-commerce, and any brand that wants to feel playful and unambiguously optimistic. Works well for tutorial-heavy interfaces (the LEGO instruction-manual DNA translates naturally to step-by-step UI), event landing pages, and campaign microsites where saturated color and chunky type can do the heavy lifting.
