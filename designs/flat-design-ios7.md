---
version: 1

meta:
  id: flat-design-ios7
  name: "iOS 7 Flat"
  description: "Apple's radical 2013 flat redesign — translucent layers, hairline strokes, and ultralight typography over pure white"
  isDark: false
  tags: [modernist, minimal, bold]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Announced WWDC June 2013; shipped September 2013; refined through iOS 10 (2016)"
  region: "Cupertino, California"
  regionZh: "美国加利福尼亚州库比蒂诺"
  keyFigures: ["Jony Ive", "Alan Dye", "Apple HI Team"]
  movements: ["Flat design movement", "Post-skeuomorphic UI", "Vibrancy/translucency aesthetic"]

introduction: |
  iOS 7 was the overnight revolution that killed skeuomorphism at Apple. Under Jony Ive's direction, every leather stitch, green-felt texture, and faux-wood bookshelf vanished, replaced by luminous white space, translucent blur panels, and typography so thin it felt weightless.

  The result defined mobile design for a decade. Bright tint colors on white, hairline separators, frosted-glass layering, and content-as-chrome became the universal language of touchscreen interfaces from 2013 onward.
introductionZh: |
  iOS 7 是苹果一夜之间终结拟物设计的革命性时刻。2013 年，在乔尼·艾维的主导下，皮革纹理、绿毡台面和仿木书架全部消失，取而代之的是纯白留白、毛玻璃模糊面板和纤细到几乎失重的字体。

  这套视觉语言定义了此后十年的移动端设计范式——明亮的色彩点缀在白色背景上，发丝般的分隔线，磨砂玻璃层叠效果，以及"内容即界面"的设计哲学，从库比蒂诺辐射至全球每一块触摸屏。

colors:
  primary:
    "50": "#E5F2FF"
    "100": "#CCE5FF"
    "200": "#99CBFF"
    "300": "#66B0FF"
    "400": "#3396FF"
    "500": "#007AFF"
    "600": "#0062CC"
    "700": "#004A99"
    "800": "#003166"
    "900": "#001933"
    "950": "#000D1A"
  secondary:
    "50": "#F0EFFE"
    "100": "#E1DFFD"
    "200": "#C3BFFB"
    "300": "#A5A0F9"
    "400": "#8780F7"
    "500": "#5856D6"
    "600": "#4645AB"
    "700": "#353480"
    "800": "#232256"
    "900": "#12112B"
    "950": "#090916"
  accent:
    "50": "#E6FAEB"
    "100": "#CDF5D7"
    "200": "#9BEBAF"
    "300": "#69E187"
    "400": "#4CD964"
    "500": "#34C759"
    "600": "#28A745"
    "700": "#1E7D34"
    "800": "#145423"
    "900": "#0A2A11"
    "950": "#051509"
  neutral:
    "50": "#F2F2F7"
    "100": "#E5E5EA"
    "200": "#D1D1D6"
    "300": "#C7C7CC"
    "400": "#AEAEB2"
    "500": "#8E8E93"
    "600": "#636366"
    "700": "#48484A"
    "800": "#3A3A3C"
    "900": "#2C2C2E"
    "950": "#1C1C1E"
  semantic:
    success: { bg: "#4CD964", text: "#FFFFFF", light: "#E6FAEB", border: "#34C759" }
    warning: { bg: "#FF9500", text: "#FFFFFF", light: "#FFF4E5", border: "#E68600" }
    error:   { bg: "#FF3B30", text: "#FFFFFF", light: "#FFE5E3", border: "#E6342B" }
    info:    { bg: "#007AFF", text: "#FFFFFF", light: "#E5F2FF", border: "#0062CC" }
  background:
    page:    "#FFFFFF"
    surface: "#FFFFFF"
    subtle:  "#F2F2F7"
  text:
    primary:   "#000000"
    secondary: "#3C3C43"
    muted:     "#8E8E93"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    body:    "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    mono:    "'SF Mono', 'Menlo', 'Consolas', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&display=swap"
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
  weights: {light: 200, normal: 300, medium: 400, semibold: 500, bold: 600, extrabold: 700}
  lineHeights: {tight: 1.2, snug: 1.3, normal: 1.4, relaxed: 1.5, loose: 1.6}
  letterSpacing: {tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.02em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%"}
  gridGap:        {sm: "8px",  md: "16px", lg: "24px", xl: "48px"}
  sectionPadding: {sm: "32px", md: "64px", lg: "96px", xl: "128px"}

borders:
  radius: {none: "0", sm: "4px", md: "8px", lg: "10px", xl: "14px", full: "9999px"}
  color:  {default: "#C7C7CC", subtle: "#E5E5EA", strong: "#8E8E93", focus: "#007AFF"}
  width:  {thin: "0.5px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "none"
  sm: "none"
  md: "none"
  lg: "none"
  xl: "none"
  "2xl": "none"
  inner: "none"
  focus: "0 0 0 3px rgba(0, 122, 255, 0.25)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.25, 0.1, 0.25, 1.0)"
    in:      "cubic-bezier(0.42, 0, 1.0, 1.0)"
    out:     "cubic-bezier(0, 0, 0.58, 1.0)"
    spring:  "cubic-bezier(0.5, 1.8, 0.4, 0.8)"
  hoverPatterns: [opacity, tint]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "glassy"
  gridIntensity: "subtle"
  rhythm:        "8px"

surfaceStyle: "glass"
blur:         "20px"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#007AFF", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#0062CC", hoverShadow: "none", hoverColor: "#FFFFFF"}
    secondary: {background: "transparent", color: "#007AFF", border: "none", shadow: "none", hoverBackground: "rgba(0, 122, 255, 0.08)", hoverShadow: "none", hoverColor: "#0062CC"}
    ghost:     {background: "transparent", color: "#007AFF", border: "none", shadow: "none", hoverBackground: "rgba(0, 122, 255, 0.05)", hoverShadow: "none", hoverColor: "#0062CC"}
    danger:    {background: "#FF3B30", color: "#FFFFFF", border: "none", shadow: "none", hoverBackground: "#E6342B", hoverShadow: "none", hoverColor: "#FFFFFF"}
    sizes:
      sm: {height: "30px", padding: "0 12px", fontSize: "0.8125rem"}
      md: {height: "36px", padding: "0 16px", fontSize: "0.9375rem"}
      lg: {height: "44px", padding: "0 20px", fontSize: "1.0625rem"}
    borderRadius: "8px"
    fontWeight: 400
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#F2F2F7"
    color: "#000000"
    border: "1px solid #E5E5EA"
    borderRadius: "8px"
    padding: "8px 12px"
    focusBorder: "1px solid #007AFF"
    placeholderColor: "#8E8E93"
  card:
    base:  {background: "rgba(255, 255, 255, 0.8)", border: "0.5px solid rgba(0, 0, 0, 0.06)", borderRadius: "10px", padding: "16px", shadow: "none"}
    hover: {shadow: "none", transform: "none"}
---

# iOS 7 Flat

> The moment Apple killed skeuomorphism overnight — translucent layers, ultralight type, and iOS blue on pure white.

## Origin

iOS 7 launched at WWDC in June 2013 as the most dramatic visual overhaul in Apple's mobile history. Jony Ive, who had taken control of software design the previous year, led a top-to-bottom rethink that replaced every skeuomorphic texture in iOS — the green felt of Game Center, the leather-stitched Calendar, the wood-grain Newsstand — with a system built on light, color, and translucency. Alan Dye and the Apple Human Interface team executed the vision in under a year, shipping it to hundreds of millions of devices that September.

The design language it established was deceptively simple: pure white canvases, tinted text buttons instead of chrome-heavy controls, hairline separators at half-pixel weight, and frosted-glass blur panels that let content bleed through layers. Helvetica Neue at ultralight weight became the signature typeface, a choice so radical that Apple later retreated to the slightly heavier San Francisco. But the core principles — flatness, translucency, and content-as-interface — defined mobile UI for the next decade and triggered the global flat-design movement.

## Overview
Composition cues:
- **Layout**: Vertical stack — full-width cells and grouped table views
- **Content width**: Container-bound (320–414pt on original devices), now scales to larger viewports
- **Framing**: Glassy — translucent blur panels float over photographic or colorful backdrops
- **Grid intensity**: Subtle — content alignment is precise but grid lines are invisible

## Colors
iOS 7's palette is built on the tension between a pure white canvas and vivid, saturated accent colors. The background is always `#FFFFFF` or the light system grey `#F2F2F7`; color enters only through interactive elements, status indicators, and vibrancy effects on translucent surfaces. iOS blue `#007AFF` is the signature — it means "tappable." The supporting palette (green, red, orange, yellow, purple, pink) is bright and unapologetically saturated, but used sparingly against the white field. Neutral greys are kept to the bare minimum: `#C7C7CC` hairlines and `#8E8E93` secondary text.

**Role usage**:
- Page background → `colors.background.page` (#FFFFFF)
- Grouped table background → `colors.background.subtle` (#F2F2F7)
- Interactive elements / tint → `colors.primary.500` (#007AFF)
- Destructive actions → `colors.semantic.error.bg` (#FF3B30)
- Success indicators → `colors.accent.400` (#4CD964)
- Primary text → `colors.text.primary` (#000000)
- Secondary / muted text → `colors.text.muted` (#8E8E93)
- Separators / hairlines → `colors.neutral.300` (#C7C7CC)

## Typography
iOS 7 introduced the thinnest system typography Apple had ever shipped. Display headlines in Helvetica Neue Ultralight (weight 200) were a deliberate shock — fragile, elegant, and impossible to confuse with the chunky Marker Felt era. Body text settled at Regular (weight 400) for legibility, while navigation elements used Light (300). The substitute font Inter captures the same neutral humanist geometry at matching weights. Line-height is kept tight at 1.4 for body copy; display sizes breathe with generous letter-spacing.

**Text styles**:
- `display-xl` — Inter, 96px, weight 200, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Inter, 64px, weight 200, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Inter, 34px, weight 300, line-height 1.2, letter-spacing -0.02em
- `heading-2` — Inter, 28px, weight 300, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Inter, 20px, weight 400, line-height 1.4, letter-spacing 0
- `body-md` — Inter, 17px, weight 400, line-height 1.4, letter-spacing 0
- `caption` — Inter, 13px, weight 400, line-height 1.4, letter-spacing 0
- `mono-md` — SF Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 8px (the iOS point grid)
- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128
- Container max-width: 1024px for web adaptation; original iOS is edge-to-edge within safe area
- Section padding: 64px vertical on desktop, 32px on mobile
- List cell height: 44px minimum (iOS touch target)
- Grouped table inset: 16px horizontal

## Elevation & Depth
iOS 7 eliminated drop shadows from UI chrome entirely. Depth is communicated exclusively through translucency — a frosted-glass panel hovering over content implies elevation without any painted shadow. The blur radius (`backdrop-filter: blur(20px)`) and a subtle white-alpha overlay create the layering effect. Control Center slides up as a blur sheet; Notification Center drops down as another. The only "shadow" in the system is the focus ring (`0 0 0 3px rgba(0,122,255,0.25)`), and even that is a glow, not a drop shadow.

- Surface style: glass — `rgba(255,255,255,0.8)` with `backdrop-filter: blur(20px)`
- No shadow ladder — all shadow tokens are `none`
- Depth is encoded in translucency alpha: higher = more opaque = closer to viewer
- Hairline borders (`0.5px solid rgba(0,0,0,0.06)`) supplement blur for edge definition

## Shapes
- App icon radius: 22% of side length (the iOS superellipse)
- Button radius: 8px
- Card / grouped table radius: 10px
- Input radius: 8px
- Maximum card radius: 14px — never rounder
- Pill shapes (search bars): `9999px` full-round
- Separator weight: 0.5px (hairline)

## Motion
iOS 7 introduced physics-based animation to the system — spring dynamics, parallax on the home screen, and zoom transitions between app icon and full-screen view. The motion language is restrained but purposeful: elements slide, fade, and scale along the z-axis to reinforce the layered spatial model. Nothing bounces gratuitously; motion exists to communicate spatial relationships between translucent planes.

- Level: restrained
- Transitions: 250ms default, 400ms for modal presentations
- Easing: `cubic-bezier(0.25, 0.1, 0.25, 1.0)` — Apple's custom ease
- Spring: `cubic-bezier(0.5, 1.8, 0.4, 0.8)` for interactive gestures
- Hover patterns: opacity fade (0.5 on press), tint color shift
- Parallax: subtle background shift on scroll (2–4px)
- Reduced motion: fully supported — cross-dissolve replaces all spatial transitions

## Techniques

### Frosted Glass Panel
The signature iOS 7 visual — a translucent surface that blurs the content beneath, creating depth without shadows.
```css
.frosted-panel {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 0.5px solid rgba(0, 0, 0, 0.06);
  border-radius: 10px;
}
```

### Hairline Separator
The ultra-thin divider that replaced heavy borders throughout iOS 7, rendered at sub-pixel weight.
```css
.hairline-separator {
  height: 0.5px;
  background: #C7C7CC;
  margin-left: 16px;
}
```

### Tint-Only Button
iOS 7's most controversial UI decision — buttons are just colored text, with no border or fill to indicate tappability.
```css
.tint-button {
  background: transparent;
  border: none;
  color: #007AFF;
  font-family: 'Inter', sans-serif;
  font-size: 17px;
  font-weight: 400;
  padding: 8px 0;
  cursor: pointer;
  transition: opacity 250ms cubic-bezier(0.25, 0.1, 0.25, 1.0);
}
.tint-button:active {
  opacity: 0.5;
}
```

## Iconography
iOS 7 replaced every filled, glossy icon in the system with thin line-stroke outlines. The icon style uses 1.5px strokes on a 24px canvas, drawn with simple geometric shapes and open endpoints. Icons are monochromatic — they inherit the current tint color — and convey meaning through silhouette rather than surface detail.

- Treatment: linear (outline only, no fill)
- Set: Lucide (closest open match to Apple's line-icon vocabulary)
- Stroke: 1.5px, round caps, round joins

## Do's & Don'ts

### ✓ Do
- Use iOS blue `#007AFF` as the default interactive tint for all tappable elements
- Keep display typography at weight 200 (ultralight) — let the thinness breathe
- Apply `backdrop-filter: blur(20px)` to any elevated surface or overlay
- Use 0.5px hairline separators instead of full-pixel borders
- Let white space dominate — content density is lower than pre-iOS-7

### ✗ Don't
- Apply skeuomorphic textures — leather, felt, wood, linen, or any material simulation
- Use heavy bold weights for display headlines (iOS 7 is ultralight, not Impact)
- Add drop-shadows to UI chrome or cards — depth comes from blur, not shadow
- Fill backgrounds with saturated flat colors — the canvas is white-first
- Set border-radius above 14px on cards or containers
- Use gradients on buttons or navigation bars (translucency, not gradients)

## Applications
iOS 7 Flat is ideal for mobile-first applications, dashboard interfaces, and any product that values clean spatial hierarchy over decorative richness. It works exceptionally well for utility apps, messaging interfaces, settings panels, and content-reading experiences where the UI should disappear behind the content. The translucent layering system is particularly effective for overlay-heavy interfaces — modals, action sheets, and contextual menus that need to maintain spatial awareness of the content beneath.
