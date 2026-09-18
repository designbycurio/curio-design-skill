---
version: 1

meta:
  id: moroccan-majorelle-blue
  name: Jardin Majorelle Blue
  description: Immersive electric-cobalt stucco struck by hot Saharan light, jeweled green and glazed yellow against painted Marrakech walls.
  isDark: true
  tags: [bold, historical, decorative, warm, organic]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1900–1950 (villa and the trademarked blue developed 1920s–1930s)"
  region: "Marrakech, Morocco"
  regionZh: "摩洛哥马拉喀什"
  keyFigures: [Jacques Majorelle, Yves Saint Laurent, Pierre Bergé]
  movements: [Orientalist / North African modernism, Art Deco-era botanical garden design]

introduction: |
  The Jardin Majorelle is the cobalt-painted garden villa that French painter Jacques Majorelle built in
  Marrakech across the 1920s and 1930s, later rescued and restored by Yves Saint Laurent and Pierre Bergé.
  Its signature is an immersive, saturated electric blue stucco — Majorelle Blue — coating walls, planters,
  and trellises.

  Against that cobalt the garden sets cactus green, glazed-yellow terracotta pots, and bare earth. This is
  North African modernism: hot Saharan light striking deep, jewel-toned painted surfaces with a chalky matte
  finish. The mood is decorative, confident, and unapologetically maximal.
introductionZh: |
  马若雷勒花园是法国画家雅克·马若雷勒在 1920 至 1930 年代于马拉喀什营造的钴蓝色别墅花园，后由伊夫·圣罗兰与皮埃尔·贝尔热购下修复。
  它最鲜明的标志，是那一种饱和到近乎发电的电光钴蓝——「马若雷勒蓝」——被刷在墙体、花盆与棚架之上，把整座园子浸入同一片蓝里。

  钴蓝之上，仙人掌的青绿、上釉陶罐的明黄、裸露陶土的橙赭彼此碰撞，被撒哈拉炽烈的阳光逼出最浓的色相。这是北非现代主义：
  灼热的光打在深色的、手刷的、带白垩哑光质感的墙面上。它的气质是装饰的、笃定的、毫不收敛的繁盛。

colors:
  primary:    {"50": "#EEECFB", "100": "#D8D3F6", "200": "#B4ABEE", "300": "#9082E6", "400": "#7869E1", "500": "#6050DC", "600": "#4636C4", "700": "#372A99", "800": "#28206E", "900": "#1A1547", "950": "#0E0B28"}
  secondary:  {"50": "#EBF5EF", "100": "#CFE7D9", "200": "#A1D0B5", "300": "#71B98F", "400": "#52A275", "500": "#3E8E5A", "600": "#327449", "700": "#275A39", "800": "#1B3F28", "900": "#102718", "950": "#08160D"}
  accent:     {"50": "#FCF5E6", "100": "#F8E8C2", "200": "#F2D389", "300": "#ECC15B", "400": "#E8B23A", "500": "#D89C25", "600": "#B07D1B", "700": "#875F16", "800": "#5E420F", "900": "#392808", "950": "#1D1404"}
  neutral:    {"50": "#EDF0F7", "100": "#D4DAEA", "200": "#A7B3D2", "300": "#7B8CB8", "400": "#56689A", "500": "#3D4D7C", "600": "#2E3A60", "700": "#222C49", "800": "#171E33", "900": "#0E1320", "950": "#070A12"}
  semantic:
    success: { bg: "#1B3F28", text: "#A1D0B5", light: "#102718", border: "#3E8E5A" }
    warning: { bg: "#5E420F", text: "#F2D389", light: "#392808", border: "#E8B23A" }
    error:   { bg: "#5A1E0C", text: "#F0A988", light: "#3A1207", border: "#C8551F" }
    info:    { bg: "#28206E", text: "#B4ABEE", light: "#1A1547", border: "#6050DC" }
  background:
    page:    "#1E40A6"
    surface: "#1A368E"
    subtle:  "#16307E"
  text:
    primary:   "#F4F6FD"
    secondary: "#C7D0EE"
    muted:     "#8E9CD4"
    inverse:   "#0F2A6B"

typography:
  families:
    heading: "'Poppins', 'Noto Sans Arabic', system-ui, sans-serif"
    body:    "'Questrial', 'Poppins', system-ui, sans-serif"
    mono:    "'Cinzel', 'Poppins', serif"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Questrial&family=Cinzel:wght@400;600;700&family=Noto+Sans+Arabic:wght@400;500;700&display=swap"
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
  radius: {none: "0", sm: "3px", md: "6px", lg: "12px", xl: "20px", full: "9999px"}
  color:  {default: "#2E3A60", subtle: "#28206E", strong: "#6050DC", focus: "#E8B23A"}
  width:  {thin: "1px", default: "1px", thick: "2px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(15,42,107,0.30)"
  sm: "0 2px 6px rgba(15,42,107,0.40)"
  md: "0 6px 18px rgba(15,42,107,0.45)"
  lg: "0 16px 40px rgba(15,42,107,0.50)"
  xl: "0 28px 64px rgba(15,42,107,0.55)"
  "2xl": "0 40px 96px rgba(15,42,107,0.60)"
  inner: "inset 0 1px 2px rgba(15,42,107,0.35)"
  focus: "0 0 0 3px rgba(232,178,58,0.55)"

motion:
  level: restrained
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, glow, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       solid
  gridIntensity: strong
  rhythm:        "4px"

surfaceStyle: solid
blur:         none

iconography:
  treatment: linear
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "1.5px"

components:
  button:
    primary:   {background: "#6050DC", color: "#F4F6FD", border: "1px solid #6050DC", shadow: "0 6px 18px rgba(15,42,107,0.45)", hoverBackground: "#7869E1", hoverShadow: "0 16px 40px rgba(96,80,220,0.45)", hoverColor: "#FFFFFF"}
    secondary: {background: "#E8B23A", color: "#1A1547", border: "1px solid #E8B23A", shadow: "0 6px 18px rgba(15,42,107,0.40)", hoverBackground: "#ECC15B", hoverShadow: "0 16px 40px rgba(232,178,58,0.40)", hoverColor: "#0E0B28"}
    ghost:     {background: "transparent", color: "#C7D0EE", border: "1px solid #2E3A60", shadow: "none", hoverBackground: "rgba(96,80,220,0.18)", hoverShadow: "none", hoverColor: "#F4F6FD"}
    danger:    {background: "#C8551F", color: "#FCEFE8", border: "1px solid #C8551F", shadow: "0 6px 18px rgba(15,42,107,0.40)", hoverBackground: "#DC6A33", hoverShadow: "0 16px 40px rgba(200,85,31,0.40)", hoverColor: "#FFFFFF"}
    sizes:     {sm: {height: "34px", padding: "0 14px", fontSize: "0.875rem"}, md: {height: "42px", padding: "0 20px", fontSize: "1rem"}, lg: {height: "52px", padding: "0 28px", fontSize: "1.125rem"}}
    borderRadius: "6px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "none"
  input:
    background: "#16307E"
    color: "#F4F6FD"
    border: "1px solid #2E3A60"
    borderRadius: "6px"
    padding: "10px 14px"
    focusBorder: "1px solid #E8B23A"
    placeholderColor: "#8E9CD4"
  card:
    base:  {background: "#1A368E", border: "1px solid #28206E", borderRadius: "12px", padding: "24px", shadow: "0 6px 18px rgba(15,42,107,0.45)"}
    hover: {shadow: "0 16px 40px rgba(15,42,107,0.50)", transform: "translateY(-4px)"}
---

# Jardin Majorelle Blue

> Immersive electric cobalt struck by Saharan light — Marrakech's painted garden in pigment form.

## Origin

The Jardin Majorelle was built in Marrakech by the French painter Jacques Majorelle, who began the villa and its gardens in the 1920s and spent the 1930s developing the immersive cobalt that would carry his name. He trademarked "Majorelle Blue" — an intense, near-electric ultramarine — and painted it across the garden's walls, planters, pergolas, and trellises until the architecture itself became a single saturated field of color. The blue was deliberately set against the greens of cactus and bamboo and the warm earth of bare terracotta.

After decades of decline the garden was bought and restored by fashion designer Yves Saint Laurent and Pierre Bergé in 1980, who preserved Majorelle's palette and later sited the Musée Yves Saint Laurent beside it. The aesthetic belongs to North African modernism and the Art Deco era of botanical garden design: Orientalist in subject, modern in its flat painted geometry, and built for the specific quality of hot, hard Moroccan sun.

## Overview
Composition cues:
- **Layout**: Structured grid with strong vertical rhythm, echoing rows of cylindrical planters and slatted trellis.
- **Content width**: Container-bound; generous painted margins of pure cobalt around content blocks.
- **Framing**: Solid panels in deeper cobalt surfaces — no glass, no transparency washes.
- **Grid intensity**: Strong — visible alignment, repeated modules, lattice-inspired dividers.

## Colors
The whole identity is immersion: a deep cobalt-painted wall (`#1E40A6`) as the page itself, with the brighter trademarked Majorelle Blue (`#6050DC`) reserved for active surfaces and primary actions. Warm jewel tones — cactus green, glazed-pot yellow, terracotta earth — are placed sparingly and at full saturation, the way bright objects punctuate the blue garden under direct sun. Never desaturate toward powder blue; the contrast of hot accents on deep cobalt is the point.

**Role usage**:
- Page background → `colors.background.page` (`#1E40A6`)
- Raised surfaces & cards → `colors.background.surface` (`#1A368E`)
- Primary actions & links → `colors.primary.500` (`#6050DC`)
- Highlight / glazed-yellow accents → `colors.accent.400` (`#E8B23A`)
- Botanical / success tones → `colors.secondary.500` (`#3E8E5A`)
- Terracotta / danger tones → `#C8551F`
- Primary body text → `colors.text.primary` (`#F4F6FD`)
- Deepest shadow cobalt → `#0F2A6B`

## Typography
Geometric and clean, the type stays calm so color can shout. Poppins carries display and headings with confident geometric weight; Questrial gives body copy a light, even texture; Cinzel supplies engraved label caps reminiscent of museum plaques; Noto Sans Arabic enables authentic bilingual headings.

**Text styles**:
- `display-xl` — Poppins, 96px, weight 700, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Poppins, 64px, weight 700, line-height 1.05, letter-spacing -0.03em
- `heading-1` — Poppins, 36px, weight 600, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Questrial, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Questrial, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Cinzel, 12px, weight 600, line-height 1.4, letter-spacing 0.05em, uppercase
- `mono-md` — Cinzel, 15px, weight 400, line-height 1.5, letter-spacing 0.05em

## Spacing & Layout
- Base unit: 4px; scale runs 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px.
- Container max widths: sm 640 / md 768 / lg 1024 / xl 1280px.
- Section padding scales from 32px (sm) to 128px (xl) for airy, sunlit blocks.
- Grid gaps 8–48px; favor consistent vertical rhythm like planted rows.

## Elevation & Depth
Surfaces are flat painted stucco, not glass: depth comes from layering darker cobalt panels and dropping warm-free, deep-blue shadows as if cast by hard noon sun. No backdrop blur, no translucency.
- Surface style: solid painted panels on a deeper cobalt page.
- Blur: none.
- Shadow ladder: xs hairline → 2xl deep cast, all tinted with `rgba(15,42,107,…)`.

## Shapes
- Corner radii: sm 3px, md 6px (buttons/inputs), lg 12px (cards), xl 20px (feature panels), full 9999px for pills.
- Keep corners modest — crisp painted edges over heavy rounding.

## Motion
Restrained and dignified: elements lift gently and accent edges glow, like sun catching glazed pottery. Nothing bounces frivolously; transitions feel like a slow shift of shadow across a wall.
- Level: restrained.
- Durations: 120ms fast → 600ms slower; default 250ms.
- Easings: default cubic-bezier(0.4,0,0.2,1); spring reserved for accents.
- Hover patterns: lift, glow, tint.

## Techniques

### Painted-stucco chalky surface
A matte, faintly mottled cobalt fill that reads as hand-painted plaster rather than flat UI.
```css
.stucco {
  background-color: #1E40A6;
  background-image:
    radial-gradient(circle at 20% 30%, rgba(96,80,220,0.10) 0, transparent 45%),
    radial-gradient(circle at 80% 70%, rgba(15,42,107,0.22) 0, transparent 55%);
  background-blend-mode: overlay;
}
```

### Zellige / mashrabiya lattice divider
A repeating geometric lattice line evoking carved screens and tilework.
```css
.lattice {
  height: 14px;
  background-image:
    linear-gradient(45deg, #E8B23A 25%, transparent 25%, transparent 75%, #E8B23A 75%),
    linear-gradient(45deg, #E8B23A 25%, transparent 25%, transparent 75%, #E8B23A 75%);
  background-size: 14px 14px;
  background-position: 0 0, 7px 7px;
  opacity: 0.85;
}
```

### Glazed-pot accent ridge
A warm yellow top edge with a soft glow, like the rim-light on a row of terracotta planters.
```css
.glazed-edge {
  border-top: 3px solid #E8B23A;
  box-shadow: 0 -2px 14px rgba(232,178,58,0.35);
}
```

## Iconography
Use clean linear icons with a consistent 1.5px stroke, kept simple and geometric to sit quietly against saturated color. Botanical and garden-adjacent glyphs (leaves, vessels, sun) suit the theme. Phosphor's regular weight is the default set.
- Treatment: linear.
- Set: phosphor.
- Stroke: 1.5px.

## Do's & Don'ts
### ✓ Do
- Use immersive cobalt `#1E40A6` as the page itself, edge to edge.
- Reserve Majorelle Blue `#6050DC` for primary actions and active surfaces.
- Place glazed-yellow, cactus-green, and terracotta accents at full saturation and sparingly.
- Keep surfaces flat and chalky like painted stucco; let hard shadows carry depth.
- Pair clean geometric Poppins/Questrial type with engraved Cinzel caps for contrast.

### ✗ Don't
- Never use cream, ivory, or plain-white backgrounds.
- Don't desaturate to a pale "powder blue" — keep the electric cobalt.
- Avoid generic Mediterranean tile clichés or whitewashed Santorini palettes.
- No corporate flat-UI gradients; preserve the chalky painted-stucco character.

## Applications
Best for bold, image-forward landing pages, cultural and travel storytelling, gallery or museum microsites, and brand work that wants saturated confidence. The deep immersive field suits hero-driven layouts and editorial features where color carries the mood.
