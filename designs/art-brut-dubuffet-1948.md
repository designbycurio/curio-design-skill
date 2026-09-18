---
version: 1

meta:
  id: art-brut-dubuffet-1948
  name: "Art Brut (Dubuffet, 1948)"
  description: "Raw, obsessive mark-making on mud-brown grounds — asylum walls turned into design system"
  isDark: true
  tags: [experimental, hand-drawn, subcultural, organic, handmade]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1945–1976 (coined 1945, Collection founded 1948, Lausanne public 1976)"
  region: "France / Switzerland"
  regionZh: "法国 / 瑞士洛桑"
  keyFigures: [Jean Dubuffet, Adolf Wölfli, Aloïse Corbaz, Henry Darger]
  movements: [Art Brut, Outsider Art, anti-academic art]

introduction: |
  Art Brut — raw art — is the movement Jean Dubuffet founded in 1948 to champion work made outside the fine-art establishment: psychiatric patients, mediums, compulsive autodidacts. The visual language is dense, obsessive, and unapologetically crude — mud-brown grounds, oxblood marks, hand-lettered text crammed edge-to-edge with no breathing room. This design system channels that horror vacui energy into interfaces that feel handmade under duress, where every surface is filled and sophistication is the enemy.
introductionZh: |
  「原生艺术」是让·杜布菲1948年在巴黎发起的运动，为精神病院患者、灵媒和自学者的创作正名——反学院、反品味、反留白。泥棕色的墙面底色、牛血红的粗糙笔触、铅白色的手写字母挤满每一寸画面，像沃尔夫利两万五千页自传手稿那样密不透风。这套设计系统把那种「不是为画廊而画，是为了活下去而画」的原始冲动，变成了界面语言。

colors:
  primary:    {"50": "#F5E8E9", "100": "#EACDCF", "200": "#D49BA0", "300": "#BF6970", "400": "#A94C54", "500": "#722F37", "600": "#66292F", "700": "#4D1F24", "800": "#33151A", "900": "#1A0A0D", "950": "#0D0506"}
  secondary:  {"50": "#F0E8E3", "100": "#E1D1C7", "200": "#C3A38F", "300": "#A57557", "400": "#7D5A42", "500": "#5C4033", "600": "#52392D", "700": "#3E2B22", "800": "#291D17", "900": "#150E0B", "950": "#0A0706"}
  accent:     {"50": "#FBF2E5", "100": "#F7E5CB", "200": "#EFCB97", "300": "#E7B163", "400": "#D69B52", "500": "#C68642", "600": "#B2783B", "700": "#855A2C", "800": "#593C1E", "900": "#2C1E0F", "950": "#160F07"}
  neutral:    {"50": "#F0ECE6", "100": "#E1D9CD", "200": "#C3B39B", "300": "#A58D69", "400": "#6E5E44", "500": "#4A3F30", "600": "#3B322A", "700": "#2C2620", "800": "#1E1915", "900": "#1C1C1C", "950": "#0E0E0E"}
  semantic:
    success: { bg: "#7A8450", text: "#EFE7D2", light: "#8F9A62", border: "#6B7345" }
    warning: { bg: "#E0C547", text: "#1C1C1C", light: "#E8D06A", border: "#C9B03F" }
    error:   { bg: "#722F37", text: "#EFE7D2", light: "#8A3A43", border: "#5C2630" }
    info:    { bg: "#C68642", text: "#1C1C1C", light: "#D49B5A", border: "#A57236" }
  background:
    page:    "#5C4033"
    surface: "#1C1C1C"
    subtle:  "#722F37"
  text:
    primary:   "#EFE7D2"
    secondary: "#D5C7A3"
    muted:     "#A58D69"
    inverse:   "#1C1C1C"

typography:
  families:
    heading: "'Caveat', cursive"
    body:    "'Crimson Text', Georgia, serif"
    mono:    "'Courier Prime', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=Permanent+Marker&family=Courier+Prime&display=swap"
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
  radius: {none: "0", sm: "2px", md: "4px", lg: "6px", xl: "8px", full: "9999px"}
  color:  {default: "#5C4033", subtle: "#4A3F30", strong: "#EFE7D2", focus: "#C68642"}
  width:  {thin: "1px", default: "2px", thick: "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "1px 1px 0 rgba(28,28,28,0.4)"
  sm: "2px 2px 0 rgba(28,28,28,0.5)"
  md: "2px 2px 0 rgba(28,28,28,0.6)"
  lg: "3px 3px 0 rgba(28,28,28,0.6)"
  xl: "4px 4px 0 rgba(28,28,28,0.7)"
  "2xl": "6px 6px 0 rgba(28,28,28,0.7)"
  inner: "inset 1px 1px 0 rgba(28,28,28,0.3)"
  focus: "0 0 0 3px rgba(198,134,66,0.5)"

motion:
  level: "minimal"
  durations: {instant: "0ms", fast: "100ms", normal: "200ms", slow: "350ms", slower: "500ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.2, 1.2, 0.4, 1)"
  hoverPatterns: [opacity, tint]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "full-bleed"
  framing:       "bordered"
  gridIntensity: "none"
  rhythm:        "4px"

surfaceStyle: "solid"
blur:         "none"

iconography:
  treatment: "outline"
  set:       "tabler"
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#722F37", color: "#EFE7D2", border: "2px solid #EFE7D2", shadow: "2px 2px 0 rgba(28,28,28,0.6)", hoverBackground: "#5C2630", hoverShadow: "3px 3px 0 rgba(28,28,28,0.7)", hoverColor: "#EFE7D2"}
    secondary: {background: "#5C4033", color: "#EFE7D2", border: "2px solid #D5C7A3", shadow: "2px 2px 0 rgba(28,28,28,0.6)", hoverBackground: "#4A3328", hoverShadow: "3px 3px 0 rgba(28,28,28,0.7)", hoverColor: "#EFE7D2"}
    ghost:     {background: "transparent", color: "#EFE7D2", border: "2px solid transparent", shadow: "none", hoverBackground: "rgba(114,47,55,0.2)", hoverShadow: "none", hoverColor: "#EFE7D2"}
    danger:    {background: "#722F37", color: "#EFE7D2", border: "2px solid #EFE7D2", shadow: "2px 2px 0 rgba(28,28,28,0.6)", hoverBackground: "#5C2630", hoverShadow: "3px 3px 0 rgba(28,28,28,0.7)", hoverColor: "#EFE7D2"}
    sizes:     {sm: {height: "32px", padding: "4px 12px", fontSize: "0.875rem"}, md: {height: "40px", padding: "8px 20px", fontSize: "1rem"}, lg: {height: "48px", padding: "12px 28px", fontSize: "1.125rem"}}
    borderRadius: "0px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#1C1C1C"
    color: "#EFE7D2"
    border: "2px solid #5C4033"
    borderRadius: "0px"
    padding: "8px 12px"
    focusBorder: "2px solid #C68642"
    placeholderColor: "#A58D69"
  card:
    base:  {background: "#1C1C1C", border: "2px solid #5C4033", borderRadius: "4px", padding: "24px", shadow: "2px 2px 0 rgba(28,28,28,0.6)"}
    hover: {shadow: "3px 3px 0 rgba(28,28,28,0.7)", transform: "translate(-1px, -1px)"}
---

# Art Brut (Dubuffet, 1948)

> Raw, obsessive, edge-to-edge — asylum-wall pigment and hand-carved marks turned into a design system that rejects every convention of taste.

## Origin

Jean Dubuffet coined "Art Brut" in 1945 to describe artwork created entirely outside the fine-art establishment — by psychiatric patients, spiritualist mediums, and compulsive self-taught makers who had no knowledge of or interest in the gallery world. In 1948 he founded the Compagnie de l'Art Brut in Paris with André Breton and others, gathering thousands of works from Swiss and French asylums. The permanent Collection de l'Art Brut opened in Lausanne's Château de Beaulieu in 1976, housing Dubuffet's hoard of Adolf Wölfli's 25,000-page illustrated autobiography, Aloïse Corbaz's obsessive colored-pencil portraits, and Augustin Lesage's vast spirit-guided canvases.

The movement's core thesis is radical: the most vital art comes from people completely uncontaminated by cultural training. No composition rules, no color theory, no negative space — just the compulsion to fill every surface. Dubuffet's own *L'Hourloupe* series (1962–1974) and his writings like *Asphyxiating Culture* made this position an explicit challenge to the Parisian art world. The visual language that emerged — dense, repetitive, horror vacui compositions on earth-pigment grounds — is one of the twentieth century's most distinctive aesthetic vocabularies.

## Overview
Composition cues:
- **Layout**: stacked, edge-to-edge, no negative space — horror vacui as organizing principle
- **Content width**: full-bleed — content pushes to the margins like Wölfli's page-filling mandalas
- **Framing**: heavy hand-drawn borders, thick outlines that feel carved rather than drawn
- **Grid intensity**: none — asymmetric, organic placement; grids are academic and therefore forbidden

## Colors
The palette is dredged from riverbed sediment and asylum-wall pigment. Mud Brown, Ochre, and Oxblood dominate — the colors of raw earth, iron oxide, and dried blood on paper. Lead White provides the only relief, the color of unprimed canvas or institutional plaster. Asphalt Black anchors the darkest grounds. Nothing is bright, nothing is saturated, nothing is pleasant. Sour acid yellow and sickly green appear only as rare, unsettling accents. The palette should feel like it was mixed from whatever pigments were available in a locked ward.

**Role usage**:
- Page background → `colors.background.page` (mud brown — asylum-wall ground)
- Surface / card background → `colors.background.surface` (asphalt black)
- Accent panel background → `colors.background.subtle` (oxblood)
- Primary text → `colors.text.primary` (lead white on dark ground)
- Secondary text → `colors.text.secondary` (bone)
- Primary actions → `colors.primary.500` (oxblood)
- Accents and focus states → `colors.accent.500` (ochre)
- Muted / disabled text → `colors.text.muted`

## Typography
The type voice is hand-made, crooked, and unapologetically naïve. Headlines in Caveat evoke the scrawled inscriptions that Wölfli and Corbaz embedded directly into their compositions — letters that are part drawing, part writing. Display text in Permanent Marker brings the raw urgency of a felt-tip on cardboard. Body text in Crimson Text provides just enough anchoring legibility without ever feeling polished; it reads like a stout serif from an old asylum logbook. Text should feel crammed in, never elegantly spaced.

**Text styles**:
- `display-xl` — Permanent Marker, 96px, weight 400, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Permanent Marker, 64px, weight 400, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Caveat, 48px, weight 700, line-height 1.2, letter-spacing 0em
- `heading-2` — Caveat, 36px, weight 700, line-height 1.2, letter-spacing 0em
- `body-lg` — Crimson Text, 18px, weight 400, line-height 1.625, letter-spacing 0em
- `body-md` — Crimson Text, 16px, weight 400, line-height 1.5, letter-spacing 0em
- `caption` — Caveat, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Courier Prime, 14px, weight 400, line-height 1.5, letter-spacing 0em

## Spacing & Layout
- Base unit: 4px
- Scale follows the token set: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px, but full-bleed backgrounds extend beyond
- Section padding: 64px vertical (md), 96px on large screens — generous but the content inside is crammed
- Spacing between elements should feel slightly too tight — reflecting horror vacui composition

## Elevation & Depth
Depth is hand-drawn, not computed. Shadows are hard-offset (no blur) like a woodcut or linocut print — as if the element was physically stamped onto the surface. The offset direction is consistently bottom-right, mimicking the ink-press effect of crude printmaking. No glass, no blur, no frosted anything. Surfaces are opaque, material, and heavy.

- Surface style: solid, opaque — no transparency
- Blur: none — Art Brut doesn't blur
- Shadow ladder: hard offset shadows (2px 2px 0 to 6px 6px 0), increasing offset for greater elevation
- Inner shadows simulate ink seeping into paper grain

## Shapes
- Button radius: 0px — hand-drawn rectangles, deliberately imperfect
- Card radius: 4px — the slight softening of worn paper corners, not polished roundness
- Large container radius: 6px
- Input radius: 0px — raw, unfinished edges
- Full (pill): 9999px — reserved only for small badges or tags

## Motion
Motion is minimal and primitive. Art Brut rejects sophistication, and smooth spring animations would betray the raw aesthetic. Interactions should feel like physical acts — a stamp pressed down, a page shifted. No bounce, no elastic overshoot, no delight micro-animations. The only acceptable motion is a slight positional shift on hover (as if the element was nudged by hand) and opacity changes.

- Level: minimal
- Durations: fast 100ms, normal 200ms — nothing lingers
- Easings: simple ease-out, no spring curves in practice
- Hover patterns: opacity reduction and tint shift; slight translate on cards (-1px, -1px)
- Reduced motion: fully supported — the aesthetic barely uses motion anyway

## Techniques

### Horror Vacui Background Fill
A repeating pattern of crude, hand-drawn marks (eyes, spirals, short parallel lines) tiled as a background texture, evoking the all-over patterning of Wölfli's manuscripts. Implemented as a subtle SVG pattern on the page body.
```css
.element {
  background-color: #5C4033;
  background-image: url("data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='20' cy='20' r='6' fill='none' stroke='%23722F37' stroke-width='1.5' opacity='0.25'/%3E%3Cline x1='8' y1='8' x2='14' y2='8' stroke='%23722F37' stroke-width='1' opacity='0.2'/%3E%3Cline x1='28' y1='32' x2='34' y2='32' stroke='%23722F37' stroke-width='1' opacity='0.2'/%3E%3C/svg%3E");
  background-size: 40px 40px;
}
```

### Hand-Drawn Border Frame
A thick, slightly uneven border that mimics the crude framing Dubuffet and Wölfli drew around their compositions. Uses box-shadow stacking to create an imperfect double-rule effect.
```css
.element {
  border: 3px solid #EFE7D2;
  box-shadow:
    2px 2px 0 #1C1C1C,
    inset 0 0 0 4px #5C4033,
    inset 0 0 0 6px #EFE7D2;
  background: #1C1C1C;
}
```

### Crude Stamp Hover
A hover interaction that shifts the element like a woodcut stamp being pressed — hard offset shadow grows, element translates slightly, simulating physical pressure. No blur, no smooth spring.
```css
.element {
  box-shadow: 2px 2px 0 rgba(28,28,28,0.6);
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.element:hover {
  transform: translate(-1px, -1px);
  box-shadow: 3px 3px 0 rgba(28,28,28,0.7);
}
```

## Iconography
Icons should feel hand-drawn and slightly crude — never polished vector perfection. Tabler icons with a heavier 2px stroke approximate the thick outlines found in Art Brut drawings, where forms are defined by bold, confident marks rather than refined contours. Icons sit inline with text, crammed into the composition rather than floating in generous whitespace.

- Treatment: outline (heavy stroke, no fill)
- Set: Tabler Icons
- Stroke: 2px — thicker than default, matching the crude border language

## Do's & Don'ts

### ✓ Do
- Fill every surface — leave no blank space unoccupied
- Use hard-offset shadows instead of blurred drop shadows
- Let text and imagery overlap and crowd each other
- Use Caveat for headlines to maintain the hand-lettered voice
- Embrace asymmetry and imperfect alignment as features, not bugs

### ✗ Don't
- Use clean vector graphics
- Create symmetrical layouts
- Apply pastel or bright saturated palettes
- Leave negative space — horror vacui means horror of the void
- Use polished sans-serif typography
- Build perfect grid systems
- Use gallery-white or cream/beige page backgrounds
- Exercise tasteful restraint — Art Brut explicitly rejects taste

## Applications
This system is built for projects that need to feel raw, urgent, and unmistakably handmade — underground music platforms, outsider art galleries, zine archives, mental health advocacy sites, experimental publishing. It works best when the content itself is dense and the maker's hand should be visible in every pixel. Not for corporate dashboards, e-commerce checkout flows, or anything that needs to feel safe and polished.
