---
version: 1

meta:
  id: frutiger-aero-2007
  name: "Frutiger Aero 2007"
  description: "Glossy techno-optimism with sky-blue gradients, glass translucency, and nature-harmonized UI"
  isDark: false
  tags: [friendly, decorative, historical, tech, retro]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "~2004–2013, peak 2006–2010"
  region: "Global — emblematic in Microsoft (Redmond), Nintendo (Kyoto), British broadcasting (London)"
  regionZh: "全球——以微软（美国雷德蒙德）、任天堂（日本京都）、英国广播业（伦敦）为代表"
  keyFigures: ["Adrian Frutiger", "Microsoft Windows Vista team", "Nintendo Wii UI team", "Apple Aqua designers"]
  movements: ["Skeuomorphism", "Glossy Web 2.0", "Techno-Optimism"]

introduction: |
  Frutiger Aero is the glossy, sky-bright design language that dominated consumer technology from roughly 2004 to 2013. Named retroactively after Swiss typographer Adrian Frutiger, it married translucent glass surfaces, photorealistic skies, and blue-green palettes into an aesthetic of boundless techno-optimism.

  From Windows Vista's Aero theme to the Wii Channel menu, from Sky Sports broadcasts to Vitaminwater packaging, this style believed technology and nature could coexist in luminous harmony. Killed by iOS 7's flat purge in 2013, Frutiger Aero now thrives as a nostalgia aesthetic among Gen Z on TikTok and Tumblr.
introductionZh: |
  Frutiger Aero 是 2004 至 2013 年间主导消费科技领域的光泽明亮设计语言，以瑞士字体设计师阿德里安·弗鲁提格的姓氏命名。它将半透明玻璃质感、逼真的蓝天白云与蓝绿色调融为一体，传递着对科技与自然和谐共存的乐观信念。

  从微软 Windows Vista 的 Aero 主题到任天堂 Wii 频道界面，从英国天空体育的片头动画到维他命水的包装设计，这种风格无处不在。2013 年 iOS 7 的扁平化革命终结了它的统治，如今 Frutiger Aero 在 TikTok 和 Tumblr 上作为 Z 世代的怀旧美学强势回归。

colors:
  primary:
    "50": "#eef7fc"
    "100": "#d5edfa"
    "200": "#b0ddf5"
    "300": "#80c9ef"
    "400": "#5cb8e6"
    "500": "#3a9fd4"
    "600": "#2b82b4"
    "700": "#216690"
    "800": "#1c5272"
    "900": "#17435d"
    "950": "#0e2c3e"
  secondary:
    "50": "#f0faf6"
    "100": "#d8f2e9"
    "200": "#b5e6d5"
    "300": "#95d6c0"
    "400": "#6ec2a6"
    "500": "#4da98c"
    "600": "#3d8b72"
    "700": "#33705d"
    "800": "#2b5a4c"
    "900": "#254a3f"
    "950": "#142e27"
  accent:
    "50": "#f4f8fa"
    "100": "#e6eef2"
    "200": "#d6dde0"
    "300": "#bcc8ce"
    "400": "#9eb0b9"
    "500": "#8399a3"
    "600": "#6b808b"
    "700": "#576972"
    "800": "#48565d"
    "900": "#3d494f"
    "950": "#272f33"
  neutral:
    "50": "#f8fafb"
    "100": "#f0f4f6"
    "200": "#e2e8ec"
    "300": "#cdd6dc"
    "400": "#a8b6bf"
    "500": "#8596a1"
    "600": "#6b7d88"
    "700": "#576670"
    "800": "#4a555c"
    "900": "#40484f"
    "950": "#292f33"
  semantic:
    success: { bg: "#22c55e", text: "#ffffff", light: "#dcfce7", border: "#86efac" }
    warning: { bg: "#f59e0b", text: "#ffffff", light: "#fef3c7", border: "#fcd34d" }
    error:   { bg: "#ef4444", text: "#ffffff", light: "#fee2e2", border: "#fca5a5" }
    info:    { bg: "#5cb8e6", text: "#ffffff", light: "#eef7fc", border: "#b0ddf5" }
  background:
    page:    "#f0f8fc"
    surface: "rgba(255, 255, 255, 0.65)"
    subtle:  "#e8f2f8"
  text:
    primary:   "#1a3a4a"
    secondary: "#3d6478"
    muted:     "#7a98a8"
    inverse:   "#ffffff"

typography:
  families:
    heading: "'Nunito', 'Lato', 'Segoe UI', sans-serif"
    body:    "'Lato', 'Nunito', 'Segoe UI', sans-serif"
    mono:    "'JetBrains Mono', 'Consolas', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Lato:wght@300;400;700&family=JetBrains+Mono:wght@400;500&display=swap"
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
  letterSpacing: { tighter: "-0.04em", tight: "-0.02em", normal: "0", wide: "0.05em" }

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap:        { sm: "8px",  md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "6px", md: "10px", lg: "14px", xl: "20px", full: "9999px" }
  color:  { default: "rgba(92, 184, 230, 0.25)", subtle: "rgba(255, 255, 255, 0.4)", strong: "rgba(92, 184, 230, 0.5)", focus: "rgba(92, 184, 230, 0.6)" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(26, 58, 74, 0.05)"
  sm: "0 2px 4px rgba(26, 58, 74, 0.08)"
  md: "0 4px 12px rgba(26, 58, 74, 0.10)"
  lg: "0 8px 24px rgba(26, 58, 74, 0.12)"
  xl: "0 16px 40px rgba(26, 58, 74, 0.14)"
  "2xl": "0 24px 56px rgba(26, 58, 74, 0.18)"
  inner: "inset 0 2px 4px rgba(26, 58, 74, 0.08)"
  focus: "0 0 0 3px rgba(92, 184, 230, 0.4)"

motion:
  level: "lively"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, glow, scale]
  reducedMotion: true

composition:
  layout:        "flex"
  contentWidth:  "container"
  framing:       "glassy"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "glass"
blur:         "12px"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:
      background: "linear-gradient(180deg, #7ac8ec 0%, #5cb8e6 40%, #3a9fd4 100%)"
      color: "#ffffff"
      border: "1px solid rgba(255, 255, 255, 0.3)"
      shadow: "0 2px 8px rgba(58, 159, 212, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.4)"
      hoverBackground: "linear-gradient(180deg, #8fd2f0 0%, #6ec2ea 40%, #4aabdc 100%)"
      hoverShadow: "0 4px 14px rgba(58, 159, 212, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.5)"
      hoverColor: "#ffffff"
    secondary:
      background: "linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(232,242,248,0.8) 100%)"
      color: "#1a3a4a"
      border: "1px solid rgba(92, 184, 230, 0.3)"
      shadow: "0 1px 4px rgba(26, 58, 74, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.6)"
      hoverBackground: "linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(238,247,252,0.95) 100%)"
      hoverShadow: "0 2px 8px rgba(26, 58, 74, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.8)"
      hoverColor: "#1a3a4a"
    ghost:
      background: "transparent"
      color: "#3a9fd4"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(92, 184, 230, 0.1)"
      hoverShadow: "none"
      hoverColor: "#2b82b4"
    danger:
      background: "linear-gradient(180deg, #f87171 0%, #ef4444 40%, #dc2626 100%)"
      color: "#ffffff"
      border: "1px solid rgba(255, 255, 255, 0.25)"
      shadow: "0 2px 8px rgba(220, 38, 38, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.3)"
      hoverBackground: "linear-gradient(180deg, #fca5a5 0%, #f87171 40%, #ef4444 100%)"
      hoverShadow: "0 4px 14px rgba(220, 38, 38, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.4)"
      hoverColor: "#ffffff"
    sizes:
      sm: { height: "32px", padding: "0 12px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 28px", fontSize: "1.125rem" }
    borderRadius: "10px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "rgba(255, 255, 255, 0.7)"
    color: "#1a3a4a"
    border: "1px solid rgba(92, 184, 230, 0.3)"
    borderRadius: "10px"
    padding: "10px 14px"
    focusBorder: "1px solid #5cb8e6"
    placeholderColor: "#7a98a8"
  card:
    base:
      background: "rgba(255, 255, 255, 0.55)"
      border: "1px solid rgba(255, 255, 255, 0.5)"
      borderRadius: "14px"
      padding: "24px"
      shadow: "0 4px 16px rgba(26, 58, 74, 0.08)"
    hover:
      shadow: "0 8px 28px rgba(26, 58, 74, 0.14)"
      transform: "translateY(-2px)"
---

# Frutiger Aero 2007

> Glossy techno-optimism — sky-blue glass, photorealistic nature, and the hopeful glow of mid-2000s consumer technology.

## Origin

Frutiger Aero is the retroactively named design aesthetic that dominated consumer technology from approximately 2004 to 2013, peaking between 2006 and 2010. The name pays homage to Swiss typographer Adrian Frutiger, whose humanist typeface family became the typographic backbone of this era. Windows Vista's "Aero" theme (2007), Nintendo's Wii Channel interface (2006), Sky Sports broadcast graphics, and the BBC iPlayer launch screen all share its DNA: translucent glass surfaces floating over photorealistic skies, blue-green gradients suggesting water and air, and an earnest belief that technology and nature were converging.

The aesthetic emerged during the rise of HD broadcasting and broadband internet, reflecting a post-Y2K optimism about technology's place in daily life. Vitaminwater bottles, PowerAde packaging, Aquafresh branding, and the iPod nano campaigns all spoke the same glossy visual language. When Apple launched iOS 7 in 2013 with its radical flat redesign, Frutiger Aero's reign ended almost overnight. Today it survives as a powerful nostalgia trigger on TikTok and Tumblr, where Gen Z has embraced it as a symbol of the internet's more innocent era.

## Overview
Composition cues:
- **Layout**: Flex-based layouts with generous whitespace and centered content blocks, evoking the dashboard feel of Wii Channels and Vista sidebar gadgets.
- **Content width**: Container-width (1024–1280px) with airy margins — the sky should breathe around the content.
- **Framing**: Glassy — translucent frosted-glass panels floating over sky-gradient backgrounds with subtle backdrop blur.
- **Grid intensity**: Soft — elements are clearly organized but the grid is invisible; alignment is felt, not drawn.

## Colors
The Frutiger Aero palette is built on the colors of an idealized daytime sky: cerulean blues, mint greens, and white cloud highlights. The signature combination of sky blue (#5cb8e6) and mint green (#95d6c0) creates that distinctive fresh, watery optimism. Silver (#d6dde0) adds a metallic tech sheen. Backgrounds are always light — typically a gentle sky gradient from pale blue at the top to near-white at the bottom. Colors are vibrant but never neon; think sunlit water, not blacklight posters.

**Role usage**:
- Page background → `colors.background.page` (pale sky blue #f0f8fc)
- Card / panel surfaces → `colors.background.surface` (translucent white at 65% opacity)
- Primary actions (buttons, links) → `colors.primary.400` (#5cb8e6)
- Secondary accent → `colors.secondary.300` (#95d6c0)
- Metallic UI chrome → `colors.accent.200` (#d6dde0)
- Body text → `colors.text.primary` (deep teal-gray #1a3a4a)
- Muted labels → `colors.text.muted` (#7a98a8)
- Success / error / warning → `colors.semantic.*`

## Typography
Typography in Frutiger Aero is warm, rounded, and humanist — the typographic equivalent of a friendly handshake. The original era used Frutiger, Myriad Pro, and Segoe UI; modern equivalents like Nunito and Lato carry the same approachable DNA. Headings use Nunito's rounded terminals for that soft, inviting quality, while body text in Lato provides excellent readability with a hint of warmth. Letter-spacing is normal to slightly tight — nothing cramped, nothing sprawling.

**Text styles**:
- `display-xl` — Nunito, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Nunito, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Nunito, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Lato, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Lato, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Lato, 12px, weight 400, line-height 1.5, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 8px rhythm, consistent with the relaxed but organized feel of dashboard-style layouts.
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container max-widths: 640 / 768 / 1024 / 1280px.
- Section padding: 32px (sm) to 128px (xl) — generous vertical breathing room to let the sky gradient show through.
- Grid gaps: 8–48px depending on density; cards prefer 24px gaps for that airy, floating quality.

## Elevation & Depth
Frutiger Aero's materiality is all about glass and light. Surfaces feel like frosted panes suspended in front of a luminous sky — semi-transparent, softly blurred, catching highlights at their edges. The shadow ladder is subtle and warm-toned (teal-tinted blacks rather than pure gray), creating depth without heaviness. The inset shadow on inputs mimics the concave surface of a glass button pressed into its frame.

- Surface style: glass — translucent white (55–70% opacity) with backdrop-filter blur.
- Blur: 12px default backdrop blur on glass surfaces.
- Shadow ladder: xs (1px ambient) → sm (2px) → md (4px lift) → lg (8px float) → xl (16px elevated) → 2xl (24px hero).
- Focus ring: 3px spread of primary blue at 40% alpha — a soft blue glow.

## Shapes
- Card corners: 14px — generously rounded but not pill-shaped.
- Button corners: 10px — softer than modern flat buttons, matching the era's bubbly aesthetic.
- Input corners: 10px — consistent with buttons.
- Badge / pill corners: 9999px (full rounding).
- Small elements (checkboxes, chips): 6px.

## Motion
Frutiger Aero is lively and responsive — surfaces shimmer on hover, buttons lift like glass panes catching light, and transitions carry a slight springiness that reflects the era's playful optimism. Nothing is instantaneous (that feels flat); nothing lingers (that feels heavy). The sweet spot is a buoyant 250ms ease-out with optional spring overshoot for delightful interactions.

- Level: lively — surfaces respond eagerly to interaction.
- Durations: instant (0ms), fast (120ms for micro-feedback), normal (250ms for most transitions), slow (400ms for panel reveals), slower (600ms for page-level entrances).
- Easings: default ease-out for most, spring cubic-bezier(0.34, 1.56, 0.64, 1) for playful bounces on hover-lift.
- Hover patterns: lift (translateY -2px), glow (box-shadow expansion), scale (1.02x subtle zoom).
- Reduced motion: respected — falls back to opacity-only transitions.

## Techniques

### Aero Glass Panel
Frosted glass surface effect — the hallmark of Windows Vista's Aero and the entire era's UI language.
```css
.aero-glass {
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-top: 1px solid rgba(255, 255, 255, 0.7);
  box-shadow: 0 4px 16px rgba(26, 58, 74, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.6);
  border-radius: 14px;
}
```

### Sky Gradient Background
The iconic Frutiger Aero sky — a multi-stop gradient with optional radial cloud highlights.
```css
.sky-background {
  background:
    radial-gradient(ellipse at 30% 20%, rgba(255, 255, 255, 0.6) 0%, transparent 50%),
    radial-gradient(ellipse at 70% 40%, rgba(149, 214, 192, 0.15) 0%, transparent 40%),
    linear-gradient(180deg, #c8e0f0 0%, #e4f0f8 40%, #f0f8fc 100%);
  min-height: 100vh;
}
```

### Glossy Gradient Button
Multi-stop gradient button with white highlight inset — the quintessential Frutiger Aero interactive element.
```css
.glossy-button {
  background: linear-gradient(180deg, #7ac8ec 0%, #5cb8e6 40%, #3a9fd4 100%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 2px 8px rgba(58, 159, 212, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.4);
  color: #fff;
  border-radius: 10px;
  font-weight: 600;
  transition: all 250ms cubic-bezier(0, 0, 0.2, 1);
}
.glossy-button:hover {
  background: linear-gradient(180deg, #8fd2f0 0%, #6ec2ea 40%, #4aabdc 100%);
  box-shadow: 0 4px 14px rgba(58, 159, 212, 0.4),
              inset 0 1px 0 rgba(255, 255, 255, 0.5);
  transform: translateY(-1px);
}
```

## Iconography
Icons in Frutiger Aero should feel light, friendly, and slightly rounded — matching the humanist typography. Linear (outline) icons work best against the translucent glass surfaces, as filled icons can feel too heavy against the delicate backdrops. A 1.5px stroke weight balances visibility with the era's characteristic softness.

- Treatment: linear (outline) — crisp but gentle.
- Set: Lucide — rounded terminals echo the humanist type feel.
- Stroke: 1.5px — visible without heaviness.

## Do's & Don'ts

### Do
- Use multi-stop gradients on buttons and key UI elements — flat fills break the illusion.
- Apply frosted glass (backdrop-filter blur) to card surfaces floating over the sky gradient.
- Keep the palette anchored in sky blue (#5cb8e6) and mint green (#95d6c0).
- Use generous border-radius (10–14px) for that soft, bubbly feel.
- Let the background sky gradient breathe — avoid cluttering the page with too many opaque surfaces.

### Don't
- Use flat, solid-color fills without any gradient or glass treatment (post-2013 flat aesthetic).
- Apply pure black backgrounds or dark mode — Frutiger Aero is always sky-bright.
- Use brutalist or raw HTML styling — exposed grids, system fonts, harsh borders.
- Choose earthy, muted, or desaturated palettes — the vibe is aquatic and luminous.
- Use sharp rectangular corners (0px radius) — everything should feel rounded and approachable.

## Applications
Frutiger Aero is ideal for product landing pages, media dashboards, weather and lifestyle apps, and any interface that wants to evoke friendly, approachable technology. It works beautifully for portfolio sites, SaaS onboarding flows, and consumer-facing tools where trust and warmth matter more than stark minimalism. The style particularly shines in hero sections, feature showcases, and card-grid layouts where glass panels can float over luminous sky backgrounds.
