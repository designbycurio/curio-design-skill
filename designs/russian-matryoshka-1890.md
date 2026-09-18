---
version: 1

meta:
  id: russian-matryoshka-1890
  name: Russian Matryoshka 1890
  description: Hand-painted birch-wood warmth channeling the original 1890 Abramtsevo nesting doll in russet, cream, and forest green
  isDark: false
  tags: [handmade, decorative, narrative, playful, historical]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1890 (first carved set); Paris debut 1900; peak Russian Revival 1890–1917"
  region: "Abramtsevo / Sergiev Posad, Russia"
  regionZh: "俄罗斯阿布拉姆采沃 / 谢尔吉耶夫镇"
  keyFigures: [Sergei Malyutin, Vasily Zvyozdochkin, Savva Mamontov, Elizaveta Mamontova]
  movements: [Russian Revival, Abramtsevo Art Circle, Narodnost nationalism]

introduction: |
  In 1890, painter Sergei Malyutin and wood-turner Vasily Zvyozdochkin created the first matryoshka at Savva Mamontov's Abramtsevo workshop — an eight-doll set depicting a peasant girl named Matryona holding a black rooster. It won a bronze medal at the 1900 Paris Universal Exposition and became Russia's most recognizable folk object.

  This design system channels the material truth of that original set: warm birch-wood surfaces, hand-painted russet and cream, Cyrillic letterforms from Russian Revival printing, and the egg-oval silhouette that nests seven smaller selves inside one.

introductionZh: |
  1890年，画家谢尔盖·马柳京和木匠瓦西里·兹维约兹多奇金在莫斯科郊外阿布拉姆采沃庄园的工坊里造出了第一套套娃——八个从大到小的白桦木人偶，最外层是抱着黑公鸡的农家少女"玛特廖娜"。这套玩偶在1900年巴黎世博会上斩获铜牌，从此成为俄罗斯民间艺术的全球符号。

  本设计系统还原的不是旅游纪念品橱窗里的套娃，而是马柳京画室里那种温暖的白桦木底色、手绘赭红与森林绿、俄文复兴体印刷字、以及一个蛋形轮廓层层嵌套的质朴工艺感。

colors:
  primary:
    "50": "#f9ebe5"
    "100": "#f2d4c8"
    "200": "#e5a991"
    "300": "#d87e5e"
    "400": "#c9634a"
    "500": "#B85240"
    "600": "#9e4536"
    "700": "#83382c"
    "800": "#692c23"
    "900": "#501f19"
    "950": "#361410"
  secondary:
    "50": "#e8edf5"
    "100": "#d1dbeb"
    "200": "#a3b7d7"
    "300": "#7593c3"
    "400": "#4a6fa5"
    "500": "#2B4F86"
    "600": "#244372"
    "700": "#1d375e"
    "800": "#162b4a"
    "900": "#101f36"
    "950": "#091322"
  accent:
    "50": "#faf4e4"
    "100": "#f5e9c9"
    "200": "#ebd393"
    "300": "#e2bd5d"
    "400": "#d9a84a"
    "500": "#D9A84A"
    "600": "#c0923a"
    "700": "#9e762f"
    "800": "#7c5c24"
    "900": "#5a431a"
    "950": "#382a10"
  neutral:
    "50": "#f5f0e8"
    "100": "#ebe1d2"
    "200": "#d7c3a5"
    "300": "#c3a578"
    "400": "#b08e5e"
    "500": "#8c7048"
    "600": "#705a3a"
    "700": "#54432c"
    "800": "#382c1e"
    "900": "#2A1F15"
    "950": "#150f0a"
  semantic:
    success: { bg: "#5C7044", text: "#F0E1C5", light: "#e8edd4", border: "#6e8452" }
    warning: { bg: "#D9A84A", text: "#2A1F15", light: "#faf4e4", border: "#c0923a" }
    error:   { bg: "#B85240", text: "#F0E1C5", light: "#f9ebe5", border: "#9e4536" }
    info:    { bg: "#2B4F86", text: "#F0E1C5", light: "#e8edf5", border: "#4a6fa5" }
  background:
    page:    "#C49A6E"
    surface: "#F0E1C5"
    subtle:  "#D7C3A5"
  text:
    primary:   "#2A1F15"
    secondary: "#54432c"
    muted:     "#8c7048"
    inverse:   "#F0E1C5"

typography:
  families:
    heading: "'Playfair Display', 'Georgia', serif"
    body:    "'EB Garamond', 'Garamond', 'Times New Roman', serif"
    mono:    "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Playfair+Display:wght@400;500;600;700;800&family=Marck+Script&family=JetBrains+Mono:wght@400;500;700&display=swap"
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
  radius: { none: "0", sm: "8px", md: "16px", lg: "24px", xl: "32px", full: "9999px" }
  color:  { default: "#8c7048", subtle: "#D7C3A5", strong: "#2A1F15", focus: "#B85240" }
  width:  { thin: "1px", default: "1px", thick: "2px" }
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(42, 31, 21, 0.08)"
  sm: "0 2px 6px rgba(42, 31, 21, 0.12)"
  md: "0 4px 14px rgba(42, 31, 21, 0.20)"
  lg: "0 8px 24px rgba(42, 31, 21, 0.22)"
  xl: "0 12px 36px rgba(42, 31, 21, 0.25)"
  "2xl": "0 20px 50px rgba(42, 31, 21, 0.30)"
  inner: "inset 0 1px 2px rgba(42, 31, 21, 0.08)"
  focus: "0 0 0 3px rgba(184, 82, 64, 0.4)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, opacity, tint]
  reducedMotion: true

composition:
  layout:        "stack"
  contentWidth:  "container"
  framing:       "solid"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "layered"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      { sm: "16px", md: "20px", lg: "24px" }
  stroke:    "1.5px"

components:
  button:
    primary:   { background: "#B85240", color: "#F0E1C5", border: "1px solid #9e4536", shadow: "0 2px 6px rgba(42, 31, 21, 0.12)", hoverBackground: "#9e4536", hoverShadow: "0 4px 14px rgba(42, 31, 21, 0.20)", hoverColor: "#F0E1C5" }
    secondary: { background: "#2B4F86", color: "#F0E1C5", border: "1px solid #244372", shadow: "0 2px 6px rgba(42, 31, 21, 0.12)", hoverBackground: "#244372", hoverShadow: "0 4px 14px rgba(42, 31, 21, 0.20)", hoverColor: "#F0E1C5" }
    ghost:     { background: "transparent", color: "#2A1F15", border: "1px solid #8c7048", shadow: "none", hoverBackground: "rgba(42, 31, 21, 0.06)", hoverShadow: "none", hoverColor: "#2A1F15" }
    danger:    { background: "#B85240", color: "#F0E1C5", border: "1px solid #692c23", shadow: "0 2px 6px rgba(42, 31, 21, 0.15)", hoverBackground: "#83382c", hoverShadow: "0 4px 14px rgba(42, 31, 21, 0.22)", hoverColor: "#F0E1C5" }
    sizes:
      sm: { height: "32px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "52px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "16px"
    fontWeight: 600
    letterSpacing: "0.02em"
    textTransform: "none"
  input:
    background: "#F0E1C5"
    color: "#2A1F15"
    border: "1px solid #8c7048"
    borderRadius: "16px"
    padding: "10px 16px"
    focusBorder: "2px solid #B85240"
    placeholderColor: "#8c7048"
  card:
    base:  { background: "#F0E1C5", border: "1px solid #D7C3A5", borderRadius: "24px", padding: "24px", shadow: "0 4px 14px rgba(42, 31, 21, 0.20)" }
    hover: { shadow: "0 8px 24px rgba(42, 31, 21, 0.22)", transform: "translateY(-2px)" }
---

# Russian Matryoshka 1890

> Hand-painted birch-wood warmth from the original 1890 Abramtsevo nesting doll — russet, cream, and forest green nested inside an egg-oval silhouette.

## Origin

In 1890, at Savva Mamontov's Abramtsevo art colony outside Moscow, painter Sergei Malyutin and wood-turner Vasily Zvyozdochkin created the first matryoshka nesting doll. The original eight-piece set depicted a peasant girl called Matryona holding a black rooster, followed by her siblings, down to a swaddled baby at the center. Mamontov — patron, railroad magnate, and champion of the Russian Revival — may have been inspired by a Japanese Fukuruma doll, though the painting was entirely Malyutin's, rendered in the warm russet, cream, and forest-green palette of Russian folk sarafan dress.

The set won a bronze medal at the 1900 Paris Universal Exposition and launched Sergiev Posad as the center of matryoshka production. Mass workshops followed in Semyonov, Polkhovsky Maidan, and beyond, but the original Abramtsevo doll — now in the Toy Museum at Sergiev Posad — remains the aesthetic anchor. Its palette comes from real materials: birch heartwood, iron-oxide-pigment reds, linseed-oil-cut greens. This design system draws from that first studio, not from the tourist-shop reproductions that followed.

## Overview
Composition cues:
- **Layout**: Stacked — content flows vertically with centered symmetry echoing the doll's bilateral form, sections nested like progressively smaller figures.
- **Content width**: Container — generous margins frame content like the painted belly-panel of a doll, never edge-to-edge.
- **Framing**: Solid — cards and panels use warm opaque fills with subtle borders, evoking painted wooden surfaces rather than glass or wireframes.
- **Grid intensity**: Soft — structure is present but organic, guided by rounded shapes and generous padding rather than rigid column lines.

## Colors
The palette is material, not digital. Every color traces to a physical substance in Malyutin's studio: birch heartwood (#C49A6E) for the page ground, iron-oxide russet (#B85240) for the painted dress, sarafan indigo (#2B4F86) for decorative borders, forest-green (#5C7044) for apron details, and Sergiev Posad gold (#D9A84A) for highlight accents. The overall impression is warm, handmade, and unmistakably pre-industrial — pigment on turned wood, not pixels on glass.

**Role usage**:
- Page background → `colors.background.page` (warm birch #C49A6E)
- Card / surface background → `colors.background.surface` (painted cream #F0E1C5)
- Primary actions and accent surfaces → `colors.primary.500` (russet rose)
- Secondary panels and deep backgrounds → `colors.secondary.500` (sarafan blue)
- Highlight accents, badges, gold details → `colors.accent.500` (Sergiev gold)
- Body text on light surfaces → `colors.text.primary` (hand-painted ink)
- Body text on dark surfaces → `colors.text.inverse` (cream)
- Muted captions → `colors.text.muted`

## Typography
Type voices the turn-of-century Russian printing house. Playfair Display headlines carry the high-contrast didone serifs of 1890s Moscow book covers — elegant but grounded, never flimsy. EB Garamond body text reads like the serif prose of a Russian Revival journal. Marck Script appears sparingly for decorative hand-painted accents — a section epigraph, a pull-quote — channeling the casual brushwork Malyutin applied to each doll's face. Section labels use wide-tracked Playfair in small caps, echoing the ornamental titling of Mamontov circle exhibition catalogs.

**Text styles**:
- `display-xl` — Playfair Display, 96px, weight 700, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Playfair Display, 64px, weight 700, line-height 1.05, letter-spacing -0.02em
- `heading-1` — Playfair Display, 48px, weight 700, line-height 1.2, letter-spacing -0.01em
- `body-lg` — EB Garamond, 20px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — EB Garamond, 16px, weight 400, line-height 1.625, letter-spacing 0
- `caption` — Playfair Display, 12px, weight 600, line-height 1.4, letter-spacing 0.05em, small-caps
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout
- Base unit: 4px, rhythm in 8px increments for generous breathing room
- Scale: 2–4–6–8–12–16–24–32–48–64–96–128px
- Container: 1024px (lg) default, with generous horizontal padding (48px minimum)
- Section padding: 64px vertical (md), 96px (lg) for hero sections
- Grid gap: 16px (md) between cards, 24px (lg) between major sections
- Cards nest inside sections with 24px internal padding — the belly-panel metaphor

## Elevation & Depth
Depth is crafted, not calculated. Surfaces feel like painted wooden panels stacked on a workshop table — warm, tangible, softly shadowed. Shadows use the ink-dark brown of the painter's outline (#2A1F15) rather than neutral grey, giving every elevation a handmade warmth. There is no glass, no frosted blur, no backdrop-filter — only solid wood and paint.

- Surface style: layered — cream panels sit on birch ground, blue panels sit deeper
- Blur: none — opacity and layering provide separation, not frosted glass
- Shadow ladder: xs (1px), sm (2px), md (4px), lg (8px), xl (12px), 2xl (20px) — all warm brown rgba
- Focus ring: 3px russet glow around interactive elements

## Shapes
- Corner radii: generously rounded — sm (8px), md (16px for buttons), lg (24px for cards), xl (32px for hero panels)
- The egg-oval silhouette of the doll drives the rounded aesthetic: no sharp corners, no angular crops
- Buttons: 16px radius (softly rounded, never pill-shaped)
- Cards: 24px radius with curved tops echoing the doll's head
- Full (9999px) reserved for avatar circles and small badge dots

## Motion
Motion is restrained and hand-crafted — the gentle rocking of a wooden toy, not the snapping of a digital interface. Transitions use natural easing curves and modest durations. Cards lift subtly on hover as if picked up by a child's hand. Nothing bounces aggressively or slides in from off-screen.

- Level: restrained
- Fast transition: 120ms (hover tint changes)
- Normal transition: 250ms (card lifts, state changes)
- Slow transition: 400ms (panel reveals, section transitions)
- Easing: natural ease-out, with a gentle spring for card interactions
- Hover patterns: lift (translateY), opacity shifts, warm tint changes
- Reduced motion: always respected

## Techniques

### Egg-Oval Doll Silhouette Card
A card shape echoing the matryoshka's egg-oval body — wider belly, narrower curved top — used for feature cards and profile panels.
```css
.doll-card {
  background: #F0E1C5;
  border: 1px solid #D7C3A5;
  border-radius: 50% 50% 24px 24px / 30% 30% 24px 24px;
  padding: 48px 32px 32px;
  box-shadow: 0 4px 14px rgba(42, 31, 21, 0.20);
  text-align: center;
}
.doll-card::before {
  content: '';
  display: block;
  width: 60px;
  height: 60px;
  margin: -24px auto 16px;
  background: #B85240;
  border-radius: 50%;
  border: 2px solid #D9A84A;
}
```

### Birch Wood-Grain Page Texture
A subtle horizontal grain applied to the page background, evoking the turned-birch surface of an unpainted doll.
```css
.birch-ground {
  background-color: #C49A6E;
  background-image: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 3px,
    rgba(42, 31, 21, 0.04) 3px,
    rgba(42, 31, 21, 0.04) 4px
  );
}
```

### Painted-Flower Ornament Border
A decorative border treatment using radial-gradient dots arranged in a floral cluster, reminiscent of the small hand-painted flower motifs on traditional matryoshka aprons.
```css
.flower-ornament {
  position: relative;
  padding: 32px;
  border: 1px solid #D7C3A5;
  border-radius: 24px;
}
.flower-ornament::after {
  content: '';
  position: absolute;
  top: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 12px;
  background:
    radial-gradient(circle 4px at 20% 50%, #B85240 95%, transparent),
    radial-gradient(circle 4px at 40% 50%, #D9A84A 95%, transparent),
    radial-gradient(circle 4px at 60% 50%, #5C7044 95%, transparent),
    radial-gradient(circle 4px at 80% 50%, #B85240 95%, transparent);
}
```

## Iconography
Icons should feel hand-drawn and warm rather than geometric and precise — linear outlines with a 1.5px stroke, suggesting ink-line illustration. Lucide provides clean linear icons that pair well with the serif typography. Icon color follows text color: ink-dark on cream surfaces, cream on russet or blue surfaces.

- Treatment: linear (outline only, no fills)
- Set: Lucide
- Stroke: 1.5px — slightly lighter than the default, echoing delicate brushwork

## Do's & Don'ts

### ✓ Do
- Use the birch-wood page color (#C49A6E) as the foundational ground — it is the turned wood, not a tint
- Apply russet rose (#B85240) for primary actions and warm surface accents
- Use egg-oval and rounded shapes to echo the doll silhouette throughout the layout
- Set headlines in Playfair Display and body in EB Garamond — the serif pairing is essential
- Reserve Marck Script for small decorative moments (pull-quotes, section labels) — never for body text

### ✗ Don't
- Use cream or beige as the page background — the page is birch wood, warm and saturated
- Fall into generic souvenir-shop matryoshka kitsch — reference the 1890 original, not tourist reproductions
- Use Soviet-era Putin or political-doll imagery — this is Abramtsevo art, not Cold War satire
- Set body text in sans-serif (Inter, Geist) — the entire system is serif-voiced
- Apply cool-grey corporate palettes — every neutral is warm brown
- Flatten to modern flat-icon aesthetics — the system is hand-painted, not geometric
- Use garish primary-color-block nesting-doll compositions — subtlety over spectacle
- Apply bright-pink Disney-princess treatments — the palette is earthy, not candy
- Use Russian propaganda red-and-yellow — the colors come from pigment and wood, not politics
- Overlay stock-photo "Russian folk" imagery — specificity to Malyutin's 1890 set, not generic folk

## Applications
Best suited for storytelling platforms, artisan and craft marketplaces, cultural heritage projects, children's educational interfaces, and any product that values warmth, nesting hierarchy, and handmade character. The rounded shapes and generous padding make it particularly effective for card-heavy layouts — product grids, portfolios, and collection browsers where each item is a self-contained "doll" in a nested set.
