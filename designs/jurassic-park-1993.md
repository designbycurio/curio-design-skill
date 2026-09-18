---
version: 1

meta:
  id: jurassic-park-1993
  name: Jurassic Park (1993)
  description: Amber-fossil yellow meets black-and-red hazard signage — a doomed theme park stamped like a warning label.
  isDark: false
  tags: [bold, narrative, retro, decorative, geometric]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1993 film release; source novel 1990; branding system 1990–1993"
  region: "Isla Nublar (fictional, off Costa Rica) — Hollywood/Universal, Los Angeles"
  regionZh: "努布拉岛（虚构，哥斯达黎加外海）— 好莱坞环球影业，洛杉矶"
  keyFigures: [Steven Spielberg, Michael Crichton, Chip Kidd, Stan Winston, John Williams]
  movements: [blockbuster brand design, hazard/wayfinding signage, natural-history museum display]

introduction: |
  Jurassic Park's design language runs on tension: a warm welcome-to-the-park amber ground crossed with the visual grammar of "do not touch, this will kill you." Chip Kidd's bone-white T-Rex skeleton, caged inside a red-ringed roundel, sits over black-and-yellow hazard chevrons and electrified-fence placards.
  Everything is stamped like signage — monolithic screaming caps, riveted metal plates, a blinking red alert lamp, and fossil bone printed at billboard scale. It feels like a rain-soaked visitor-center banner: glowing amber resin, sharp black keylines, and the constant sense that the tour is about to go very wrong.
introductionZh: |
  《侏罗纪公园》的设计语言建立在一种张力之上：温暖的琥珀黄迎宾底色，叠上「请勿触碰，会致命」的危险标识语法。奇普·基德那具骨白色的霸王龙骨架，被关在红环圆牌里，压在黑黄危险人字纹与电网警示牌之上。

  一切都像标识牌一样被压印出来——巨型全大写标题、铆钉金属板、闪烁的红色警报灯，还有以广告牌尺度印刷的化石骨骼。它像一面被雨水浸透的游客中心横幅：发光的琥珀树脂、锋利的黑色描边，以及那种游览即将失控的持续预感。

colors:
  primary:    {"50": "#FCEBE9", "100": "#F7CFCB", "200": "#EDA39C", "300": "#E1746A", "400": "#D14F42", "500": "#B62E24", "600": "#9C261D", "700": "#7C1D16", "800": "#5C1611", "900": "#3E0F0B", "950": "#260805"}
  secondary:  {"50": "#EDECEA", "100": "#D2D0CC", "200": "#A6A29B", "300": "#7A756C", "400": "#4E4A42", "500": "#16130E", "600": "#12100C", "700": "#0E0C09", "800": "#0A0806", "900": "#060503", "950": "#030201"}
  accent:     {"50": "#E8F0EA", "100": "#C7DBCC", "200": "#98BCA2", "300": "#679B76", "400": "#437A52", "500": "#2E5D3A", "600": "#264D30", "700": "#1E3D26", "800": "#162D1C", "900": "#0F1F13", "950": "#08110A"}
  neutral:    {"50": "#F6F2E5", "100": "#F3EFE2", "200": "#E4DAC0", "300": "#CFC199", "400": "#B09A6A", "500": "#8B7648", "600": "#6B4A22", "700": "#523818", "800": "#3A2811", "900": "#251A0B", "950": "#150E05"}
  semantic:
    success: { bg: "#E8F0EA", text: "#1E3D26", light: "#C7DBCC", border: "#2E5D3A" }
    warning: { bg: "#F1C255", text: "#3A2811", light: "#F7DA96", border: "#E7A81E" }
    error:   { bg: "#FCEBE9", text: "#7C1D16", light: "#F7CFCB", border: "#B62E24" }
    info:    { bg: "#EDECEA", text: "#16130E", light: "#D2D0CC", border: "#4E4A42" }
  background:
    page:    "#E7A81E"
    surface: "#F1C255"
    subtle:  "#16130E"
  text:
    primary:   "#16130E"
    secondary: "#523818"
    muted:     "#6B4A22"
    inverse:   "#F3EFE2"

typography:
  families:
    heading: "'Anton', 'Barlow Condensed', Impact, sans-serif"
    body:    "'Barlow', 'Barlow Condensed', system-ui, sans-serif"
    mono:    "'Space Mono', 'IBM Plex Mono', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&family=Space+Mono:wght@400;700&display=swap"
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
  radius: {none: "0", sm: "2px", md: "4px", lg: "4px", xl: "6px", full: "9999px"}
  color:  {default: "#16130E", subtle: "#6B4A22", strong: "#16130E", focus: "#B62E24"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 0 rgba(22,19,14,0.6)"
  sm: "0 2px 0 rgba(22,19,14,0.85)"
  md: "0 3px 0 rgba(22,19,14,0.9)"
  lg: "0 5px 0 rgba(22,19,14,0.92)"
  xl: "0 8px 0 rgba(22,19,14,0.95)"
  "2xl": "0 12px 0 rgba(22,19,14,0.95)"
  inner: "inset 0 2px 4px rgba(22,19,14,0.25)"
  focus: "0 0 0 3px rgba(182,46,36,0.5)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, stroke, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        "4px"

surfaceStyle: flat
blur:         none

iconography:
  treatment: filled
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#B62E24", color: "#F3EFE2", border: "2px solid #16130E", shadow: "0 3px 0 rgba(22,19,14,0.9)", hoverBackground: "#9C261D", hoverShadow: "0 5px 0 rgba(22,19,14,0.92)", hoverColor: "#F3EFE2"}
    secondary: {background: "#16130E", color: "#F3EFE2", border: "2px solid #16130E", shadow: "0 3px 0 rgba(22,19,14,0.9)", hoverBackground: "#0E0C09", hoverShadow: "0 5px 0 rgba(22,19,14,0.92)", hoverColor: "#E7A81E"}
    ghost:     {background: "transparent", color: "#16130E", border: "2px solid #16130E", shadow: "none", hoverBackground: "#F1C255", hoverShadow: "0 3px 0 rgba(22,19,14,0.9)", hoverColor: "#16130E"}
    danger:    {background: "#B62E24", color: "#F3EFE2", border: "2px solid #16130E", shadow: "0 3px 0 rgba(22,19,14,0.9)", hoverBackground: "#7C1D16", hoverShadow: "0 5px 0 rgba(22,19,14,0.92)", hoverColor: "#F3EFE2"}
    sizes:     {sm: {height: "36px", padding: "0 16px", fontSize: "0.875rem"}, md: {height: "44px", padding: "0 24px", fontSize: "1rem"}, lg: {height: "56px", padding: "0 32px", fontSize: "1.25rem"}}
    borderRadius: "2px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#F1C255"
    color: "#16130E"
    border: "2px solid #16130E"
    borderRadius: "2px"
    padding: "10px 14px"
    focusBorder: "2px solid #B62E24"
    placeholderColor: "#6B4A22"
  card:
    base:  {background: "#F1C255", border: "2px solid #16130E", borderRadius: "4px", padding: "24px", shadow: "0 3px 0 rgba(22,19,14,0.9)"}
    hover: {shadow: "0 5px 0 rgba(22,19,14,0.92)", transform: "translateY(-2px)"}
---

# Jurassic Park (1993)

> Amber-fossil yellow meets black-and-red hazard signage — a doomed theme park stamped like a warning label.

## Origin

Jurassic Park's visual identity was born on a book jacket. In 1990, Chip Kidd designed the cover for Michael Crichton's novel at Knopf, reducing a T-Rex to a bone-white skeleton caged inside a red-ringed roundel — a mark so strong Universal adopted it wholesale for Steven Spielberg's 1993 film. Around that logo grew a full park-branding kit: electrified-fence warning placards, jungle survey signage, jeep livery, and amber-cane merchandise, all built on the tension between a warm welcome and mortal danger.

The system draws on OSHA/ANSI hazard grammar — black-and-yellow chevrons, red alert lamps — fused with natural-history museum display, like the American Museum of Natural History's saurischian halls. Stan Winston's animatronics gave the dinosaurs weight; John Williams's score gave them awe. But the design's enduring signature is Kidd's skeleton-in-a-roundel, printed at billboard scale over glowing amber resin — the color of fossilized tree sap lit from behind, holding a mosquito that started the whole disaster.

## Overview

Composition cues:
- **Layout**: strict signage grid — placards, dividers, and hazard-stripe bars snapped to a hard 4px rhythm
- **Content width**: container-bound, like a bounded visitor-center wall of signs
- **Framing**: bordered — heavy black 2px keylines around every plate and card
- **Grid intensity**: strong — visible structure, chevron dividers, riveted panels

## Colors

The palette runs on a single hot idea: warm amber welcome crossed with lethal red-and-black warning. Amber yellow is the glowing resin ground; danger red rings the logo and lights the alerts; bone white carries the skeleton and signage type; near-black draws hazard chevrons and gate ironwork; jungle green marks containment and foliage.

**Role usage**:
- Page background → `colors.background.page` (`#E7A81E` amber yellow)
- Placard / card surface → `colors.background.surface` (`#F1C255` lighter amber)
- Gate / dark panel → `colors.background.subtle` (`#16130E` near-black)
- Primary CTAs, logo ring, alert lamp → `colors.primary.500` (`#B62E24` danger red)
- Hazard chevrons, keylines, heavy type → `colors.secondary.500` (`#16130E` hazard black)
- Containment / foliage accent → `colors.accent.500` (`#2E5D3A` jungle green)
- Signage text on black, skeleton silhouette → `colors.text.inverse` (`#F3EFE2` bone white)
- Fossil-brown shadows in amber → `colors.neutral.600` (`#6B4A22`)

## Typography

The voice is signage: monolithic, all-caps, tracked, and loud. Headlines scream in a single-weight banner face; body copy stays utilitarian and wayfinding-clean; monospace handles control-room readouts and specimen tags.

**Text styles**:
- `display-xl` — Anton, 96px, weight 400, line-height 1.0, letter-spacing -0.02em, uppercase
- `display-lg` — Anton, 64px, weight 400, line-height 1.05, letter-spacing -0.01em, uppercase
- `heading-1` — Anton, 40px, weight 400, line-height 1.1, letter-spacing 0, uppercase
- `body-lg` — Barlow, 18px, weight 500, line-height 1.5, letter-spacing 0
- `body-md` — Barlow, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Barlow Condensed, 13px, weight 600, line-height 1.375, letter-spacing 0.05em, uppercase
- `mono-md` — Space Mono, 15px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; scale climbs 2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128
- Container maxes at 1280px, defaulting to a bounded wall-of-signage width
- Section padding: 64px (md) to 128px (xl), generous like a park concourse
- Grid gaps stay tight (8–24px) so placards read as a dense signage board

## Elevation & Depth

Materiality is flat printed plate, not glass. Surfaces are opaque amber placards with hard black keylines; depth comes from a solid, offset drop shadow like a physical sign standing off a wall, never a soft blur.

- Surface style: flat matte plates, no translucency
- Blur: none — flat plates and hard keylines only
- Shadow ladder: hard-edged offset drops, `md = 0 3px 0 rgba(22,19,14,0.9)`, climbing to `xl` for standing panels
- Focus ring: red halo `0 0 0 3px rgba(182,46,36,0.5)`

## Shapes

- Buttons: 2px radius — near-square, sign-stamped
- Cards / placards: 4px radius
- Roundels: full `9999px` for the red-ringed logo frame
- Everything else: sharp rectangular plates with heavy black keylines

## Motion

Motion is restrained and mechanical — signs don't dance, they clunk and light up. Hovers lift plates a hair or thicken their stroke; the only lively element is a pulsing red alert lamp.

- Level: restrained
- Durations: 120ms (fast) to 400ms (slow)
- Easings: standard `cubic-bezier(0.4,0,0.2,1)`; spring reserved for the alert-lamp pulse
- Hover patterns: lift (offset shadow grows), stroke (keyline thickens), tint (amber wash)
- `prefers-reduced-motion` honored — alert pulse falls back to static

## Techniques

### Hazard-Stripe Divider
Diagonal black-and-amber caution stripes as section dividers and footers.
```css
.hazard-stripe {
  height: 16px;
  background: repeating-linear-gradient(
    -45deg,
    #16130E 0 20px,
    #E7A81E 20px 40px
  );
  border-top: 2px solid #16130E;
  border-bottom: 2px solid #16130E;
}
```

### Amber-Resin Inclusion Panel
Translucent fossilized-resin depth with a suspended-inclusion fleck — used for hero panels.
```css
.amber-resin {
  background:
    radial-gradient(circle at 62% 40%, rgba(243,239,226,0.14) 0 6px, transparent 7px),
    radial-gradient(ellipse at 30% 20%, #F1C255 0%, #E7A81E 45%, #6B4A22 130%);
  border: 2px solid #16130E;
  border-radius: 4px;
  box-shadow: inset 0 2px 10px rgba(22,19,14,0.25);
}
```

### Red-Ring Roundel Frame
The red-ringed roundel caging a bone silhouette, echoing the skeleton logo.
```css
.roundel {
  display: grid;
  place-items: center;
  width: 160px; height: 160px;
  border-radius: 9999px;
  background: #16130E;
  border: 6px solid #B62E24;
  box-shadow: 0 0 0 2px #16130E, 0 5px 0 rgba(22,19,14,0.92);
  color: #F3EFE2; /* bone silhouette / glyph */
}
```

## Iconography

Icons read as filled hazard glyphs, not thin linework — chevron arrows, warning triangles, and bone silhouettes with weight. Prefer a heavy filled set (Phosphor fill) at 2px equivalent presence, sized 16–24px. Pair pictograms with all-caps labels the way park wayfinding does.

## Do's & Don'ts

### ✓ Do
- Use danger red (`#B62E24`) for primary actions, the logo ring, and alert lamps
- Set headlines in Anton, all-caps, tracked, and monolithic
- Break sections with black-and-amber hazard-stripe dividers and heavy keylines
- Keep the amber ground saturated and glowing, like backlit resin
- Frame bone silhouettes inside red-ringed roundels, screen-printed with coarse halftone

### ✗ Don't
- Use cream or parchment page backgrounds — the amber is saturated, not faded
- Use soft pastels or rounded friendly UI — keep it sharp hazard signage
- Set headlines in thin elegant serifs — they must be heavy and monolithic
- Reproduce the exact film logo artwork or any script text/quotes
- Use muddy desaturated yellows, gradients, or glassmorphism — flat plates only
- Let blue dominate or use over-cute cartoon dinosaurs — silhouettes and skeletons, not mascots

## Applications

Best for bold, high-drama landing pages, event and product-launch posters, and merch-style branding where tension and warning are the point. It excels at hazard-themed dashboards, ticketing and admission UIs, and any "welcome, but keep your hands inside the vehicle" narrative surface.
