---
name: perlead-crm-sync
description: Use after triage, calls and weekly review to keep the owner's CRM in line with the dossiers. Proposes changes; writes only what the owner allowed.
version: 0.1.0-stub
---
# CRM sync (stub)

Status: stub in v0.1. Behavior below is the contract; detailed steps per CRM come in a later version.

- Search before you create. Never create duplicates, never delete or merge records.
- Log touches and replies as activities linked to the contact and company.
- Stage, owner, amount and lifecycle changes are **proposals** with evidence, applied only if the owner allowed that type of write in onboarding.
- No CRM: keep the dossier spreadsheet as the CRM.
- Supported targets to start: HubSpot, Attio, Pipedrive, Google Sheets.
