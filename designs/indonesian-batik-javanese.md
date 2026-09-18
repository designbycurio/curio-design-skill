---
version: 1

meta:
  id: indonesian-batik-javanese
  name: Javanese Batik
  description: Indonesian wax-resist textile tradition rendered as a disciplined court palette of indigo, soga-brown, and undyed cotton cream.
  isDark: false
  tags: [decorative, historical, organic, ornate, handmade]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Pre-Islamic Java wax-resist references; Mataram codification c. 1600s; Yogyakarta-Surakarta Kraton division 1755; UNESCO ICH 2009"
  region: "Java island, Indonesia — Yogyakarta + Surakarta (court) and Pekalongan + Cirebon + Lasem (coastal pesisir)"
  regionZh: "印度尼西亚爪哇 — 日惹与梭罗（宫廷蜡染）、北加浪岸与井里汶（沿海蜡染）"
  keyFigures: [Iwan Tirta, Eliza van Zuylen, Oey Soe Tjoen, Edward Hutabarat]
  movements: [Javanese court ceremonial dress, Pesisir coastal trade-influenced batik, Post-1945 batik as Indonesian national identity]

introduction: |
  Javanese batik is Indonesia's wax-resist textile tradition codified across centuries of Kraton court ateliers — molten beeswax hand-drawn with a copper-pot canting onto cotton, then soaked in indigo and soga-brown dye vats across multiple cycles. The court palette is a strict three-tone discipline: deep indigo, soga-brown, and undyed cotton cream, with motifs like parang and kawung historically reserved for royalty.

  Translated to interface, batik becomes pattern-as-language: every diagonal, every interlocking circle is precise mathematical tile-repeat, bounded by cream-resist hairlines. The system feels ceremonial — heading serifs in soga-brown, indigo hero panels with batik-tile fills, and a measured rhythm that respects the handcraft signature of the canting's slight hesitation.

introductionZh: |
  爪哇蜡染（Batik）是印度尼西亚爪哇岛的蜡染防染纺织传统，自玛塔兰苏丹国时期被宫廷编纂成法度，2009年列入联合国教科文组织非物质文化遗产名录。工匠用一种叫"加曼"（canting）的小铜壶笔，将熔化的蜂蜡逐线绘上棉布，再浸入靛蓝与梭加棕染缸，循环多次显出纹样。日惹与梭罗的宫廷蜡染严守三色基调：深靛蓝、梭加棕、未染棉米色，纹样如"帕朗"斜剑纹与"卡翁"四圆互锁过去专属王室。

  移植到界面，蜡染是一种纹样语言：每一道斜纹、每一组互锁的圆圈都是精确的数学瓷砖重复，由米色防染细线勾勒。整套系统庄重克制——衬线标题用梭加棕，英雄区铺以靛蓝底色与蜡染瓷砖纹，节奏沉稳，尊重加曼笔尖那一丝手工的迟疑与温度。

colors:
  primary:    {"50": "#E8ECF5", "100": "#C7CFE2", "200": "#9CA8C5", "300": "#6E7DA6", "400": "#475A87", "500": "#1F2D52", "600": "#1A2647", "700": "#131F3A", "800": "#0E172C", "900": "#080E1C", "950": "#04070F"}
  secondary:  {"50": "#F5EFE6", "100": "#E6D7BF", "200": "#CFB489", "300": "#B68F5A", "400": "#947038", "500": "#6B4124", "600": "#5A361D", "700": "#472A17", "800": "#341E10", "900": "#22130A", "950": "#120A05"}
  accent:     {"50": "#FBEAE7", "100": "#F4C5BF", "200": "#E89A91", "300": "#D86E63", "400": "#C04D43", "500": "#A8362F", "600": "#8E2A25", "700": "#71201D", "800": "#541714", "900": "#380E0C", "950": "#1D0606"}
  neutral:    {"50": "#FFFBEE", "100": "#F8F0D9", "200": "#F0E5C8", "300": "#DDCEA8", "400": "#B8A47C", "500": "#8F7440", "600": "#735C33", "700": "#574527", "800": "#3C2F1B", "900": "#221A0F", "950": "#100C07"}
  semantic:
    success: { bg: "#E6F0E8", text: "#1F5A35", light: "#F2F7F3", border: "#A4C8AC" }
    warning: { bg: "#F8E9C8", text: "#7A5414", light: "#FBF3DF", border: "#D6B26A" }
    error:   { bg: "#F4D7D2", text: "#7A201A", light: "#FAEAE7", border: "#D89289" }
    info:    { bg: "#DEE3F0", text: "#1F2D52", light: "#EEF1F8", border: "#9CA8C5" }
  background:
    page:    "#F0E5C8"
    surface: "#FFFBEE"
    subtle:  "#F8F0D9"
  text:
    primary:   "#6B4124"
    secondary: "#8F7440"
    muted:     "#B8A47C"
    inverse:   "#F0E5C8"

typography:
  families:
    heading: "'DM Serif Display', 'Cormorant Garamond', Georgia, serif"
    body:    "'EB Garamond', 'Crimson Pro', Georgia, serif"
    mono:    "'JetBrains Mono', ui-monospace, SFMono-Regular, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Crimson+Pro:ital,wght@0,400;0,500;0,600;1,400&family=Klee+One:wght@400;600&family=Noto+Sans+Javanese&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.2, snug: 1.375, normal: 1.55, relaxed: 1.7, loose: 1.85}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "2px", md: "4px", lg: "8px", xl: "12px", full: "9999px"}
  color:  {default: "#DDCEA8", subtle: "#F0E5C8", strong: "#6B4124", focus: "#1F2D52"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(31, 45, 82, 0.06)"
  sm: "0 1px 3px rgba(31, 45, 82, 0.10)"
  md: "0 2px 8px rgba(31, 45, 82, 0.15)"
  lg: "0 6px 16px rgba(31, 45, 82, 0.18)"
  xl: "0 14px 32px rgba(31, 45, 82, 0.22)"
  "2xl": "0 24px 56px rgba(31, 45, 82, 0.28)"
  inner: "inset 0 1px 2px rgba(107, 65, 36, 0.10)"
  focus: "0 0 0 3px rgba(31, 45, 82, 0.30)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "140ms", normal: "280ms", slow: "440ms", slower: "680ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.2, 0.64, 1)"
  hoverPatterns: [tint, underline, stroke]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: layered
blur:         none

iconography:
  treatment: linear
  set:       custom
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#6B4124", color: "#F0E5C8", border: "1px solid #6B4124", shadow: "0 2px 8px rgba(31, 45, 82, 0.15)", hoverBackground: "#5A361D", hoverShadow: "0 6px 16px rgba(31, 45, 82, 0.18)", hoverColor: "#FFFBEE"}
    secondary: {background: "#FFFBEE", color: "#1F2D52", border: "1px solid #1F2D52", shadow: "none", hoverBackground: "#F0E5C8", hoverShadow: "0 2px 8px rgba(31, 45, 82, 0.15)", hoverColor: "#131F3A"}
    ghost:     {background: "transparent", color: "#6B4124", border: "1px solid transparent", shadow: "none", hoverBackground: "rgba(107, 65, 36, 0.08)", hoverShadow: "none", hoverColor: "#5A361D"}
    danger:    {background: "#A8362F", color: "#FFFBEE", border: "1px solid #A8362F", shadow: "0 2px 8px rgba(168, 54, 47, 0.20)", hoverBackground: "#8E2A25", hoverShadow: "0 6px 16px rgba(168, 54, 47, 0.25)", hoverColor: "#FFFBEE"}
    sizes:     {sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "40px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "4px"
    fontWeight: 500
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#FFFBEE"
    color: "#6B4124"
    border: "1px solid #DDCEA8"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "1px solid #1F2D52"
    placeholderColor: "#B8A47C"
  card:
    base:  {background: "#FFFBEE", border: "1px solid #DDCEA8", borderRadius: "8px", padding: "24px", shadow: "0 2px 8px rgba(31, 45, 82, 0.15)"}
    hover: {shadow: "0 6px 16px rgba(31, 45, 82, 0.18)", transform: "translateY(-1px)"}
---

# Javanese Batik

> Indonesia's wax-resist textile grammar — indigo, soga-brown, and undyed cotton, rendered as ceremonial digital surfaces.

## Origin

Javanese batik is Indonesia's wax-resist textile-dyeing tradition that became national identity and UNESCO Intangible Cultural Heritage in 2009. For centuries — with oldest references c. 1500s but the tradition older still — Javanese women and court artisans hand-applied molten beeswax to cotton using a *canting* (a small copper-pot pen with bamboo handle), then dipped the cloth in indigo and soga-brown vats across multiple dye cycles. Peeling the wax revealed the resist-pattern in cream beneath. The Yogyakarta–Surakarta Kraton division of 1755 codified court batik with hierarchical motif protocol: *parang* (diagonal sword-blades) and *kawung* (four-circle interlock) were historically reserved for royalty.

Two great schools emerged. **Classical court batik** of Yogyakarta and Surakarta locked itself to a strict three-tone palette of deep indigo, soga-brown, and undyed cream. **Coastal pesisir batik** of Pekalongan, Cirebon, and Lasem absorbed Chinese and European trade influence — red, green, pink, the *mega mendung* cloud-bank of Cirebon, the *buketan* European bouquet. Iwan Tirta later modernized batik for Sukarno-era state-formal wear, and today the UN diplomat's batik shirt is a quiet badge of Indonesian identity.

## Overview

Composition cues:
- **Layout**: bordered cards on cream page, occasional indigo hero panels with cream typography
- **Content width**: container-bound (1280px max), measured ceremonial rhythm — not full-bleed
- **Framing**: hairline cream-resist borders on every surface (1px subtle cream-on-cream, like the canting's wax trace)
- **Grid intensity**: soft 8px rhythm with batik-tile pattern backgrounds in hero and divider strips

## Colors

The palette is the court palette of Yogyakarta–Surakarta: deep indigo `#1F2D52` from indigo-vat dye, soga-brown `#6B4124` from soga-tree bark, and undyed-cotton cream `#F0E5C8` as the resist-cleared ground. These three are the canonical court discipline — flat saturated blocks bounded by cream-resist hairlines. Pesisir accents (madder-red, malachite-green, Chinese-pink) appear only in non-court contexts and never mix with strict court compositions.

**Role usage**:
- Page background → `colors.background.page` `#F0E5C8` (undyed cotton)
- Card surface → `colors.background.surface` `#FFFBEE` (lighter cream)
- Hero / dark panel → `colors.primary.500` `#1F2D52` (court indigo)
- Primary CTA → `colors.secondary.500` `#6B4124` (soga-brown filled)
- Body text → `colors.secondary.500` `#6B4124` (never pure black)
- Muted text → `colors.neutral.500` `#8F7440`
- Pesisir accent (non-court only) → `colors.accent.500` `#A8362F` (madder-red)
- Hairline borders → `colors.neutral.300` `#DDCEA8` (cream-resist line)

## Typography

A literary serif voice. Headings are set in DM Serif Display with Cormorant Garamond for sub-headlines — both with high stroke contrast that echoes the wax-resist hairline. Body runs in EB Garamond, with Crimson Pro as fallback. Indonesian-script ornamentation can use Noto Sans Javanese (Hanacaraka) sparingly as graphic motif. No modern sans-serif (Inter, Geist) — they break the cultural register.

**Text styles**:
- `display-xl` — DM Serif Display, 96px, weight 400, line-height 1.0, letter-spacing -0.04em
- `display-lg` — DM Serif Display, 64px, weight 400, line-height 1.05, letter-spacing -0.03em
- `heading-1` — DM Serif Display, 48px, weight 400, line-height 1.15, letter-spacing -0.02em
- `heading-2` — Cormorant Garamond, 36px, weight 600, line-height 1.2, letter-spacing -0.01em
- `heading-3` — Cormorant Garamond, 24px, weight 600, line-height 1.3, letter-spacing 0
- `body-lg` — EB Garamond, 18px, weight 400, line-height 1.7, letter-spacing 0
- `body-md` — EB Garamond, 16px, weight 400, line-height 1.7, letter-spacing 0
- `caption` — Klee One, 13px, weight 400, line-height 1.55, letter-spacing 0.02em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.6, letter-spacing 0

## Spacing & Layout

- **Base unit**: 4px; rhythm doubles on 8px for ceremonial cadence
- **Scale**: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- **Container**: 1280px max-width centered with 32px gutters
- **Section padding**: 96px top/bottom on desktop, 64px on tablet, 32px on mobile

## Elevation & Depth

The materiality is layered textile — flat cream paper on top, indigo dye vat beneath. Surfaces never feel glassy or transparent; they feel like cotton cards laid over a sarong panel. Shadows are tinted with indigo halo (`rgba(31, 45, 82, ...)`) instead of neutral gray, so even depth signals the dye-vat origin.

- **Surface style**: layered (cream cards on cream page, separated by hairline + soft indigo shadow)
- **Blur**: none — batik is physical resist, not optical haze
- **Shadow ladder**: indigo-tinted, restrained — `0 2px 8px rgba(31, 45, 82, 0.15)` (md) through `0 24px 56px rgba(31, 45, 82, 0.28)` (2xl)

## Shapes

- `radius.sm` — 2px (hairline)
- `radius.md` — 4px (button — restrained, ceremonial)
- `radius.lg` — 8px (card)
- `radius.xl` — 12px (hero panel)
- `radius.full` — 9999px (pill, used sparingly for ceremonial tags)

## Motion

Motion is restrained and ceremonial — the canting moves slowly across the cloth. No bounce, no spring overshoot in primary surfaces; interactions resolve in 280ms with a measured ease-out. Hover signals are tint, hairline-stroke, and underline — never scale or glow, because batik does not "light up."

- **Level**: restrained
- **Durations**: fast 140ms (toggles), normal 280ms (panels), slow 440ms (page transitions)
- **Easings**: default `cubic-bezier(0.4, 0, 0.2, 1)`; spring reserved for one-off ceremonial reveals
- **Hover patterns**: tint, underline, stroke
- **Reduced motion**: respected; transitions collapse to opacity-only

## Techniques

### Parang diagonal sword-tile background
The signature court motif — 45° diagonal sword-blades repeating as a CSS background pattern. Used for hero panels, divider strips, and quiet section dividers. The cream-resist hairline is the gap between blades.

```css
.batik-parang {
  background-color: #1F2D52;
  background-image:
    repeating-linear-gradient(
      45deg,
      #1F2D52 0px,
      #1F2D52 14px,
      #6B4124 14px,
      #6B4124 28px,
      #F0E5C8 28px,
      #F0E5C8 30px,
      #6B4124 30px,
      #6B4124 44px
    );
  background-size: 60px 60px;
  border: 1px solid rgba(240, 229, 200, 0.4);
}
```

### Kawung four-circle interlock
Four interlocking circles — historically a royal-only court motif. Rendered as a tiled radial-gradient background for ceremonial card surfaces and sidebar accents.

```css
.batik-kawung {
  background-color: #F0E5C8;
  background-image:
    radial-gradient(circle at 0 0,    #1F2D52 0 9px, transparent 10px),
    radial-gradient(circle at 24px 0, #1F2D52 0 9px, transparent 10px),
    radial-gradient(circle at 0 24px, #1F2D52 0 9px, transparent 10px),
    radial-gradient(circle at 24px 24px, #1F2D52 0 9px, transparent 10px);
  background-size: 24px 24px;
  background-position: 0 0;
}
```

### Cream-resist hairline border
The canting's wax-line is what gives batik its bounded silhouette. Every card and divider uses a 1px cream-on-cream hairline (or cream-on-indigo for dark surfaces) — never a hard black rule.

```css
.resist-hairline {
  border: 1px solid #DDCEA8;
  box-shadow: inset 0 0 0 1px rgba(255, 251, 238, 0.6);
  border-radius: 8px;
  background: #FFFBEE;
  padding: 24px;
}

.resist-hairline--on-indigo {
  border: 1px solid rgba(240, 229, 200, 0.35);
  box-shadow: inset 0 0 0 1px rgba(240, 229, 200, 0.15);
  background: #1F2D52;
  color: #F0E5C8;
}
```

## Iconography

Custom linear icons in 1.5px stroke, soga-brown on cream surfaces and cream on indigo surfaces. The icon library leans on cultural motifs where appropriate — parang diagonal-blade, kawung four-circle, mega mendung cloud-bank, truntum eight-petal floral — used as decorative accents in section dividers and badges, not as functional UI icons.

- **Treatment**: linear, even-weight strokes echoing the canting's wax-line
- **Set**: custom (with motif library for decorative contexts)
- **Stroke**: 1.5px

## Do's & Don'ts

### ✓ Do
- Lock court compositions to the three-tone palette: court indigo, soga-brown, and undyed cream
- Use repeating-tile backgrounds (parang, kawung, truntum) as mathematical tile-repeats — never as random scatter
- Set body text in soga-brown `#6B4124`, never pure black
- Bound every surface with a cream-resist hairline (1px) — the canting's signature
- Reserve pesisir accents (madder-red, malachite-green, Chinese-pink) for non-court contexts only

### ✗ Don't
- Place patterns randomly — batik is precise mathematical tile-repeat
- Use modern sans-serif (Inter, Geist forbidden) — respect cultural typography context
- Use pastel or faded palette — must be saturated dye-vat tones
- Mix court and coastal vocabularies in the same composition
- Use photographic illustration — must feel wax-resist dye-block textile
- Use pure white as page background — use undyed-cotton cream
- Reduce to generic "Asian textile" stereotype — use specific Batik vocabulary (parang, kawung, mega mendung, soga, canting hairline)

## Applications

Best fit for editorial and ceremonial digital surfaces with cultural weight: Indonesian heritage publications, museum and UNESCO-affiliated sites, batik-house e-commerce, diplomatic and state-formal communications, slow-fashion textile brands, and long-form storytelling around craft traditions. The disciplined three-tone palette and serif voice make it equally at home in luxury craft commerce and academic-leaning editorial. Less suited to fast SaaS dashboards or modern tech-product chrome — the rhythm is ceremonial, not utilitarian.
