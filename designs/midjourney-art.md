---
version: 1

meta:
  id: midjourney-art
  name: Midjourney
  description: "Pitch-black gallery aesthetic where AI-generated imagery is the brand and the chrome is invisible"
  isDark: true
  tags: [experimental, bold, futuristic, minimal, tech]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "2022 launched; current visual ~2023–2024"
  region: "San Francisco, California"
  regionZh: "美国旧金山"
  keyFigures: ["David Holz", "Midjourney research team"]
  movements: ["Generative AI image synthesis", "Discord-native AI products", "Post-Stable-Diffusion creator tools"]

introduction: |
  Midjourney is the AI image generator that became a cultural-aesthetic engine. Born as a Discord bot in 2022, it evolved into a full web experience whose design philosophy is radical restraint — pitch-black backgrounds, razor-thin serif type, and zero chromatic branding. Every pixel of color comes from the generated artwork itself.

  The interface disappears so the images can speak. Like a world-class gallery with matte-black walls, the chrome exists only to frame the work. This design system captures that invisible-brand ethos: museum-grade minimalism where the content is the spectacle.
introductionZh: |
  Midjourney 是那个从 Discord 机器人成长为文化美学引擎的 AI 图像生成器。它的设计哲学是极致克制——纯黑背景、纤细衬线字体、零色彩品牌元素。所有色彩都来自生成的图像本身。

  界面消隐，让作品自己说话。如同一座世界级美术馆的哑光黑墙，所有界面元素只为裱框作品而存在。这套设计系统捕捉了"隐形品牌"的精髓：博物馆级的极简主义，内容即奇观。

colors:
  primary:
    "50": "#FFFFFF"
    "100": "#F5F5F5"
    "200": "#E5E5E5"
    "300": "#D4D4D4"
    "400": "#C0C0C0"
    "500": "#FFFFFF"
    "600": "#E0E0E0"
    "700": "#BDBDBD"
    "800": "#9E9E9E"
    "900": "#757575"
    "950": "#616161"
  secondary:
    "50": "#1A1A1A"
    "100": "#171717"
    "200": "#141414"
    "300": "#121212"
    "400": "#0F0F0F"
    "500": "#0A0A0A"
    "600": "#080808"
    "700": "#050505"
    "800": "#030303"
    "900": "#010101"
    "950": "#000000"
  accent:
    "50": "#FAFAFA"
    "100": "#F5F5F5"
    "200": "#E8E8E8"
    "300": "#D6D6D6"
    "400": "#B8B8B8"
    "500": "#808080"
    "600": "#6B6B6B"
    "700": "#525252"
    "800": "#3D3D3D"
    "900": "#2B2B2B"
    "950": "#1A1A1A"
  neutral:
    "50": "#FAFAFA"
    "100": "#F5F5F5"
    "200": "#E5E5E5"
    "300": "#D4D4D4"
    "400": "#A3A3A3"
    "500": "#808080"
    "600": "#525252"
    "700": "#404040"
    "800": "#262626"
    "900": "#171717"
    "950": "#0A0A0A"
  semantic:
    success: { bg: "#0A2A0A", text: "#4ADE80", light: "#132B13", border: "#1A3A1A" }
    warning: { bg: "#2A2A0A", text: "#FACC15", light: "#2B2B13", border: "#3A3A1A" }
    error:   { bg: "#2A0A0A", text: "#F87171", light: "#2B1313", border: "#3A1A1A" }
    info:    { bg: "#0A0A2A", text: "#60A5FA", light: "#13132B", border: "#1A1A3A" }
  background:
    page:    "#000000"
    surface: "#141414"
    subtle:  "#0A0A0A"
  text:
    primary:   "#F5F5F5"
    secondary: "#A3A3A3"
    muted:     "#808080"
    inverse:   "#000000"

typography:
  families:
    heading: "'Cormorant Garamond', 'Georgia', serif"
    body:    "'Inter', 'Helvetica Neue', sans-serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
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
  weights: { light: 300, normal: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800 }
  lineHeights: { tight: 1.2, snug: 1.375, normal: 1.5, relaxed: 1.625, loose: 1.8 }
  letterSpacing: { tighter: "-0.04em", tight: "-0.015em", normal: "0", wide: "0.05em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "4px",  md: "8px",  lg: "16px", xl: "24px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "2px", md: "4px", lg: "6px", xl: "8px", full: "9999px" }
  color:  { default: "#1A1A1A", subtle: "#111111", strong: "#333333", focus: "#FFFFFF" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
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
  focus: "0 0 0 2px rgba(255,255,255,0.15)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "100ms", normal: "200ms", slow: "350ms", slower: "500ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.175, 0.885, 0.32, 1.275)"
  hoverPatterns: ["opacity", "tint"]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "full-bleed"
  framing:       "minimal"
  gridIntensity: "strong"
  rhythm:        "4px"

surfaceStyle: "flat"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:   { background: "#FFFFFF", color: "#000000", border: "none", shadow: "none", hoverBackground: "#E0E0E0", hoverShadow: "none", hoverColor: "#000000" }
    secondary: { background: "transparent", color: "#F5F5F5", border: "1px solid #333333", shadow: "none", hoverBackground: "#141414", hoverShadow: "none", hoverColor: "#FFFFFF" }
    ghost:     { background: "transparent", color: "#A3A3A3", border: "none", shadow: "none", hoverBackground: "rgba(255,255,255,0.05)", hoverShadow: "none", hoverColor: "#F5F5F5" }
    danger:    { background: "#F87171", color: "#000000", border: "none", shadow: "none", hoverBackground: "#EF4444", hoverShadow: "none", hoverColor: "#000000" }
    sizes:
      sm: { height: "32px", padding: "0 12px", fontSize: "0.8125rem" }
      md: { height: "40px", padding: "0 16px", fontSize: "0.875rem" }
      lg: { height: "48px", padding: "0 24px", fontSize: "1rem" }
    borderRadius: "4px"
    fontWeight: 500
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#0F0F0F"
    color: "#F5F5F5"
    border: "1px solid #1A1A1A"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "#FFFFFF"
    placeholderColor: "#525252"
  card:
    base:  { background: "#000000", border: "1px solid #1A1A1A", borderRadius: "4px", padding: "0", shadow: "none" }
    hover: { shadow: "none", transform: "none" }
---

# Midjourney

> The brand that disappears so the art can speak — pitch-black gallery chrome, serif whispers, and full-bleed generated imagery.

## Origin

Midjourney launched in July 2022 as a Discord-only AI image generator founded by David Holz, a former Leap Motion co-founder. Operating from San Francisco with a deliberately small team, the product exploded in popularity by letting users generate images through simple text prompts typed into Discord channels — an unconventional distribution strategy that turned a chat platform into an art studio visited by millions.

By 2024, Midjourney had shipped a dedicated web application at midjourney.com and released its V6 model, which dramatically improved photorealism and text rendering. Throughout this evolution, the brand's visual identity remained radically minimal: pure black backgrounds, refined serif typography, and zero chromatic brand colors. Every drop of color in the interface comes from the generated artwork itself — the chrome is a museum wall, and the images are the exhibition.

## Overview

Composition cues:
- **Layout**: Dense image grid, gallery-style — masonry or uniform tiles filling the viewport edge-to-edge
- **Content width**: Full-bleed; images run wall-to-wall, text blocks use narrow containers within
- **Framing**: Minimal — cards are frameless image tiles with razor-thin dark borders at most
- **Grid intensity**: Strong — tight 4–8px gaps creating a mosaic of generated artwork

## Colors

Midjourney's palette is the absence of palette. The interface is pure black `#000000` — not dark gray, not charcoal, but void-black. Text arrives in off-white `#F5F5F5`, secondary information in middle gray `#808080`, and borders in near-invisible `#1A1A1A`. There are no brand accent colors whatsoever. All chromatic energy is delegated to the generated images, which become the only source of hue on any screen. This creates a gallery effect: the interface recedes completely, and the artwork pops with maximum contrast against the black ground.

**Role usage**:
- Page background → `colors.background.page` (`#000000`)
- Card / surface background → `colors.background.surface` (`#141414`)
- Input field fill → `#0F0F0F`
- Primary text → `colors.text.primary` (`#F5F5F5`)
- Secondary text → `colors.text.secondary` (`#A3A3A3`)
- Muted / placeholder text → `colors.text.muted` (`#808080`)
- Borders and dividers → `borders.color.default` (`#1A1A1A`)
- Primary action (button) → `colors.primary.500` (`#FFFFFF` on black)

## Typography

The typographic voice is gallery-catalog minimalism. Cormorant Garamond — a refined, high-contrast serif — handles headlines with quiet authority, set at semibold with tight `-0.015em` letter-spacing that feels like art-book titling. Inter at light or regular weight serves as the body face, providing Swiss-clean readability against the black ground. JetBrains Mono appears in prompt displays and technical metadata. The overall impression is editorial restraint: type exists to label, not to decorate.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 600, line-height 1.0, letter-spacing -0.015em
- `display-lg` — Cormorant Garamond, 64px, weight 600, line-height 1.05, letter-spacing -0.015em
- `heading-1` — Cormorant Garamond, 48px, weight 600, line-height 1.1, letter-spacing -0.015em
- `body-lg` — Inter, 18px, weight 300, line-height 1.6, letter-spacing 0
- `body-md` — Inter, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Inter, 13px, weight 400, line-height 1.4, letter-spacing 0
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px
- Scale follows 4px rhythm: 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128
- Grid gaps are tight (4–8px between image tiles) to create dense mosaic layouts
- Section padding: 32–128px vertical, scaling with viewport
- Container widths reach full-bleed for image grids; narrow (640–768px) for text content

## Elevation & Depth

Midjourney's interface is deliberately flat. There are no box shadows — none. Depth comes exclusively from the images themselves (which may contain photographed or painted depth) and from the contrast between the pure black background and the slightly lighter surface color `#141414`. This flatness reinforces the gallery metaphor: you don't put drop shadows on paintings in a museum.

- Surface style: flat, no blur, no glass effects
- Shadow ladder: all levels set to `none`
- Focus ring: a subtle `0 0 0 2px rgba(255,255,255,0.15)` — just enough for accessibility without visual noise
- Depth hierarchy achieved through background-color stepping: `#000000` → `#0A0A0A` → `#141414`

## Shapes

- Corner radii are minimal: 0–4px throughout
- Buttons: 4px border-radius (rectilinear, not pill-shaped)
- Cards: 4px border-radius (image frames)
- Inputs: 4px border-radius
- Full-round reserved only for avatar circles

## Motion

Midjourney's motion is restrained and gallery-appropriate — no bouncy transitions, no playful easing. Movement serves function: content fades in, images load with a subtle opacity transition, hover states shift tint. The interface should feel like walking through a quiet exhibition, not a theme park.

- Level: restrained
- Durations: fast 100ms for micro-interactions, normal 200ms for state changes, slow 350ms for content reveals
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)` — smooth deceleration
- Hover patterns: opacity fade (0.7 → 1.0), subtle tint overlay on image tiles
- `prefers-reduced-motion` fully respected — all transitions collapse to instant

## Techniques

### Gallery-wall image grid
A dense, edge-to-edge image grid that recreates the salon-style hanging of a contemporary gallery. Images sit in a CSS grid with minimal gaps and no card chrome, letting the artwork touch.
```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 4px;
  padding: 0;
  background: #000000;
}
.gallery-grid img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 4px;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.gallery-grid img:hover {
  opacity: 0.85;
}
```

### Void-frame card
An image card with zero visual chrome — the image IS the card. A hairline border appears only on hover to delineate the tile from the black ground.
```css
.void-card {
  position: relative;
  background: #000000;
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid transparent;
  transition: border-color 200ms ease;
}
.void-card:hover {
  border-color: #1A1A1A;
}
.void-card img {
  width: 100%;
  display: block;
}
```

### Serif-whisper heading
The characteristic Midjourney heading treatment — a refined serif set large against the void, with tight tracking and light weight that suggests art-catalog titling rather than web UI.
```css
.serif-whisper {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.05;
  color: #F5F5F5;
  margin: 0;
  padding: 0;
}
```

## Iconography

Icons are linear and whisper-thin, matching the minimal chrome philosophy. They appear sparingly — for navigation, actions, and metadata — never as decoration. Stroke-based Lucide icons at 1.5px weight in `#808080` or `#A3A3A3`, gaining full white on interactive hover.

- Treatment: linear (stroke-only)
- Set: Lucide
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use pure `#000000` black as the universal background — never dark gray
- Let generated images provide all chromatic interest; the UI is achromatic
- Set headings in Cormorant Garamond semibold with tight `-0.015em` tracking
- Keep card chrome invisible — images are their own frames
- Use tight grid gaps (4–8px) to create dense, gallery-wall image mosaics

### ✗ Don't
- Use light mode — Midjourney is canonically a dark gallery
- Introduce chromatic brand accent colors — color belongs to imagery only
- Apply decorative gradients to UI surfaces
- Use friendly, playful illustrations or mascots
- Shape buttons as pills — Midjourney is strictly rectilinear (4px radius max)
- Add box shadows to surfaces — the interface must remain flat

## Applications

This design system is purpose-built for image-forward platforms: AI art generators, photography portfolios, digital galleries, and creative showcase tools. It excels wherever the primary content is visual media that should dominate the viewport, and the interface should vanish behind it. The pitch-black gallery aesthetic also works for luxury editorial sites and minimal creative-tool dashboards.
