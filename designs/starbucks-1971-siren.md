---
version: 1

meta:
  id: starbucks-1971-siren
  name: "Starbucks (Siren)"
  description: "Forest-green Siren medallion on warm cream — third-place café hospitality rendered as a global design system"
  isDark: false
  tags: [retro, warm, decorative, narrative, organic]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1971 founded; current Siren-only mark since 2011"
  region: "Seattle, Washington, USA"
  regionZh: "美国华盛顿州西雅图"
  keyFigures: ["Howard Schultz", "Terry Heckler", "Connie Birdsall", "Lippincott"]
  movements: ["Third-place café culture", "Specialty coffee branding", "Modern hospitality industrial systems"]

introduction: |
  Starbucks distilled fifty years of café culture into a single twin-tailed Siren on forest green. The 2011 rebrand stripped the wordmark away, letting the medallion breathe alone on cream paper cups, chalkboard menus, and foil-stamped seasonal sleeves. Every touchpoint channels Howard Schultz's "third place" — warmer than an office, more intentional than home.

  This system translates that hospitality into tokens: deep #006241 green anchors every primary action, cream #F1E9D9 provides the paper-cup substrate, and gold accents mark premium moments. Typography stays within the Sodo Sans family for 95% of needs, with Lander Display reserved for chalkboard-energy headlines.
introductionZh: |
  星巴克用半个世纪将咖啡馆文化浓缩为一枚森林绿底的双尾海妖徽章。2011年品牌焕新去掉了文字标识，让海妖独立呼吸于奶油色纸杯、粉笔手写菜单板和烫金季节性杯套之上。每一个触点都在传递霍华德·舒尔茨的"第三空间"理念——比办公室温暖，比家更有仪式感。

  这套设计系统将那份待客之道转化为可用的设计令牌：深邃的 #006241 绿锚定所有主要交互，奶油色 #F1E9D9 充当纸杯般的底色基底，金色点缀标记高端时刻。排版以 Sodo Sans 字族覆盖绝大多数场景，Lander Display 仅在需要粉笔板手写能量的标题中登场。

colors:
  primary:
    "50": "#E6F2ED"
    "100": "#CCE5DB"
    "200": "#99CBB7"
    "300": "#66B193"
    "400": "#33976F"
    "500": "#006241"
    "600": "#00472F"
    "700": "#003D28"
    "800": "#002E1E"
    "900": "#1E3932"
    "950": "#0F1D19"
  secondary:
    "50": "#FDF9F3"
    "100": "#FBF4E7"
    "200": "#F7E9CF"
    "300": "#F3DEB7"
    "400": "#F1E9D9"
    "500": "#E8DCC5"
    "600": "#D4C7A8"
    "700": "#B8A882"
    "800": "#9C8A5E"
    "900": "#7A6B45"
    "950": "#5A4E32"
  accent:
    "50": "#FDF8EE"
    "100": "#FAF0DC"
    "200": "#F2DFB3"
    "300": "#E8CD88"
    "400": "#D9B86A"
    "500": "#CBA258"
    "600": "#B08A3E"
    "700": "#8E6E31"
    "800": "#6C5425"
    "900": "#4A3A1A"
    "950": "#2E2410"
  neutral:
    "50": "#F8F6F3"
    "100": "#F1EDE7"
    "200": "#E3DBCF"
    "300": "#D5C9B7"
    "400": "#B8A892"
    "500": "#9A8A70"
    "600": "#7A6D58"
    "700": "#5C5242"
    "800": "#3E372D"
    "900": "#1E3932"
    "950": "#0F1D19"
  semantic:
    success: { bg: "#006241", text: "#FFFFFF", light: "#E6F2ED", border: "#33976F" }
    warning: { bg: "#CBA258", text: "#1E3932", light: "#FDF8EE", border: "#D9B86A" }
    error:   { bg: "#D62828", text: "#FFFFFF", light: "#FDE8E8", border: "#E85555" }
    info:    { bg: "#006241", text: "#FFFFFF", light: "#E6F2ED", border: "#66B193" }
  background:
    page: "#F1E9D9"
    surface: "#FFFFFF"
    subtle: "#E8DCC5"
  text:
    primary: "#006241"
    secondary: "#1E3932"
    muted: "#5C5242"
    inverse: "#FFFFFF"

typography:
  families:
    heading: "'Sodo Sans', 'Lander', sans-serif"
    body: "'Sodo Sans', 'Inter', sans-serif"
    mono: "'JetBrains Mono', 'Fira Code', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"
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
  container: { sm: "640px", md: "768px", lg: "1024px", xl: "1280px", full: "100%" }
  gridGap: { sm: "8px", md: "16px", lg: "24px", xl: "48px" }
  sectionPadding: { sm: "32px", md: "64px", lg: "96px", xl: "128px" }

borders:
  radius: { none: "0", sm: "4px", md: "8px", lg: "12px", xl: "16px", full: "9999px" }
  color: { default: "#E8DCC5", subtle: "#F1EDE7", strong: "#006241", focus: "#006241" }
  width: { thin: "1px", default: "1px", thick: "2px" }
  style: "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(0,98,65,0.05)"
  sm: "0 1px 4px rgba(0,98,65,0.08)"
  md: "0 2px 8px rgba(0,98,65,0.15)"
  lg: "0 4px 16px rgba(0,98,65,0.12)"
  xl: "0 8px 32px rgba(0,98,65,0.14)"
  "2xl": "0 16px 48px rgba(0,98,65,0.18)"
  inner: "inset 0 1px 2px rgba(30,57,50,0.04)"
  focus: "0 0 0 3px rgba(0,98,65,0.25)"

motion:
  level: "restrained"
  durations: { instant: "0ms", fast: "120ms", normal: "250ms", slow: "400ms", slower: "600ms" }
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in: "cubic-bezier(0.4, 0, 1, 1)"
    out: "cubic-bezier(0, 0, 0.2, 1)"
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: [lift, tint, opacity]
  reducedMotion: true

composition:
  layout: "stack"
  contentWidth: "container"
  framing: "solid"
  gridIntensity: "soft"
  rhythm: "8px"

surfaceStyle: "solid"
blur: "none"

iconography:
  treatment: "linear"
  set: "lucide"
  size: { sm: "16px", md: "20px", lg: "24px" }
  stroke: "1.5px"

components:
  button:
    primary:
      background: "#006241"
      color: "#FFFFFF"
      border: "none"
      shadow: "0 1px 4px rgba(0,98,65,0.08)"
      hoverBackground: "#00472F"
      hoverShadow: "0 2px 8px rgba(0,98,65,0.15)"
      hoverColor: "#FFFFFF"
    secondary:
      background: "#FFFFFF"
      color: "#006241"
      border: "1px solid #006241"
      shadow: "none"
      hoverBackground: "#E6F2ED"
      hoverShadow: "none"
      hoverColor: "#006241"
    ghost:
      background: "transparent"
      color: "#006241"
      border: "none"
      shadow: "none"
      hoverBackground: "rgba(0,98,65,0.06)"
      hoverShadow: "none"
      hoverColor: "#00472F"
    danger:
      background: "#D62828"
      color: "#FFFFFF"
      border: "none"
      shadow: "none"
      hoverBackground: "#B02020"
      hoverShadow: "0 2px 8px rgba(214,40,40,0.2)"
      hoverColor: "#FFFFFF"
    sizes:
      sm: { height: "32px", padding: "0 16px", fontSize: "0.875rem" }
      md: { height: "40px", padding: "0 24px", fontSize: "1rem" }
      lg: { height: "48px", padding: "0 32px", fontSize: "1.125rem" }
    borderRadius: "9999px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FFFFFF"
    color: "#1E3932"
    border: "1px solid #E8DCC5"
    borderRadius: "4px"
    padding: "10px 14px"
    focusBorder: "#006241"
    placeholderColor: "#9A8A70"
  card:
    base:
      background: "#FFFFFF"
      border: "1px solid #E8DCC5"
      borderRadius: "4px"
      padding: "24px"
      shadow: "0 2px 8px rgba(0,98,65,0.15)"
    hover:
      shadow: "0 4px 16px rgba(0,98,65,0.12)"
      transform: "translateY(-2px)"
---

# Starbucks (Siren)

> Forest-green Siren medallion on warm cream — third-place café hospitality as a design system.

## Origin

Starbucks opened at Pike Place Market in 1971 with a twin-tailed Siren woodcut adapted from a 16th-century Norse engraving by designer Terry Heckler. The mark evolved through five iterations — gaining a green ring in 1987, zooming in on the Siren's face in 1992, and finally shedding the wordmark entirely in 2011 under Lippincott's direction (led by Connie Birdsall). That final liberation let the Siren stand alone on cups, storefronts, and digital surfaces worldwide.

Howard Schultz's "third place" philosophy — a café that is neither home nor office — drove every visual decision: warm cream paper stock, hand-lettered chalkboard menus, and deep forest green that reads as both natural and premium. The 2018 brand expression refresh introduced Sodo Sans as the house typeface, completing the transition from coffeehouse eclecticism to a disciplined global system that still feels handmade at the edges.

## Overview

Composition cues:
- **Layout**: Vertical stack with generous section padding; cup-portrait 9:16 aspect for hero moments
- **Content width**: Container (max 1024–1280px) with cream page margins
- **Framing**: Solid cream surfaces with subtle green borders; circular medallion motifs for focal points
- **Grid intensity**: Soft — content breathes with ample whitespace on warm cream

## Colors

The palette is anchored by Starbucks Green `#006241` — the most-recognized green in retail — set against House Cream `#F1E9D9` that evokes the paper cup sleeve. Soy-ink black `#1E3932` handles body text with warmth, while gold `#CBA258` marks premium Reserve-tier moments. Holiday red `#D62828` is reserved for seasonal capsules only. The system avoids lime or neon greens entirely; every green must read as deep forest.

**Role usage**:
- Page background → `colors.background.page` (#F1E9D9 cream)
- Card / surface → `colors.background.surface` (#FFFFFF)
- Primary actions & headings → `colors.primary.500` (#006241)
- Body text → `colors.text.secondary` (#1E3932)
- Premium accents & badges → `colors.accent.500` (#CBA258 gold)
- Seasonal / error states → semantic.error (#D62828)
- Muted / caption text → `colors.text.muted` (#5C5242)

## Typography

Sodo Sans carries 95% of the typographic load — a custom humanist sans-serif commissioned in 2018 that balances approachability with global legibility. Lander Display provides chalkboard-energy display headlines with hand-drawn warmth. The system avoids competing typefaces; hierarchy is achieved through weight and scale within the Sodo Sans family.

**Text styles**:
- `display-xl` — Sodo Sans, 96px, weight 800, line-height 1.0, letter-spacing -0.04em
- `display-lg` — Sodo Sans, 64px, weight 700, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Sodo Sans, 48px, weight 700, line-height 1.2, letter-spacing -0.02em
- `body-lg` — Sodo Sans, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Sodo Sans, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Sodo Sans, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — JetBrains Mono, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 4px; primary rhythm on 8px increments
- Scale: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128px
- Container max-width: 1280px with 24px horizontal padding
- Section padding: 64px vertical (md), 96px (lg) for generous café-like breathing room
- Grid gap: 16px (md) for card grids, 24px (lg) for feature sections

## Elevation & Depth

Surfaces are solid and warm — no glass or blur effects. Depth is communicated through subtle green-tinted shadows that feel like the shadow a paper cup casts on a wooden counter. The shadow ladder uses rgba(0,98,65,α) to keep shadows on-brand rather than neutral gray.

- Surface style: solid white cards on cream page
- Blur: none — materiality is opaque paper and wood
- Shadow ladder: xs (1px) → sm (4px) → md (8px, default card) → lg (16px, elevated) → xl (32px, modal)
- Focus ring: 3px spread in rgba(0,98,65,0.25)

## Shapes

- Buttons: fully rounded pill (9999px) — echoing the Siren medallion's circularity
- Cards: 4px radius — subtle softness without losing the paper-stock feel
- Inputs: 4px radius — matching card treatment
- Badges / tags: 9999px pill
- Medallion containers: 50% (perfect circle)

## Motion

Restrained and warm — motion should feel like steam rising from a cup, not a tech product snapping into place. Transitions are smooth and unhurried, reinforcing the third-place calm.

- Level: restrained
- Fast interactions (hover, focus): 120ms
- Standard transitions: 250ms
- Page-level animations: 400ms
- Easing: cubic-bezier(0.4, 0, 0.2, 1) for most; spring for playful micro-interactions
- Hover patterns: lift (translateY -2px), tint (green overlay), opacity fade
- Reduced motion: respected — all animations collapse to opacity-only

## Techniques

### Siren Medallion Stamp

A circular badge treatment that echoes the logo's medallion form — used for featured items, awards, or seasonal callouts.

```css
.medallion-stamp {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 2px solid #006241;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FFFFFF;
  box-shadow: 0 2px 8px rgba(0,98,65,0.15);
  position: relative;
}
.medallion-stamp::after {
  content: '';
  position: absolute;
  inset: 4px;
  border-radius: 50%;
  border: 1px solid #E8DCC5;
}
```

### Chalkboard Panel

A dark-green panel with cream text that evokes the hand-lettered menu boards in every Starbucks store.

```css
.chalkboard-panel {
  background: #1E3932;
  color: #F1E9D9;
  padding: 32px;
  border-radius: 4px;
  font-family: 'Lander', 'Sodo Sans', sans-serif;
  font-weight: 700;
  letter-spacing: 0.02em;
  position: relative;
  overflow: hidden;
}
.chalkboard-panel::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 28px,
    rgba(241,233,217,0.03) 28px,
    rgba(241,233,217,0.03) 29px
  );
  pointer-events: none;
}
```

### Gold Foil Accent Border

A warm gold gradient border used on premium / Reserve-tier cards and seasonal elements.

```css
.gold-foil-border {
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
  border-radius: 4px;
}
.gold-foil-border::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 6px;
  background: linear-gradient(135deg, #CBA258, #E8CD88, #CBA258);
  z-index: -1;
}
```

## Iconography

Icons follow a linear (outline) treatment at 1.5px stroke weight, matching the Siren mark's fine engraved linework. The Lucide set provides the base vocabulary — its humanist geometry aligns with Sodo Sans's curves.

- Treatment: linear outlines
- Set: Lucide
- Stroke: 1.5px, round caps and joins

## Do's & Don'ts

### ✓ Do
- Use Starbucks Green #006241 for all primary actions and headings
- Set type in Sodo Sans for 95% of content; reserve Lander for display moments
- Apply pill-radius (9999px) to all buttons — echo the Siren's circular medallion
- Keep backgrounds warm (cream #F1E9D9) — never cold white or gray
- Use gold #CBA258 sparingly for premium badges and seasonal accents

### ✗ Don't
- Use lime or neon green — must be deep forest
- Apply a modern flat-tech aesthetic — Starbucks has hospitality warmth
- Feature photography of latte art alone — favor cup + sleeve + medallion composition
- Mix multiple competing fonts — Sodo Sans family handles 95% of needs
- Use sharp 90° corners on customer-facing artifacts
- Set anything on pure black backgrounds — favor cream + green + chalkboard

## Applications

This system is ideal for café loyalty apps, menu and ordering interfaces, seasonal campaign landing pages, and brand storytelling microsites. It works best when content is structured vertically (like a cup) with generous whitespace and warm cream backgrounds that make the forest green pop as a confident accent rather than an overwhelming fill.
