---
version: 1

meta:
  id: peanuts-comic-schulz-1950
  name: Peanuts Comic Schulz (1950)
  description: Warm cream newsprint and gentle ink lines channeling Schulz's 50-year hand-drawn comic strip vocabulary
  isDark: false
  tags: [hand-drawn, warm, narrative, friendly, retro]
  status: published
  tier: free
  generatedBy: claude

origin:
  era: "1950–2000; daily strip launched October 2, 1950; visual canon established through 2,600-paper syndication"
  region: "USA — Santa Rosa, California / Saint Paul, Minnesota"
  regionZh: "美国加利福尼亚州圣罗莎 / 明尼苏达州圣保罗"
  keyFigures: ["Charles M. Schulz", "Vince Guaraldi", "Lee Mendelson", "Bill Melendez"]
  movements: ["post-war American newspaper comic strip", "mid-century gentle-melancholy narrative", "animated television special canon"]

introduction: |
  Peanuts distilled fifty years of daily cartooning into a visual language of cream newsprint, wobbling ink lines, and muted Sunday-strip color. Schulz's hand never wavered from its gentle imperfection — every panel border slightly rounded, every letter shaped by brush-pen rather than typeset.

  This system captures that warmth: Charlie Brown yellow as the primary accent, Linus-blanket blue as the secondary voice, and Christmas red for emotional punctuation — all floating on cream paper with the quiet melancholy of a four-panel strip.
introductionZh: |
  《花生漫画》用五十年的日报连载锻造出一套独特的视觉语言——奶油色新闻纸底、微微颤抖的墨线、周日版柔和的中世纪色调。舒尔茨的笔触从未追求机械精确，每一格边框都带着手绘的圆润，每一个字母都出自毛笔而非铅字。

  这套设计系统捕捉了那份温暖：查理·布朗的黄色锯齿衫作为主色调，莱纳斯的蓝色毯子作为辅助声音，圣诞红用于情感标点——一切都漂浮在奶油纸上，带着四格漫画特有的温柔忧郁。

colors:
  primary:    {"50": "#FEFCF0", "100": "#FDF8DC", "200": "#FBF2B8", "300": "#F9EB8E", "400": "#F7E06C", "500": "#F5D44F", "600": "#D4B033", "700": "#A8892A", "800": "#7D6520", "900": "#574618", "950": "#3B2F10"}
  secondary:  {"50": "#EFF6FB", "100": "#DCEDF7", "200": "#B5D9EF", "300": "#85C0E3", "400": "#55A5D4", "500": "#3D81B5", "600": "#326A96", "700": "#285375", "800": "#1F3F58", "900": "#172D3F", "950": "#0F1E2A"}
  accent:     {"50": "#FDF2F2", "100": "#FBE0E0", "200": "#F7BFBF", "300": "#F09494", "400": "#E45A5A", "500": "#C41E1E", "600": "#A31919", "700": "#7F1414", "800": "#5E0F0F", "900": "#420B0B", "950": "#2B0707"}
  neutral:    {"50": "#FAF7F0", "100": "#F5F0E5", "200": "#EBE4D4", "300": "#DDD4BF", "400": "#C4B89E", "500": "#A89A7E", "600": "#8A7C63", "700": "#6B604D", "800": "#504839", "900": "#383228", "950": "#24211A"}
  semantic:
    success: { bg: "#E8F5E0", text: "#2D6A1E", light: "#F2FAF0", border: "#8BC77A" }
    warning: { bg: "#FFF4D6", text: "#7A5C00", light: "#FFFBEB", border: "#F5D44F" }
    error:   { bg: "#FDE8E8", text: "#9B1B1B", light: "#FFF2F2", border: "#E45A5A" }
    info:    { bg: "#E8F2FA", text: "#1F4E73", light: "#F0F7FC", border: "#85C0E3" }
  background:
    page:    "#F8F0DE"
    surface: "#FBF6E9"
    subtle:  "#FFFFFF"
  text:
    primary:   "#0F0F0F"
    secondary: "#3D3530"
    muted:     "#5A4A4A"
    inverse:   "#FBF6E9"

typography:
  families:
    heading: "'Caveat', 'Kalam', cursive"
    body:    "'Quicksand', 'Nunito', sans-serif"
    mono:    "'Source Code Pro', monospace"
    googleFontsImport: "https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&family=Quicksand:wght@300;400;500;600;700&family=Permanent+Marker&family=Source+Code+Pro:wght@400;500&display=swap"
  scale: {"2xs": "0.625rem", "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "4rem", "7xl": "6rem"}
  weights: {"light": 300, "normal": 400, "medium": 500, "semibold": 600, "bold": 700, "extrabold": 800}
  lineHeights: {"tight": 1.2, "snug": 1.375, "normal": 1.5, "relaxed": 1.625, "loose": 1.8}
  letterSpacing: {"tighter": "-0.04em", "tight": "-0.02em", "normal": "0", "wide": "0.05em"}

spacing:
  base: "4px"
  scale: ["2px","4px","6px","8px","12px","16px","24px","32px","48px","64px","96px","128px"]
  container:      {"sm": "640px", "md": "768px", "lg": "1024px", "xl": "1280px", "full": "100%"}
  gridGap:        {"sm": "8px", "md": "16px", "lg": "24px", "xl": "48px"}
  sectionPadding: {"sm": "32px", "md": "64px", "lg": "96px", "xl": "128px"}

borders:
  radius: {"none": "0", "sm": "8px", "md": "12px", "lg": "16px", "xl": "24px", "full": "9999px"}
  color:  {"default": "#0F0F0F", "subtle": "#DDD4BF", "strong": "#0F0F0F", "focus": "#C41E1E"}
  width:  {"thin": "1px", "default": "2px", "thick": "3px"}
  style:  "solid"

shadows:
  none: "none"
  xs: "0 1px 2px rgba(15, 15, 15, 0.04)"
  sm: "0 2px 4px rgba(15, 15, 15, 0.08)"
  md: "0 3px 8px rgba(15, 15, 15, 0.12)"
  lg: "0 6px 16px rgba(15, 15, 15, 0.14)"
  xl: "0 10px 24px rgba(15, 15, 15, 0.16)"
  "2xl": "0 16px 40px rgba(15, 15, 15, 0.20)"
  inner: "inset 0 1px 3px rgba(15, 15, 15, 0.06)"
  focus: "0 0 0 3px rgba(196, 30, 30, 0.25)"

motion:
  level: "restrained"
  durations: {"instant": "0ms", "fast": "120ms", "normal": "250ms", "slow": "400ms", "slower": "600ms"}
  easings:
    default: "cubic-bezier(0.4, 0, 0.2, 1)"
    in:      "cubic-bezier(0.4, 0, 1, 1)"
    out:     "cubic-bezier(0, 0, 0.2, 1)"
    spring:  "cubic-bezier(0.34, 1.56, 0.64, 1)"
  hoverPatterns: ["lift", "tint", "scale"]
  reducedMotion: true

composition:
  layout:        "grid"
  contentWidth:  "container"
  framing:       "bordered"
  gridIntensity: "soft"
  rhythm:        "8px"

surfaceStyle: "solid"
blur:         "none"

iconography:
  treatment: "linear"
  set:       "lucide"
  size:      {"sm": "16px", "md": "20px", "lg": "24px"}
  stroke:    "2px"

components:
  button:
    primary:   {"background": "#F5D44F", "color": "#0F0F0F", "border": "2px solid #0F0F0F", "shadow": "0 3px 8px rgba(15,15,15,0.12)", "hoverBackground": "#F7E06C", "hoverShadow": "0 6px 16px rgba(15,15,15,0.14)", "hoverColor": "#0F0F0F"}
    secondary: {"background": "#FBF6E9", "color": "#0F0F0F", "border": "2px solid #3D81B5", "shadow": "none", "hoverBackground": "#DCEDF7", "hoverShadow": "0 2px 4px rgba(15,15,15,0.08)", "hoverColor": "#0F0F0F"}
    ghost:     {"background": "transparent", "color": "#0F0F0F", "border": "2px solid #0F0F0F", "shadow": "none", "hoverBackground": "#F8F0DE", "hoverShadow": "none", "hoverColor": "#0F0F0F"}
    danger:    {"background": "#C41E1E", "color": "#FFFFFF", "border": "2px solid #9B1B1B", "shadow": "0 3px 8px rgba(196,30,30,0.2)", "hoverBackground": "#A31919", "hoverShadow": "0 6px 16px rgba(196,30,30,0.25)", "hoverColor": "#FFFFFF"}
    sizes:     {"sm": {"height": "32px", "padding": "6px 14px", "fontSize": "0.875rem"}, "md": {"height": "40px", "padding": "8px 20px", "fontSize": "1rem"}, "lg": {"height": "48px", "padding": "12px 28px", "fontSize": "1.125rem"}}
    borderRadius: "12px"
    fontWeight: 600
    letterSpacing: "0"
    textTransform: "none"
  input:
    background: "#FBF6E9"
    color: "#0F0F0F"
    border: "2px solid #DDD4BF"
    borderRadius: "12px"
    padding: "10px 14px"
    focusBorder: "2px solid #C41E1E"
    placeholderColor: "#5A4A4A"
  card:
    base:  {"background": "#FBF6E9", "border": "2px solid #0F0F0F", "borderRadius": "16px", "padding": "24px", "shadow": "0 3px 8px rgba(15,15,15,0.12)"}
    hover: {"shadow": "0 6px 16px rgba(15,15,15,0.14)", "transform": "translateY(-2px)"}
---

# Peanuts Comic Schulz (1950)

> Cream newsprint, wobbling ink lines, and Charlie Brown yellow — fifty years of gentle melancholy distilled into a design system.

## Origin

Charles M. Schulz drew every one of the 17,897 *Peanuts* strips by hand from October 2, 1950 to February 13, 2000, never employing assistants or a studio system. Working first in Saint Paul, Minnesota and later in Santa Rosa, California, Schulz built a visual language of clean brush-pen ink on cream newsprint — rounded panel borders, hand-lettered captions, and a restrained Sunday-strip color palette rooted in mid-century printing limitations.

The strip's aesthetic became inseparable from American visual culture: Charlie Brown's yellow zigzag shirt, Linus's blue blanket, Snoopy's doghouse silhouette. Vince Guaraldi's 1965 jazz score for *A Charlie Brown Christmas* extended the gentle-melancholy tone into sound, cementing the Peanuts world as a place where warmth and wistfulness coexist without irony.

## Overview

Composition cues:
- **Layout**: Four-panel horizontal strip grid — the canonical Peanuts daily format, adapted to card-based UI
- **Content width**: Container (1024px max) — generous margins echoing the breathing room of a newspaper page
- **Framing**: Bordered — hand-drawn-weight ink borders (2px) on cream surfaces, slightly rounded
- **Grid intensity**: Soft — visible panel structure without rigid mechanical precision

## Colors

The palette draws from Sunday-strip printing on cream newsprint: muted, warm, never digitally saturated. Charlie Brown yellow dominates as the primary action color — it's the zigzag shirt, the kite, the optimism. Linus blue provides calm secondary support (the security blanket, the sky). Christmas red punctuates emotional moments sparingly. The entire system floats on warm cream (#F8F0DE) that evokes aged newsprint without yellowing into illegibility.

**Role usage**:
- Page background → `colors.background.page` (#F8F0DE cream newsprint)
- Card/panel surfaces → `colors.background.surface` (#FBF6E9 paler cream)
- Primary actions & highlights → `colors.primary.500` (Charlie Brown yellow)
- Secondary accents & links → `colors.secondary.500` (Linus blue)
- Error states & emotional emphasis → `colors.accent.500` (Christmas red)
- Body text & ink lines → `colors.text.primary` (#0F0F0F ink black)
- Subdued captions → `colors.text.muted` (#5A4A4A warm gray)

## Typography

The type voice is the cartoonist's hand — never typeset, never mechanical. Headings use Caveat to evoke Schulz's specific brush-pen lettering: slightly wobbly, warm, unmistakably human. Body text uses Quicksand for friendly rounded readability that doesn't fight the hand-drawn headings. Permanent Marker appears for exclamatory display moments ("GOOD GRIEF!"). No austere geometric sans-serif enters this system.

**Text styles**:
- `display-xl` — Permanent Marker, 96px, weight 400, line-height 1.0, letter-spacing -0.02em
- `display-lg` — Permanent Marker, 64px, weight 400, line-height 1.1, letter-spacing -0.02em
- `heading-1` — Caveat, 48px, weight 700, line-height 1.2, letter-spacing 0
- `heading-2` — Caveat, 36px, weight 700, line-height 1.2, letter-spacing 0
- `body-lg` — Quicksand, 18px, weight 400, line-height 1.625, letter-spacing 0
- `body-md` — Quicksand, 16px, weight 400, line-height 1.5, letter-spacing 0
- `caption` — Quicksand, 14px, weight 500, line-height 1.375, letter-spacing 0.05em
- `mono-md` — Source Code Pro, 14px, weight 400, line-height 1.5, letter-spacing 0

## Spacing & Layout

- Base unit: 8px rhythm (Schulz's panels breathe — never cramped)
- Scale: 2px → 128px in 12 steps
- Container max-width: 1024px (newspaper-column proportion)
- Section padding: 64px vertical default, 96px for hero sections
- Grid gap: 16px default (panel gutter width)
- Cards maintain 24px internal padding (generous comic-panel breathing room)

## Elevation & Depth

Depth is minimal and warm — this is ink on paper, not glass floating in space. Shadows use warm black (rgba 15,15,15) at low opacity to suggest newsprint stacking rather than digital elevation. The primary shadow (0 3px 8px at 12% opacity) mimics a comic page lifted slightly off a desk surface.

- Surface style: solid cream panels with ink-weight borders
- Blur: none (ink doesn't blur)
- Shadow ladder: xs (subtle page lift) → md (default card) → lg (hover emphasis) → xl (modal/overlay)
- Cards rely on border + subtle shadow rather than heavy drop-shadows

## Shapes

- Button radius: 12px (round, friendly, hand-drawn feel)
- Card radius: 16px (soft panel corners — Schulz never drew sharp rectangles)
- Input radius: 12px (matching buttons)
- Small elements (tags, badges): 8px
- Pill/full: 9999px for toggles and avatars

## Motion

Motion is restrained and gentle — matching Schulz's quiet storytelling pace. Nothing snaps or bounces aggressively. Hover states lift cards like picking up a comic page. Transitions use soft easing that suggests a hand-drawn frame advancing rather than a digital state change.

- Level: restrained
- Default duration: 250ms (unhurried, like reading a strip)
- Hover lift: translateY(-2px) over 250ms ease-out
- Scale on press: scale(0.98) — gentle acknowledgment
- Easing: cubic-bezier(0.4, 0, 0.2, 1) default; spring for playful micro-interactions
- Hover patterns: lift, tint, scale
- Reduced motion: respected (transitions collapse to instant)

## Techniques

### Hand-drawn wavy border
Simulates Schulz's slightly imperfect panel borders using SVG filter displacement.
```css
.panel-border {
  border: 2px solid #0F0F0F;
  border-radius: 16px;
  filter: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='wobble'%3E%3CfeTurbulence baseFrequency='0.02' numOctaves='3' seed='2'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='1.5'/%3E%3C/filter%3E%3C/svg%3E#wobble");
}
```

### Newsprint paper texture
Adds subtle grain to cream surfaces evoking aged newspaper stock.
```css
.newsprint-surface {
  background-color: #F8F0DE;
  background-image: url("data:image/svg+xml,%3Csvg width='200' height='200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='grain'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23grain)' opacity='0.03'/%3E%3C/svg%3E");
}
```

### Four-panel strip grid
The canonical Peanuts daily-strip layout adapted for card-based content.
```css
.strip-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  padding: 24px;
  background: #FBF6E9;
  border: 2px solid #0F0F0F;
  border-radius: 16px;
  box-shadow: 0 3px 8px rgba(15, 15, 15, 0.12);
}
```

## Iconography

Icons follow the hand-drawn line-art spirit — linear strokes at 2px weight on the Lucide set, which provides the cleanest rounded-corner aesthetic matching Schulz's gentle geometry. Icons should feel like they could have been drawn with a brush pen.

- Treatment: linear (outline only — no fills, matching ink-line vocabulary)
- Set: Lucide (rounded, friendly proportions)
- Stroke: 2px (matching border weight for visual consistency)

## Do's & Don'ts

### ✓ Do
- Use Caveat for all headings to maintain the cartoonist's hand-lettered voice
- Keep the cream newsprint background as the dominant surface — panels float on it
- Apply 2px ink-black borders on cards and interactive elements
- Maintain generous whitespace between panels (Schulz's strips breathe)
- Use Charlie Brown yellow (#F5D44F) for primary actions and highlights

### ✗ Don't
- Use modern flat-design sans-serif typefaces — the voice is rigorously handwritten
- Apply saturated digital colors — stay within Sunday-comic muted mid-century palette
- Use sharp angular geometry — Schulz's line is rounded, gentle, slightly wobbly
- Adopt a cynical or dark-humor tone — Schulz's melancholy is gentle, never bitter
- Include photographic imagery — hand-drawn line-art only, in Schulz vocabulary
- Use black or dark backgrounds — forever cream-newsprint light-mode
- Fall into generic "comic strip" clichés — use specific Peanuts visual vocabulary

## Applications

This system is ideal for storytelling platforms, children's educational content, personal blogs with a warm narrative voice, newsletter designs, and any product that wants to feel handmade, approachable, and gently nostalgic. It works beautifully for reading-focused interfaces where content panels unfold like comic strips — documentation sites, recipe collections, journaling apps, or portfolio pages that prioritize warmth over corporate polish.
