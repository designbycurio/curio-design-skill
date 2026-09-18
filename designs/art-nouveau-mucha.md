---
version: 1

meta:
  id: art-nouveau-mucha
  name: Art Nouveau (Mucha)
  description: "Turn-of-century botanical ornament — sinuous organic curves, muted lithographic colors, and Mucha's halo-framed poster elegance"
  isDark: false
  tags: [decorative, organic, historical, luxurious]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "~1890–1910; peak poster output 1894–1904"
  region: "Paris, Brussels, Vienna, Prague, Glasgow"
  regionZh: "法国巴黎、比利时布鲁塞尔、奥地利维也纳、捷克布拉格、苏格兰格拉斯哥"
  keyFigures: [Alphonse Mucha, Hector Guimard, Gustav Klimt, Aubrey Beardsley]
  movements: [Art Nouveau, British Arts & Crafts, Jugendstil, Vienna Secession]

introduction: |
  Art Nouveau was the dominant decorative movement at the turn of the 20th century, rejecting Victorian rigidity in favor of long, sinuous lines drawn from natural forms — flowers, vines, flowing hair, and water. Alphonse Mucha's elaborate theatre posters, with their botanical halos and muted lithographic palettes, remain the movement's most recognizable graphic expression.

  This design system translates that sensibility into interface tokens: warm cream grounds recalling lithograph paper, muted sage and rose accents, ornamental serif typography, and flowing curves that echo whiplash arabesques. Every element favors organic elegance over mechanical precision.
introductionZh: |
  新艺术运动是二十世纪之交最具影响力的装饰风格，以源自花卉、藤蔓、流水的蜿蜒有机线条取代维多利亚时代的刻板几何。捷克裔法国艺术家阿尔丰斯·穆夏为莎拉·伯恩哈特创作的剧院海报——以植物光环和柔和石版印刷色调闻名——至今仍是该运动最具辨识度的视觉符号。

  这套设计系统将穆夏的美学精髓转化为界面语汇：温暖的奶油色底色如同石版画纸张，灰绿与灰玫瑰的柔和点缀，装饰性衬线字体的优雅流动，以及呼应鞭线式阿拉伯花纹的有机曲线——每一个元素都追求自然的典雅而非机械的精确。

colors:
  primary:
    "50": "#F2F5EF"
    "100": "#DFE6D8"
    "200": "#C2D0B5"
    "300": "#A3B891"
    "400": "#8FA17D"
    "500": "#7a8b6a"
    "600": "#68785A"
    "700": "#55634A"
    "800": "#434E3B"
    "900": "#313A2C"
    "950": "#1F251C"
  secondary:
    "50": "#F9F2F2"
    "100": "#F0DCDC"
    "200": "#E2C0C0"
    "300": "#D4A5A5"
    "400": "#C89C9C"
    "500": "#c89494"
    "600": "#AD7A7A"
    "700": "#8F6363"
    "800": "#704D4D"
    "900": "#523838"
    "950": "#352424"
  accent:
    "50": "#FBF8EF"
    "100": "#F5EDD6"
    "200": "#ECDCB0"
    "300": "#E0C884"
    "400": "#D4B35E"
    "500": "#C4993E"
    "600": "#A57E32"
    "700": "#846428"
    "800": "#644B1E"
    "900": "#453415"
    "950": "#2B200D"
  neutral:
    "50": "#F5EDD6"
    "100": "#EDE4C8"
    "200": "#DDD2B0"
    "300": "#C5B898"
    "400": "#A89E82"
    "500": "#8B846E"
    "600": "#6E6A5A"
    "700": "#525046"
    "800": "#3A3832"
    "900": "#24221F"
    "950": "#141310"
  semantic:
    success: { bg: "#EFF5EC", text: "#3D6B2E", light: "#F5FAF2", border: "#A3B891" }
    warning: { bg: "#FBF5E8", text: "#8B6A1E", light: "#FDF9F0", border: "#E0C884" }
    error: { bg: "#F9EFEF", text: "#8B3A3A", light: "#FCF5F5", border: "#D4A5A5" }
    info: { bg: "#EFF2F5", text: "#3A5A7A", light: "#F5F7FA", border: "#9BB5CF" }
  background:
    page: "#f5edd6"
    surface: "#FEFBF2"
    subtle: "#EDE4C8"
  text:
    primary: "#2C2418"
    secondary: "#5A5040"
    muted: "#8B846E"
    inverse: "#F5EDD6"

typography:
  families:
    heading: "'Cormorant Garamond', 'Georgia', serif"
    body: "'Lora', 'Georgia', serif"
    mono: "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=JetBrains+Mono:wght@400;500;700&display=swap"
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
    sm: "4px"
    md: "8px"
    lg: "12px"
    xl: "16px"
    full: "9999px"
  color:
    default: "#C5B898"
    subtle: "#DDD2B0"
    strong: "#8B846E"
    focus: "#7a8b6a"
  width:
    thin: "1px"
    default: "1px"
    thick: "2px"
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(44,36,24,0.05)"
  sm: "0 2px 4px rgba(44,36,24,0.08)"
  md: "0 4px 12px rgba(44,36,24,0.10)"
  lg: "0 8px 24px rgba(44,36,24,0.12)"
  xl: "0 16px 40px rgba(44,36,24,0.14)"
  "2xl": "0 24px 56px rgba(44,36,24,0.16)"
  inner: "inset 0 1px 2px rgba(44,36,24,0.04)"
  focus: "0 0 0 3px rgba(122,139,106,0.35)"

motion:
  level: "restrained"
  durations:
    instant: "0ms"
    fast: "120ms"
    normal: "250ms"
    slow: "400ms"
    slower: "600ms"
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.22, 1, 0.36, 1)"
  hoverPatterns: [opacity, underline, tint]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "container"
  framing: "bordered"
  gridIntensity: "subtle"
  rhythm: "8px"

surfaceStyle: "layered"
blur: "none"

iconography:
  treatment: "linear"
  set: "lucide"
  size:
    sm: "16px"
    md: "20px"
    lg: "24px"
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#7a8b6a"
      color: "#F5EDD6"
      border: "1px solid #7a8b6a"
      shadow: "0 2px 4px rgba(44,36,24,0.08)"
      hoverBackground: "#68785A"
      hoverShadow: "0 4px 12px rgba(44,36,24,0.12)"
      hoverColor: "#F5EDD6"
    secondary:
      background: "transparent"
      color: "#7a8b6a"
      border: "1px solid #7a8b6a"
      shadow: "none"
      hoverBackground: "rgba(122,139,106,0.08)"
      hoverShadow: "none"
      hoverColor: "#55634A"
    ghost:
      background: "transparent"
      color: "#5A5040"
      border: "1px solid transparent"
      shadow: "none"
      hoverBackground: "rgba(122,139,106,0.06)"
      hoverShadow: "none"
      hoverColor: "#2C2418"
    danger:
      background: "#8B3A3A"
      color: "#F5EDD6"
      border: "1px solid #8B3A3A"
      shadow: "none"
      hoverBackground: "#A04545"
      hoverShadow: "0 4px 12px rgba(139,58,58,0.2)"
      hoverColor: "#F5EDD6"
    sizes:
      sm: { height: "32px", padding: "0 14px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 20px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 28px", fontSize: "1.125rem" }
    borderRadius: "8px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FEFBF2"
    color: "#2C2418"
    border: "1px solid #C5B898"
    borderRadius: "8px"
    padding: "10px 14px"
    focusBorder: "1px solid #7a8b6a"
    placeholderColor: "#8B846E"
  card:
    base:
      background: "#FEFBF2"
      border: "1px solid #C5B898"
      borderRadius: "12px"
      padding: "24px"
      shadow: "0 4px 12px rgba(44,36,24,0.10)"
    hover:
      shadow: "0 8px 24px rgba(44,36,24,0.14)"
      transform: "translateY(-2px)"
---

# Art Nouveau (Mucha)

> Sinuous botanical ornament and muted lithographic color on warm cream — the graphic elegance of Mucha's poster art rendered as a design system.

## Origin

Art Nouveau ("New Art") emerged in the 1890s as a pan-European rejection of Victorian historicism, drawing its formal vocabulary from the natural world: the curve of a vine tendril, the spiral of a nautilus shell, the cascade of loosened hair. The movement found its graphic apotheosis in the work of Alphonse Mucha, a Czech artist working in Paris, whose 1894 poster for Sarah Bernhardt's *Gismonda* launched both his career and the modern decorative poster. Mucha's signature — women framed by circular halos of botanical ornament, printed in soft lithographic tones on cream paper — became synonymous with the entire movement.

Art Nouveau flourished simultaneously across Europe under regional names: Jugendstil in Germany, Modernisme in Barcelona (Gaudí), Sezessionstil in Vienna (Klimt, Olbrich). Hector Guimard's sinuous cast-iron Paris Métro entrances, Émile Gallé's cameo glass, and Aubrey Beardsley's ink illustrations extended the idiom into architecture, craft, and publishing. By 1910, the style's ornamental exuberance was yielding to the geometric severity of early modernism, and World War I would bury it entirely — but its influence on graphic design, illustration, and decorative arts has never fully receded.

## Overview
Composition cues:
- **Layout**: Centered stacked compositions framed by ornamental borders, echoing poster cartouche layouts
- **Content width**: Container-bound (max 1024–1280px), centered with generous margins
- **Framing**: Bordered — decorative double-rule borders, ornamental corner flourishes, and subtle botanical dividers
- **Grid intensity**: Subtle — structure serves content but never dominates; organic asymmetry within ordered frames

## Colors
The palette is a lithographer's workshop: warm cream paper as the ground, muted sage greens and dusty roses as the organic accents, ochre gold for ornamental highlights. Every color feels hand-mixed and slightly desaturated, as if applied by stone-printed ink rather than digital precision. The overall impression is warm, earthy, and gentle — never garish, never cold.

**Role usage**:
- Page background → `colors.background.page` (#f5edd6 warm cream)
- Card / surface panels → `colors.background.surface` (#FEFBF2 lighter cream)
- Subtle dividers and inset backgrounds → `colors.background.subtle` (#EDE4C8)
- Primary body text → `colors.text.primary` (#2C2418 warm dark brown)
- Secondary text → `colors.text.secondary` (#5A5040)
- Muted labels and captions → `colors.text.muted` (#8B846E)
- Primary interactive accent → `colors.primary.500` (#7a8b6a sage green)
- Secondary accent → `colors.secondary.500` (#c89494 dusty rose)
- Ornamental highlights → `colors.accent.500` (#C4993E ochre gold)

## Typography
The typographic voice is an ornamental serif whisper — elegant, historical, and warm. Display headlines use Cormorant Garamond in italic weights, a high-contrast serif that channels the calligraphic flourishes of Mucha's hand-drawn letterforms without requiring a novelty face. Body text is set in Lora, a warm contemporary serif with gentle curves that read clearly at paragraph length while maintaining the organic warmth of the system. The pairing avoids the rigidity of geometric sans-serifs entirely — every letterform bends and breathes.

**Text styles**:
- `display-xl` — Cormorant Garamond, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Cormorant Garamond, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Cormorant Garamond, 48px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Lora, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Lora, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Lora, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px; primary rhythm on an 8px grid
- Spacing scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1024px (lg) to 1280px (xl), centered
- Section padding: 64–96px vertical, generous breathing room that lets ornamental borders and botanical motifs frame content without crowding
- Cards use 24px internal padding with warm-toned borders

## Elevation & Depth
Depth is achieved through warm-toned layering rather than cold drop shadows or transparency. The material metaphor is hand-pressed paper stock — surfaces sit atop the cream ground like overlaid lithograph prints, separated by subtle warm shadows that suggest physical stacking rather than digital floating.

- Surface style: Layered opaque cream panels (#FEFBF2 on #f5edd6)
- Blur: None — glass effects contradict the hand-printed materiality
- Shadow ladder: xs (barely perceptible) → sm → md (card default) → lg → xl → 2xl, all using warm brown rgba(44,36,24,_) rather than pure black
- Focus ring: `0 0 0 3px rgba(122,139,106,0.35)` — a soft sage green halo

## Shapes
- Button border-radius: 8px (elegantly rounded, never sharp-cornered)
- Card border-radius: 12px (softly organic)
- Input border-radius: 8px
- General: radii between 4–16px; sharp 0px corners are avoided as anti-Nouveau
- Ornamental corner flourishes may overlay radii on hero and feature sections

## Motion
Motion is restrained and graceful — the unfurling of a fern frond, not a mechanical snap. Transitions favor slow opacity fades and gentle vertical lifts. Interactive elements respond with organic ease, as if guided by natural growth rather than spring physics. Nothing should feel abrupt or industrial.

- Level: Restrained
- Durations: fast 120ms (micro-interactions), normal 250ms (state changes), slow 400ms (reveals), slower 600ms (page transitions)
- Easings: default `cubic-bezier(0.4, 0, 0.2, 1)`, spring `cubic-bezier(0.22, 1, 0.36, 1)` for gentle lifts
- Hover patterns: opacity fade, underline reveal, subtle tint shift toward sage or rose
- Reduced-motion: fully supported — all animation respects `prefers-reduced-motion`

## Techniques

### Ornamental Botanical Border
A double-rule border with decorative corner accents evoking Mucha's poster cartouches — the ornamental frame that makes content feel like a hand-printed lithograph panel.
```css
.botanical-border {
  position: relative;
  border: 2px solid #C5B898;
  outline: 1px solid #DDD2B0;
  outline-offset: 4px;
  padding: 32px;
  border-radius: 12px;
}
.botanical-border::before,
.botanical-border::after {
  content: "❦"; /* floral heart */
  position: absolute;
  font-size: 20px;
  color: #7a8b6a;
  opacity: 0.5;
}
.botanical-border::before {
  top: -4px;
  left: 16px;
}
.botanical-border::after {
  bottom: -4px;
  right: 16px;
}
```

### Dusty Rose Watercolor Wash
A subtle gradient background that mimics the hand-tinted washes in Mucha's lithographic prints — soft rose bleeding into cream, applied to hero sections and feature panels.
```css
.watercolor-wash {
  background: linear-gradient(
    135deg,
    rgba(200, 148, 148, 0.12) 0%,
    rgba(245, 237, 214, 0) 40%,
    rgba(122, 139, 106, 0.08) 100%
  );
  border-radius: 12px;
}
```

### Art Nouveau Halo Frame
A circular ornamental frame inspired by Mucha's signature halo motif — used for avatars, featured images, or decorative section accents.
```css
.halo-frame {
  position: relative;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  border: 2px solid #C5B898;
  box-shadow:
    0 0 0 6px #f5edd6,
    0 0 0 8px #7a8b6a,
    0 0 0 14px #f5edd6,
    0 0 0 15px #C5B898;
  overflow: hidden;
}
.halo-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## Iconography
Icons use a thin linear treatment — clean outlines that complement the ornamental serif typography without competing with it. The Lucide set provides geometric clarity that balances the flowing organic curves elsewhere in the system. Icons appear in muted brown (#5A5040) by default, shifting to sage green for active and interactive states.

- Treatment: Linear (outline only)
- Set: Lucide
- Stroke: 1.5px

## Do's & Don'ts

### ✓ Do
- Use Cormorant Garamond for all display-level headlines to maintain the ornamental serif identity
- Keep the palette within muted, desaturated lithographic tones — sage, rose, ochre, cream
- Frame content with decorative borders and ornamental flourishes that reference poster cartouches
- Favor organic, rounded shapes (8–16px radii) in all interactive elements
- Let sections breathe with generous vertical padding to create a gallery-like rhythm

### ✗ Don't
- Use pure black backgrounds — Art Nouveau lithographs lived on warm cream paper
- Employ geometric sans-serifs for any visible typography
- Introduce saturated or neon colors — muted and hand-mixed only
- Create sharp 90° angles in primary geometry — curves and organic forms are essential
- Apply industrial or mechanical motifs — those belong to Art Deco, not Art Nouveau

## Applications
Art Nouveau (Mucha) is ideally suited to cultural institution websites, art gallery portfolios, botanical garden platforms, artisanal craft marketplaces, luxury stationery brands, and editorial publications with a historical or decorative sensibility. It thrives wherever the audience values ornamental beauty, handcrafted quality, and a warm connection to natural forms — and where the warm cream palette and flowing serif typography will feel intentional rather than dated.
