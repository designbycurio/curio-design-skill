---
version: 1

meta:
  id: miro-collab-yellow
  name: Miro Collab Yellow
  description: Saturated Miro-yellow plus warm hand-drawn whiteboard warmth for remote-team collaboration.
  isDark: false
  tags: [tech, friendly, playful, modernist, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2011 founded as RealtimeBoard; rebranded Miro 2019; current identity ~2019–2024"
  region: "San Francisco, USA (HQ); origin Perm, Russia; globally distributed"
  regionZh: "美国旧金山（总部）／俄罗斯彼尔姆（创立地），全球远程分布"
  keyFigures: ["Andrey Khusid", "Oleg Shardin", "Miro in-house brand team"]
  movements: ["digital-whiteboard SaaS", "remote-collaboration boom 2020+", "warm-modernist SaaS aesthetic"]

introduction: |
  Miro is the online-whiteboard collaboration SaaS that turned distributed brainstorming into a $17B+ category. Founded 2011 as RealtimeBoard and rebranded Miro in 2019, the visual identity centers on a saturated Miro-yellow anchor, warm hand-drawn illustration, and a sticky-note rainbow.

  The aesthetic feels like miro.com itself: white ground, Miro-yellow CTAs, friendly Inter typography, and hero blocks rendered as whiteboard mockups full of sticky notes, sketched arrows, and circled callouts. It says "remote teams sketching together," not "enterprise SaaS slab."
introductionZh: |
  Miro 是把"远程团队一起在白板上贴便利贴"这件事做成 170 亿美元生意的在线协作 SaaS。2011 年由 Andrey Khusid 与 Oleg Shardin 在俄罗斯彼尔姆创立，原名 RealtimeBoard，2019 年正式更名为 Miro，总部迁至美国旧金山，疫情后随远程办公浪潮成为白板协作的代名词。

  这套视觉的核心是饱和的 Miro 黄 `#F4D74C`，配深紫黑 `#050038` 文字与纯白底，外加便利贴粉、便利贴蓝、便利贴绿、便利贴橙的"小彩虹"系统色。字体首选 Inter，备选 Manrope，气质干净现代但又带手绘暖意。Hero 区常以白板模型呈现：手绘箭头、圆圈批注、贴满便利贴的画布，像一群人正围着同一面墙做头脑风暴。它要的是温暖、友好、协作感，而不是冷冰冰的企业风。

colors:
  primary:    {"50": "#FFFBEA", "100": "#FEF6CC", "200": "#FCEC99", "300": "#FAE266", "400": "#F7DB55", "500": "#F4D74C", "600": "#DCC141", "700": "#C2A92F", "800": "#8A7820", "900": "#564B14", "950": "#2B250A"}
  secondary:  {"50": "#FDF2F9", "100": "#FCE6F2", "200": "#F9C8E2", "300": "#F7A8D2", "400": "#F58FC4", "500": "#F472B6", "600": "#D85E9F", "700": "#B14982", "800": "#7F3460", "900": "#4B1F39", "950": "#26101C"}
  accent:     {"50": "#EFF5FF", "100": "#DCE9FE", "200": "#B9D3FD", "300": "#8FB7FB", "400": "#6299F8", "500": "#3B82F6", "600": "#2F6BD6", "700": "#2553A8", "800": "#1B3D7A", "900": "#11254A", "950": "#091428"}
  neutral:    {"50": "#FAFAFA", "100": "#F7F7F7", "200": "#E5E7EB", "300": "#D1D5DB", "400": "#9CA3AF", "500": "#6B7280", "600": "#4B5563", "700": "#374151", "800": "#1F2937", "900": "#111827", "950": "#050038"}
  semantic:
    success: { bg: "#ECFDF5", text: "#065F46", light: "#A7F3D0", border: "#10B981" }
    warning: { bg: "#FFFBEA", text: "#8A7820", light: "#FCEC99", border: "#F4D74C" }
    error:   { bg: "#FEF2F2", text: "#991B1B", light: "#FECACA", border: "#EF4444" }
    info:    { bg: "#EFF5FF", text: "#1E3A8A", light: "#DCE9FE", border: "#3B82F6" }
  background:
    page:    "#FFFFFF"
    surface: "#F7F7F7"
    subtle:  "#FFFBEA"
  text:
    primary:   "#050038"
    secondary: "#374151"
    muted:     "#6B7280"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Inter', 'Manrope', system-ui, sans-serif"
    body:    "'Inter', system-ui, sans-serif"
    mono:    "'JetBrains Mono', 'Menlo', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap"
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
  radius: {none: "0", sm: "4px", md: "8px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "#E5E7EB", subtle: "#F7F7F7", strong: "#050038", focus: "#F4D74C"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(5, 0, 56, 0.05)"
  sm: "0 2px 4px rgba(5, 0, 56, 0.06)"
  md: "0 4px 12px rgba(244, 215, 76, 0.15)"
  lg: "0 8px 24px rgba(5, 0, 56, 0.10)"
  xl: "0 16px 40px rgba(5, 0, 56, 0.14)"
  "2xl": "0 24px 60px rgba(244, 215, 76, 0.25)"
  inner: "inset 0 1px 2px rgba(5, 0, 56, 0.05)"
  focus: "0 0 0 3px rgba(244, 215, 76, 0.45)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, scale, tint, glow]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       solid
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: linear
  set:       lucide
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.75px"

components:
  button:
    primary:
      background: "#F4D74C"
      color: "#050038"
      border: "1px solid #F4D74C"
      shadow: "0 4px 12px rgba(244, 215, 76, 0.35)"
      hoverBackground: "#FAE266"
      hoverShadow: "0 6px 18px rgba(244, 215, 76, 0.45)"
      hoverColor: "#050038"
    secondary:
      background: "#FFFFFF"
      color: "#050038"
      border: "1px solid #050038"
      shadow: "none"
      hoverBackground: "#F7F7F7"
      hoverShadow: "0 2px 8px rgba(5, 0, 56, 0.08)"
      hoverColor: "#050038"
    ghost:
      background: "transparent"
      color: "#050038"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "#FFFBEA"
      hoverShadow: "none"
      hoverColor: "#050038"
    danger:
      background: "#EF4444"
      color: "#FFFFFF"
      border: "1px solid #EF4444"
      shadow: "0 2px 8px rgba(239, 68, 68, 0.25)"
      hoverBackground: "#DC2626"
      hoverShadow: "0 4px 12px rgba(239, 68, 68, 0.35)"
      hoverColor: "#FFFFFF"
    sizes:
      sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}
      md: {height: "40px", padding: "0 18px", fontSize: "1rem"}
      lg: {height: "48px", padding: "0 24px", fontSize: "1.125rem"}
    borderRadius: "8px"
    fontWeight: 600
    letterSpacing: "-0.01em"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#050038"
    border: "1px solid #E5E7EB"
    borderRadius: "8px"
    padding: "10px 14px"
    focusBorder: "1px solid #F4D74C"
    placeholderColor: "#9CA3AF"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid #E5E7EB"
      borderRadius: "16px"
      padding: "24px"
      shadow: "0 4px 12px rgba(244, 215, 76, 0.15)"
    hover:
      shadow: "0 8px 24px rgba(244, 215, 76, 0.22)"
      transform: "translateY(-2px)"
---

# Miro Collab Yellow

> Saturated Miro-yellow plus warm hand-drawn whiteboard warmth — the visual language of remote-team brainstorming.

## Origin

Miro began in 2011 as RealtimeBoard, founded in Perm, Russia by Andrey Khusid and Oleg Shardin to give distributed teams a shared infinite canvas. After a 2019 rebrand to Miro and a 2022 valuation of $17.5B, it became the de facto whiteboard for remote workshops, agile ceremonies, design sprints, and post-it-note brainstorming. The current identity dates from that 2019 rebrand and has been refined alongside the rise of Figma's FigJam, Mural, Lucidspark, and Whimsical in the pandemic-era collaboration boom.

The brand's visual anchor is a single saturated yellow — Miro-yellow `#F4D74C` — paired with a deep purple-black `#050038` for type. Around that anchor sits a small "sticky-note rainbow" of pink, blue, green, and orange that maps directly to the colored notes users drop on a real Miro board. Hero areas read like whiteboard mockups: hand-drawn arrows, circled callouts, sticky-note clusters, and the friendly geometry of Inter typography. The aesthetic deliberately avoids cold corporate SaaS chrome in favor of warm illustration that says "humans collaborating."

## Overview

Composition cues:
- **Layout**: 12-column grid with generous gutters; hero blocks framed as whiteboard mockups
- **Content width**: 1280px container with 96px section padding
- **Framing**: solid white surfaces with Miro-yellow accent panels and soft drop shadows
- **Grid intensity**: soft — visible rhythm without rigid lines; hand-drawn dividers replace strict rules

## Colors

The palette is built around one loud anchor and a friendly chorus. Miro-yellow `#F4D74C` carries every primary CTA and accent panel; deep purple-black `#050038` carries all body text and structural strokes; pure white `#FFFFFF` is the canvas, with `#F7F7F7` as a subtle alt surface. The "sticky-note rainbow" — pink `#F472B6`, blue `#3B82F6`, green `#10B981`, orange `#F59E0B` — is reserved for note clusters, illustration, and category tags, never for chrome.

**Role usage**:
- Page background → `colors.background.page` (`#FFFFFF`)
- Alt / section background → `colors.background.surface` (`#F7F7F7`)
- Yellow hero panel → `colors.primary['500']` (`#F4D74C`)
- Body text → `colors.text.primary` (`#050038`)
- Muted text → `colors.text.muted` (`#6B7280`)
- Primary CTA fill → `colors.primary['500']` with `text.primary` label
- Sticky-note pink / blue / green / orange → `secondary.500` / `accent.500` / `semantic.success.border` / `semantic.warning` family
- Focus ring → `colors.primary['500']` at 45% alpha

## Typography

Inter is the workhorse — chosen for its open apertures, friendly geometric warmth, and excellent rendering at small UI sizes. Manrope is the alternative for marketing headlines that want a slightly more rounded display feel. Letter-spacing is gently negative on display sizes (`-0.02em` to `-0.04em`), normal on body. Weights run from 400 body to 700 display; nothing heavier — Miro never shouts.

**Text styles**:
- `display-xl` — Inter, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Inter, 64px, weight 700, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Inter, 48px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-2` — Inter, 32px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Inter, 18px, weight 400, line-height 1.625
- `body-md` — Inter, 16px, weight 400, line-height 1.5
- `caption` — Inter, 13px, weight 500, line-height 1.4, color `text.muted`
- `mono-md` — JetBrains Mono, 14px, weight 500, line-height 1.5

## Spacing & Layout

- Base unit: 4px; rhythm doubles to 8px for component padding
- Scale: 2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 px
- Container: 1280px max-width with 24px gutter padding
- Section padding: 96px top/bottom on desktop; 64px on tablet; 48px on mobile
- Grid gap: 24px between cards; 48px between major content blocks

## Elevation & Depth

Materiality is friendly-flat: solid surfaces, soft shadows, no glass or heavy blur. The signature elevation is a warm yellow halo — `0 4px 12px rgba(244, 215, 76, 0.15)` — that hints at the yellow brand without ever fighting the white ground. Card hovers lift 2px with a slightly deeper yellow glow; sticky notes get a tiny rotated shadow that mimics paper on whiteboard.

- Surface style: solid
- Blur: none
- Shadow ladder: xs · sm · md (yellow halo) · lg · xl · 2xl (deep yellow halo) · inner · focus (yellow ring)

## Shapes

- `radius.sm` 4px — sticky notes and tags
- `radius.md` 8px — buttons and inputs
- `radius.lg` 16px — cards and panels (the signature friendly-rounded)
- `radius.xl` 24px — large hero blocks and feature tiles
- `radius.full` — pill chips and avatar circles

## Motion

Motion is lively but never frantic — quick fades, gentle springs, and warm-yellow hover tints. Buttons lift on hover with a deeper yellow glow; sticky notes can wiggle 1–2° on drop; cards translate up 2px. A subtle `spring` easing reserves the bouncy feel for sticky-note interactions only.

- Level: lively
- Durations: 0 · 120 · 250 · 400 · 600 ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)`
- Spring easing (sticky drops): `cubic-bezier(0.34, 1.56, 0.64, 1)`
- Hover patterns: lift, scale, tint, glow
- Reduced motion: honored — all transforms collapse to opacity-only

## Techniques

### Miro-yellow CTA with warm halo
The signature Miro button — saturated yellow with deep-slate label and a warm yellow halo that intensifies on hover.
```css
.miro-cta {
  background: #F4D74C;
  color: #050038;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  letter-spacing: -0.01em;
  border: 0;
  border-radius: 8px;
  padding: 14px 24px;
  box-shadow: 0 4px 12px rgba(244, 215, 76, 0.35);
  transition: transform 250ms cubic-bezier(0.4,0,0.2,1),
              box-shadow 250ms cubic-bezier(0.4,0,0.2,1);
}
.miro-cta:hover {
  transform: translateY(-1px);
  background: #FAE266;
  box-shadow: 0 6px 18px rgba(244, 215, 76, 0.45);
}
```

### Sticky-note tile
A canonical Miro post-it: small rounded square, sticky-color fill, slight rotation, and a soft offset shadow to mimic paper on whiteboard.
```css
.sticky-note {
  display: inline-block;
  width: 144px;
  height: 144px;
  padding: 16px;
  background: #F4D74C;
  color: #050038;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 14px;
  line-height: 1.35;
  border-radius: 4px;
  transform: rotate(-2deg);
  box-shadow: 2px 4px 8px rgba(5, 0, 56, 0.12);
}
.sticky-note.pink  { background: #F472B6; color: #FFFFFF; }
.sticky-note.blue  { background: #3B82F6; color: #FFFFFF; transform: rotate(1.5deg); }
.sticky-note.green { background: #10B981; color: #FFFFFF; transform: rotate(-1deg); }
```

### Hand-drawn arrow divider
A whiteboard-style section divider rendered as a 1px deep-slate stroke with a tiny SVG arrowhead — the visual cue that says "Miro board," not "SaaS marketing page."
```css
.hand-arrow {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #050038;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
}
.hand-arrow::before {
  content: "";
  flex: 1;
  height: 1px;
  background: #050038;
  transform: translateY(0) skewY(-0.5deg);
}
.hand-arrow::after {
  content: "→";
  font-size: 18px;
  color: #050038;
  transform: rotate(-4deg);
}
```

## Iconography

Lucide line icons at 1.75px stroke, rendered in `text.primary` deep slate so they read as confident pen-marks rather than thin UI ornamentation. Sizes 16/20/24 px. For illustration and hero blocks, allow a hand-drawn flavor (slightly imperfect strokes, sketched arrows, circled callouts) — but never mix hand-drawn and lucide inside the same icon row.

- Treatment: linear
- Set: lucide
- Stroke: 1.75px (heavier than default to match the warm-friendly tone)

## Do's & Don'ts

### ✓ Do
- Use Miro-yellow `#F4D74C` as the single saturated anchor for CTAs and hero accents.
- Pair Miro-yellow with deep-slate `#050038` typography for maximum warmth and legibility.
- Treat hero blocks as whiteboard mockups: sticky notes, sketched arrows, circled callouts.
- Reserve the sticky-note rainbow (pink, blue, green, orange) for illustration and category tags — never for chrome.
- Keep type to Inter (or Manrope for display) — generous, friendly, never condensed.

### ✗ Don't
- Don't use serif primary type — Miro is modernist sans-serif with friendly warmth.
- Don't use cream or paper backgrounds — Miro is a pure-white digital tool.
- Don't fall into cold corporate-only feel — Miro is warm-friendly with hand-drawn illustration.
- Don't pastel the palette — Miro-yellow and sticky-note colors must stay saturated.
- Don't lean on generic "whiteboard" stereotype — use specific Miro vocabulary (sticky-note, post-it, Miro-yellow, warm-illustration).
- Don't use photographic-only heroes — Miro uses whiteboard-mockup illustration.

## Applications

This system fits remote-collaboration SaaS, workshop and brainstorming tools, agile-coach and design-sprint marketing, and any product that wants to say "humans sketching together" rather than "enterprise software." It's strongest in landing pages with whiteboard-mockup heroes, template-library galleries with sticky-note thumbnails, and dashboards where category tags borrow the sticky-note rainbow. Avoid it for luxury, editorial, or finance contexts — the saturated yellow and hand-drawn warmth will read as too playful.
