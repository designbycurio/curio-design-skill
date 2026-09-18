---
version: 1

meta:
  id: emoji-design-blob-noto-2013
  name: "Emoji & Sticker Design"
  description: "Glossy candy-fill emoji art — the canonical yellow smiley staged on deep charcoal so saturated sticker colors pop"
  isDark: true
  tags: [playful, friendly, bold, organic, handmade]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2013 (Google blobs debut in Android 4.4 KitKat) → 2017 retirement → 2021 revival via Emoji Kitchen"
  region: "Global / internet (Unicode emoji; Google, Apple, vendor sets)"
  regionZh: "全球 / 互联网（Unicode 表情符号；Google、Apple 等厂商表情集）"
  keyFigures: ["IC4DESIGN", "Noto Color Emoji team"]
  movements: ["Unicode emoji standardization", "Cross-platform sticker art", "Friendly vector iconography"]

introduction: |
  Cross-platform emoji and sticker design centers on the glossy yellow smiley — a shiny ball with a highlight-to-shade gradient, bold dark outlines, and soft playful drop shadows. Born with Google's 2013 "blob" emoji and carried forward by Noto Color Emoji, the language is chunky, friendly, and saturated.

  Here the classic blob smiley is staged on a deep neutral charcoal so the candy fills read at full pop. Rounded type, generous radii, glossy spheres, and bold outlines define a warm, instantly legible visual system built for joy.
introductionZh: |
  跨平台表情与贴纸设计的核心是那颗发亮的黄色笑脸——一颗带高光到暗部渐变的圆球，配上粗黑描边与柔和俏皮的投影。它始于 Google 2013 年的「blob」气泡表情，又由 Noto Color Emoji 一路延续，整套视觉语言圆润、亲切、饱和。

  在这里，经典的 blob 笑脸被放置在一片深邃的中性炭灰背景上，让糖果般的填色以最浓郁的方式跳出来。圆润的字体、慷慨的圆角、光泽的球体与粗壮的描边，共同构成一套温暖、第一眼就读得懂的视觉系统，为「快乐」而生。

colors:
  primary:
    "50": "#FFF9E6"
    "100": "#FEF1C2"
    "200": "#FEE389"
    "300": "#FDD550"
    "400": "#FCCB30"
    "500": "#FCC21B"
    "600": "#E0A911"
    "700": "#B5860C"
    "800": "#8A6509"
    "900": "#604607"
    "950": "#3A2A04"
  secondary:
    "50": "#FFF6E2"
    "100": "#FEEABC"
    "200": "#FDD884"
    "300": "#FCC74D"
    "400": "#FAB52F"
    "500": "#F8A91B"
    "600": "#E08F11"
    "700": "#B6710D"
    "800": "#8B5609"
    "900": "#603C07"
    "950": "#392404"
  accent:
    "50": "#FFFCEB"
    "100": "#FFF6C7"
    "200": "#FEED90"
    "300": "#FEE56A"
    "400": "#FDE34F"
    "500": "#FBD42A"
    "600": "#E6BC10"
    "700": "#BC960C"
    "800": "#917209"
    "900": "#665006"
    "950": "#3E3003"
  neutral:
    "50": "#F4F4F4"
    "100": "#E6E6E6"
    "200": "#C9C9C9"
    "300": "#A8A8A8"
    "400": "#7E7E7E"
    "500": "#5E5E5E"
    "600": "#4A4A4A"
    "700": "#3B3B3B"
    "800": "#2A2A2A"
    "900": "#1B1B1B"
    "950": "#101010"
  semantic:
    success: { bg: "#2BB673", text: "#063A22", light: "#C9F2DE", border: "#1E9A5E" }
    warning: { bg: "#F8A91B", text: "#392404", light: "#FEEABC", border: "#E08F11" }
    error: { bg: "#EF4B4B", text: "#FFE8E8", light: "#FCD2D2", border: "#D02F2F" }
    info: { bg: "#3B9CEF", text: "#04254A", light: "#CFE6FB", border: "#2C7FCF" }
  background:
    page: "#3B3B3B"
    surface: "#4A4A4A"
    subtle: "#2A2A2A"
  text:
    primary: "#F4F4F4"
    secondary: "#C9C9C9"
    muted: "#A8A8A8"
    inverse: "#1B1B1B"

typography:
  families:
    heading: "'Baloo 2', 'Fredoka', system-ui, sans-serif"
    body: "'Fredoka', 'Baloo 2', system-ui, sans-serif"
    mono: "'Noto Color Emoji', 'Baloo 2', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Fredoka:wght@300;400;500;600;700&family=Noto+Color+Emoji&display=swap"
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
    sm: "8px"
    md: "16px"
    lg: "24px"
    xl: "32px"
    full: "9999px"
  color:
    default: "#5C3B12"
    subtle: "rgba(92, 59, 18, 0.4)"
    strong: "#1B1B1B"
    focus: "#FCC21B"
  width:
    thin: "1px"
    default: "2px"
    thick: "4px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(27, 27, 27, 0.25)"
  sm: "0 2px 6px rgba(27, 27, 27, 0.30)"
  md: "0 4px 12px rgba(27, 27, 27, 0.35)"
  lg: "0 8px 20px rgba(27, 27, 27, 0.40)"
  xl: "0 14px 32px rgba(27, 27, 27, 0.45)"
  "2xl": "0 22px 48px rgba(27, 27, 27, 0.50)"
  inner: "inset 0 2px 4px rgba(27, 27, 27, 0.30)"
  focus: "0 0 0 4px rgba(252, 194, 27, 0.45)"

motion:
  level: "playful"
  durations:
    instant: "0ms"
    fast: "120ms"
    normal: "250ms"
    slow: "400ms"
    slower: "600ms"
  easings:
    default: "cubic-bezier(0.34, 1.56, 0.64, 1)"
    in: "cubic-bezier(0.55, 0, 1, 0.45)"
    out: "cubic-bezier(0, 0.55, 0.45, 1)"
    spring: "cubic-bezier(0.68, -0.55, 0.27, 1.55)"
  hoverPatterns: [scale, lift, glow, tint]
  reducedMotion: true

composition:
  layout: "grid"
  contentWidth: "container"
  framing: "solid"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "solid"
blur: "none"

iconography:
  treatment: "filled"
  set: "phosphor"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "2px"

components:
  button:
    primary:
      background: "#FCC21B"
      color: "#5C3B12"
      border: "2px solid #5C3B12"
      shadow: "0 4px 0 #B5860C, 0 6px 12px rgba(27, 27, 27, 0.35)"
      hoverBackground: "#FDD550"
      hoverShadow: "0 6px 0 #B5860C, 0 8px 16px rgba(27, 27, 27, 0.40)"
      hoverColor: "#5C3B12"
    secondary:
      background: "#4A4A4A"
      color: "#FCC21B"
      border: "2px solid #FCC21B"
      shadow: "0 2px 6px rgba(27, 27, 27, 0.30)"
      hoverBackground: "#5E5E5E"
      hoverShadow: "0 4px 12px rgba(27, 27, 27, 0.35)"
      hoverColor: "#FDD550"
    ghost:
      background: "transparent"
      color: "#F4F4F4"
      border: "2px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(252, 194, 27, 0.12)"
      hoverShadow: "none"
      hoverColor: "#FCC21B"
    danger:
      background: "#EF4B4B"
      color: "#FFE8E8"
      border: "2px solid #5C3B12"
      shadow: "0 4px 0 #D02F2F, 0 6px 12px rgba(27, 27, 27, 0.35)"
      hoverBackground: "#F36868"
      hoverShadow: "0 6px 0 #D02F2F, 0 8px 16px rgba(27, 27, 27, 0.40)"
      hoverColor: "#FFE8E8"
    sizes:
      sm: { height: "36px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "44px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "54px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "9999px"
    fontWeight: 700
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#4A4A4A"
    color: "#F4F4F4"
    border: "2px solid #5C3B12"
    borderRadius: "16px"
    padding: "12px 16px"
    focusBorder: "#FCC21B"
    placeholderColor: "#A8A8A8"
  card:
    base:
      background: "#4A4A4A"
      border: "2px solid #5C3B12"
      borderRadius: "24px"
      padding: "24px"
      shadow: "0 8px 20px rgba(27, 27, 27, 0.40)"
    hover:
      shadow: "0 14px 32px rgba(27, 27, 27, 0.45)"
      transform: "translateY(-4px) scale(1.02)"
---

# Emoji & Sticker Design

> The glossy yellow smiley, staged on charcoal: highlight-to-shade gradients, bold outlines, candy fills, and the chunky friendliness of cross-platform emoji.

## Origin

Cross-platform emoji and sticker design as a coherent visual language crystallized in 2013, when Google shipped its "blob" emoji in Android 4.4 KitKat — soft, gumdrop-shaped characters drawn by the studio **IC4DESIGN** and rendered through the **Noto Color Emoji** font. The blobs were polarizing and quirky, defined by glossy spherical bodies, bold dark outlines, and a signature smiley yellow. After Google retired the blobs in 2017 in favor of round-headed emoji for cross-vendor consistency, the originals gained cult status and were revived in 2021 through Emoji Kitchen, the mash-up sticker maker baked into Gboard.

Across this arc, the constant is the glossy yellow smiley — a shiny ball with a darker-yellow shaded gradient, a crisp highlight, and a soft drop shadow. It belongs to the broader project of Unicode emoji standardization, where every vendor (Google, Apple, Samsung, Twitter) interprets the same code point in chunky, friendly, saturated vector art. This system distills that lineage: rounded forms, bold outlines, candy-bright fills, and the canonical blob smiley as the hero motif.

## Overview

Composition cues:
- **Layout**: Centered grid of rounded "sticker" cards and chunky pills, each form floating with a soft drop shadow on the charcoal stage
- **Content width**: Container width — friendly, legible, never edge-to-edge clutter
- **Framing**: Solid — bold dark outlines and filled rounded shapes define every element; no glass, no hairlines
- **Grid intensity**: Soft — generous gaps let each glossy form read as its own happy object

## Colors

The palette is the smiley itself: the canonical blob yellow (`#FCC21B`) as primary, with a deeper shade (`#F8A91B`) and warm shade (`#EF8E2E`) forming the spherical gloss gradient, and a bright highlight (`#FDE34F`) for the catch-light. Bold brown (`#5C3B12`) supplies the outline-and-shadow ink that gives every form its sticker-cut edge, and near-black (`#1B1B1B`) anchors the deepest shadows. The page itself is a deep neutral charcoal (`#3B3B3B`) — a reinterpretation of the classic "drop shadow on white" stage, because cream and plain white are forbidden; the dark ground lets the saturated candy fills read at full pop. Nothing here is muted: the word is *saturated*.

**Role usage**:
- Page background → `colors.background.page` (charcoal `#3B3B3B`, the dark stage)
- Content surface / sticker cards → `colors.background.surface` (lighter charcoal `#4A4A4A`)
- Recessed / alt blocks → `colors.background.subtle` (deep charcoal `#2A2A2A`)
- Primary actions / smiley body → `colors.primary.500` (blob yellow `#FCC21B`)
- Gloss shade gradient → `colors.secondary.500` (deeper yellow `#F8A91B`)
- Highlight / catch-light → `colors.accent.400` (bright yellow `#FDE34F`)
- Outline & shadow ink → `borders.color.default` (brown `#5C3B12`)
- Body text on charcoal → `colors.text.primary` (near-white `#F4F4F4`)

## Typography

The type voice is rounded, chunky, and friendly — the lettering equivalent of a glossy sticker. **Baloo 2** drives headlines and display with its heavy, bouncy, fully-rounded terminals that echo the bold-outline emoji silhouette. **Fredoka** handles body and UI text: rounded but a touch more upright and legible at small sizes. **Noto Color Emoji** is the literal blob-emoji font, reserved for inline emoji glyphs and the "mono" role so real emoji render in their native vendor form. All three are genuine Google Fonts. Weights run heavy — 600–800 for headings — because emoji type wants presence, not restraint. No thin elegant serifs ever appear here.

**Text styles**:
- `display-xl` — Baloo 2, 96px, weight 800, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Baloo 2, 64px, weight 800, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Baloo 2, 40px, weight 700, line-height 1.2, letter-spacing 0
- `body-lg` — Fredoka, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Fredoka, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Fredoka, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Noto Color Emoji, 16px, weight 400, line-height 1.8, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container max-widths: sm 640px, md 768px, lg 1024px, xl 1280px
- Section padding: 64px vertical (md), 96px (lg) — generous breathing room around floating sticker forms
- Grid gaps: 16px (md) to 24px (lg) — soft spacing so each glossy object reads on its own

## Elevation & Depth

Depth here is *cartoon dimensionality*, not photographic realism. Every glossy form sits above the charcoal stage on a soft, slightly warm-dark drop shadow — the same playful shadow that anchors a sticker peeled onto a page. Buttons carry a stacked "extruded" shadow (a solid color offset plus a soft blur) so they look like physical candy buttons you could press. The spherical gloss itself is built from layered gradients and a bright catch-light highlight, never a flat fill.

- Surface style: solid (filled, outlined sticker shapes — no transparency or glass)
- Blur: none (vector emoji is crisply rendered, edges stay sharp)
- Shadow ladder: dark-neutral rgba — xs through 2xl use `rgba(27, 27, 27, ...)` at ascending opacity and offset
- Inner shadow: subtle dark inset for recessed input wells
- Focus ring: 4px blob-yellow glow at 45% opacity

## Shapes

- `none`: 0 — rare; this system is anti-sharp-corner
- `sm`: 8px — tags, small chips
- `md`: 16px — inputs, minor containers
- `lg`: 24px — cards and sticker panels (the default friendly radius)
- `xl`: 32px — hero panels and large feature blocks
- `full`: 9999px — pills, buttons, and the spherical smiley body

## Motion

Motion is playful and springy — every interaction should feel like a happy little bounce. Hovers scale and lift with overshoot easing, as if the sticker is delighted to be touched. Nothing is stiff or linear; the temperament is bouncy candy, tuned just shy of cartoonish.

- Level: playful
- Durations: instant 0ms, fast 120ms, normal 250ms, slow 400ms, slower 600ms
- Default easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` — gentle overshoot for a springy settle
- Spring easing: `cubic-bezier(0.68, -0.55, 0.27, 1.55)` — pronounced bounce for press feedback
- Hover patterns: scale (grow on hover), lift (translateY up), glow (yellow focus glow), tint (brighten fill)
- `reducedMotion: true` — all bounce and scale animations respect `prefers-reduced-motion`

## Techniques

### Glossy smiley sphere
The hero motif: a yellow ball built from a radial highlight, a highlight-to-shade gradient body, a bold brown outline, and a soft drop shadow — never a flat single-tone fill.
```css
.smiley {
  width: 160px;
  height: 160px;
  border-radius: 9999px;
  border: 4px solid #5C3B12;
  background:
    radial-gradient(circle at 34% 28%, #FDE34F 0%, transparent 38%),
    radial-gradient(circle at 50% 120%, #EF8E2E 0%, transparent 60%),
    linear-gradient(160deg, #FCC21B 0%, #F8A91B 70%);
  box-shadow:
    0 14px 28px rgba(27, 27, 27, 0.45),
    inset 0 -10px 18px rgba(92, 59, 18, 0.25);
}
```

### Extruded candy button
A pressable button with a stacked solid-color offset under a soft blur, giving the chunky "physical sticker" depth that snaps down on press.
```css
.candy-btn {
  background: #FCC21B;
  color: #5C3B12;
  border: 2px solid #5C3B12;
  border-radius: 9999px;
  font-family: 'Baloo 2', sans-serif;
  font-weight: 700;
  box-shadow: 0 4px 0 #B5860C, 0 6px 12px rgba(27, 27, 27, 0.35);
  transition: transform 120ms cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 120ms ease;
}
.candy-btn:active {
  transform: translateY(4px);
  box-shadow: 0 0 0 #B5860C, 0 2px 6px rgba(27, 27, 27, 0.30);
}
```

### Sticker-cut outline
The peeled-sticker silhouette: a thick white-or-bordered ring plus a soft drop shadow that lifts any shape off the charcoal stage, mimicking a die-cut sticker edge.
```css
.sticker {
  border: 4px solid #5C3B12;
  border-radius: 24px;
  background: #4A4A4A;
  box-shadow:
    0 0 0 6px #3B3B3B,
    0 10px 22px rgba(27, 27, 27, 0.45);
  filter: drop-shadow(0 2px 0 rgba(27, 27, 27, 0.30));
}
```

## Iconography

Icons should feel like mini stickers, not utility glyphs — bold, filled, rounded, and outlined to match the emoji vocabulary. Prefer chunky filled shapes with generous corner radii and a heavy 2px outline so each icon reads like a tiny candy form. Where a functional icon set is needed, use Phosphor in its **fill** weight at a 2px equivalent stroke, and lean on real emoji (via Noto Color Emoji) wherever an emoji can do the job directly.

- Treatment: filled (bold solid shapes with rounded corners)
- Set: Phosphor (fill weight)
- Stroke: 2px

## Do's & Don'ts

### ✓ Do
- Stage everything on charcoal `#3B3B3B` — the dark ground is what makes the candy fills pop
- Build the smiley as a glossy sphere with a highlight-to-shade gradient — layer radial highlight, gradient body, and brown outline
- Outline forms with brown `#5C3B12` and lift them with soft drop shadows so they read as die-cut stickers
- Use Baloo 2 for headlines and Fredoka for body — keep type rounded, chunky, and heavy
- Make interactions bounce — scale and lift on hover with overshoot easing, press down with a satisfying snap

### ✗ Don't
- Use cream, ivory, or plain-white page backgrounds — even though the classic emoji stage is white, use charcoal instead
- Use a flat single-tone yellow — the smiley must carry a highlight-to-shade gradient
- Use thin elegant serifs — emoji and sticker type is rounded and chunky
- Use muted or desaturated palettes — fills are saturated candy colors
- Make shapes sharp-cornered or sit them flat with no shadow — friendly forms are rounded and float

## Applications

This system is ideal for messaging and sticker products, kids' and family apps, casual games, reaction and reward surfaces, and any playful consumer brand that wants warmth and instant approachability. It shines on onboarding screens, empty states, achievement toasts, and emoji-picker UIs where a glossy smiley does the emotional heavy lifting. The charcoal-plus-candy palette also suits dark-mode marketing pages and app stores where saturated, friendly art needs to pop against a neutral stage.
