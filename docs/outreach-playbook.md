# AIBD Scout: outreach playbook

How Perlead finds pilot users and early buyers among people who ask for this in public. The scout finds and drafts. **Simo sends everything.** Nothing is posted, replied or messaged automatically.

## Who runs it

A dedicated agent, **AIBD Scout**, with read access to X and web search only. No access to any other company's data or memory. Weekdays at 9:30 (America/Mendoza), one pass.

## The flow Simo uses

1. **Public touch first.** Either:
   - a short reply on their post: "I can help with this. Here's what we've been building." plus one useful, specific line about their problem, or
   - a quote of one of Simo's own posts on the topic, answering their question with it.
2. **Then the link by DM.** If they engage (reply, like, follow, or ask), Simo sends the Perlead link by DM.
3. No link in the first public reply unless they ask for it.

The scout prepares both pieces as drafts: the public reply (or which of Simo's posts to quote, with the quote text) and the follow-up DM.

## Search queries (X)

```
1. ("AI SDR" OR "AI sales rep" OR "sales bot") ("looking for" OR recommend OR "anyone using" OR "any good") -is:retweet lang:en
2. ("follow up" OR "follow-ups" OR followups) (leads OR prospects OR pipeline) (automate OR "AI agent" OR bot) ("how do" OR "looking for" OR "I wish") -is:retweet
3. ("grok bot" OR @bot) (sales OR "follow up" OR leads OR CRM OR outbound) -is:retweet
4. ("forgot to follow up" OR "leads go cold" OR "deals die" OR "lost the lead") -is:retweet lang:en
5. (seguimiento OR "follow up") (leads OR clientes OR ventas) (IA OR bot OR agente) (recomienden OR "alguien usa" OR busco) -is:retweet lang:es
6. conversation_id:<large Grok Bot feedback thread> (sales OR "follow up" OR CRM OR leads)
Exclude in all: -hiring -"we help" -"DM me" -"book a demo"
```

LinkedIn (web search, no login, no automation): `site:linkedin.com/posts ("AI SDR" OR "follow-up" OR "seguimiento") (recommend OR "looking for" OR recomienden)`. LinkedIn drafts only.

## Scoring (0 to 10)

| Signal | Points |
| --- | --- |
| Explicitly asks for a tool or help with follow-ups, AI SDR or a sales bot | +3 |
| Sells B2B (bio or post: founder, sales, agency, SaaS) | +2 |
| Makes the buying decision (founder, CEO, head of sales) | +2 |
| Post is less than 72 hours old | +1 |
| Already uses Grok Bot or another agent | +1 |
| Real account with its own history | +1 |
| Sells a competing tool or outbound services | Exclude |
| Already contacted, or asked not to be contacted | Exclude |

6 or more: draft. 4 or 5: "worth a look" list. Below 4: skip.

## Caps and anti-spam rules

- At most 5 public reply drafts and 3 DM drafts per day. Highest scores first.
- One touch per person. No follow-up on X if they do not engage.
- DM only after they engaged, or if DMs are open and the score is 8 or more.
- The reply answers their question first and is specific to their post. Never the same text twice.
- Say plainly that Simo is building this. No fake neutrality.
- Do not reply to posts older than 7 days.
- Keep the contacted list in a private sheet, never in this repo.
- If anyone complains, pause the scout and review these rules.

## Daily output

A list in chat: post link, author, score, why it fits, the reply draft (or the post to quote and the quote text), and the DM draft for later. Simo picks, edits and sends.

## Budget

About 6 searches of up to 25 posts each: around 150 X reads per day.
