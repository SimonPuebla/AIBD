# Perlead design system

Version 0.2. Goal: read like a serious financial or infrastructure company, not like an AI tool. Quiet, precise, confident.

Patterns are adopted from public B2B sites studied on 2026-11-22: Carta, Instantly, Clay, Stripe, Mercury, Attio, Ramp, Linear. No assets, logos, illustrations or copy were taken from them. Fonts are free (Google Fonts).

## Principles

1. **Editorial, not techy.** Serif display headlines over a neutral sans body. (Carta, Mercury, Attio use serif display faces; Ramp and Linear keep body sans.)
2. **Warm paper, black ink, one accent.** No gradients, no glow, no glass. (Carta `#fbf8f7` with `#1a1a1a`; Clay `#f4f3f0`; Ramp `#f4f2f0`.)
3. **Show the product, not a metaphor.** The hero carries a real-looking product view: a lead dossier and a draft waiting for approval. (Ramp, Attio and Linear lead with UI mockups.)
4. **Structure is visible.** Hairline rules, a 12-column grid, mono labels with a small square marker. (Carta's corner ticks, square bullets and mono labels; Linear's FIG labels.)
5. **Say less.** Short declarative headlines, a one-sentence subhead, two CTAs at most. No "supercharge", "unlock", "10x", emoji, or AI hype. (Ramp "Time is money. Save both."; Mercury "Radically different banking".)
6. **Proof is stated with its caveat.** Numbers sit in a ruled band with mono labels, and the caveat is printed next to them. (Ramp's metric ticker; Carta's "Trusted by" band, adapted honestly since Perlead has no customer logos yet.)

## Tokens

### Color

| Token | Value | Use | Reference |
| --- | --- | --- | --- |
| `--paper` | `#f7f5f1` | Page background | Carta, Clay, Ramp warm off-whites |
| `--paper-2` | `#efece6` | Alternate section, mockup chrome | Clay `#e0dedc` family |
| `--card` | `#ffffff` | Cards, mockup panels | Attio, Ramp |
| `--ink` | `#16181b` | Headlines, primary buttons | Carta `#1a1a1a`, Attio `#101112` |
| `--ink-2` | `#3d4248` | Body text | Carta `#394040` |
| `--muted` | `#6b7078` | Secondary text, captions | Instantly `#6d727e`, Attio `#75777c` |
| `--rule` | `#dcd8d0` | Hairlines and borders | Carta `#dedfdf`, Clay `#e0dedc` |
| `--accent` | `#1f4d3a` | Markers, links, focus, the one highlighted plan | Single accent rule from Carta (orange) and Ramp (lime), in a deep green that reads as finance |
| `--accent-soft` | `#e3ece6` | Status pills | |
| `--warn` | `#8a5a12` / `#f5ecd9` | "Awaiting approval" pill | |
| `--dark` | `#121416` | Dark band (case study) | Carta and Linear dark sections |

### Type

Fonts: **Newsreader** (display serif, close in role to Tiempos and Sang Bleu), **Inter** (body), **IBM Plex Mono** (labels; Carta uses IBM Plex Mono).

| Style | Font | Size / line height | Weight | Tracking |
| --- | --- | --- | --- | --- |
| Display | Newsreader | clamp(44px, 6vw, 76px) / 1.02 | 400 | -0.02em |
| H2 | Newsreader | clamp(32px, 4vw, 48px) / 1.08 | 400 | -0.015em |
| H3 | Inter | 17px / 1.35 | 600 | -0.005em |
| Lead | Inter | 19px / 1.55 | 400 | 0 |
| Body | Inter | 16px / 1.6 | 400 | 0 |
| Small | Inter | 14px / 1.5 | 400 | 0 |
| Label | IBM Plex Mono | 12px / 1.4, uppercase | 500 | 0.08em |
| Metric | Newsreader | 44px / 1 | 400 | -0.02em |

Rules: serif only for display, H2 and metrics. Never bold serif. Labels always mono uppercase with a 7px square marker (Carta).

### Spacing and grid

- 4px base. Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
- Container 1200px, 32px side padding (20px on mobile). 12 columns, 24px gutter.
- Section padding 112px desktop, 72px mobile. Sections separated by a full-width 1px rule (Carta, Linear).

### Radii and shadows

- Radius: 2px buttons and inputs, 6px cards and mockup (Carta is near-square; Ramp and Attio ~4 to 8px). No pills except status chips (999px).
- Shadow: only on the product mockup: `0 1px 0 rgba(0,0,0,.04), 0 24px 48px -24px rgba(20,20,20,.18)` (Attio, Ramp mockup lift). Everything else is flat with hairlines.

## Components

- **Nav.** Wordmark left in Newsreader, 4 text links in Inter 14px, right: a text link "Install free" and a solid black button "Get the Pack". Bottom hairline. (Attio, Ramp, Clay: one solid black CTA plus one quiet secondary.)
- **Hero.** Left-aligned (Carta, Ramp, Linear), mono label, display headline on two lines, one-sentence lead, two buttons (solid ink + outline). Below it, full-width product mockup.
- **Product mockup card.** A window with thin chrome. Left pane: the lead dossier (company, stage, facts each with source and date, promises, next step). Right pane: the follow-up draft with status pill "Awaiting your approval", evidence list, judge checks, and Edit / Approve and send (human) actions. Built in HTML and CSS, no images. (Ramp approvals UI, Attio record view.)
- **Principles band.** Under the hero, instead of a logo bar: four short rules in mono-labeled columns divided by hairlines. (Carta logo band layout; Perlead has no customers to show yet, so no fake logos.)
- **Feature rows.** Two-column rows: H2 and paragraph left, a small numbered list or spec table right. Numbered labels "01" to "05" in mono. (Linear FIG labels, Carta "The Carta difference" grid.)
- **Metric band.** Dark section, five metrics in a ruled row, mono labels, caveat paragraph directly under. (Ramp ticker, Carta dark sections.)
- **Pricing table.** Three columns in one bordered table with hairline dividers, not floating cards. Highlighted plan gets an accent top border, not a color fill. TBD shown as a mono tag. (Stripe, Linear pricing tables.)
- **FAQ.** Two columns: H2 left, `details` list right with hairline separators and a plus sign. (Attio, Linear.)
- **Footer.** Wordmark, one-line description, link columns, small print with the drafts-only statement. (Carta, Mercury.)
- **Buttons.** Solid: ink background, paper text, 2px radius, 44px tall, Inter 15px 500. Outline: 1px ink border. Text link with a trailing arrow. No gradients.

## Copy rules

- Short declarative sentences. Present tense. Sentence case headlines.
- Concrete nouns: lead, dossier, draft, follow-up, reply, CRM. Avoid: AI-powered, supercharge, unlock, seamless, revolutionize, game-changing, magic, 10x.
- Every claim must be true today. Numbers carry their caveat. Prices say TBD until set.
- Always state that a human sends.
