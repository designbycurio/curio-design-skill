---
version: 1

meta:
  id: spotify-rainbow-wrap-2023
  name: Spotify Wrapped 2023
  description: Saturated pink-orange gradient cards designed to be screenshotted and shared on every story feed
  isDark: true
  tags: [bold, playful, experimental, retro, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2016–present; 2023 edition is the visual peak"
  region: "Stockholm / New York City / Global"
  regionZh: "瑞典斯德哥尔摩 / 美国纽约 / 全球"
  keyFigures: [Rasmus Wängelin, Marisa Gallagher]
  movements: [Year-in-review marketing, Instagram Story design, social-shareable data art]

introduction: |
  Spotify Wrapped 2023 turned a data dump into a cultural moment. Every December, hundreds of millions of users shared their listening stats on social media — not because the numbers were interesting, but because the design made them feel like concert posters. The "Sound Town" / "Me in 2023" edition pushed saturated pink-coral-orange gradients, chunky display type, and sticker-style character illustrations into a mobile-first story format that the entire internet tried to copy.

  The design system works because it treats every card as a shareable artifact. Huge stat numbers, full-bleed gradients, and playful illustration collages are optimized for the 9:16 story aspect ratio. Nothing is subtle — every element is built to survive thumbnail compression on a social feed.
introductionZh: |
  Spotify Wrapped 2023 把年度听歌数据变成了一场全民参与的视觉盛事。每年十二月，数亿用户自发地把自己的听歌总结分享到社交媒体——吸引人的不是数字本身，而是那套让统计数据看起来像演唱会海报的设计语言。"Sound Town"/"Me in 2023"版本把高饱和粉橙渐变、超粗标题字体和贴纸风格角色插画推到了极致，整套移动端卡片经过精密优化，就是为了在 9:16 的竖屏故事流中被截图、被传播。

  这套设计系统的核心逻辑是：每一张卡片都是一件可分享的社交货币。巨大的数据数字、满屏渐变色块和拼贴式插画——所有元素都经过缩略图级别的极限测试，确保在社交信息流中依然抢眼。

colors:
  primary:    {"50": "#FFF0F7", "100": "#FFD6EB", "200": "#FFB3DE", "300": "#FF8ACE", "400": "#FF52B5", "500": "#FF1493", "600": "#E0117F", "700": "#B80D67", "800": "#8F0A50", "900": "#66073A", "950": "#3D0423"}
  secondary:  {"50": "#FFF5ED", "100": "#FFE5D1", "200": "#FFD0AB", "300": "#FFBB85", "400": "#FFA552", "500": "#FFA552", "600": "#E08A3A", "700": "#B86E2A", "800": "#8F551F", "900": "#663D16", "950": "#3D240D"}
  accent:     {"50": "#E8FFF0", "100": "#C3FFD9", "200": "#8DFBB5", "300": "#57ED8F", "400": "#2FD96E", "500": "#1DB954", "600": "#18A048", "700": "#13833B", "800": "#0E662E", "900": "#094A21", "950": "#052E14"}
  neutral:    {"50": "#F5F5F5", "100": "#E5E5E5", "200": "#CCCCCC", "300": "#B3B3B3", "400": "#999999", "500": "#666666", "600": "#535353", "700": "#404040", "800": "#2A2A2A", "900": "#1A1A1A", "950": "#0D0D0D"}
  semantic:
    success: { bg: "#1DB954", text: "#FFFFFF", light: "#E8FFF0", border: "#18A048" }
    warning: { bg: "#FFA552", text: "#3D240D", light: "#FFF5ED", border: "#E08A3A" }
    error:   { bg: "#FF4444", text: "#FFFFFF", light: "#FFE5E5", border: "#CC3636" }
    info:    { bg: "#5BC0EB", text: "#0A2E3D", light: "#E5F5FC", border: "#4A9EC2" }
  background:
    page:    "#000000"
    surface: "#1A1A1A"
    subtle:  "#2A2A2A"
  text:
    primary:   "#FFFFFF"
    secondary: "#B3B3B3"
    muted:     "#666666"
    inverse:   "#000000"

typography:
  families:
    heading: "'Inter', 'Helvetica Neue', sans-serif"
    body:    "'Inter', 'Helvetica Neue', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap"
  scale: {"2xs": "0.625rem", xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.125rem", xl: "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800}
  lineHeights: {tight: 1.0, snug: 1.1, normal: 1.4, relaxed: 1.6, loose: 1.8}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "8px", md: "16px", lg: "24px", xl: "32px", full: "9999px"}
  color:  {default: "#2A2A2A", subtle: "#1A1A1A", strong: "#FFFFFF", focus: "#FF1493"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 3px rgba(0,0,0,0.3)"
  sm: "0 2px 8px rgba(0,0,0,0.4)"
  md: "0 8px 32px rgba(255, 20, 147, 0.3)"
  lg: "0 12px 48px rgba(255, 20, 147, 0.4)"
  xl: "0 20px 64px rgba(255, 20, 147, 0.5)"
  "2xl": "0 32px 80px rgba(255, 20, 147, 0.6)"
  inner: "inset 0 2px 4px rgba(0,0,0,0.3)"
  focus: "0 0 0 3px rgba(255, 20, 147, 0.5)"

motion:
  level: "playful"
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "350ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.2, 0, 0, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [scale, glow, tint, lift]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "full-bleed"
  framing:       "solid"
  gridIntensity: "none"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "20px"

iconography:
  treatment: "filled"
  set:       "phosphor"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "linear-gradient(135deg, #FF1493, #FFA552)", color: "#FFFFFF", border: "none", shadow: "0 8px 32px rgba(255, 20, 147, 0.3)", hoverBackground: "linear-gradient(135deg, #E0117F, #E08A3A)", hoverShadow: "0 12px 48px rgba(255, 20, 147, 0.5)", hoverColor: "#FFFFFF"}
    secondary: {background: "#1A1A1A", color: "#FFFFFF", border: "2px solid #FFFFFF", shadow: "none", hoverBackground: "#2A2A2A", hoverShadow: "0 8px 32px rgba(255,255,255,0.1)", hoverColor: "#FFFFFF"}
    ghost:     {background: "transparent", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "rgba(255,255,255,0.1)", hoverShadow: "none", hoverColor: "#FFFFFF"}
    danger:    {background: "#FF4444", color: "#FFFFFF", border: "none", shadow: "0 4px 16px rgba(255,68,68,0.3)", hoverBackground: "#CC3636", hoverShadow: "0 8px 32px rgba(255,68,68,0.4)", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "36px", padding: "0 16px", fontSize: "0.875rem"}, md: {height: "44px", padding: "0 24px", fontSize: "1rem"}, lg: {height: "56px", padding: "0 32px", fontSize: "1.125rem"}}
    borderRadius: "9999px"
    fontWeight: 700
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#1A1A1A"
    color: "#FFFFFF"
    border: "2px solid #2A2A2A"
    borderRadius: "9999px"
    padding: "12px 20px"
    focusBorder: "2px solid #FF1493"
    placeholderColor: "#666666"
  card:
    base:  {background: "#1A1A1A", border: "none", borderRadius: "24px", padding: "24px", shadow: "0 8px 32px rgba(0,0,0,0.4)"}
    hover: {shadow: "0 12px 48px rgba(255, 20, 147, 0.3)", transform: "translateY(-4px)"}
---

# Spotify Wrapped 2023

> The year-end marketing event that made every other consumer brand jealous of a music app's design system.

## Origin

Spotify Wrapped started in 2016 as a year-end listening recap, but the 2023 "Sound Town" / "Me in 2023" edition represents its visual apex. Spotify Design in Stockholm and NYC, working with agency M ss ng P eces, shipped a story-format mobile experience drenched in saturated pink-orange-coral gradients, chunky display typography, and character illustrations — building an annual visual identity that the entire internet tries to replicate every December.

The design borrows from Y2K poster art, 1990s rave flyers, and the Instagram Story template ecosystem, but wraps it all into a coherent system optimized for one purpose: cards you screenshot and share. Every element — from the massive stat callouts to the sticker-style badges — is designed to survive thumbnail compression in a 9:16 social feed. The result is a design language so recognizable that "Wrapped season" has become a cultural event independent of the data it presents.

## Overview
Composition cues:
- **Layout**: Vertical story stack — each card is a full-bleed 9:16 viewport
- **Content width**: Full-bleed — gradients and type run edge to edge
- **Framing**: Solid gradient blocks with sticker-style white-bordered elements floating on top
- **Grid intensity**: None — deliberately unstructured, collage-style placement

## Colors
The Wrapped 2023 palette is aggressively warm and saturated. Hot Pink (#FF1493) and Sunset Orange (#FFA552) dominate as the year's signature gradient pair, creating a thermal glow across every card. The black page background (#000000) acts as a void that makes gradient blocks punch harder. Spotify Green (#1DB954) is relegated to accent duty — logos and secondary badges only. Bonus pop colors like Electric Lime (#D6FF1F) and Sky (#5BC0EB) appear in data visualizations and callout badges. There is no tasteful restraint here — every color is dialed to maximum saturation.

**Role usage**:
- Page background → `colors.background.page` (#000000 void canvas)
- Gradient hero blocks → `colors.primary.500` to `colors.secondary.500` (pink-to-orange)
- Body text and stat numbers → `colors.text.primary` (#FFFFFF)
- Spotify logo and accent badges → `colors.accent.500` (#1DB954)
- Supporting text → `colors.text.secondary` (#B3B3B3)
- Card surfaces → `colors.background.surface` (#1A1A1A)
- Pop color callouts → Electric Lime (#D6FF1F) or Sky (#5BC0EB)
- Sticker borders → `colors.text.primary` (#FFFFFF thick stroke)

## Typography
The type voice is loud, chunky, and unapologetic. Headlines set in Inter at weight 900 (or Bebas Neue for extra-condensed stat callouts) dominate every card with aggressive sizing — stat numbers often fill half the viewport. Tracking is tight, line-height is compressed, and occasional outlined or 3D-extruded treatments add a Y2K poster dimension. Body text in Inter at regular weight stays clean and readable against gradient backgrounds. The overall effect is a design system that treats type as graphic element first and readable text second.

**Text styles**:
- `display-xl` — Inter, 96px, weight 900, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Inter, 72px, weight 900, line-height 1.0, letter-spacing -0.04em
- `heading-1` — Inter, 48px, weight 800, line-height 1.1, letter-spacing -0.02em
- `body-lg` — Inter, 18px, weight 400, line-height 1.5, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 12px, weight 500, line-height 1.4, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.6, letter-spacing 0
- `stat-xl` — Bebas Neue, 120px, weight 400, line-height 0.9, letter-spacing -0.02em

## Spacing & Layout
- Base unit: 8px rhythm for all component spacing
- Scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128
- Container: max-width rarely used — full-bleed is the default
- Section padding: 32px mobile, 64px tablet, 96px desktop
- Cards stack vertically with 16–24px gap in story flow
- Internal card padding: 24–32px

## Elevation & Depth
Depth comes from two sources: the black void behind gradient blocks, and colored glow shadows beneath floating elements. There is no frosted glass or blur transparency — surfaces are opaque and layered like stickers on a laptop lid. The pink glow shadow (rgba(255, 20, 147, 0.3)) is the signature depth cue, making cards and buttons feel like they radiate light.

- Surface style: Solid opaque blocks on black canvas
- Blur: 20px reserved for ambient glow effects, not glass
- Shadow ladder: xs (subtle dark) → md (pink glow 0.3) → xl (pink glow 0.5) → 2xl (intense pink glow 0.6)
- Sticker elements get a soft drop shadow with white border for "peeled off" feel

## Shapes
- Cards: 24px radius — large, friendly, sticker-like
- Buttons: 9999px (full pill) — Instagram sticker aesthetic
- Badges and tags: 9999px pill
- Stat callout blocks: 16px radius
- Avatar/album art frames: 8px radius or full circle
- No sharp corners anywhere — everything feels soft and approachable

## Motion
Motion is playful and bouncy — cards scale in with spring easing, numbers count up with overshoot, and hover states feel tactile. Nothing moves slowly or elegantly. The overall tempo matches the energy of scrolling through story slides: quick, punchy, and rewarding. Transitions use a custom spring curve that overshoots slightly before settling, giving everything a rubber-band quality.

- Level: playful
- Durations: fast 100ms (micro), normal 200ms (transitions), slow 350ms (card entrances), slower 500ms (stat count-up)
- Easings: spring cubic-bezier(0.34, 1.56, 0.64, 1) for entrances, ease-out for exits
- Hover: scale(1.03) + pink glow shadow intensification
- Stagger: story cards enter with 80ms stagger delay
- Reduced motion: respect prefers-reduced-motion, collapse to instant

## Techniques

### Pink Glow Gradient Block
Full-bleed gradient section with a radiating pink glow that makes content feel like it's lit from behind.
```css
.gradient-block {
  background: linear-gradient(135deg, #FF1493 0%, #FFA552 100%);
  position: relative;
  overflow: hidden;
}
.gradient-block::after {
  content: '';
  position: absolute;
  inset: -50%;
  background: radial-gradient(circle at 30% 40%, rgba(255, 20, 147, 0.4) 0%, transparent 60%);
  pointer-events: none;
}
```

### Sticker Badge Element
White-bordered floating element with a soft drop shadow, mimicking Instagram sticker aesthetics.
```css
.sticker-badge {
  display: inline-flex;
  align-items: center;
  padding: 8px 20px;
  background: #000000;
  color: #FFFFFF;
  border: 3px solid #FFFFFF;
  border-radius: 9999px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transform: rotate(-3deg);
}
```

### Stat Number Counter
Massive viewport-filling stat numbers with subtle noise texture and tight tracking.
```css
.stat-number {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(4rem, 15vw, 10rem);
  line-height: 0.9;
  letter-spacing: -0.02em;
  color: #FFFFFF;
  text-align: center;
  position: relative;
}
.stat-number::after {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/%3E%3C/svg%3E");
  mix-blend-mode: overlay;
  pointer-events: none;
}
```

## Iconography
Icons are filled and chunky to match the bold typographic voice — thin strokes would disappear against saturated gradients. Phosphor icons in fill weight provide the right heft while maintaining clarity at small sizes on mobile story cards.

- Treatment: filled
- Set: Phosphor (fill weight)
- Stroke: 2px (for the rare outline variant)

## Do's & Don'ts

### ✓ Do
- Use Hot Pink (#FF1493) as the dominant brand color on every key card
- Make stat numbers comically large — they should fill at least half the viewport
- Apply noise grain texture to all gradient surfaces
- Design every component as if it will be screenshotted at story-size
- Use sticker-style white borders on floating badges and character elements

### ✗ Don't
- Use muted or tasteful palettes — Wrapped is loud
- Fall back to single-color flat design
- Use serif typography anywhere in the system
- Lay out content in sober editorial grids
- Apply subtle gradients — saturation must be at maximum
- Use photography-only heroes without graphic overlay
- Make Spotify Green the background color — it's accent only
- Use cool-toned palettes — this year's identity is warm

## Applications
Spotify Wrapped 2023's design system is purpose-built for social-shareable data visualization cards, year-in-review campaigns, and mobile-first story-format experiences. It works best when the content is personal data presented as celebration — listening stats, ranking lists, personality quizzes — anything that gives users a reason to screenshot and share. The aesthetic translates well to event marketing, festival branding, and any consumer product that wants to feel like a cultural moment rather than a feature update.
