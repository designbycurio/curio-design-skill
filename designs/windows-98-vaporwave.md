---
version: 1

meta:
  id: windows-98-vaporwave
  name: Windows 98 Vaporwave
  description: "Bevelled Win98 chrome meets purple-pink-cyan vaporwave gradients, Greek busts, and JPEG decay"
  isDark: false
  tags: [vaporwave, retro, subcultural, experimental, narrative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "Windows 98 launched 1998; vaporwave genre coined 2011; Win98 vaporwave aesthetic peaked 2014–2018"
  region: "Born online — USA, UK, Japan, Russia via Tumblr / SoundCloud / Are.na"
  regionZh: "互联网原生——美国、英国、日本、俄罗斯，经由Tumblr / SoundCloud / Are.na传播"
  keyFigures: [Ramona Xavier / Vektroid, Daniel Lopatin, James Ferraro, Mary Bell]
  movements: [vaporwave, post-internet art, seapunk]

introduction: |
  Windows 98 Vaporwave fuses the literal GUI chrome of Microsoft's 1998 operating system — bevelled 3D buttons, Tahoma bitmap type, marble-cream panels — with the purple-pink-cyan gradient dreamscape of early-2010s vaporwave music culture. Greek marble busts float over JPEG-degraded sunsets; katakana neon signs glow beside 16-color VGA dithering.

  The result is an aesthetic of ironic corporate melancholy: the operating system as metaphor for late capitalism, every pixel deliberately compressed, every window frame a monument to digital nostalgia.
introductionZh: |
  Windows 98 蒸汽波将微软1998年操作系统的真实GUI元素——凸起的3D按钮、Tahoma位图字体、大理石奶油色面板——与2010年代初蒸汽波音乐文化的紫粉青渐变梦境融为一体。希腊大理石半身像漂浮在JPEG压缩伪影的落日之上，片假名霓虹灯在16色VGA抖动旁闪烁。

  这是一种讽刺性企业忧郁美学：操作系统作为晚期资本主义的隐喻，每个像素都被刻意压缩，每个窗口边框都是数字怀旧的纪念碑。

colors:
  primary:    {"50": "#F3ECFD", "100": "#E7D9FB", "200": "#CFB3F7", "300": "#B78DF3", "400": "#9F67EF", "500": "#8C52E0", "600": "#7042B3", "700": "#543187", "800": "#38215A", "900": "#1C102D", "950": "#0E0817"}
  secondary:  {"50": "#FFF0F7", "100": "#FFE1EF", "200": "#FFC3DF", "300": "#FFA5CF", "400": "#FF8EC3", "500": "#FF77B7", "600": "#CC5F92", "700": "#99476E", "800": "#663049", "900": "#331825", "950": "#1A0C12"}
  accent:     {"50": "#EDFBFB", "100": "#DBF7F7", "200": "#B8EFEF", "300": "#94E7E7", "400": "#70DFDF", "500": "#52E0E0", "600": "#42B3B3", "700": "#318787", "800": "#215A5A", "900": "#102D2D", "950": "#081717"}
  neutral:    {"50": "#FAF8FC", "100": "#F5F1F9", "200": "#EBE3F3", "300": "#DDD3E8", "400": "#C4B5D4", "500": "#A898BA", "600": "#8A7A9E", "700": "#6A5A7A", "800": "#4A3D56", "900": "#2A2232", "950": "#15111A"}
  semantic:
    success: { bg: "#52E0A0", text: "#0A3020", light: "#DBFAED", border: "#42B380" }
    warning: { bg: "#E0C052", text: "#3A2E0A", light: "#FAF3DB", border: "#B39942" }
    error:   { bg: "#E05272", text: "#3A0A15", light: "#FADBE2", border: "#B3425B" }
    info:    { bg: "#52A0E0", text: "#0A2030", light: "#DBF0FA", border: "#4280B3" }
  background:
    page:    "linear-gradient(135deg, #8C52E0 0%, #FF77B7 50%, #52E0E0 100%)"
    surface: "#F0E0CC"
    subtle:  "#FFFFFF"
  text:
    primary:   "#0A0A0A"
    secondary: "#4A3D56"
    muted:     "#6A5A7A"
    inverse:   "#FFFFFF"

typography:
  families:
    heading: "'DM Sans', 'Tahoma', sans-serif"
    body:    "'Inter', 'Tahoma', sans-serif"
    mono:    "'VT323', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=Inter:wght@400;500;600&family=VT323&family=Noto+Sans+JP:wght@400;700&display=swap"
  scale: {"2xs": "0.625rem", "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
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
  radius: {none: "0", sm: "0", md: "2px", lg: "2px", xl: "4px", full: "9999px"}
  color:  {default: "#808080", subtle: "#C0C0C0", strong: "#404040", focus: "#8C52E0"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #808080"
  sm: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040"
  md: "inset 2px 2px 0 #FFFFFF, inset -2px -2px 0 #404040, 2px 2px 4px rgba(0,0,0,0.15)"
  lg: "inset 2px 2px 0 #FFFFFF, inset -2px -2px 0 #404040, 4px 4px 8px rgba(0,0,0,0.2)"
  xl: "inset 2px 2px 0 #FFFFFF, inset -2px -2px 0 #404040, 6px 6px 12px rgba(0,0,0,0.25)"
  "2xl": "inset 2px 2px 0 #FFFFFF, inset -2px -2px 0 #404040, 8px 8px 16px rgba(0,0,0,0.3)"
  inner: "inset 1px 1px 0 #404040, inset -1px -1px 0 #FFFFFF"
  focus: "0 0 0 3px rgba(140, 82, 224, 0.4)"

motion:
  level: "restrained"
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "350ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [tint, opacity, scale]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "strong"
  rhythm:        "4px"

surfaceStyle: "layered"
blur:         "none"

iconography:
  treatment: "outline"
  set:       "lucide"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#C0C0C0", color: "#0A0A0A", border: "2px solid", shadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040", hoverBackground: "#D4D4D4", hoverShadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040", hoverColor: "#0A0A0A"}
    secondary: {background: "#F0E0CC", color: "#0A0A0A", border: "2px solid", shadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040", hoverBackground: "#F5EAD9", hoverShadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040", hoverColor: "#0A0A0A"}
    ghost:     {background: "transparent", color: "#8C52E0", border: "2px solid #52E0E0", shadow: "none", hoverBackground: "rgba(82, 224, 224, 0.1)", hoverShadow: "none", hoverColor: "#8C52E0"}
    danger:    {background: "#C0C0C0", color: "#CC0000", border: "2px solid", shadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040", hoverBackground: "#D4D4D4", hoverShadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040", hoverColor: "#CC0000"}
    sizes:     {sm: {height: "24px", padding: "2px 8px", fontSize: "0.75rem"}, md: {height: "32px", padding: "4px 16px", fontSize: "0.875rem"}, lg: {height: "40px", padding: "6px 24px", fontSize: "1rem"}}
    borderRadius: "0"
    fontWeight: 700
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#0A0A0A"
    border: "2px solid"
    borderRadius: "0"
    padding: "4px 8px"
    focusBorder: "#8C52E0"
    placeholderColor: "#6A5A7A"
  card:
    base:  {background: "#F0E0CC", border: "2px solid #808080", borderRadius: "0", padding: "16px", shadow: "inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040"}
    hover: {shadow: "inset 2px 2px 0 #FFFFFF, inset -2px -2px 0 #404040, 4px 4px 8px rgba(0,0,0,0.2)", transform: "none"}
---

# Windows 98 Vaporwave

> Bevelled Win98 GUI chrome collides with purple-pink-cyan vaporwave gradients, Greek marble busts, and JPEG-compression melancholy.

## Origin

Windows 98 Vaporwave emerged from the collision of two timelines: Microsoft's 1998 operating system — with its bevelled 3D buttons, Tahoma bitmap type, 16-color VGA palette, and beige-plastic Compaq monitor frames — and the vaporwave music genre coined in 2011 by artists like Ramona Xavier (Vektroid / Macintosh Plus) and Daniel Lopatin. The aesthetic peaked between 2014 and 2018 on Tumblr, aesthetic.fm, and Are.na, where anonymous creators layered Windows 98 GUI screenshots over purple-pink-cyan gradients, Greek marble busts, dolphins, palm trees, and katakana neon signs.

The subculture reads the operating system as a metaphor for late capitalism — the GUI chrome becomes melancholy, the Greek bust becomes irony, and everything is deliberately JPEG-degraded. Unlike generic vaporwave, this variant explicitly quotes Microsoft Windows 1998 chrome as its primary visual vocabulary, creating a specific nostalgia for the corporate-beige desktop era filtered through post-internet art sensibility.

## Overview

Composition cues:
- **Layout**: Grid-based, mimicking Windows 98 desktop tile arrangements and dialog-box stacking
- **Content width**: Container (1024px–1280px), referencing 1024×768 monitor resolutions
- **Framing**: Bordered — every surface uses bevelled 3D-button borders (raised/sunken vocabulary)
- **Grid intensity**: Strong — visible structure echoing the rigid rectilinear Windows chrome

## Colors

The palette layers three worlds: the purple-pink-cyan vaporwave gradient that dominates the page background (the "sunset" layer), the marble-cream and pure-white of Windows content panels (the "chrome" layer), and 16-color VGA accent pops of bright purple, cyan, and magenta (the "glitch" layer). The gradient is never subtle — it is the soul of the aesthetic, always present as the environmental context behind bevelled panels.

**Role usage**:
- Page background → `colors.background.page` (the purple-pink-cyan gradient)
- Card / panel surfaces → `colors.background.surface` (marble cream #F0E0CC)
- Content areas → `colors.background.subtle` (pure white #FFFFFF)
- Primary actions & focus states → `colors.primary.500` (vaporwave purple #8C52E0)
- Decorative accents & highlights → `colors.secondary.500` (vaporwave pink #FF77B7)
- Links & interactive hints → `colors.accent.500` (vaporwave cyan #52E0E0)
- Body text → `colors.text.primary` (#0A0A0A on light surfaces)
- Muted labels → `colors.text.muted` (#6A5A7A)

## Typography

The type voice is deliberately anachronistic: DM Sans (a modern geometric revival of Tahoma's spirit) for headings, Inter or Tahoma for body text, Times New Roman for ironic-corporate display moments, Noto Sans JP for katakana vaporwave motifs, and VT323 for terminal/monospace accents. The overall effect should feel like a Windows 98 dialog box that gained sentience and started writing poetry.

**Text styles**:
- `display-xl` — 'Times New Roman', serif, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — 'Times New Roman', serif, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — 'DM Sans', sans-serif, 48px, weight 800, line-height 1.2, letter-spacing -0.02em
- `heading-2` — 'DM Sans', sans-serif, 36px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — 'Inter', sans-serif, 18px, weight 400, line-height 1.6, letter-spacing 0
- `body-md` — 'Inter', sans-serif, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — 'Inter', sans-serif, 12px, weight 500, line-height 1.4, letter-spacing 0.05em
- `mono-md` — 'VT323', monospace, 16px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px
- Scale follows Windows 98 dialog-box proportions: compact internal padding (4–8px), generous section separation (48–96px)
- Container max-width: 1024px default, 1280px wide
- Section padding: 64px vertical (md), 96px (lg) for hero sections
- Grid gap: 16px between cards/tiles, 8px within component groups

## Elevation & Depth

Depth is expressed through the Windows 98 bevelled-border vocabulary rather than modern drop shadows. Raised surfaces get a white inset highlight on top-left and a dark inset shadow on bottom-right. Sunken surfaces (inputs, wells) invert this pattern. The layering creates a distinctly 1990s sense of physicality — plastic buttons you want to click.

- Raised surface: `inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040`
- Sunken surface: `inset 1px 1px 0 #404040, inset -1px -1px 0 #FFFFFF`
- Heavy raised: `inset 2px 2px 0 #FFFFFF, inset -2px -2px 0 #404040`
- Floating panel: bevelled border + `4px 4px 8px rgba(0,0,0,0.2)` drop shadow

## Shapes

- Button border-radius: 0 (pure Windows 98 chrome — no curves)
- Card border-radius: 0
- Input border-radius: 0
- Only exception: `full` (9999px) for avatar circles or pill badges when explicitly needed
- All corners are hard rectilinear, referencing the rigid geometry of Win98 dialog boxes

## Motion

Motion is restrained and mechanical — mimicking the instant-snap feel of Windows 98 UI interactions. No elastic bounces or fluid organic transitions. Hover states change instantly or with minimal duration. The aesthetic is "click and it happens" rather than "gesture and it flows."

- Level: restrained
- Hover transitions: 100–200ms, linear or ease-out
- Page transitions: 200–350ms, ease-out
- Easing: `cubic-bezier(0.4, 0, 0.2, 1)` default; no spring/bounce
- Hover patterns: tint (background color shift), opacity fade, subtle scale (1.01x max)
- Reduced motion: respected — all animations optional

## Techniques

### Win98 Bevelled Button

The canonical Windows 98 raised-button effect using inset box-shadows to simulate 3D plastic chrome.

```css
.win98-button {
  background: #C0C0C0;
  border: none;
  padding: 4px 16px;
  font-family: 'DM Sans', 'Tahoma', sans-serif;
  font-weight: 700;
  font-size: 0.875rem;
  color: #0A0A0A;
  box-shadow: inset 1px 1px 0 #FFFFFF, inset -1px -1px 0 #404040;
  cursor: pointer;
}
.win98-button:active {
  box-shadow: inset 1px 1px 0 #404040, inset -1px -1px 0 #FFFFFF;
}
```

### JPEG Compression Artifact Overlay

A pseudo-element texture that simulates JPEG degradation on accent surfaces, using a repeating SVG noise pattern with reduced opacity.

```css
.jpeg-artifact {
  position: relative;
}
.jpeg-artifact::after {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4'%3E%3Crect width='2' height='2' fill='%23FF77B7' opacity='0.08'/%3E%3Crect x='2' y='2' width='2' height='2' fill='%2352E0E0' opacity='0.06'/%3E%3C/svg%3E") repeat;
  mix-blend-mode: overlay;
  pointer-events: none;
  image-rendering: pixelated;
}
```

### Vaporwave Gradient Panel

The signature purple-pink-cyan gradient applied as a page or hero background, with a CRT-scanline overlay for period authenticity.

```css
.vaporwave-gradient {
  background: linear-gradient(135deg, #8C52E0 0%, #FF77B7 50%, #52E0E0 100%);
  position: relative;
}
.vaporwave-gradient::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.03) 2px,
    rgba(0, 0, 0, 0.03) 4px
  );
  pointer-events: none;
}
```

## Iconography

Icons should feel utilitarian and slightly pixelated — referencing the 16×16 and 32×32 icon grids of Windows 98 system icons. Use outline-style icons from Lucide at standard sizes, but consider rendering them with `image-rendering: pixelated` at small sizes for authenticity.

- Treatment: outline (referencing Win98 toolbar icons)
- Set: Lucide (clean geometry that echoes system-icon simplicity)
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use bevelled 3D-button borders on all interactive elements (the Win98 chrome vocabulary)
- Apply the purple-pink-cyan gradient as the dominant environmental background
- Include JPEG-compression-artifact textures on accent surfaces
- Use Times New Roman for ironic-corporate display headings
- Layer marble-cream panels over the gradient background for content readability
- Reference 16-color VGA palette for spot-color accents

### ✗ Don't
- Use modern smooth-rounded-design (Win98 vaporwave is bevelled 3D-chrome, not pill buttons)
- Apply saturated true neons (must be pastel-vaporwave specifically, not cyberpunk)
- Introduce decorative typography beyond Tahoma / DM Sans / Times / katakana
- Use clean-photographic imagery without JPEG-compression artifacts
- Use dark backgrounds without the gradient (pastel-purple-pink-cyan gradient is the soul)
- Render anti-aliased smooth fonts where bitmap pixelation would be more authentic
- Create subtle / minimalist compositions (Win98 vaporwave is meme-density layered)

## Applications

Windows 98 Vaporwave is ideal for music-related landing pages, nostalgic portfolio sites, meme-culture editorial platforms, retro-computing community hubs, and SoundCloud/Bandcamp artist pages. It works best when the content itself engages with internet nostalgia, post-ironic aesthetics, or 1990s computing culture — any context where bevelled chrome and Greek busts feel like commentary rather than confusion.
