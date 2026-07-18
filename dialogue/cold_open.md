# Chapter 1 — Cold Open (FINALIZED SCRIPT)

Authoritative verbatim text + presentation for the game's opening. Supersedes the
bible §16.2 Beat-1 placeholder (which named *How Distant Your Heart* and had no
Tenebris framing). Sync the bible to this later.

**Music:** Osrid's Theme (`MUS_OSRID_THEME`) begins the instant **New Game** is
chosen and plays unbroken through the entire cold open (narration → reflection →
letter). Pelluca Valley music only comes up later, at the dock (Beat 1 continuation).

**Framing device:** the whole opening is presented as *the recovered notes of
Professor Tenebris* — Cadmus Umbra's ~2000-years-later descendant from Dreamstone
Mysteries, who walked ancient Cormoria herself and was studying Koraidon at DM's
close. The redacted date **XX-XX-29** (rendered literally) implies the notes were
found sometime after DM's events, possibly read by the DM champion (her assistant,
who became Champion of Cormoria after defeating Kohla). This frames Ruination as
Tenebris's reconstruction and bookends the game (→ the Veddev/Eden ending).

---

## Presentation flow

1. **New Game** chosen → screen black; Osrid's Theme begins.
2. The header appears first, alone, on black:
   **From the notes of Professor Tenebris - XX-XX-29**
3. The header fades, and the notes write on **word by word** — smooth, flowing,
   white text centered on black — the three paragraphs below. *(Bespoke intro
   render, NOT the standard message box.)*
4. The notes finish → everything sinks to black; hold a beat.
5. Osrid (masked overworld sprite) materializes, looking down at his own
   reflection in a dark pool. The first message box rises at the bottom.
6. **Umbra's letter** plays out in the box for the player to read + click through
   (Cadmus portrait, expression toggling neutral ↔ smile).
7. Portrait switches to **Osrid** (masked; nameplate **"Prince ???"**) → the
   **name-entry prompt** (default **Osrid**) → Osrid's reply line. The signature
   IS the reply.
8. *(Beat 1 continues — fade, southern Pelluca dock w/ the* Pale Veluza*, meet
   Umbra, to the lab. Pending the Pelluca Valley map build.)*

---

## Part 1 — The Tenebris notes  *(white-on-black, word-by-word reveal)*

**Header:**
> From the notes of Professor Tenebris - XX-XX-29

**¶1:**
> 3000 years before Red started his journey from Pallet Town, the world of Pokémon was a very different place.

**¶2:**
> It was a terrifying era of imperial conflict and strange cults, a setting so far removed from what we know in the modern Pokémon world that "they" who decided history have done everything they possibly could to bury those records forever.

**¶3:**
> This is the story I know of that place and time, the seed of all which would come to be...

---

## Part 2 — The reflection

Notes clear → black holds → Osrid's masked overworld sprite + the dark-water
reflection materialize under the same music. The letter box rises.

---

## Part 3 — Umbra's letter  *(portrait: Cadmus; box text below; `\p`/`\l` pagination added at scripting)*

`[Cadmus — neutral]`
> My Prince, it has been far too long since our last correspondence.

> Word has reached me of your current physical condition in light of what happened during the Sevii campaign. It is sheer travesty.

> My fury at Boran Surge's negligence and the incompetence of his commanding officers in their choice of strategy against both Kanto and Johto is a fury I cannot transcribe here in written form, for the very ink would turn to fire if I were to try.

> As you can imagine, I have made my displeasure to your superiors excruciatingly known.

`[Cadmus — smile]`
> You will be given full details later, I will say that in brief, you are now reassigned formally to service under my authority as Vizier Of Education, along with an honorable promotion to the rank of Rainhawk.

> You will be the youngest in Cormoria's history to achieve this rank...yes, even younger than "him".

`[Cadmus — neutral]`
> I will see you at my laboratories soon. I am making arrangements with the captain of the Pale Veluza to receive you, so inquire with General Albrecht for additional details. By the time you receive this, he will have more to share with you.

> P.S. Please burn this letter as soon as you have drafted your acceptance, as we must minimize the paper trail. There are many eyes in places even I cannot grasp.

> Please sign your response with the name that only "you" know, so I may know this was not intercepted. The Templar near your current base of operations should be able to deliver your response to me directly.

`[Cadmus — smile]`
> My dearest regards,
> Cadmus Umbra

---

## Part 4 — Osrid's reply

`[Osrid — masked; nameplate "Prince ???"]` → **name-entry prompt** (default Osrid)
→ reply line:

> Request acknowledged and accepted. I will make preparations to travel immediately.

---

## Notes for scripting

- **Signature is name-free everywhere except the player's entry.** The letter and
  the reply never state his name, so it stays consistent whether the player keeps
  "Osrid" or renames him. Umbra's "the name that only 'you' know" makes the naming
  prompt a security check, diegetically.
- **The quoted "him" and "you"** are deliberate — subtext the player isn't in on
  yet (curly quotes render fine on GBA).
- **Portrait toggle map** (adjust freely): neutral for the opening, the Sevii
  condition, and the Boran fury (cold, controlled anger reads harder than a
  scowl); smile for the Rainhawk promotion / "even younger than 'him'" and the
  closing "My dearest regards"; neutral for the P.S. / burn instruction / "eyes
  even I cannot grasp."
- **Assets already in place:** `MUS_OSRID_THEME`; Osrid's masked portrait
  (scene-driven nameplate → "Prince ???"); Cadmus portrait neutral + smile;
  Osrid + Cadmus overworld sprites; the engine naming screen. Not yet built: the
  intro render (word-by-word notes), the reflection scene, and the Pelluca dock/lab
  maps.
