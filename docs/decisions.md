# Decisions log

Each decision has a short rationale and, where possible, a source. Newest first.

## 2026-11-22 · v0.2: decided and implemented without waiting on Simo

| # | Decision | Why | Source |
| --- | --- | --- | --- |
| 1 | **Mockup lead is fictional**: "Fernhill Data", contact Maya Okafor, emails on the reserved `.example` domain, labeled "Example · fictional company". | A real company would be a false endorsement. `.example` is reserved by RFC 2606 and can never belong to anyone. Facts are dated and sourced, which is what the product actually does. | RFC 2606 |
| 2 | **Accent stays deep green `#1f4d3a`.** | 8.8:1 contrast on the page background (AAA). No large B2B reference uses it: Carta is orange, Instantly and Attio blue, Stripe purple, Ramp lime, Clay multicolor. Green reads as finance and "go" without the AI-purple cliché. | WCAG 2.1; colors read from each site's CSS, 2026-11-22 |
| 3 | **Fonts self-hosted** (Newsreader, Inter, IBM Plex Mono, latin WOFF2) with OFL files in `web/fonts/`. | Removes every third-party request, so the privacy notice can truthfully say "no third parties". Google Fonts calls send visitor IPs to Google, which a Munich court ruled a GDPR violation in 2022. OFL allows bundling with the license included. | SIL OFL 1.1; LG München I, 3 O 17493/20 |
| 4 | **Public repo keeps only the free Starter** (skills 00 to 02), the site, the methodology, Case 0 and this log. **Pack skills (03 to 10), the install prompt for buyers, templates and internal ops** (plan, payments, outreach playbook) moved to the private repo `SimonPuebla/perlead-pro`. | A paid product can't be in a public repo. Creem delivers files after purchase and can also grant access to a private GitHub repo, so private is the natural source of truth. **Note:** the public repo's git history still contains the v0.1 Pack files and playbook. Removing them would need a history rewrite and a force push, which needs Simo's explicit OK. The exposure is small (one day public, plain text), and value comes from updates and setup. | https://docs.creem.io/features/addons/file-downloads, Creem API product feature `githubRepository` |
| 5 | **Licenses**: MIT for site code and tools; CC BY 4.0 for Starter content; brand (name, logo) all rights reserved; the Pack gets a commercial license (perpetual, internal use by the buying organization, unlimited seats, no redistribution, 12 months of updates). | MIT is the norm for site code. CC BY makes the free Starter shareable while requiring a link back, which works as distribution. The Pack license protects the paid part without per-seat friction. | https://choosealicense.com, https://creativecommons.org/licenses/by/4.0/ |
| 6 | **Refund policy**: Pack, 14 days full refund with no questions; Setup, full refund if cancelled 24 h or more before the session, and a fix-or-refund guarantee for 14 days after it. Published at `web/refund.html`, plus plain `terms.html` and `privacy.html`. | Creem lets sellers set the policy but can refund within 60 days anyway to prevent chargebacks (25 USD each). A generous 14-day window matches the EU withdrawal norm, costs little on a digital product and lowers purchase anxiety. | https://docs.creem.io/merchant-of-record/finance/refunds-and-chargebacks, https://www.creem.io/buyer-terms |
| 7 | **Prices: Starter $0, Pack $49 one-time, Setup $450 one-time** (includes the Pack). | Lavender, the closest paid tool, charges $29/mo Starter and $49/mo Pro (checked 2026-11-05). Free marketplace packs set the floor, so the Pack must be an easy one-time buy: $49 equals one month of Lavender Pro and sits at the top of the tested $29 to $49 range. B2B buyers are less price-sensitive, and one-time pricing has no subscription objection. Setup is about 3 to 4 hours of work. $450 is a round, institutional number near the top of the $300 to $500 range and below Lavender's Ora agent at $500 per month. | https://thesdrlist.com/tools/lavender/, https://moderninbound.com/blog/lavender-vs-cold-email-agency |
| 8 | **Logo**: a Newsreader "P" with a small square (the system's "next step" marker) on a deep-green rounded square, plus the wordmark in Newsreader 500 converted to outlines. SVG sources, PNGs (32, 180, 192, 512, 1200) and a 1200×630 OG image in `web/brand/`, built by scripts in `tools/`. | It reuses the type and marker that already define the site, so it is consistent from day one. Outlines mean no font dependency. | `web/DESIGN.md` § Brand |
| 9 | **Realism**: product panels for the lead record, approval queue and weekly review, all labeled fictional; a full footer with legal links and contact; meta, OG and Twitter tags; `404.html`, `robots.txt`, `sitemap.xml`, web manifest. Absolute URLs assume `web/` is deployed at the root of `https://perlead.ai`. | Real company sites have these, and every item is true today. No customer logos, testimonials or numbers beyond Case 0. | Patterns from Ramp, Attio and Linear (see DESIGN.md) |
| 10 | **Contact email**: `simonpueblafin@gmail.com` until `perlead.ai` is bought, then switch to `hello@perlead.ai`. | A `hello@perlead.ai` address would bounce today. Legal pages must show a working contact and who the operator is; Argentine consumer law requires clear, truthful information to buyers. | Ley 24.240 (Defensa del Consumidor) |
| 11 | **Setup sold through Creem; Polar is the fallback** if Creem's review rejects a service product. | Creem's terms define "Product" as including services. Their review is the final word. | https://www.creem.io/terms §2.1.11 |

## 2026-11-22 · v0.1

| Decision |
| --- |
| Name: Perlead. Domain perlead.ai (not bought yet). |
| Positioning: digital B2B product for companies, not a course. |
| Website language: English. |
| Payments: Creem as merchant of record, selling as an individual. Polar as backup. |
| Case 0 described only as "a B2B legaltech", reported and unaudited. |
| All outbound (email, LinkedIn, X) is draft-only; a human sends. |

## Still needs Simo (legal or physical only)

- Creem account: identity verification (KYC) and payout account.
- Create the two Creem products (Pack $49 with the zip from `perlead-pro`, Setup $450) and paste their checkout links where the site says `CREEM_CHECKOUT_URL`.
- Buy `perlead.ai`, then deploy `web/` and switch the contact email.
