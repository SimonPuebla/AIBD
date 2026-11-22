# Payments

Decision (2026-11-22): **Creem** as merchant of record, selling as an individual. **Polar** as backup. No Stripe account needed.

## Creem (default)

- Fee: 3.9% + USD 0.40 per successful transaction, no monthly fee, no international card surcharge. Source: https://www.creem.io/pricing
- Merchant of record: handles buyer-side sales tax and VAT, refunds and chargebacks.
- Argentina is a supported merchant country; individuals can sell after KYC, no company needed. Source: https://docs.creem.io/merchant-of-record/supported-countries
- Payouts on the 1st and 15th. Bank transfer: USD 7 or 1% of the payout, whichever is higher. Stablecoin (USDC on Polygon): 2%. Source: https://docs.creem.io/merchant-of-record/finance/payout-accounts
- Net example: USD 49 sale leaves USD 46.69; USD 300 leaves USD 287.90 (before payout fees).

Unverified, check during signup:
- Whether a Wise account can be the payout bank account.
- Whether Creem allows selling a service (the done-for-you setup). If not, invoice the setup through PayPal or Payoneer.

## Polar (backup)

- Fee: 5% + USD 0.50, plus 1.5% for non-US cards. Source: https://polar.sh/docs/merchant-of-record/fees
- Payouts through Stripe Connect Express (no Stripe account needed), to a bank in your country in local currency. Source: https://polar.sh/docs/features/finance/accounts

## Not used

- Lemon Squeezy: closed new sign-ups on 2026-11-16, stops processing on 2027-03-31. Source: https://www.lemonsqueezy.com/blog/saying-goodbye-to-lemon-squeezy
- Gumroad: 10% + USD 0.50 plus card fees; no Wise payouts. Source: https://gumroad.com/help/article/13-getting-paid
- Wise Business: not available for Argentine residents.

## Wiring the landing

The landing uses the placeholder `CREEM_CHECKOUT_URL` in `web/index.html`. Replace it with the real Creem checkout links (one per paid offer) once products exist in Creem.

## Taxes

The merchant of record covers the buyer's sales tax. The seller's own income tax and any local invoicing or currency rules are the seller's responsibility: check with an accountant.
