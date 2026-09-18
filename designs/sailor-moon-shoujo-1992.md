---
version: 1

meta:
  id: sailor-moon-shoujo-1992
  name: Sailor Moon Shoujo
  description: Saturated pink-and-pastel magical-girl shoujo with sparkle, rose-petals, and crescent-moon ornament.
  isDark: false
  tags: [decorative, narrative, friendly, ornate, subcultural]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1991 manga debut (Nakayoshi); 1992 anime; ongoing through Sailor Moon Crystal 2014+"
  region: "Japan; global magical-girl and shoujo-anime influence"
  regionZh: "日本东京"
  keyFigures: ["Naoko Takeuchi", "Toei Animation", "Junichi Sato", "Kunihiko Ikuhara"]
  movements: ["1990s magical-girl anime", "shoujo manga golden age", "bishoujo aesthetic"]

introduction: |
  Sailor Moon Shoujo is the canonical 1990s magical-girl visual language: saturated pink and lavender,
  cream paper backdrops, sparkle overlays, rose petals, and ornate transformation-sequence flourishes.
  Born in Naoko Takeuchi's manga and Toei Animation's 1992 anime, it set the template for shoujo romance
  and magical-girl genres for decades.

  The aesthetic feels like a transformation sequence frozen mid-spin — saturated pastel-rainbow swirls,
  crescent-moon tiaras, ribbons, and editorial italic flourishes. Sweet, ornate, narrative, unmistakably shoujo.

introductionZh: |
  Sailor Moon 美少女战士的视觉语言来自武内直子 1991 年于《好朋友》月刊连载的少女漫画，以及
  东映动画 1992 年的电视动画化版本。它定义了整个 1990 年代魔法少女流派的视觉范式：饱和的
  粉红与薰衣草紫，奶油色纸感底色，星光闪烁的叠层，玫瑰花瓣的飘落，以及变身桥段标志性的
  繁复装饰花纹。

  整体气质像一段被定格的变身序列：饱和的彩虹色漩涡、新月发饰、丝带与勋章、华丽的意大利体
  花字。甜美、繁复、叙事性强，是不折不扣的少女漫画美学，至今仍在 Sailor Moon Crystal 重制版
  与无数后继魔法少女作品中延续。

colors:
  primary:
    "50":  "#FFF1F5"
    "100": "#FFE0EA"
    "200": "#FFC8D9"
    "300": "#FFB0C6"
    "400": "#FF9EBC"
    "500": "#FF8FB1"
    "600": "#EE7FA0"
    "700": "#D86F8A"
    "800": "#B85871"
    "900": "#923F55"
    "950": "#5C2433"
  secondary:
    "50":  "#F8F2FD"
    "100": "#EFE2FA"
    "200": "#E3CDF5"
    "300": "#D6B8EF"
    "400": "#CFAEEA"
    "500": "#C9A8E8"
    "600": "#B48ED5"
    "700": "#9670B8"
    "800": "#735393"
    "900": "#4F386A"
    "950": "#2C1E3D"
  accent:
    "50":  "#FFFBE0"
    "100": "#FFF7C2"
    "200": "#FFF099"
    "300": "#FFEB7A"
    "400": "#FFE863"
    "500": "#FFE352"
    "600": "#EFCC2E"
    "700": "#C9A91D"
    "800": "#9A8016"
    "900": "#6A580E"
    "950": "#3D3206"
  neutral:
    "50":  "#FBF7EE"
    "100": "#F5EEDB"
    "200": "#F0E5D0"
    "300": "#E2D3B8"
    "400": "#C9B69A"
    "500": "#A8927A"
    "600": "#8F6F6F"
    "700": "#6E5252"
    "800": "#4F3838"
    "900": "#3D2424"
    "950": "#221414"
  semantic:
    success: { bg: "#EFF9E8", text: "#3F6A2A", light: "#D4F0BD", border: "#A8E89A" }
    warning: { bg: "#FFF7D6", text: "#7A5A0E", light: "#FFEE9F", border: "#FFE352" }
    error:   { bg: "#FFE5EE", text: "#8C1F46", light: "#FFC4D4", border: "#E83A8A" }
    info:    { bg: "#E8F0F9", text: "#34557A", light: "#C8DCEF", border: "#A8C5E8" }
  background:
    page:    "#F0E5D0"
    surface: "#FFFFFF"
    subtle:  "#FBF7EE"
  text:
    primary:   "#3D2424"
    secondary: "#6E5252"
    muted:     "#8F6F6F"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'DM Serif Display', 'Cormorant Garamond', Georgia, serif"
    body:    "'Inter', 'Cormorant Garamond', system-ui, sans-serif"
    mono:    "'JetBrains Mono', 'Menlo', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Italianno&family=Sacramento&family=Inter:wght@400;500;600;700&display=swap"
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
  radius: {none: "0", sm: "8px", md: "12px", lg: "20px", xl: "28px", full: "9999px"}
  color:  {default: "#E3CDF5", subtle: "#F5EEDB", strong: "#FF8FB1", focus: "#E83A8A"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(255, 143, 177, 0.10)"
  sm: "0 2px 6px rgba(255, 143, 177, 0.12)"
  md: "0 4px 16px rgba(255, 143, 177, 0.18)"
  lg: "0 10px 28px rgba(232, 58, 138, 0.20)"
  xl: "0 20px 48px rgba(201, 168, 232, 0.28)"
  "2xl": "0 32px 72px rgba(232, 58, 138, 0.30)"
  inner: "inset 0 1px 3px rgba(216, 111, 138, 0.18)"
  focus: "0 0 0 3px rgba(232, 58, 138, 0.35)"

motion:
  level: "playful"
  durations: {instant: "0ms", fast: "140ms", normal: "280ms", slow: "480ms", slower: "720ms"}
  easings:
    default: "cubic-bezier(0.34, 1.36, 0.64, 1)"
    in:      "cubic-bezier(0.55, 0.06, 0.68, 0.19)"
    out:     "cubic-bezier(0.22, 0.61, 0.36, 1)"
    spring:  "cubic-bezier(0.5, 1.6, 0.5, 1)"
  hoverPatterns: [lift, glow, scale, tint]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "8px"

iconography:
  treatment: "duotone"
  set:       "phosphor"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "#FF8FB1"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 4px 16px rgba(255, 143, 177, 0.35)"
      hoverBackground: "#E83A8A"
      hoverShadow: "0 6px 22px rgba(232, 58, 138, 0.45)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "#FFFFFF"
      color: "#D86F8A"
      border: "1.5px solid #FF8FB1"
      shadow: "0 2px 8px rgba(255, 143, 177, 0.15)"
      hoverBackground: "#FFF1F5"
      hoverShadow: "0 4px 14px rgba(255, 143, 177, 0.25)"
      hoverColor: "#E83A8A"
    ghost:
      background: "transparent"
      color: "#D86F8A"
      border: "none"
      shadow: "none"
      hoverBackground: "#FFF1F5"
      hoverShadow: "none"
      hoverColor: "#E83A8A"
    danger:
      background: "#E83A8A"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 4px 16px rgba(232, 58, 138, 0.35)"
      hoverBackground: "#C42B6F"
      hoverShadow: "0 6px 22px rgba(232, 58, 138, 0.50)"
      hoverColor: "#FFFFFF"
    sizes:
      sm: {height: "32px", padding: "0 14px", fontSize: "0.875rem"}
      md: {height: "44px", padding: "0 22px", fontSize: "1rem"}
      lg: {height: "54px", padding: "0 32px", fontSize: "1.125rem"}
    borderRadius: "12px"
    fontWeight: 600
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#3D2424"
    border: "1.5px solid #E3CDF5"
    borderRadius: "12px"
    padding: "12px 16px"
    focusBorder: "1.5px solid #E83A8A"
    placeholderColor: "#8F6F6F"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid #F0E5D0"
      borderRadius: "20px"
      padding: "28px"
      shadow: "0 4px 16px rgba(255, 143, 177, 0.18)"
    hover:
      shadow: "0 10px 28px rgba(232, 58, 138, 0.20)"
      transform: "translateY(-3px)"
---

# Sailor Moon Shoujo

> Magical-girl mythology in saturated pink and lavender — sparkle overlays, rose petals, crescent-moon tiaras, and ornate transformation flourishes.

## Origin

Sailor Moon began in 1991 when Naoko Takeuchi serialized her magical-girl manga in Kodansha's *Nakayoshi* magazine. Toei Animation's 1992 anime adaptation made it a global phenomenon, running five television seasons plus theatrical films through 1997. Across 18 manga volumes and 200 episodes of animation, Takeuchi and Toei built a visual vocabulary — saturated pinks, crescent-moon tiaras, transformation sparkle, ribbon-laced sailor uniforms — that became the canonical 1990s magical-girl look.

The aesthetic radiates outward through Cardcaptor Sakura, Tokyo Mew Mew, Pretty Cure, Madoka Magica, and the entire 2010s magical-girl revival. Sailor Moon Crystal (2014+) and the Eternal film cycle continue the line. The look is also foundational to shoujo-romance and bishoujo aesthetics globally — its rose-petal flourishes and ornate ribbon work now signal "shoujo" to readers worldwide.

## Overview

Composition cues:
- **Layout**: vertically stacked editorial flow with generous breathing room; not a hard grid
- **Content width**: container (max ~1180px), centered, framed by cream margins
- **Framing**: layered cream/white panels over pink/lavender washes, rounded 20px corners, soft pink shadows
- **Grid intensity**: soft — alignment is felt, not enforced; ornaments break the grid by design

## Colors

The palette is a saturated magical-girl pastel-rainbow grounded in cream paper: cream `#F0E5D0` provides the warm backdrop, saturated pink `#FF8FB1` carries primary actions and emotion, lavender `#C9A8E8` softens secondary surfaces, and hot-yellow `#FFE352` flashes like sparkle. Sky-blue `#A8C5E8`, mint `#A8E89A`, and hot-pink `#E83A8A` round out the rainbow. Text is warm brown-black `#3D2424`, never neutral grey — every color carries warmth.

**Role usage**:
- Page background → `colors.background.page` (`#F0E5D0` cream paper)
- Card / panel surface → `colors.background.surface` (`#FFFFFF`)
- Subtle inset panel → `colors.background.subtle` (`#FBF7EE`)
- Primary CTA + emotion → `colors.primary.500` (`#FF8FB1` saturated pink)
- Hover / pressed primary → `colors.primary.700` (`#D86F8A`)
- Secondary surfaces, badges → `colors.secondary.500` (`#C9A8E8` lavender)
- Sparkle / highlight accents → `colors.accent.500` (`#FFE352` hot-yellow)
- Body text → `colors.text.primary` (`#3D2424` warm brown-black)
- Muted captions → `colors.text.muted` (`#8F6F6F`)

## Typography

The type voice mixes editorial-romantic serif with hand-written script flourish. **DM Serif Display** is the heading face — high-contrast, slightly theatrical, italics readily used for emphasis. **Cormorant Garamond** carries longer-form prose with classical warmth. **Italianno** and **Sacramento** appear sparingly for hand-script flourishes (chapter openers, signature-style callouts, transformation phrases). **Inter** handles small UI text where script wouldn't read. Letter-spacing is generous and decorative — ornate, never tight.

**Text styles**:
- `display-xl` — DM Serif Display, 96px, weight 400 italic, line-height 1.0, letter-spacing -0.02em
- `display-lg` — DM Serif Display, 72px, weight 400, line-height 1.05, letter-spacing -0.02em
- `display-script` — Italianno, 84px, weight 400, line-height 1.1, letter-spacing 0.02em
- `heading-1` — DM Serif Display, 48px, weight 400, line-height 1.15, letter-spacing -0.01em
- `heading-2` — DM Serif Display, 36px, weight 400 italic, line-height 1.2
- `heading-3` — Cormorant Garamond, 28px, weight 600, line-height 1.25
- `body-lg` — Cormorant Garamond, 20px, weight 400, line-height 1.6
- `body-md` — Inter, 16px, weight 400, line-height 1.625
- `caption` — Inter, 13px, weight 500, line-height 1.5, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 500, line-height 1.5

## Spacing & Layout

- **Base unit**: 4px (rhythm allows 8px steps for breath)
- **Scale**: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- **Container**: sm 640 / md 768 / lg 1024 / xl 1280
- **Grid gap**: sm 8 / md 16 / lg 24 / xl 48
- **Section padding**: sm 32 / md 64 / lg 96 / xl 128 — sections breathe like a manga page

## Elevation & Depth

Surfaces feel like paper layered over a watercolor wash. Shadows are tinted pink, not neutral grey — they reinforce the saturated palette rather than mute it. Cards float on cream backgrounds with `0 4px 16px rgba(255, 143, 177, 0.18)`; on hover the shadow deepens toward hot-pink. Modal and elevated surfaces use a longer lavender-tinted halo.

- **Surface style**: layered (cream → white → pink wash)
- **Blur**: 8px for sparkle-overlay decorations only — never glassmorphism on UI
- **Shadow ladder**: xs / sm / md / lg / xl / 2xl, all hue-tinted pink-to-hot-pink
- **Inner shadow**: subtle warm-rose inset for pressed states

## Shapes

- Buttons: 12px radius — softly rounded, sweet but not bubble-y
- Cards: 20px radius — pronounced sweet-rounded corners
- Inputs: 12px radius
- Avatars / chips: 9999px (full)
- Section panels: 28px radius for marquee surfaces

## Motion

Motion is playful and slightly bouncy — every transition wants to sparkle. Default easing uses a soft spring (`cubic-bezier(0.34, 1.36, 0.64, 1)`) that overshoots a touch, evoking the bounce of a transformation pose. Durations skew slightly longer than corporate UI (280ms normal vs 200ms) to feel ornate. Hovers lift the surface, brighten the tint, and glow softly. Sparkle and rose-petal motifs animate on scroll for hero surfaces. Reduced-motion strips the bounce but keeps the tint transitions.

- **Level**: playful
- **Durations**: instant 0 / fast 140 / normal 280 / slow 480 / slower 720
- **Easings**: spring default, ease-out for entrances, snappy ease-in for exits
- **Hover patterns**: lift + glow + scale + tint
- **Reduced motion**: respected (drop bounce, keep tint)

## Techniques

### Crescent-moon tiara gradient border
A signature shoujo flourish: a rounded surface ringed by a soft pink-to-lavender-to-yellow gradient, evoking Sailor Moon's tiara crescent and transformation halo.

```css
.tiara-card {
  position: relative;
  background: #FFFFFF;
  border-radius: 20px;
  padding: 28px;
}
.tiara-card::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: 22px;
  padding: 2px;
  background: conic-gradient(from 220deg,
    #FF8FB1, #FFE352, #C9A8E8, #A8C5E8, #FF8FB1);
  -webkit-mask:
    linear-gradient(#000 0 0) content-box,
    linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  pointer-events: none;
}
```

### Sparkle-overlay backdrop
The hallmark transformation-sequence shimmer — soft glowing sparkles scattered across a hero surface using layered radial gradients. No images required.

```css
.sparkle-hero {
  position: relative;
  background:
    radial-gradient(2px 2px at 18% 22%, rgba(255,227,82,0.95), transparent 70%),
    radial-gradient(3px 3px at 72% 38%, rgba(255,255,255,0.85), transparent 70%),
    radial-gradient(2px 2px at 44% 78%, rgba(255,143,177,0.9), transparent 70%),
    radial-gradient(1.5px 1.5px at 88% 64%, rgba(201,168,232,0.95), transparent 70%),
    linear-gradient(135deg, #FFE0EA 0%, #EFE2FA 55%, #FFF1F5 100%);
  border-radius: 28px;
  overflow: hidden;
}
.sparkle-hero::after {
  content: "✦";
  position: absolute;
  top: 16%; right: 12%;
  font-size: 28px;
  color: #FFE352;
  filter: drop-shadow(0 0 12px rgba(255, 227, 82, 0.7));
}
```

### Rose-petal divider
A horizontal rule built from inline rose-petal glyphs flanked by hairline pink rules — replaces the generic `<hr>` for editorial section breaks.

```css
.petal-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #E83A8A;
  font-family: 'DM Serif Display', serif;
  font-style: italic;
}
.petal-divider::before,
.petal-divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg,
    transparent, #FF8FB1 30%, #FF8FB1 70%, transparent);
}
.petal-divider .petal { font-size: 20px; }
/* Usage: <div class="petal-divider"><span class="petal">❀</span></div> */
```

## Iconography

Icons lean duotone with soft 1.5px stroke — Phosphor's duotone set blends with the ornate aesthetic without becoming saccharine. Crescent-moon, sparkle, rose, ribbon, and heart motifs appear as bespoke ornaments alongside utility icons. Stroke weight stays soft (1.5px), never crisp engineering-grade.

- **Treatment**: duotone with pink/lavender pairing
- **Set**: Phosphor (duotone) + custom motif library (crescent, sparkle, rose, ribbon)
- **Stroke**: 1.5px, rounded line-caps and joins

## Do's & Don'ts

### ✓ Do
- Use saturated pink `#FF8FB1` for primary CTAs and emotional accents
- Layer cream `#F0E5D0`, white surfaces, and pink/lavender washes for depth
- Apply DM Serif Display italics for headings and Italianno script for flourish moments
- Sprinkle sparkle and rose-petal motifs to break the grid and add narrative warmth
- Tint shadows pink — `rgba(255, 143, 177, 0.18)` md, deepening to hot-pink on hover

### ✗ Don't
- Don't use cool desaturated palettes — stay in the saturated magical-girl pastel-rainbow
- Don't strip the ornament for minimalist restraint — this aesthetic lives in decorative warmth
- Don't fall back on generic anime stereotypes — use specific Sailor Moon vocabulary (crescent-moon, tiara, sparkle, rose-petal)
- Don't apply sleek-modernist-corporate framing — keep shoujo-anime-warmth and sweet-pastel softness

## Applications

Sailor Moon Shoujo fits magical-girl fandom sites, shoujo-manga editorial layouts, sweet-pastel lifestyle brands, romance fiction platforms, anime convention identity work, and decorative landing pages aimed at fans of 1990s-2000s shoujo aesthetics. It is also a strong pick for personal blogs, beauty and stationery brands, and any product that wants to signal warmth, narrative, and ornate femininity. It is not suited to enterprise dashboards, technical documentation, or contexts that demand restrained corporate neutrality.
