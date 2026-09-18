---
version: 1

meta:
  id: duolingo-2024
  name: Duolingo 2024
  description: Gamified learning in a candy-bright world of rounded owls, bouncy 3D buttons, and streak-guilting green.
  isDark: false
  tags: [playful, friendly, bold, tech]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2011 founded; 2023 major rebrand (Duo personality + bolder identity); current visual 2024"
  region: "Pittsburgh, Pennsylvania, USA"
  regionZh: "美国宾夕法尼亚州匹兹堡"
  keyFigures: [Luis von Ahn, Severin Hacker, Duolingo Design Team, Duo the Owl]
  movements: [Gamified education, Mascot-driven branding, Mobile-first design]

introduction: |
  Duolingo is gamification made adorable — a candy-bright world of rounded corners, thick outlines, and a green owl who will guilt-trip you into finishing your lesson. The 2023 rebrand cranked up the chaos: bolder Feather Green, chunkier geometry, and a mascot that went from friendly teacher to unhinged meme.

  Every surface feels like a toy. Buttons sit on thick bottom-shadows that beg to be pushed. Hearts, streaks, XP bars, and badges borrow directly from mobile gaming. The voice says: learn or Duo will find you — and somehow you keep coming back.
introductionZh: |
  Duolingo 把严肃的语言学习塞进了糖果色的手游外壳里——满屏的圆角、粗描边、一只绿色的猫头鹰 Duo 在你身后紧盯着连续打卡的火苗。2023 年品牌焕新后，整套视觉比以往更嚣张：羽毛绿更饱和、几何形更圆胖、Duo 也从温柔的老师变成了网络迷因本体。

  它的界面没有一处是冷冰冰的。按钮踩着厚厚的下边阴影，一按就"弹"下去；爱心是生命值、连胜是火焰、经验值像游戏进度条。每一次点击都伴随着 1.02 倍的轻微弹跳，像在玩一款永远不会通关的手机游戏——而这正是它让你停不下来的秘密。

colors:
  primary:
    "50":  "#F0FCE5"
    "100": "#D7F4BC"
    "200": "#B8EA8C"
    "300": "#95E05C"
    "400": "#79D635"
    "500": "#58CC02"
    "600": "#46A302"
    "700": "#377F02"
    "800": "#2A5F01"
    "900": "#1E4401"
    "950": "#0F2300"
  secondary:
    "50":  "#FFF9E0"
    "100": "#FFF0B3"
    "200": "#FFE680"
    "300": "#FFDC4D"
    "400": "#FFD21F"
    "500": "#FFC800"
    "600": "#CCA000"
    "700": "#997800"
    "800": "#665000"
    "900": "#332800"
    "950": "#1A1400"
  accent:
    "50":  "#E3F5FE"
    "100": "#BEE7FC"
    "200": "#8FD7FB"
    "300": "#5FC6F9"
    "400": "#3EBBF7"
    "500": "#1CB0F6"
    "600": "#0A8FCE"
    "700": "#086E9D"
    "800": "#064D6D"
    "900": "#032C3E"
    "950": "#021620"
  neutral:
    "50":  "#F7F7F7"
    "100": "#E5E5E5"
    "200": "#D4D4D4"
    "300": "#AFAFAF"
    "400": "#777777"
    "500": "#4B4B4B"
    "600": "#3C3C3C"
    "700": "#2D2D2D"
    "800": "#1E1E1E"
    "900": "#131313"
    "950": "#000000"
  semantic:
    success: { bg: "#58CC02", text: "#FFFFFF", light: "#D7F4BC", border: "#46A302" }
    warning: { bg: "#FFC800", text: "#4B4B4B", light: "#FFF0B3", border: "#CCA000" }
    error:   { bg: "#FF4B4B", text: "#FFFFFF", light: "#FFD6D6", border: "#E53838" }
    info:    { bg: "#1CB0F6", text: "#FFFFFF", light: "#BEE7FC", border: "#0A8FCE" }
  background:
    page:    "#235390"
    surface: "#FFFFFF"
    subtle:  "#F7F7F7"
  text:
    primary:   "#4B4B4B"
    secondary: "#777777"
    muted:     "#AFAFAF"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Nunito', 'Helvetica Neue', Arial, sans-serif"
    body:    "'Nunito', 'Helvetica Neue', Arial, sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', ui-monospace, monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap"
  scale:
    "2xs": "0.625rem"
    xs:    "0.75rem"
    sm:    "0.875rem"
    base:  "1rem"
    lg:    "1.125rem"
    xl:    "1.25rem"
    "2xl": "1.5rem"
    "3xl": "1.875rem"
    "4xl": "2.25rem"
    "5xl": "3rem"
    "6xl": "4rem"
    "7xl": "6rem"
  weights:
    light:     300
    normal:    400
    medium:    600
    semibold:  700
    bold:      800
    extrabold: 900
  lineHeights:
    tight:   1.2
    snug:    1.375
    normal:  1.5
    relaxed: 1.625
    loose:   1.8
  letterSpacing:
    tighter: "-0.04em"
    tight:   "-0.02em"
    normal:  "0"
    wide:    "0.05em"

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px",  md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "8px", md: "16px", lg: "20px", xl: "24px", full: "9999px" }
  color:  { default: "#E5E5E5", subtle: "#F7F7F7", strong: "#AFAFAF", focus: "#1CB0F6" }
  width:  { thin: "2px", default: "2px", thick: "3px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 2px 0 #E5E5E5"
  sm: "0 3px 0 #E5E5E5"
  md: "0 4px 0 #46A302"
  lg: "0 6px 0 #46A302"
  xl: "0 8px 0 #46A302, 0 12px 24px rgba(35,83,144,0.15)"
  "2xl": "0 10px 0 #46A302, 0 20px 40px rgba(35,83,144,0.20)"
  inner: "inset 0 2px 0 rgba(0,0,0,0.08)"
  focus: "0 0 0 4px rgba(28,176,246,0.35)"

motion:
  level: playful
  durations: { instant: "0ms", fast: "120ms", normal: "220ms", slow: "380ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [scale, lift, tint, glow]
  reducedMotion: true

composition:
  layout:        stack
  contentWidth:  container
  framing:       solid
  gridIntensity: subtle
  rhythm:        "4px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: filled
  set:       phosphor
  size:      { sm: "20px", md: "24px", lg: "32px" }
  stroke:    "2px"

components:
  button:
    primary:
      background:      "#58CC02"
      color:           "#FFFFFF"
      border:          "2px solid #58CC02"
      shadow:          "0 4px 0 #46A302"
      hoverBackground: "#61E002"
      hoverShadow:     "0 4px 0 #46A302"
      hoverColor:      "#FFFFFF"
    secondary:
      background:      "#FFFFFF"
      color:           "#1CB0F6"
      border:          "2px solid #E5E5E5"
      shadow:          "0 4px 0 #E5E5E5"
      hoverBackground: "#DDF4FF"
      hoverShadow:     "0 4px 0 #BEE7FC"
      hoverColor:      "#1CB0F6"
    ghost:
      background:      "transparent"
      color:           "#4B4B4B"
      border:          "2px solid transparent"
      shadow:          "none"
      hoverBackground: "#F7F7F7"
      hoverShadow:     "none"
      hoverColor:      "#4B4B4B"
    danger:
      background:      "#FF4B4B"
      color:           "#FFFFFF"
      border:          "2px solid #FF4B4B"
      shadow:          "0 4px 0 #E53838"
      hoverBackground: "#FF6363"
      hoverShadow:     "0 4px 0 #E53838"
      hoverColor:      "#FFFFFF"
    sizes:
      sm: { height: "40px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "48px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "56px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "16px"
    fontWeight:   800
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background:       "#FFFFFF"
    color:            "#4B4B4B"
    border:           "2px solid #E5E5E5"
    borderRadius:     "12px"
    padding:          "14px 16px"
    focusBorder:      "2px solid #1CB0F6"
    placeholderColor: "#AFAFAF"
  card:
    base:
      background:   "#FFFFFF"
      border:       "2px solid #E5E5E5"
      borderRadius: "16px"
      padding:      "24px"
      shadow:       "0 2px 0 #E5E5E5"
    hover:
      shadow:    "0 4px 0 #E5E5E5"
      transform: "translateY(-2px)"
---

# Duolingo 2024

> Gamified language learning rendered in candy-bright green, thick rounded outlines, and 3D push-buttons that dare you to skip a day.

## Origin

Duolingo was founded in 2011 in Pittsburgh, Pennsylvania by Luis von Ahn and Severin Hacker, born from von Ahn's earlier work on reCAPTCHA and the idea that machine translation could be crowdsourced through free language education. The app launched publicly in 2012 and grew from a quiet educational tool into one of the most recognizable mobile apps in the world, fueled by streak counters, experience points, and a mascot — Duo the owl — that became a cultural character in its own right.

The 2023 rebrand pushed Duolingo's visual language from "friendly edtech" into full gamified theatricality. Feather Green `#58CC02` became louder and more saturated, corner radii grew, borders thickened to 2–3px, and every interactive element was redrawn as a 3D push-button with a hard bottom-shadow. Duo himself was redesigned from a flat cartoon into an unhinged, meme-literate character. The 2024 interface inherits this legacy: toy-like, bouncy, unapologetically bold, and engineered to make missing a lesson feel emotionally unacceptable.

## Overview
Composition cues:
- **Layout**: single-column stacks, large tappable targets, hero illustrations center-stage
- **Content width**: container — roughly 640–960px max, mobile-first even on desktop
- **Framing**: solid white surfaces with thick rounded borders; no glass, no translucency
- **Grid intensity**: subtle — rhythm comes from spacing and repetition of pill-shaped modules, not grid lines

## Colors
Duolingo's palette is a children's game box applied to adult software. Feather Green dominates; Bee yellow, Cardinal blue, and Macaw red punctuate with full saturation. There are no dusty tones, no muted mid-tones — every color is bright, flat, and toy-like, sitting atop clean white surfaces or the signature deep blue `#235390` that Duolingo uses for onboarding and promo screens.

**Role usage**:
- Page background → `colors.background.page` (#235390 promo blue, or white for in-app)
- Primary surfaces → `colors.background.surface` (#FFFFFF)
- Primary actions (Continue, Check, Claim) → `colors.primary.500` (Feather Green)
- Streaks, XP, achievements → `colors.secondary.500` (Bee yellow)
- Skill nodes, info, progress → `colors.accent.500` (Cardinal blue)
- Hearts, errors, destructive → `colors.semantic.error` (Macaw red #FF4B4B)
- Body text on white → `colors.text.primary` (#4B4B4B, "Eel")
- Muted UI / helper text → `colors.text.secondary` (#777777, "Wolf")
- Text on blue background → `colors.text.inverse` (#FFFFFF)

## Typography
Nunito is the entire voice. Everything is rounded, bouncy, and built on bold weights — 700 for body emphasis, 800 for headings, 900 for heroic streak counters and XP numbers. Duolingo never uses thin or elegant typography; the letterforms must feel chunky enough to hold a mascot next to them without looking formal. Uppercase with wide tracking is reserved for button labels and badges.

**Text styles**:
- `display-xl` — Nunito, 96px, weight 900, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Nunito, 64px, weight 900, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Nunito, 36px, weight 800, line-height 1.15, letter-spacing -0.02em
- `heading-2` — Nunito, 28px, weight 800, line-height 1.2, letter-spacing -0.01em
- `heading-3` — Nunito, 20px, weight 800, line-height 1.3, letter-spacing 0
- `body-lg` — Nunito, 18px, weight 600, line-height 1.5, letter-spacing 0
- `body-md` — Nunito, 16px, weight 500, line-height 1.5, letter-spacing 0
- `button` — Nunito, 16px, weight 800, line-height 1.0, letter-spacing 0.05em, UPPERCASE
- `caption` — Nunito, 12px, weight 700, line-height 1.4, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 500, line-height 1.6

## Spacing & Layout
- Base unit: 4px; everything snaps to this rhythm
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 px
- Container: `md` 768px default; lessons feel tight at `sm` 640px; marketing stretches to `xl` 1280px
- Section padding: 32–128px vertical; generous breathing room between chunky modules
- Grid gap: 16px between cards in a lesson tree, 24px between marketing blocks

## Elevation & Depth
There is no glass, no haze, no ambient blur. Depth comes entirely from **hard offset shadows** — a 4–8px solid-color drop that mimics the edge of a physical button. Surfaces are candy-smooth and flat; the only "material" is the implication of a pushable plastic tile.

- Surface style: solid; no blur, no translucency
- Blur: none anywhere
- Shadow ladder is solid-color, not feathered:
  - `xs` — `0 2px 0 #E5E5E5` (resting card)
  - `sm` — `0 3px 0 #E5E5E5` (raised card)
  - `md` — `0 4px 0 #46A302` (primary button — the signature Duolingo push)
  - `lg` — `0 6px 0 #46A302` (large primary CTA)
  - `xl` — hard shadow + soft blue ambient for marketing heroes
- On press, the button translates down `translateY(4px)` and the shadow collapses to `0 0 0 #46A302` — that's the "clunk."

## Shapes
- Radii: 8 / 16 / 20 / 24 / 9999 px
- 16px is the default for buttons, inputs, and cards (`borders.radius.md`)
- Tags, streak flame containers, avatar frames, and skill node buttons are fully circular (`radius.full`)
- No sharp 0px corners anywhere — even code blocks get 8px

## Motion
Motion is theatrical and playful. Everything bounces. Success events trigger confetti, streak animations, and Duo reactions. Hover states are the "Duo bounce": a 1.02–1.05x scale with a spring easing that overshoots slightly before settling. Press states are the hard "clunk" — the button translates down the exact height of its shadow.

- Level: playful
- Durations: fast 120ms (hover), normal 220ms (standard), slow 380ms (modal enter), slower 600ms (streak celebration)
- Easings: spring `cubic-bezier(0.34, 1.56, 0.64, 1)` is the house easing — overshoots to feel bouncy
- Hover patterns: scale (1.02–1.05x), lift (−2px), tint (background brightens ~8%), glow (colored drop-shadow on icons)
- Respects `prefers-reduced-motion` — scales drop to 1.0, shadows still hard but no translate

## Techniques

### 3D Push Button
The Duolingo signature — every primary action sits on a hard bottom-shadow the exact color of its 600-shade. On press, it "clunks" down by translating Y and collapsing the shadow.

```css
.duo-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  padding: 0 24px;
  background: #58CC02;
  color: #FFFFFF;
  border: 2px solid #58CC02;
  border-radius: 16px;
  box-shadow: 0 4px 0 #46A302;
  font-family: 'Nunito', sans-serif;
  font-weight: 800;
  font-size: 16px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer;
  transition: transform 120ms cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 120ms ease,
              background 120ms ease;
}

.duo-button:hover {
  background: #61E002;
  transform: translateY(-1px);
  box-shadow: 0 5px 0 #46A302;
}

.duo-button:active {
  transform: translateY(4px);
  box-shadow: 0 0 0 #46A302;
}
```

### Streak Flame Badge
The gamified status pill — a rounded container with a thick border, bold number, and emoji-style flame that subtly pulses to draw the eye.

```css
.duo-streak {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: #FFF0B3;
  border: 2px solid #FFC800;
  border-radius: 9999px;
  box-shadow: 0 2px 0 #CCA000;
  font-family: 'Nunito', sans-serif;
  font-weight: 900;
  font-size: 18px;
  color: #4B4B4B;
}

.duo-streak::before {
  content: "🔥";
  font-size: 20px;
  animation: duo-flicker 1.2s ease-in-out infinite;
  transform-origin: bottom center;
}

@keyframes duo-flicker {
  0%, 100% { transform: scale(1) rotate(-2deg); }
  50%      { transform: scale(1.08) rotate(2deg); }
}
```

### Progress Arc Bar
The lesson progress indicator — a chunky rounded pill with an inner fill that animates with a spring ease, mirroring the bouncy personality of the app.

```css
.duo-progress {
  position: relative;
  height: 16px;
  background: #E5E5E5;
  border-radius: 9999px;
  overflow: hidden;
}

.duo-progress__fill {
  height: 100%;
  width: var(--progress, 40%);
  background: linear-gradient(180deg, #79D635 0%, #58CC02 100%);
  border-radius: 9999px;
  box-shadow: inset 0 3px 0 rgba(255, 255, 255, 0.35);
  transition: width 380ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Iconography
Icons are filled, chunky, and unapologetically kid-friendly — Phosphor Fill or custom illustrations in the Duolingo house style. They frequently sit inside circular colored wells (skill nodes), and the mascot Duo himself is the loudest icon of all. Strokes, when used, are thick (2px minimum) to match the border weight of buttons and cards.

- Treatment: filled by default; linear only for tertiary UI
- Set: Phosphor (Fill) or custom Duolingo illustrations
- Stroke: 2px when outlined; otherwise solid-fill shapes with generous corner radii

## Do's & Don'ts
### ✓ Do
- Use Feather Green `#58CC02` for every primary call-to-action — Continue, Check, Claim, Start Lesson.
- Give every interactive surface a hard-offset `0 4px 0 <shade-600>` shadow to create the pushable 3D feel.
- Pair bold Nunito 800/900 headings with colorful filled icons or the Duo mascot to keep the tone playful.
- Make hover states bouncy — scale 1.02–1.05x with spring easing, never a flat fade.
- Round everything to 16px minimum; pills and circles for anything playful like streaks and badges.

### ✗ Don't
- Don't use serif fonts — Duolingo is purely rounded sans.
- Don't build dark, moody palettes — this brand lives in candy-bright saturation.
- Don't use sharp 0px corners; every surface must be rounded.
- Don't reach for elegant or luxurious aesthetics; this is a toy, not a boutique.
- Don't set thin type weights — 600 minimum, 800 for headings, 900 for display numbers.
- Don't dull the colors with muted or desaturated tones; keep hexes at full saturation.

## Applications
Best for language learning, edtech, children's apps, gamified onboarding, habit trackers, fitness streak apps, and any consumer product where engagement loops, mascots, and cheerful reward mechanics are central to the experience. Especially strong for mobile-first interfaces, marketing pages that need to feel fun and approachable, and any UI that benefits from making micro-interactions feel like small celebrations.
