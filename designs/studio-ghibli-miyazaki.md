---
version: 1

meta:
  id: studio-ghibli-miyazaki
  name: Studio Ghibli (Miyazaki)
  description: Hand-painted wonder — watercolor skies, meadow greens, and luminous warmth from Miyazaki's hand-drawn world.
  isDark: false
  tags: [organic, friendly, narrative, decorative, hand-drawn, warm]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1985 founded; visual language peak 1988–2001; ongoing through 2023"
  region: "Koganei, Tokyo, Japan"
  regionZh: "日本东京小金井市"
  keyFigures: [Hayao Miyazaki, Isao Takahata, Kazuo Oga, Joe Hisaishi]
  movements: [Japanese animation, watercolor background painting, hand-drawn anti-CGI philosophy]

introduction: |
  Studio Ghibli's visual world is a hand-painted one — watercolor skies drift over meadow greens, and every frame looks like a painting you could step inside. Founded by Hayao Miyazaki and Isao Takahata in 1985, the studio built its style around Kazuo Oga's luminous background paintings for *My Neighbor Totoro* (1988) and *Spirited Away* (2001).

  This design system translates that painterly warmth into interface language: soft cumulus blues, lush green landscapes, sunset orange accents, and warm paper surfaces. Typography leans literary and hand-touched; geometry is rounded and organic. The design says: slow down and notice the clouds.

introductionZh: |
  吉卜力工作室的视觉世界是手绘的 —— 水彩的天空漂浮在翠绿的原野之上，每一帧画面都像一幅可以走进去的画。1985 年，宫崎骏与高畑勋在东京小金井创立工作室，由美术监督男鹿和雄以水彩笔触绘就的《龙猫》（1988）与《千与千寻》（2001）背景画，奠定了这一视觉语言。

  这套设计系统把那份画笔的温度翻译为界面语汇：柔和的积雨云蓝、丰饶的草甸绿、夕阳橘的点缀，以及温润的米纸底色。字体是文学而带手写感的 Cormorant Garamond 与 Lora，辅以 Caveat 的手写笔记气质；形体圆润、有机，没有尖锐的棱角。它想对你说的是：慢下来，抬头看看云。

colors:
  primary:
    "50":  "#EEF7EE"
    "100": "#D6ECD6"
    "200": "#AFD8AF"
    "300": "#87C387"
    "400": "#65AE65"
    "500": "#4A9B4A"
    "600": "#3D823D"
    "700": "#326832"
    "800": "#275027"
    "900": "#1D3B1D"
    "950": "#112411"
  secondary:
    "50":  "#EEF7FC"
    "100": "#D6ECF6"
    "200": "#B2DBEE"
    "300": "#87CEEB"
    "400": "#6FB9E0"
    "500": "#5BA3D9"
    "600": "#4585BC"
    "700": "#366C9A"
    "800": "#2A5578"
    "900": "#1F3F59"
    "950": "#122636"
  accent:
    "50":  "#FDF3EC"
    "100": "#FAE2D1"
    "200": "#F4C3A4"
    "300": "#EFAA85"
    "400": "#EBA078"
    "500": "#E8956A"
    "600": "#D17650"
    "700": "#AC5C3F"
    "800": "#854531"
    "900": "#5E3122"
    "950": "#371C13"
  neutral:
    "50":  "#FAF7F1"
    "100": "#F5F0E8"
    "200": "#E8E0D2"
    "300": "#D3C7B4"
    "400": "#B0A088"
    "500": "#8B7B64"
    "600": "#6B5E50"
    "700": "#514739"
    "800": "#3A3028"
    "900": "#26201B"
    "950": "#14100D"
  semantic:
    success: { bg: "#EEF7EE", text: "#275027", light: "#D6ECD6", border: "#AFD8AF" }
    warning: { bg: "#FBEFD8", text: "#7A5418", light: "#F7E1B8", border: "#E8C788" }
    error:   { bg: "#F8E2DA", text: "#7A3322", light: "#F0C9BB", border: "#D99A85" }
    info:    { bg: "#EEF7FC", text: "#2A5578", light: "#D6ECF6", border: "#87CEEB" }
  background:
    page:    "#F5F0E8"
    surface: "#FFFFFF"
    subtle:  "#FAF7F1"
  text:
    primary:   "#3A3028"
    secondary: "#6B5E50"
    muted:     "#8B7B64"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Cormorant Garamond', 'Noto Serif JP', Georgia, serif"
    body:    "'Lora', 'Noto Serif JP', Georgia, serif"
    mono:    "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Caveat:wght@400;500;600;700&family=Noto+Serif+JP:wght@400;500;700&display=swap"
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
  radius: {none: "0", sm: "6px", md: "12px", lg: "16px", xl: "24px", full: "9999px"}
  color:  {default: "#E8E0D2", subtle: "#F5F0E8", strong: "#D3C7B4", focus: "#5BA3D9"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(58, 48, 40, 0.05)"
  sm: "0 1px 3px rgba(58, 48, 40, 0.06), 0 1px 2px rgba(58, 48, 40, 0.04)"
  md: "0 2px 12px rgba(0, 0, 0, 0.08)"
  lg: "0 8px 24px rgba(58, 48, 40, 0.10), 0 2px 6px rgba(58, 48, 40, 0.06)"
  xl: "0 16px 40px rgba(58, 48, 40, 0.12), 0 4px 12px rgba(58, 48, 40, 0.06)"
  "2xl": "0 32px 64px rgba(58, 48, 40, 0.16)"
  inner: "inset 0 1px 2px rgba(58, 48, 40, 0.05)"
  focus: "0 0 0 3px rgba(91, 163, 217, 0.35)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "160ms", normal: "280ms", slow: "440ms", slower: "680ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.55, 0, 1, 0.45)"
    out:     "cubic-bezier(0, 0.55, 0.45, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, glow]
  reducedMotion: true

composition:
  layout:        stack
  contentWidth:  container
  framing:       solid
  gridIntensity: soft
  rhythm:        "8px"

surfaceStyle: layered
blur:         "12px"

iconography:
  treatment: linear
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "#4A9B4A"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 2px 8px rgba(74, 155, 74, 0.25)"
      hoverBackground: "#3D823D"
      hoverShadow: "0 4px 16px rgba(74, 155, 74, 0.30)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "#FFFFFF"
      color: "#3A3028"
      border: "1px solid #D3C7B4"
      shadow: "0 1px 3px rgba(58, 48, 40, 0.06)"
      hoverBackground: "#FAF7F1"
      hoverShadow: "0 2px 8px rgba(58, 48, 40, 0.08)"
      hoverColor: "#3A3028"
    ghost:
      background: "transparent"
      color: "#4A9B4A"
      border: "none"
      shadow: "none"
      hoverBackground: "rgba(74, 155, 74, 0.08)"
      hoverShadow: "none"
      hoverColor: "#3D823D"
    danger:
      background: "#D99A85"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 2px 8px rgba(217, 154, 133, 0.25)"
      hoverBackground: "#AC5C3F"
      hoverShadow: "0 4px 16px rgba(172, 92, 63, 0.30)"
      hoverColor: "#FFFFFF"
    sizes:
      sm: {height: "32px", padding: "0 12px", fontSize: "0.875rem"}
      md: {height: "40px", padding: "0 20px", fontSize: "1rem"}
      lg: {height: "48px", padding: "0 28px", fontSize: "1.125rem"}
    borderRadius: "16px"
    fontWeight: 500
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#3A3028"
    border: "1px solid #D3C7B4"
    borderRadius: "12px"
    padding: "10px 14px"
    focusBorder: "1px solid #5BA3D9"
    placeholderColor: "#8B7B64"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid #E8E0D2"
      borderRadius: "12px"
      padding: "24px"
      shadow: "0 2px 12px rgba(0, 0, 0, 0.08)"
    hover:
      shadow: "0 8px 24px rgba(58, 48, 40, 0.10), 0 2px 6px rgba(58, 48, 40, 0.06)"
      transform: "translateY(-2px)"
---

# Studio Ghibli (Miyazaki)

> Hand-painted wonder — watercolor skies, meadow greens, and Miyazaki's quiet conviction that the world is beautiful.

## Origin

Studio Ghibli was founded in 1985 in Koganei, on the western edge of Tokyo, by Hayao Miyazaki, Isao Takahata, and producer Toshio Suzuki, after the success of *Nausicaä of the Valley of the Wind* (1984). From the opening cumulus of *My Neighbor Totoro* (1988) onward, the studio's look was shaped above all by background art director Kazuo Oga, whose watercolor landscapes — sunlit rice fields, drifting clouds, mossy forests — became the visual DNA of Ghibli's world. Composer Joe Hisaishi's scores gave that world its breath.

The studio's painterly peak spans *Princess Mononoke* (1997), *Spirited Away* (2001, Academy Award for Best Animated Feature), and *Howl's Moving Castle* (2004), continuing through *The Boy and the Heron* (2023). Miyazaki's refusal to move to CGI kept every frame hand-drawn, hand-painted, and unmistakably human. The Ghibli Museum in Mitaka and Ghibli Park (2022) extend that hand-drawn worldview into architecture and exhibit design.

## Overview

Composition cues:
- **Layout**: vertical stack, painterly scenes stacked like film storyboards — sky, midground, foreground
- **Content width**: `container` (1280px max), generously gutter-padded
- **Framing**: solid, paper-like surfaces with soft warm shadows — never hard glass or sharp bevels
- **Grid intensity**: soft — the grid is implied by rhythm and whitespace, not by visible rules

## Colors

The palette is a watercolor pigment box: Ghibli cumulus blue from sky (`#87CEEB`) to deeper blue (`#5BA3D9`) for the signature sky wash, meadow green (`#4A9B4A`) for living landscape, sunset orange (`#E8956A`) for magic-hour warmth, and warm paper (`#F5F0E8`) as the canvas. Text is a warm dark brown (`#3A3028`) rather than black — ink on washi, never pure digital black. Every stop leans slightly warm, as if sun-soaked.

**Role usage**:
- Page background → `colors.background.page` (`#F5F0E8` warm paper)
- Surface / card → `colors.background.surface` (`#FFFFFF`)
- Hero sky wash → gradient of `secondary.300 → secondary.500`
- Primary action / nature motif → `colors.primary.500` (meadow green)
- Secondary / link → `colors.secondary.500` (sky blue)
- Accent / highlight / call-to-wonder → `colors.accent.500` (sunset orange)
- Primary text → `colors.text.primary` (warm dark brown)
- Supporting text → `colors.text.secondary`

## Typography

Type is warm and literary, never sterile tech. Headlines use **Cormorant Garamond** — a revived Garamond with high contrast and expressive italics that echoes the brushed Japanese calligraphy on Ghibli posters. Body copy uses **Lora**, a warm, slightly calligraphic serif that reads like a storybook. **Caveat** handles signatures, marginalia, and "notebook" touches that evoke Miyazaki's working sketches. In Japanese contexts, **Noto Serif JP** pairs seamlessly at the same weight. Tracking is mostly relaxed; headlines allow slight negative tracking to settle the form.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 600, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Cormorant Garamond, 64px, weight 600, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Cormorant Garamond, 48px, weight 600, line-height 1.2, letter-spacing -0.02em
- `heading-2` — Cormorant Garamond, 36px, weight 500, line-height 1.25, letter-spacing -0.01em
- `heading-3` — Cormorant Garamond, 24px, weight 500, line-height 1.3, letter-spacing 0
- `body-lg` — Lora, 18px, weight 400, line-height 1.7, letter-spacing 0
- `body-md` — Lora, 16px, weight 400, line-height 1.625, letter-spacing 0
- `caption` — Lora italic, 14px, weight 400, line-height 1.5, letter-spacing 0
- `hand` — Caveat, 22px, weight 500, line-height 1.3 (margin notes and signatures)
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit **4px**; 8px rhythm for most vertical flow
- Scale: 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128 px — generous steps, never cramped
- Container max **1280px**, comfortable gutters (24–48px)
- Section padding **96px desktop / 64px tablet / 32px mobile** — landscapes need room to breathe
- Grid gaps lean wide (`lg: 24px`, `xl: 48px`) so cards feel like separate paintings

## Elevation & Depth

Surfaces are layered like watercolor planes — foreground foliage over midground hills over distant sky. Depth comes from soft warm shadows and overlapping translucent washes, not sharp drop shadows or glass blur. Shadows are tinted toward `#3A3028` (warm brown ink) rather than neutral black, so they feel sun-warmed rather than synthetic.

- Surface style: **layered** — multiple overlapping paper-like planes
- Blur: `12px` used sparingly, e.g. atmospheric cloud overlays at section boundaries
- Shadow ladder: `xs` (hairline lift) → `sm` (paper lift) → `md` (card signature, `0 2px 12px rgba(0,0,0,0.08)`) → `lg` (floating panel) → `xl` (modal) → `2xl` (hero mist)
- Focus ring uses sky-blue alpha for a gentle, non-harsh halo

## Shapes

- Corner radii lean rounded and friendly: `sm 6px`, `md 12px` (cards), `lg 16px` (buttons), `xl 24px` (hero panels)
- `full 9999px` for avatars, pills, and circular illustrations (clouds, Totoro silhouettes)
- Prefer continuous curves — no sharp 2px radii or knife-edge corners

## Motion

Motion is gentle and wind-driven, like a breeze moving through leaves. Everything drifts into place rather than snapping; springs are soft, never bouncy. Hovers raise surfaces a couple pixels, tint gently, or pulse a warm glow. Nothing should feel mechanical or tech-y.

- Level: **restrained**
- Durations: `fast 160ms`, `normal 280ms`, `slow 440ms`, `slower 680ms` (for ambient cloud drift)
- Easings: default ease-in-out; `spring` for playful elements (Totoro bounce, leaf fall); `out` for entrances
- Hover patterns: **lift** (translateY -2px), **tint** (soft overlay), **glow** (warm halo)
- Honor `prefers-reduced-motion`: reduce drift/floating loops to static

## Techniques

### Watercolor sky gradient hero
Signature Ghibli cumulus-sky wash used behind hero content, with a soft paper-edge fade at the bottom so foreground art settles onto the page.
```css
.ghibli-sky {
  background:
    radial-gradient(ellipse 80% 50% at 20% 30%, rgba(255,255,255,0.8), transparent 60%),
    radial-gradient(ellipse 60% 40% at 75% 40%, rgba(255,255,255,0.6), transparent 55%),
    linear-gradient(180deg, #87CEEB 0%, #5BA3D9 65%, #F5F0E8 100%);
  position: relative;
}
.ghibli-sky::after {
  content: "";
  position: absolute;
  inset: auto 0 0 0;
  height: 120px;
  background: linear-gradient(180deg, transparent, #F5F0E8);
  pointer-events: none;
}
```

### Watercolor-edged paper card
A card that looks hand-torn and laid on paper — subtle grain, warm ink shadow, soft inner light.
```css
.ghibli-card {
  background:
    radial-gradient(ellipse at top left, rgba(255,255,255,0.9), transparent 60%),
    #FFFFFF;
  border: 1px solid #E8E0D2;
  border-radius: 12px;
  padding: 24px;
  box-shadow:
    0 2px 12px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  background-image:
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='0.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 0.23  0 0 0 0 0.19  0 0 0 0 0.16  0 0 0 0.04 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>"),
    radial-gradient(ellipse at top left, rgba(255,255,255,0.9), transparent 60%),
    linear-gradient(#FFFFFF, #FFFFFF);
}
```

### Drifting cloud accent
Slow, ambient motion for hero backgrounds — soft white shapes drifting across the sky wash, disabled under reduced-motion.
```css
@keyframes drift {
  0%   { transform: translateX(-10%); opacity: 0.7; }
  50%  { opacity: 0.9; }
  100% { transform: translateX(110%); opacity: 0.7; }
}
.ghibli-cloud {
  position: absolute;
  width: 240px;
  height: 80px;
  border-radius: 9999px;
  background: radial-gradient(ellipse at center, rgba(255,255,255,0.95), rgba(255,255,255,0) 70%);
  filter: blur(2px);
  animation: drift 40s linear infinite;
}
@media (prefers-reduced-motion: reduce) {
  .ghibli-cloud { animation: none; }
}
```

## Iconography

Linear, rounded, hand-touched. Prefer **Phosphor** (regular or duotone at 1.5px stroke) for its friendly continuous curves; supplement with custom hand-drawn SVGs for narrative motifs (leaf, cloud, acorn, soot sprite). Never use square-cornered or mechanical enterprise iconography.

- Treatment: `linear` with occasional duotone fills in accent orange
- Set: `phosphor` with custom narrative icons
- Stroke: `1.5px` rounded caps and joins

## Do's & Don'ts

### ✓ Do
- Use meadow green (`#4A9B4A`) for primary actions and nature motifs.
- Set hero backgrounds to the Ghibli sky gradient (`#87CEEB` → `#5BA3D9`).
- Write copy in a literary, slow voice — short paragraphs of Lora, with Caveat margin notes.
- Give every section generous whitespace so landscapes can breathe.
- Prefer warm brown text (`#3A3028`) over pure black; warm shadows over neutral gray.

### ✗ Don't
- Introduce sharp geometric shapes or knife-edge corners.
- Use dark or moody palettes; Ghibli light is always luminous and warm.
- Adopt industrial or brutalist aesthetics.
- Use neon, fluorescent, or artificial colors.
- Set UI type in modern tech sans-serif like Inter or Geist.
- Render surfaces as flat matte — always hint at depth and luminosity.
- Use pixel, glitch, or overtly digital effects.

## Applications

Best for storytelling products where warmth matters more than throughput: travel journals, bookshops, children's publishing, ecological nonprofits, slow-living blogs, creative studios, museum sites, and illustrated portfolios. It also suits brand microsites that want to evoke craft and handwork — bakeries, ceramicists, nurseries, film retrospectives — anywhere the design should make the reader look up and notice the clouds.
