# find-my-generation

Enter birth year → see how you relate to every US generation.

## Session rules
- Work starts from a pasted `HANDOFF.md`. Run ONLY the ticket it names.
- Read only: this file, `docs/STATUS.md`, the ticket file, and files the ticket lists. Don't explore the repo beyond that.
- User is a scientist, hobbyist coder. Concise answers; explain non-obvious coding terms briefly.
- User is on API billing. Keep token use low.

## Finishing a ticket (required)
1. Meet the ticket's "Done when".
2. Update the docs the ticket lists, plus `docs/STATUS.md` (status + one-line note).
3. Add any new decision to `docs/DECISIONS.md`.
4. Overwrite `HANDOFF.md` to point at the next ticket (see `docs/tickets/_TEMPLATE.md` for format).
5. Tell user: what was done, which model the next ticket needs, and to run `/clear` then `/model <x>` before pasting the handoff.

## Don'ts
- Don't start the next ticket on your own.
- Don't choose the method for B (membership %); that is ticket T04's job.
