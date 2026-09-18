---
version: 1

meta:
  id: fifties-diner-aqua-chrome
  name: 1950s Diner Aqua
  description: Jukebox-era roadside Americana in saturated aqua, chrome trim, cherry-red vinyl and neon script.
  isDark: false
  tags: [retro, bold, playful, warm, decorative]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1950s (post-war), enduring 1950–1990"
  region: "United States, North America"
  regionZh: "美国"
  keyFigures: [Worcester Lunch Car Company, Valentine Manufacturing, Paramount Diners]
  movements: [Mid-Century Modern roadside, Googie commercial vernacular]

introduction: |
  The post-war American diner is a Formica-and-vinyl world: turquoise boomerang
  counters, chrome banding, cherry-red leatherette booths and checkerboard floors,
  all washed in the buzz of neon. Optimistic and loud, it is roadside Americana at
  its most confident.

  This system treats the saturated aqua wall as the ground, not white. Chrome gloss
  catches light, neon script glows, and slab headers shout the daily special. Every
  surface is built to feel like a counter you could slide a milkshake across.
introductionZh: |
  五十年代美式快餐厅是一个由富美家塑料板和乙烯基皮革构成的世界：绿松石色的回旋镖
  吧台、镀铬包边、樱桃红的卡座沙发、黑白棋盘格地面，全都浸在霓虹灯的嗡鸣里。它乐观、
  响亮，是公路边美式风情最自信的样子。

  这套系统把饱和的湖水蓝当作底色——绝不是白色。镀铬的光泽捕捉光线，霓虹手写体发光，
  厚重的板状标题大声喊出今日特餐。每一个表面都像一张你能把奶昔滑过去的吧台。

colors:
  primary:    {"50": "#E4FAF7", "100": "#C0F4ED", "200": "#8FE9DE", "300": "#5DD8CB", "400": "#3AC7B9", "500": "#1FB6A6", "600": "#179286", "700": "#136F67", "800": "#0F524C", "900": "#0B3A36", "950": "#062320"}
  secondary:  {"50": "#FDECEC", "100": "#FAD0D1", "200": "#F5A5A6", "300": "#EF7779", "400": "#E85457", "500": "#E03A3C", "600": "#C12A2C", "700": "#9C2122", "800": "#771A1B", "900": "#551313", "950": "#330B0B"}
  accent:     {"50": "#FEF8EA", "100": "#FBEEC6", "200": "#F8E09C", "300": "#F5D072", "400": "#F3C45D", "500": "#F2C14E", "600": "#D9A22E", "700": "#AE7E21", "800": "#835E18", "900": "#5C4110", "950": "#382709"}
  neutral:    {"50": "#F7F8F9", "100": "#EEF0F1", "200": "#E0E3E5", "300": "#C9CDD0", "400": "#A4AAAE", "500": "#7E858A", "600": "#5F6569", "700": "#464B4E", "800": "#2F3335", "900": "#1A1A1A", "950": "#0D0D0D"}
  semantic:
    success: { bg: "#E4FAF7", text: "#136F67", light: "#C0F4ED", border: "#5DD8CB" }
    warning: { bg: "#FEF8EA", text: "#AE7E21", light: "#FBEEC6", border: "#F3C45D" }
    error:   { bg: "#FDECEC", text: "#9C2122", light: "#FAD0D1", border: "#EF7779" }
    info:    { bg: "#E4FAF7", text: "#179286", light: "#C0F4ED", border: "#3AC7B9" }
  background:
    page:    "#2BB7AE"
    surface: "#F4F1E9"
    subtle:  "#7ED4CC"
  text:
    primary:   "#1A1A1A"
    secondary: "#2F3335"
    muted:     "#5F6569"
    inverse:   "#F4F1E9"

typography:
  families:
    heading: "'Alfa Slab One', 'Lobster', cursive"
    body:    "'Oswald', 'Arial Narrow', sans-serif"
    mono:    "'Oswald', 'Courier New', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Lobster&family=Oswald:wght@300;400;500;600;700&family=Pacifico&display=swap"
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
  radius: {none: "0", sm: "6px", md: "12px", lg: "20px", xl: "32px", full: "9999px"}
  color:  {default: "#C9CDD0", subtle: "#7ED4CC", strong: "#1A1A1A", focus: "#F2C14E"}
  width:  {thin: "1px", default: "2px", thick: "4px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,0,0,0.10)"
  sm: "0 2px 4px rgba(0,0,0,0.14)"
  md: "0 4px 10px rgba(0,0,0,0.18)"
  lg: "0 10px 22px rgba(0,0,0,0.22)"
  xl: "0 18px 40px rgba(0,0,0,0.26)"
  "2xl": "0 28px 60px rgba(0,0,0,0.30)"
  inner: "inset 0 2px 6px rgba(0,0,0,0.18)"
  focus: "0 0 0 3px rgba(242,193,78,0.55)"

motion:
  level: lively
  durations: {instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, glow, scale, tint]
  reducedMotion: true

composition:
  layout:        grid
  contentWidth:  container
  framing:       bordered
  gridIntensity: strong
  rhythm:        "4px"

surfaceStyle: layered
blur:         none

iconography:
  treatment: filled
  set:       phosphor
  size:      {sm: "16px", md: "20px", lg: "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {background: "#E03A3C", color: "#F4F1E9", border: "2px solid #1A1A1A", shadow: "0 4px 0 #1A1A1A", hoverBackground: "#C12A2C", hoverShadow: "0 6px 14px rgba(224,58,60,0.45)", hoverColor: "#F4F1E9"}
    secondary: {background: "#1FB6A6", color: "#1A1A1A", border: "2px solid #1A1A1A", shadow: "0 4px 0 #1A1A1A", hoverBackground: "#179286", hoverShadow: "0 6px 14px rgba(31,182,166,0.40)", hoverColor: "#F4F1E9"}
    ghost:     {background: "transparent", color: "#F4F1E9", border: "2px solid #C9CDD0", shadow: "none", hoverBackground: "rgba(244,241,233,0.12)", hoverShadow: "none", hoverColor: "#F4F1E9"}
    danger:    {background: "#1A1A1A", color: "#F2C14E", border: "2px solid #1A1A1A", shadow: "0 4px 0 #5F6569", hoverBackground: "#0D0D0D", hoverShadow: "0 6px 14px rgba(0,0,0,0.4)", hoverColor: "#F2C14E"}
    sizes:     {sm: {height: "36px", padding: "0 16px", fontSize: "0.875rem"}, md: {height: "44px", padding: "0 24px", fontSize: "1rem"}, lg: {height: "56px", padding: "0 36px", fontSize: "1.25rem"}}
    borderRadius: "9999px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  input:
    background: "#F4F1E9"
    color: "#1A1A1A"
    border: "2px solid #1A1A1A"
    borderRadius: "12px"
    padding: "12px 16px"
    focusBorder: "2px solid #F2C14E"
    placeholderColor: "#7E858A"
  card:
    base:  {background: "#F4F1E9", border: "2px solid #1A1A1A", borderRadius: "20px", padding: "24px", shadow: "0 10px 22px rgba(0,0,0,0.22)"}
    hover: {shadow: "0 18px 40px rgba(0,0,0,0.26)", transform: "translateY(-4px)"}
---

# 1950s Diner Aqua

> Jukebox-era roadside Americana — saturated aqua, chrome trim, cherry-red vinyl and glowing neon script.

## Origin
The American roadside diner crystallized after World War II, when prefab builders like the Worcester Lunch Car Company, Valentine Manufacturing and Paramount Diners shipped stainless-clad eateries to highway lots across the country. Inside, the era's new materials ran the show: Formica counters in turquoise and boomerang patterns, vinyl-leatherette booths in cherry red, chrome banding everywhere, and black-and-white checkerboard floors. Out front, commercial neon sign shops wired up tubes that buzzed the menu into the night.

By the 1950s this had become a coherent commercial vernacular — part Mid-Century Modern, part Googie exuberance, all optimism. The look endured through the 1990s as nostalgia, but its native moment was the post-war jukebox age, when a milkshake counter felt like the future. This system reconstructs that confidence: loud saturated color, glossy reflective surfaces, fat slab headlines and neon-script flourishes, grounded on the aqua wall rather than a polite white page.

## Overview
Composition cues:
- **Layout**: Strong grid — menu-card decks, counter-strip headers, boomerang dividers.
- **Content width**: Container-bound, like a booth you sit inside, not full-bleed.
- **Framing**: Bordered — heavy 2px black outlines and chrome banding around every surface.
- **Grid intensity**: Strong; checkerboard rhythm and aligned card rows.

## Colors
The palette is loud on purpose: a saturated diner aqua ground (`#2BB7AE`) carries water-aqua primary, cherry-red vinyl, mustard yellow and chrome silver, all anchored by hard black outline and a cream surface for menu cards. Nothing is muted — the diner sells optimism through saturation.

**Role usage**:
- Page background → `colors.background.page` (`#2BB7AE`, saturated diner aqua, never white)
- Menu cards / panels → `colors.background.surface` (`#F4F1E9` cream)
- Primary actions / aqua accents → `colors.primary.500` (`#1FB6A6`)
- Hot CTAs / specials → `colors.secondary.500` (`#E03A3C` cherry vinyl)
- Highlights / starbursts → `colors.accent.500` (`#F2C14E` mustard)
- Chrome trim / banding → `colors.neutral.300` (`#C9CDD0`)
- Outlines / headline ink → `colors.text.primary` (`#1A1A1A`)

## Typography
The voice is signage: fat slab headlines that shout the daily special, looping neon script for the brand flourish, and a tight condensed sans for everything you actually read. Headlines feel painted on chrome; body copy reads like a printed menu strip.

**Text styles**:
- `display-xl` — Alfa Slab One, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Alfa Slab One, 64px, weight 700, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Alfa Slab One, 36px, weight 700, line-height 1.1, letter-spacing 0
- `script-accent` — Lobster, 48px, weight 400, line-height 1.1, letter-spacing 0
- `body-lg` — Oswald, 18px, weight 400, line-height 1.6, letter-spacing 0.01em
- `body-md` — Oswald, 16px, weight 400, line-height 1.6, letter-spacing 0.01em
- `caption` — Oswald, 12px, weight 500, line-height 1.4, letter-spacing 0.08em, uppercase
- `mono-md` — Oswald, 15px, weight 500, line-height 1.5, letter-spacing 0.05em

## Spacing & Layout
- Base unit: 4px, with an 8px working rhythm for card grids.
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128.
- Container: caps at 1280px; content stays booth-width, never edge-to-edge.
- Section padding: 64px (md) to 128px (xl), letting the aqua ground breathe between card rows.

## Elevation & Depth
Surfaces are layered and glossy: cream menu cards float on the aqua wall with hard 2px black outlines, chrome-silver banding, and a solid drop offset that reads like a printed sticker. No frosted glass — this is painted metal and laminate that catches light.

- Surface style: layered cream cards on saturated aqua; chrome banding as separator.
- Blur: none — everything is crisp gloss, not haze.
- Shadow ladder: xs hairline → 2xl deep drop; primary buttons use a hard `0 4px 0` offset for the sticker/booth feel.

## Shapes
- Corner radii: none 0, sm 6px, md 12px, lg 20px, xl 32px, full 9999px.
- Buttons are pills (full); menu cards use lg–xl rounding like a vinyl booth back.
- Outlines are heavy and black; chrome trim wraps the rounded edges.

## Motion
Lively but mechanical — things pop, glow and slide like a jukebox selector landing. Hovers lift cards, flick on neon glow and nudge scale; nothing drifts slowly. Spring easing gives buttons a confident bounce.

- Level: lively.
- Durations: fast 120ms for hovers, normal 250ms for cards, slow 400ms for neon flicker-on.
- Easings: default for UI, spring `cubic-bezier(0.34,1.56,0.64,1)` for button press.
- Hover patterns: lift, glow, scale, tint.
- Respects `prefers-reduced-motion`: neon flicker collapses to a static glow.

## Techniques
Brand-specific recipes that make a surface read unmistakably as a 1950s diner.

### Neon tube glow
A looping script header lit like a wired neon sign against the aqua wall.
```css
.neon-sign {
  font-family: 'Lobster', cursive;
  color: #FDECEC;
  text-shadow:
    0 0 4px #FDECEC,
    0 0 10px #E85457,
    0 0 22px #E03A3C,
    0 0 40px #C12A2C;
}
```

### Chrome trim band
A polished metal banding strip used to frame counters and card headers.
```css
.chrome-band {
  height: 14px;
  border-radius: 9999px;
  background: linear-gradient(
    180deg,
    #F7F8F9 0%, #C9CDD0 38%,
    #7E858A 52%, #C9CDD0 66%, #EEF0F1 100%
  );
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.8),
              0 2px 4px rgba(0,0,0,0.25);
}
```

### Checkerboard floor
The black-and-white diner floor as a section divider or footer ground.
```css
.checkerboard {
  background-image:
    linear-gradient(45deg, #1A1A1A 25%, transparent 25%),
    linear-gradient(-45deg, #1A1A1A 25%, transparent 25%),
    linear-gradient(45deg, transparent 75%, #1A1A1A 75%),
    linear-gradient(-45deg, transparent 75%, #1A1A1A 75%);
  background-size: 48px 48px;
  background-position: 0 0, 0 24px, 24px -24px, -24px 0;
  background-color: #F4F1E9;
}
```

## Iconography
Filled, chunky pictograms with a friendly retro weight — think Phosphor's filled set rendered at a 2px optical heft. Use solid shapes (burgers, jukeboxes, milkshakes, stars) over thin line icons, and let boomerang and atomic-starburst motifs do the decorative work between content.

- Treatment: filled, solid silhouettes.
- Set: phosphor (filled).
- Stroke: 2px equivalent weight; no hairline icons.

## Do's & Don'ts
### ✓ Do
- Ground every page on saturated diner aqua `#2BB7AE`, never white.
- Use cherry-red `#E03A3C` for hot CTAs and mustard `#F2C14E` for starburst highlights.
- Set headlines in Alfa Slab One and brand flourishes in Lobster or Pacifico.
- Wrap surfaces in heavy black outlines and chrome banding for the laminate-booth feel.
- Embrace gloss and neon glow — let reflective chrome catch the light.

### ✗ Don't
- Never use cream/ivory or plain-white backgrounds — use saturated diner aqua.
- Don't reach for a muted, desaturated "modern minimal" palette; keep colors loud.
- Don't set headlines in a clean geometric sans — use neon script or fat slab.
- Don't flatten everything to matte; embrace chrome gloss and neon glow.

## Applications
Best for menus, event posters, retro brand landing pages, music and food packaging, and any playful nostalgia-forward marketing that wants to shout. It excels where saturation and personality win over restraint; skip it for somber, data-dense or corporate-minimal contexts.
