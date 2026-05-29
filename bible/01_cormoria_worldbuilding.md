<!-- This file is a split-section view derived from dreamstone_ruination_bible_v0.9.7.md (the canonical full bible at the repo root). Lines below correspond to the source lines noted in INDEX.md. Edit the canonical file and regenerate splits — do not edit splits directly. -->

## 2. Worldbuilding Foundations

These are the *meta-rules* we operate under — production-side principles that constrain (and enable) story-side decisions. Locked into v0.4 after substantial discovery work in the codebase and source materials.

### Data-layer baseline `[LOCKED]`

**Every Pokémon species from generations 1 through 9 is present in the Dreamstone Mysteries codebase data tables.** This includes legendaries, mythicals, Paradox Pokémon, regional variants, and all four Treasures Of Ruin. The Dreamstone Mysteries creator deliberately curated a *smaller obtainable* dex for his game, but the underlying data is complete.

**Implication:** Our Pokémon roster choices are *purely curatorial*, not "can we even use this species." We pick which species are obtainable, where, how, and at what rate. No species needs to be added from scratch to our codebase — only individual Pokémon *forms* (e.g., Mega Baxcalibur, see below) need new data.

### Source of truth hierarchy `[LOCKED]`

When determining what currently exists in Dreamstone Mysteries (the game we are forking), authority order is:

1. **The user's direct play experience** — highest authority for any player-facing question
2. **The Dreamstone Mysteries Dex spreadsheet** (uploaded to project) — authoritative for the *currently obtainable* dex, locations, rarities, and bonus items
3. **The Dreamstone Mysteries source tree** — authoritative for data and assets that exist *but may or may not be reachable* in normal play
4. **`pokeemerald-expansion` upstream documentation** — authoritative for engine behavior and base mechanics
5. **Canon Pokémon material** (Bulbapedia, official sources) — authoritative for canonical story, species data, and mainline-game mechanics

**Anti-pattern explicitly flagged:** The source tree contains substantial inherited base-Emerald data that is NOT reachable in Dreamstone Mysteries gameplay (Hoenn Routes 101-104, unused starters from earlier base Emerald, encounter tables for unobtainable Pokémon, etc.). The presence of data in source does not mean it's playable. We verify obtainability via #1 or #2, never #3 alone.

### Geographic reuse principle `[LOCKED]`

**Dreamstone Mysteries' Cormoria is a temporally-aged version of empire-era Cormoria.** Our game is the *prequel*; the land we build is what existed ~2,000 years before DM. Across that gulf:

- **Empires fall.** What is a thriving imperial city in our era may be a base camp, ruin, graveyard, or wilderness in DM. The reverse is rarely true (cities don't grow from nothing across millennia of imperial collapse).
- **Base camps become cities (in our era).** DM's "Ceram Base Camp," "Mirroh Base Camp Graveyard," and "Rivetshore Ranger Day-Care" are explicitly the *remnants* of larger empire-era settlements in our game's timeline. We can flesh them out into full cities with names, infrastructure, and political identities.
- **DM's "Ancient" areas are direct windows into our era.** DM's "Ancient Ceram" and "Ancient Mirroh" maps are accessed through dreamstone time-travel events. Players who play both games will see *the same locations* — once in their imperial prime (our game), once as ruined remnants (DM).
- **We can add locations DM doesn't have.** Empire-era Cormoria was larger and more developed than DM's modern Cormoria. We can introduce cities, fortresses, academies, military bases, embassies, and other locations destroyed or abandoned by DM's era.

This is a *worldbuilding gift*: the geographic reuse isn't a constraint, it's a *narrative device*. Players who notice will feel the weight of millennia.

### Known Cormorian geography (from DM Dex spreadsheet) `[LOCKED]`

These are the named locations confirmed in modern Dreamstone Mysteries. Our game can reuse, expand, rename, or precede them.

**Cities:**
- **Fennilahl Town** — has the Fennilahl Underpass beneath it
- **Galecrest City** — has the "rich lady pearl quest"
- **Gastree City** — teahouse quest location
- **Pelluca City** — near Route 6
- **Rivetshore City** — has the Ranger Institute and Day-Care
- **Silversun City** — has the Sewers and Somber HQ in the theater

**Mountain systems:**
- **Mt. Ceram** + Mt. Ceram Caves + Mt. Ceram Peak
- **Mt. Mirroh** + Interior (1F / B1F / B2F) + Peak
- **Ancient Ceram** (time-displaced version, accessed via dreamstone events)
- **Ancient Mirroh** (time-displaced version, accessed via dreamstone events)

**Wilderness / forests:**
- **Vilethorn Woods** — Drowzee, Morelull, Foongus, etc.
- **Ivy Forest** + **Ivy River**
- **Lily Pond**
- **Winterlily Hollow**
- **Vine Caverns**
- **Static Cave**

**Underground:**
- **Fennilahl Underpass** — Teddiursa, Meditite, Tinkatink in DM
- **Silversun Sewers**

**Story-only / minor:**
- **Carabrue Town** — Tenebris's Lab (no wild encounters)
- **Ceram Base Camp** — has the Drilbur drill event
- **Mirroh Base Camp Graveyard**
- **Rivetshore Ranger Institute**, **Route 6 Ranger Institute**

**Routes:** Route 1 through Route 7 (numbered, not named-after-Hoenn)

**Endgame:** Victory Road, Cormoria Hall of Fame

These names are *DM's* names. We are free to keep, rename, or expand them for the empire-era. Particularly suggestive renames:
- "Base Camp" locations → likely full cities in our era
- "Ranger Institute" → some empire-era institutional building (military academy? scout corps?)
- "Carabrue Town" → may or may not be founded yet; if it exists, its character will be very different
- "Winterlily Hollow" — name has fairytale resonance, may have deeper history

### Project scope ambition `[LOCKED]`

Our project may *expand* Cormoria significantly beyond DM's footprint:
- Adding empire-era cities that no longer exist by DM's era
- Adding embassies, military fortresses, the imperial capital itself (DM may not feature it as a wild-encounter location)
- Adding satellite locations: Paldean diplomatic compound, Western Coalition border fortifications, Sevii Islands settlement (lost to Kanto in the war)

Scope is a real constraint — every added location is map work, encounter table work, NPC work, and scripting work. We will not enumerate the full expansion now; we will add as the story demands.

### Engineering handoff document `[LOCKED]`

**`DREAMSTONE_HANDOFF.md`** is canonical project documentation, located alongside this bible. It is a record from a prior Claude session that successfully made ~15 changes to the Dreamstone Mysteries codebase and produced a working compiled `.gba` that the user verified in mGBA.

The handoff doc contains **verified patterns** for the most common change types we will be making — Pokémon stats/abilities/evolutions, moves, sprites + palettes, scripts (map dialogue, wild encounters, eggs), PC starting items, regional Pokédex registration — plus gotchas, anti-patterns, and the build's specific behavior in GenSpark.

**Anything in the handoff doc takes precedence over my prior assumptions about how things work.** Specifically: I was treating the encounter JSON file as authoritative for what's reachable in the game; I was producing palette patches without analyzing per-index sprite mappings; I was generating patches without the "delete compiled binaries to force rebuild" trick. The handoff doc corrects all of these and shows what *actually works* in this codebase. I should consult it before any production patch.

**The pipeline is validated.** Real edits → compiled `.gba` → playable in mGBA is a verified loop. No further validation patch is needed; we move directly to real production work.

### Local compile pipeline `[LOCKED v0.9.6]`

**As of v0.9.6, the compile pipeline runs locally in the Claude session environment.** Previous compilations went through GenSpark; this is no longer needed. The local pipeline was validated in v0.9.6 by successfully compiling a 32MB BPEE01 GBA ROM containing the v10 Bloodsnow Teddiursa-line palette patch.

**Required toolchain (install via `apt-get install` without sudo, already root in session):**
```bash
apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi \
                   build-essential libpng-dev pkg-config golang-go
```
(GCC 13.2.1 installed via this command works; GenSpark used 14.2.1 but the difference is irrelevant.)

**Critical gotcha — poryscript Mach-O binary:** The bundled `tools/poryscript/poryscript` in dsmyst is a **macOS Mach-O ARM64 binary** that will not run on Linux. Build a Linux ELF replacement from source:
```bash
cd /tmp && git clone --depth 1 https://github.com/huderlem/poryscript.git
cd /tmp/poryscript && go build -o poryscript .
cp /tmp/poryscript/poryscript <dsmyst_working_tree>/tools/poryscript/poryscript
chmod +x <dsmyst_working_tree>/tools/poryscript/poryscript
```
This needs to be done once per fresh working tree. After replacement, normal `make` invocations work.

**Build invocation:**
```bash
cd <dsmyst_working_tree>
make tools          # First-time only — builds the bundled C/C++ tools
make -j$(nproc) modern   # Full build. ~4 minutes single-core; faster with more cores
```
Output: `pokeemerald.gba` (32MB) with "POKEMON EMER" header (BPEE01). Verify with `file pokeemerald.gba`.

**Memory budget tracking (current as of v0.9.6 Bloodsnow integration):**
- EWRAM: 87.60% used
- IWRAM: 86.54% used
- ROM:   86.90% used

Future feature additions need to track these. We have ~13% headroom in each but it's not huge.

**Storage management:** After compilation, the `build/` directory and `pokeemerald.gba` / `pokeemerald.elf` / `pokeemerald.map` can be removed to save ~150MB of disk if storage becomes tight. The patch and source modifications are preserved separately in the working tree.

**Network availability:** The session's `bash_tool` egress is restricted to a whitelist that includes `github.com`, `archive.ubuntu.com`, `pypi.org`, `npmjs.com`, and a few others. This is enough to install the toolchain and build poryscript but NOT enough to reach arbitrary domains. If a future build needs a package not on the whitelist, escalate to user for alternatives.

### Recent historical events shaping the present `[LOCKED]`

These are background facts about the Cormorian Empire's recent past (within the last ~30 years) that are *not* the plot of the game but provide essential context for many characters' motivations.

**~30 years before story start: The Cormoria-Sinnoh Territorial Dispute.**
- A border conflict between Cormoria and Sinnoh
- Resulted in significant civilian displacement on the Sinnohian side
- The Cormorian Empire took in Sinnohian war orphans through state-run military-managed orphanages
- This is the institutional pathway by which **Nemo Korolev** (Section 7) entered Cormorian service: he was one of these orphans, conscripted into the military as a teenager
- Implications: Cormoria has demographic presence of Sinnohian descent in its military and civic life. Not all Cormorians are Cormorian-born.

**10 years before story start: The Assassination of Prince-Consort Eldred Nightfall.**
- Eldred Nightfall — Empress Pierra's husband, Osrid and Rhydia's father — was assassinated by the proto-Sword Cult
- Osrid and Rhydia were both **10 years old** at the time
- **Sable Ashland** (Eldred's best friend and military colleague) was *also* at the scene; he was kidnapped during the attack and used in a Dreamstone resonance experiment that displaced him into Ancient Cormoria
- Because of Sable's simultaneous disappearance, the **Ashland family was suspected** of complicity in Eldred's death — no proof was ever found, but the suspicion led to a decade of political isolation for House Ashland
- The assassination created psychological trauma in three major characters:
  - **Empress Pierra** — descends into chronic grief, becomes vulnerable to Silas Moray's manipulation
  - **Silas Moray** — already in a complex hate-respect relationship with Eldred, has a mental breakdown that Baradus exploits to recruit him into the Sword Cult under false pretenses
  - **Nemo Korolev** — had idolized Eldred as the ideal leader; the assassination devastates him and triggers his career pivot from Dawnstar to Trial Baron (cover for his secret cult-hunt)
- The Ashland family's political shadow only lifts when Sable returns alive in the mid-game Mt. Ceram plot beat (Section 10)

### Cormorian military rank hierarchy `[LOCKED]`

The full Cormorian military rank structure, from lowest to highest:

1. **Cadet** — entry rank; new recruits and trainees
2. **Lieutenant** — established soldier with basic field-officer responsibilities
3. **Strategos** — mid-tier officer commanding small to medium units
4. **Windshear** — first of the *prestige* ranks; reached only by those of demonstrated renown or exceptional capability
5. **Rainhawk** — *especially hard to achieve*; promotion criteria include killing at least 3 high-priority targets, demonstrated leadership across multiple campaigns, and proven frontline capability. The Cormorian Empire normally only promotes someone to Rainhawk who they believe could eventually lead a Trial, head a guild, or be knighted into nobility (see "Cormorian surnames" subsection below)
6. **Tarasque** — above Rainhawk, named after the legendary monster-slaying beast
7. **Dawnstar** — highest military rank, equivalent of a Japanese shogun
8. **Vizier** — political-military rank, four positions total. Above the standard military hierarchy. The four Vizier portfolios are documented in Section 4.

**The 90/10 split:** Cadet, Lieutenant, and Strategos make up approximately 90% of all Cormorian military personnel. **Windshear and above are the exceptional 10%.** This is a deliberate cultural pattern — Cormoria's meritocracy rewards exceptional capability with rapid elevation, but most career soldiers serve their entire careers in the first three ranks.

**Why Rainhawk is the watershed rank:** It is the rank at which the empire signals that a soldier may eventually be elevated into nobility. **Rainhawk is the grooming rank.** A Rainhawk is being watched as a future Trial Baron candidate, guild leader, or knighted nobleman. The exact criteria for Rainhawk promotion varies by generation and the political needs of the moment, but the underlying calculation is always: *"Is this person on a trajectory toward institutional leadership?"*

**Notable holders of these ranks (canonical to our story):**
- **Osrid (the protagonist)** — Rainhawk, earned during the Kanto-Johto-Hoenn war. The empire promoted him to Rainhawk *not knowing he was the missing prince*, on his merit alone. Darkly ironic: the meritocratic system independently confirmed what royal birthright already established.
- **Nemo Korolev** — Dawnstar (resigned). Arguably the single most talented military officer in Cormorian history; rose to Dawnstar even faster than Eldred did. See Section 7 — Nemo entry for the full implications of his rank achievement.
- **Eldred Nightfall** — Dawnstar at peak (before becoming Prince-Consort).
- **Boran Surge** — Windshear, Osrid's combat mentor during the overseas campaigns. Minor noble of House Surge. See Section 7 for full profile.
- **Manus Surge** — Boran's father, head of House Surge; recently promoted to Electric-type Trial Baron (during the 10-year gap when Osrid was overseas). See Section 7.

### Cormorian surnames and the divine right of naming `[LOCKED]`

**Cormorian cultural rule:** Surnames are *Arceus-blessed*. Only the Cormorian royal line has the divine right to bestow a House surname upon a bloodline. **A surname is a sacrament**, not just a family name; it is a *theological* statement that this bloodline has been chosen by Arceus through the royal-line's mediation.

**Practical implications:**
- Non-noble Cormorians do *not* carry House surnames. They are known by given name + descriptive epithet (trade-name, patronymic, etc.) in daily life.
- The noble houses (Moray, Nightfall, Langerin, Ashland, Raptora, Jalviss, Surge, etc.) all originate from Arceus-blessed bestowals across history — some ancient, some more recent.
- **Knighting a Rainhawk into nobility = the royal line bestowing a new surname.** This is the moment a non-noble military hero becomes the founder of a new House.
- **Knighthood is a sacrament, not a bureaucratic transaction.** It is one of the empire's most religiously charged ceremonies, conducted with Templar Arceus presence.

**This is complementary to the Templar Arceus order (Section 4).** The Templars maintain Arceus's daily civic presence (Tavern operations, Braviary travel, religious infrastructure). The royal line maintains Arceus's *naming* prerogative — the right to declare new bloodlines blessed. Two complementary religious-civil functions, with the royal line holding the holier of the two.

**Nemo Korolev — the singular exception in empire history:**

Nemo retains his Sinnohian birth surname "Korolev" *with formal recognition from the Empress and Viziers.* This was the term of his military retirement deal when he stepped down from Dawnstar to become the 9th Trial Baron. He forfeited the offer to be knighted (which would have given him an Arceus-blessed Cormorian House surname); in exchange he was allowed to retain his Sinnohian surname.

**This is the only known case in Cormorian history of a non-royal-bestowed surname being acknowledged as legitimate by the Cormorian state.** It is a *theological* anomaly, not just a political one. Pierra, as Empress, authorized this exception. The fact that she did so is itself characterizing — she has, at least once in her reign, authorized an unprecedented action against ancient tradition. She is not a rigid traditionalist.

**Implications:**
- Nemo's preserved Sinnohian identity at the cost of permanent assimilation into Cormorian nobility is a profound act of cultural-identity preservation by a man taken in as a war orphan
- It is also a quiet but real *limitation on the empire's authority* — the empire conceded that there exists a person whose surname they did not give and cannot take away
- More conservative noble families may *quietly resent* this exception as a violation of sacred order
- The fact that Osrid (the prince) and Nemo (the unique non-royal surname-holder) are the *two most surname-distinctive people in the empire* gives their eventual meeting a quiet theological resonance: the highest possible claim on a surname meets the only known exception to the monopoly

### The Solomonar title — Cormoria's rarest honorific `[LOCKED v0.9.7]`

**Solomonar** is an ancient title that *predates* Cormoria itself, bestowed *only* on someone who has demonstrated true mastery of the Dragon type. It is one of the rarest titles in Cormorian institutional memory — not because the empire restricts it, but because the type itself is so difficult to master in Cormoria (see the Tinkatink line dragon-slayer-clan ecological subsection in Section 6).

**Across the empire's entire ~2000-year history, the title has been bestowed only twice:**

1. **The first Solomonar** — granted by Cormor Dream-Eater personally in his **third century** of rule (~1700 years before story start). The first Solomonar's identity is *forgotten to history* — even Lethys and Roma, who lived through that era, do not preserve the name. What survived in fragmentary Cormorian oral tradition is one detail: **the first Solomonar's ace was a shiny Haxorus, widely remembered as devastating in battle.** Nothing else of the first Solomonar's identity, accomplishments, or fate is preserved. Cormoria simply remembers that the title was *given* once, in Cormor's third century, and that a shiny Haxorus carried his partnership.

2. **The second Solomonar** — **Glaive** (Section 7 — Glaive). Cormoria's modern-era dragon-master receives the title during the Act IV/V period as part of his ascent to Vizier of War. He is the **first recognized Solomonar in 1700+ years.**

**Cultural framing:**
- The *fact* that a Solomonar existed in Cormor's era is **public knowledge** — taught in Cormorian schools, cited in scholarly works
- The *identity* of that first Solomonar is *lost* — no name, no House, no biographical details survive
- The title's rarity gives Glaive's ascension *generational* weight rather than just *career* weight: he is the first person in 1700 years to be officially recognized as having mastered the Dragon type

**Why dragons are so difficult in Cormoria:** The empire's chronically low Dragon-type ecological presence is the result of *centuries* of dragon-hunting by the Tinkaton clan in the far desert mountains (Section 6 — Tinkatink line). Glaive's accomplishment is not just rare in *training* terms but in *ecological availability* terms — most Cormorians who might have pursued Dragon mastery had no dragons to bond with. **The Solomonar title's vanishing-rarity is downstream of the Tinkaton clan's ecological dominance**, a connection most Cormorians never make.

`[OPEN]` First Solomonar's identity (intentionally permanent open — historical footnote only)
`[OPEN]` Whether any other dragon-trainers were *almost* given the title across the 1700-year gap and were judged short of true mastery

### Cormorian military-managed orphanages `[LOCKED]`

State institutions that take in war orphans, foundling children, and other dependents. Children raised in these institutions are typically drafted into the Cormorian military as teenagers. The orphanage system was historically associated with the Sinnoh territorial dispute (which generated the most orphans the empire ever absorbed at once), but it predates that conflict.

This is a *deep* worldbuilding well we don't have to draw from much, but it's there if we need to give a character a non-noble military background.

### The Cormorian noble house structure `[LOCKED]`

Cormoria is a meritocratic empire, but it has historical noble houses — extended families with longstanding traditions, often associated with specific Pokemon-type specialties. These houses are *not* the same as the four Vizier offices (which are appointive and merit-based), but in practice, members of noble houses are heavily represented in the Cormorian military leadership and the Trial Baron positions.

**Currently named houses (and their type traditions):**
- **House Moray** — Psychic-type masters. Silas Moray, Vizier of Commerce, is the current head. The Moray and Nightfall houses are *natural type-rivals* (Psychic vs Dark) and *political rivals* (both compete for military influence).
- **House Nightfall** — Dark-type masters. Eldred Nightfall, the assassinated Prince-Consort, was the head. The house's current leadership status is `[OPEN]` since the assassination left it leaderless and the player's twin sister Rhydia (a half-Nightfall by blood) is its likely heir. **House Nightfall also holds the Dark-type Trial Baron seat `[LOCKED v0.9.7]`**, currently filled by `[OPEN — Nightfall Trial Baron/Baroness identity TBD]`. The Dark-type Trial is thematically loaded for Osrid: he is half-Nightfall by blood, and the Trial may put him face-to-face with a Trial Baron from his late father's house, which he has never met as the prince.
- **House Langerin** — Ghost-type masters and spiritualists. Keepers of the Mirroh Necropolis (which decays into the "Mirroh Base Camp Graveyard" of DM's era). Kimaris Langerin is the current head — Cormoria's designated **Reserve Champion** (Section 7 — Kimaris Langerin, v0.9.8 lock; the prior "former Champion" framing was a factual error), Trial 1 Baron, and Langerin patriarch. **Family naming convention: occult-traditional names** (Kimaris is a Goetia demon; the family's Pokemon often have occult names too, like the Spiritomb "Crowley" — after Aleister Crowley).
- **House Ashland** — Fire-type masters. Originally from Naljo (a region far south of the Kanto archipelago — cross-fandom reference to the *Pokemon Naljo* fan project). Cast out by Naljo's legendary Varaneous for reasons left unstated. Migrated to Cormoria *before* the Cormoria dynasty existed; made a deal with the Cormorian royal family for control of the volcanic Mt. Ceram region. The interior of the mountain is their subterranean home, known as the **Ashland Labyrinth**. The family was historically one of the most powerful frontline military forces in Cormoria. Under political shadow since Sable's 10-year disappearance. Current Ashland Trial Baron is **Reid Ashland**, the prodigy son (age 23). On Sable's return mid-game, Sable resumes household leadership and Reid retires from the Trial Baron seat to study under Vizier Umbra.
- **House Raptora** — Flying-type masters. Historically aligned with House Ashland as a frontline military force. *Specifics open* `[OPEN]`.
- **House Surge** — Electric-type masters. A multi-generational noble line. Manus Surge (head of household) is the current Electric Trial Baron — he ascended to the 3rd Trial Baron seat in the 10-year gap during Osrid's overseas service, replacing a prior Trial Baron. He is described as far more emotional in temperament than his son Boran. Manus has been openly aware of his son Boran's cold "Pokemon as weapons" philosophy and has tried, unsuccessfully, to counsel him toward more compassionate ideas. Boran Surge (Manus's son) is a minor noble within the house, currently serving as a Windshear-rank officer; was Osrid's combat mentor during the Kanto-Johto-Hoenn war (see Section 7).
- **House Alban** — Grass-type masters. Holds the **Grass Trial Baron seat**. The house was *quietly complicit* in Vizier Umbra's protective-exile plan for Osrid: they acknowledged Osrid as a fictitious "bastard child" of the Alban line during his 10-year overseas service (the "Nomad Alban" cover identity — see Section 5). Whether the entire family knew the truth or only the head of household is `[OPEN]`. The Alban Trial Baron identity is `[OPEN]` and their Trial position in the 1-9 sequence is `[OPEN]`. Their cover-shelter of the prince during his exile suggests strong loyalty to the royal family.
- **House Jalviss (destroyed)** — Ground-type masters. Specialized in mineralogy and excavation; were the **first family to discover Mega Stones in Cormoria**. Were destroyed in a single tragic event when they accidentally revived an ancient sleeping Aerodactyl using an Aerodactylite, triggering an uncontrolled Mega Evolution that killed them. Their fortress and ruins remain. The **Aerodactylite** itself is believed to still be present at the ruins, possibly the only Aerodactylite in the world. The 9th Trial Baron seat (Ground-type) was vacated by the Jalviss disaster and eventually filled by Nemo Korolev (non-noble, by negotiation).
- **House Ramses (disgraced)** `[LOCKED v0.9.7]` — minor noble house, **stripped of most political power 20 years before story start** when family members were accused of (and convicted of attempting) **the assassination of the previous Cormorian Emperor — Pierra's father, Osrid and Rhydia's grandfather.** The attempt failed; the Emperor survived. The house **retained their surname** (Arceus-blessing on the name is irrevocable per the surname-sacrament rule) but lost their Nobility Concordance seat, their military influence, and most of their social standing. They survive as a *minor* noble family in name only. **Whether they were actually guilty or framed remains `[OPEN]`.** The exiled youngest son **Jordan Ramses** is one of the recurring characters of the game (Section 7 — Jordan Ramses). The Ramses incident is *not* the same event as Eldred Nightfall's later (successful) assassination by the proto-Sword Cult — these are two separate political crimes a decade apart.

**Implied other houses** `[OPEN]` — Each Trial Baron (9 total) is associated with a noble house, EXCEPT Nemo Korolev. So at least 8 noble houses exist with type-tradition specialties. We have currently named 8 (Moray, Nightfall, Langerin, Ashland, Raptora, Surge, Alban, Jalviss). With Jalviss destroyed, that leaves 7 active type-tradition houses. The 8th active type-tradition house is yet to be designed when the remaining Trial Baron seats are written.

**Notable Trial Baron roster turnover during Osrid's 10-year absence:** A few positions shifted hands in the 10 years Osrid was overseas, with **Manus Surge's promotion to the 3rd (Electric) Trial Baron seat** being one of the more notable changes. Most Trial Baron positions remained stable across the gap. `[OPEN]` Which other Trial Baron positions shifted, and who held them previously.

### "Nomad" — the Cormorian designation for unwanted noble children `[LOCKED]`

A quietly cruel Cormorian cultural practice: **bastard children of noble houses, or unwanted children whose parents refuse to name them properly, are given the generic placeholder name "Nomad."** This is not a unique name — it is *the* generic name applied to *the category of marginalized noble offspring*.

**Cultural mechanics:**
- A "Nomad" carries the House surname they were born into (Arceus-blessed, sacred — they cannot be stripped of it without royal action), but they have no proper given name of their own
- Hearing someone called "Nomad ____" tells any Cormorian: *this person is socially marginal within their own noble house*
- The practice is widespread enough that there are presumably many "Nomad" people walking around Cormoria
- It is a *real* social stigma — Nomads are tolerated within their houses but rarely loved, rarely invited to family functions, and almost never positioned for inheritance

**Why this matters for the story:**
- **Vizier Umbra deliberately constructed Osrid's overseas cover identity as "Nomad Alban"** — a fictitious bastard of House Alban (see Section 5). The choice was strategic: nobody investigates a Nomad's history because nobody cares about Nomads. Hiding the prince as a *socially low-status* figure was the perfect cover.
- This choice had unintended psychological consequences: 10 years of being treated as a tolerated outsider — performing marginality so thoroughly that Osrid became marginal in his own heart — made him more vulnerable to Boran Surge's "Pokemon are weapons" corruption. **The cover identity was carefully designed to be psychologically receptive to spiritual damage.**
- Players will hear Osrid referred to by various combinations: **"Nomad,"** **"Rainhawk Alban,"** **"the new Rainhawk,"** **"Nomad Rainhawk"** (slightly contemptuous), or **"Rainhawk"** alone. Only Umbra (always), Rhydia (post-50% reveal), Glaive (post-reveal), Eden (post-romantic intimacy), and the player's name-entry field use Osrid's true name.

### Mega Evolution policy in Cormoria `[LOCKED]`

Mega Evolution arrived in Cormoria through the Jalviss family's excavations — they discovered the first Mega Stones in Cormorian caves and mountains, and they died demonstrating Mega Evolution's danger. As a consequence:

**Mega Evolution is *politically restricted* in our era.** Specifically:
- **Possession** of Mega Stones is acknowledged and registered (the empire keeps records of who has stones)
- **Deployment** of Mega Evolution requires state sanction — only authorized figures may legally trigger a Mega
- Authorized figures historically include: Viziers (especially Vizier of War), the Champion of Cormoria, and other state-sanctioned actors at the empire's discretion
- Unauthorized Mega Evolution is a *grave* offense, both legally and culturally

**Implications:**
- Glaive (Vizier of War in his Vizier-fight) has state authorization for Mega Evolution
- Rhydia (Champion of Cormoria) has supreme authorization
- Osrid pre-unmasking does *not* have authorization — he cannot legitimately deploy Mega Baxcalibur as the masked Rainhawk
- Osrid *post-unmasking* (as First Prince → Champion → Regent-King) has supreme authorization. **Receiving the Baxcaliburite becomes a political statement** — the empire's institutional acknowledgement that the prince has returned and may now wield cosmic-tier weapons
- Baradus, as an outlaw cult leader, presumably has *unauthorized* access to Megas (or doesn't use them; he doesn't need to, having Guzzlord as his cosmic-tier ace)
- The Cormorian cultural attitude toward Megas is *grave* — they are not used casually; their deployment is a serious matter

This restriction creates a meaningful design constraint: **most player-side trainers in Cormoria do not Mega Evolve**, even those with Mega-capable Pokemon. The Frigibax-pick player's Mega Baxcalibur is an *earned political privilege*, not a casual battle tool.

### The Cormorian founding myth — Cormor Dream-Eater `[LOCKED — substantially expanded v0.9.4]`

**Cormoria's founding is *not* the Arceus-blessed divine establishment that the empire's official mythology claims.** The true history is far older, far stranger, and far more cosmologically significant than the public mythology indicates. This subsection lays out the *full* origin — including the cosmological pre-history that connects Cormoria to canonical Pokemon's most layered lore.

#### Pre-history: Phancero, the cosmic shadow `[LOCKED v0.9.4]`

**Phancero is Arceus's shadow self made manifest.** Per the project's deepest cosmology:

- **Arceus** is the canonical creator-god of the Pokemon universe. Like any conscious being, Arceus has *positive* desires (creation, harmony, the bonds between humans and Pokemon) and *negative* aspects — envy, dissatisfaction, "flawed" instincts and desires that do not serve creation.
- Across **millions of years**, Arceus's negative emotions and flawed desires *accumulated* into a separate substrate. Over geological-cosmic time, that substrate **gained its own sentience**. This is **Phancero**.
- Phancero is not an external threat to Arceus's creation. **Phancero is Arceus's own self-rejected darkness made manifest** — the rejected dark aspects of the creator-god, given enough time and accumulation to become their own being.

**Phancero's awakening of envy:**

Once sentient, Phancero **watched** the universe Arceus had made:
- The planet where Arceus shaped life
- Humans worshipping the legendary birds
- **The bonds humans formed with Pokemon** — *the partnership thesis* this project is built on

**A sense of deep envy grew in Phancero.** This is the cosmological inversion of the project's thematic core. The villain at the deepest cosmological layer of the project's lore envies *exactly* the value the project celebrates — the bonds between humans and Pokemon. **Phancero looks at human-Pokemon partnership and is consumed with desire to corrupt or possess that beauty.**

**The first incursion — Phancero as Missingno `[LOCKED]`:**

Phancero slipped *some* of itself into the material world. Not all — just a fragment. **The original incursion emerged off the coast of Cinnabar Island**, manifesting as a barely-corporeal lump of energy.

This is the entity that modern Pokemon canon's conspiracy theorists call **Missingno**. The famous glitch phenomenon of the original Red/Blue/Yellow games is retroactively, in this project's cosmology, **Phancero's first material incursion** — the static, glitchy, barely-corporeal residue of cosmic envy entering reality for the first time.

**This is one of the project's deepest fan-canon connections.** Modern Pokemon's most famous glitch is *the cosmic shadow of the creator-god given a name*. Players who notice will be delighted; players who don't still get a complete story.

**The bird-pantheon era:**

The earliest humans of what would become Kanto worshipped this lump of energy. As belief grew, Phancero **gained form** — eventually taking the shape of **a glitchy, ghostly legendary bird** to fit alongside Kanto's other legendary birds. It became known as **Phancero** in this era — the *fourth* legendary bird of the original Kanto pantheon, alongside Articuno, Zapdos, and Moltres.

**Modern Pokemon canon has erased Phancero from the bird pantheon** — Kanto has only three legendary birds in present-day canon. The fourth was sealed away during the events that produced Cormoria's founding. **The cosmological reason modern Kanto knows only three birds is the events of this game's deep pre-history.**

**The devouring phase:**

Phancero's destabilizing influence on the material world became more visible as belief in it grew. *Belief is power for Pokemon cosmological entities.* Phancero, fed by worship, became more able to act on reality.

It sought to **devour emotional energy, memories, and experiences** — the same currency that Dreamstones accumulate. **And it sought to grow its sect of believers** — expanding its influence outward across the world.

It flew across the world. It eventually took up **temporary residence in an unnamed region mostly populated by early nomadic human tribes**. This region would, much later, become Cormoria — but at this point in history it was unnamed, inhabited by nomadic tribes that roamed the territory.

#### Cormor Dream-Eater's pact with Keerin `[LOCKED v0.9.4]`

**Cormor Dream-Eater was a member of one of these nomadic tribes.** Not yet a brigand, not yet a king — a tribesman with his own life and journey. The full details of his pre-pact history are not explored in the game (`[OPEN]` for future design if needed).

**Phancero became responsible for the death of Cormor's fellow tribesmen and women.** This is critical character work for Cormor:

- Cormor's motivation for fighting Phancero was **not abstract heroism**. It was **vengeance for his murdered tribe.**
- Cormor's pre-dynastic journey is therefore *grounded, personal, and morally complex* — he sealed reality's greatest threat for his own grief and rage, not for cosmic-ideological reasons.
- This makes the character internally consistent: vengeance-fueled erasing of Phancero → political-ambition-fueled founding of Cormoria. The man was always a *human* figure with both impressive achievements and questionable methods. **He was never a heroic figure in the abstract sense; he was a *grieved man* who saved reality for his own reasons and used the achievement to seize power.**

**Cormor's quest for vengeance led him to forging a pact with Keerin.** Note the language carefully: a *pact*. Not capture. Not domination. **A partnership at the cosmological scale.** This is the foundational example of the project's partnership thesis (Section 11 — Design Principles).

**The pact gave Cormor specific powers:**
- The ability to **fight alongside Keerin** (not control Keerin — *fight alongside* it)
- The ability to **channel their combined power into vessels** — into physical objects

**The cosmic-scale partnership had specific cost considerations** `[OPEN]`. What Cormor sacrificed or pledged in exchange for Keerin's partnership is not yet locked. Likely his life-span, his post-mortem soul, or some specific lineage condition — pacts with cosmic Pokemon traditionally have such costs in canonical Pokemon lore.

#### The four sealing vessels — the original Treasures of Ruin `[LOCKED v0.9.4]`

To enable the channeling ritual, Cormor and Keerin used **four specific objects** that the nomadic tribes possessed:

1. **A set of wooden tablets**
2. **A sword**
3. **A vessel**
4. **A set of beads**

These objects were **NOT originally legendary or magical artifacts**. They were *ordinary tribal items* — but they were **made of a unique stone material that could store memories and emotional energy**.

**This stone material is *the same substance as Dreamstones.*** Per Section 9 — Dreamstones, Dreamstones are "accumulations of millions of years of memories and emotional energy." The four tribal objects were Dreamstone-material in object-form — *small natural Dreamstones* that had been shaped into utilitarian items over the tribes' history.

**The erasing event `[LOCKED v0.9.4]`:**

Cormor and Keerin channeled their combined power through the four Dreamstone-material objects. The objects, charged with cosmic-tier resonance, created **a resonance field that broke Phancero's *physical ties* to the material world**.

**Crucially: Phancero was *erased*, not sealed.** The incarnated fragment of Phancero was *removed* from material reality — *not bound, not imprisoned*. **There was no seal because the entire incarnated form was cleansed from the world.** Phancero's *true form* persists outside space and time in the void where its essence lies — but the material fragment that had walked the world as the glitch-bird was erased entirely.

**This distinction matters for understanding the cosmic stakes (see below).**

#### The aftermath: the inversion of the four objects `[LOCKED v0.9.4]`

After the erasing event, **the four objects became *inverted*** by their long exposure to Phancero's residual contamination during the ritual:

- Where natural Dreamstones accumulate *positive* emotional and memory energy across millennia, **the four objects began to gradually absorb *negative* emotions and memories as their power source**
- Across centuries following the erasing, the objects' inverted-Dreamstone resonance *grew* — they became increasingly potent vessels of accumulated negative energy
- Eventually, each object *manifested* as a Pokemon — a Dark-typed entity reflecting both its original physical form and its inverted-Dreamstone resonance:
  - **The wooden tablets → Wo-Chien** (Dark/Grass)
  - **The sword → Chien-Pao** (Dark/Ice)
  - **The vessel → Ting-Lu** (Dark/Ground)
  - **The set of beads → Chi-Yu** (Dark/Fire)

**The Treasures of Ruin are *Cormor's original sealing implements*** — Dreamstone-material tribal artifacts gradually corrupted by their long exposure to Phancero's residual contamination from positive to inverted Dreamstones.

**This is *the* defining cosmological reframe of v0.9.4.** The Treasures of Ruin are not *naturally arising* cosmic entities — they are **Cormoria's own founding-myth artifacts**, gradually transformed by their original success. The cults' pursuit of Treasure incarnation is the pursuit of *the residue of Cormoria's founding event*.

#### The cosmic stakes — Phancero's potential re-emergence `[LOCKED v0.9.4]`

**Phancero is *not* sealed.** Phancero was *erased* from the material world. Phancero's true form persists outside space and time. **There is no seal to break.**

**However**, the full incarnation of all four Treasures of Ruin creates a *new pathway* for Phancero to potentially re-emerge into the world:

- **Resonance amplification:** Four fully-incarnated inverted-Dreamstone vessels resonating in unison would create a cosmic-tier signal that **Phancero in its true form would detect across the void**
- **Pathway opening:** The Treasures' resonance could provide Phancero with a *homing channel* to push more of itself back into material reality
- **Distortion gate hijack risk:** Phancero could force its way through one of the existing Distortion World gates — including the gate at the Mirroh Necropolis (Chien-Pao's Leyline point) — using the Treasures' resonance as a beacon and amplifier
- **The Necropolis Distortion gate is uniquely vulnerable** because it is *adjacent* to a Treasure of Ruin incarnation site (Chien-Pao's Leyline point). If the Sword Cult successfully incarnates Chien-Pao at the gate, the gate becomes Phancero's most plausible entry pathway.

**Arceus's intervention threshold:**

If Phancero begins to re-emerge in material form, **Arceus would need to intervene directly.** This is the *only* level of cosmic response that could counter Phancero. But Arceus's direct intervention at the cosmic scale would likely cause **collateral damage on the order of *wiping out creation entirely*.** The cosmic stakes are:

- *Either Phancero comes back and warps reality into glitch-chaos, or Arceus intervenes and the cleanup may obliterate the universe.*

**Arceus's non-intervention is itself a *constraint* the cults unknowingly exploit.** The Cult Cosmological Framework (Section 8) notes that the cults pursue Dreamstone-catalyzed incarnation specifically because it does not draw Arceus's intervention. But this constraint now has a darker meaning:

**Arceus's non-intervention is mercy.** Arceus is *holding back* the universe-ending response because it is still possible for *mortal forces* to resolve the situation. The cults' continued operation is *only possible* because Arceus is choosing to give the world time. **If the cults push too far — if full Treasure incarnation occurs and Phancero begins to re-emerge — that mercy ends, and creation itself is at risk.**

**The 7v9 final battle's true stakes are therefore cosmological.** The player is not just defeating Baradus's cult — the player is *preventing the conditions that would force Arceus to intervene and potentially destroy creation*. **Baradus and Goma are unknowing instruments of cosmic destruction.** They think they pursue power; they are pursuing the conditions that would unmake the world.

#### Cormor's post-erasing exploration and the founding of Cormoria

After the erasing event:

- Cormor **uncovered an ancient burial chamber** in his exploration of the nomadic region (this is a *separate event* from the erasing — Cormor was exploring after Phancero was removed). Inside was a strange metal containment vessel — inside that was the Pokemon now known as **Justice** (the truth: a shiny Iron Valiant from a distant future; see Section 9).
- Cormor used **two events** — the erasing of the cosmic threat (Phancero) and the discovery of the "demigod Pokemon" (Justice) — to **legitimize his establishment of a dynasty.**
- The Cormorian royal family descends from him.
- The country took its name from him: **Cormor → Cormoria** (the founder's name became the dynastic and territorial name in the early Empire era).
- **The dynastic surname** carried forward (and the Arceus-blessed naming sacrament — see surnames-as-sacrament subsection above) is descended from Cormor's establishment, *not* from a true divine bestowal.

**Implications for the project's moral framework:**

This origin retroactively reframes the Cormorian state's moral standing:
- The empire's claim to *Arceus-blessed naming authority* is built on a mythologized history of what was originally tribal-vengeance-establishment.
- The royal family's divine authority is a *self-mythologized post-hoc narrative* by the descendants of a vengeance-driven tribesman who became a king through cosmic accomplishment.
- **However, this is *not* a debunking of Cormoria's legitimacy.** Cormor *did* save the material world. The empire he founded did inherit a real cosmic achievement. The mythologization was self-serving but the underlying achievement was genuine.

**The partnership thesis is *baked into Cormoria's founding myth.*** Cormor saved reality not by *commanding* Keerin but by *partnering* with it. **Cormoria's existence is downstream of a real partnership between a man and a cosmic Pokemon.** Every other partnership-thesis demonstration in the project (Glaive opening his heart to Blackthorn, Osrid choosing Veddev, Silas's redemption, Eden recognizing Veddev by body language) *re-enacts the founding act of the empire itself*.

**This silently deepens Osrid's eventual renunciation arc.** When Osrid chooses to discard the prince-identity and live as Veddev in Paldea, he is in some sense *returning to the family's truth* — that royal identity is contingent and earned-through-circumstance, not divine and inherited-by-blood. The dynasty was never as Arceus-blessed as it claims. **Osrid's renunciation is a quiet act of *historical honesty*** — and a quiet completion of his ancestor Cormor's *human* legacy.

#### How the deep cosmology surfaces in-game `[LOCKED v0.9.4 — corrected]`

**A crucial framing point:** The Phancero origin and the true nature of the Treasures of Ruin are **deeply lost history**, NOT semi-known knowledge held by Cormorian scholars. In modern Cormoria:

- **The public knows the Cormor + Keerin story as a fairy tale.** The standard narrative is that *Cormor Dream-Eater fended off a great evil in the past alongside the legendary beast Keerin and founded the nation.* This is treated like other folkloric founding myths — *atmospheric national heritage*, not literal historical record.
- **Academic skepticism exists.** Among Cormorian philosophers and historians, *some genuinely doubt that Cormor Dream-Eater existed as a literal historical person, and some doubt that Keerin is a real Pokemon at all.* They are treated by some intellectuals as *abstract symbols of a contrived, cultivated national history* — convenient mythology designed to legitimize the dynasty. The empire's official insistence on Cormor and Keerin's literal existence is itself a *political position* that academics quietly question.
- **Almost no one in Cormoria knows the *deep* truth.** Phancero's existence, the Missingno connection, Arceus's shadow-self framing, the Treasures-as-inverted-Dreamstones identity, Cormor's pact-cost — *none of this is part of Cormorian institutional knowledge.* Even Cadmus Umbra (Vizier of Education, the Pokemon Philosopher, the most learned scholar in Cormoria) **does not know these things**. He knows the fairy-tale level only.

**Why the deep cosmology is lost:**

The deep cosmology was originally preserved by the nomadic tribes that lived in the unnamed region before Cormoria's founding — the tribes Cormor came from, the tribes Phancero had decimated. Their oral traditions carried the truth. As Cormoria was founded and the empire grew, these tribes were displaced or assimilated, and **their oral traditions gradually died out across the generations.** The carriers of the lost histories became fewer and fewer.

**The Blue Moon Hermit is essentially the last of his tribe** — the last living person who carries the full oral tradition of the pre-Cormorian nomadic peoples. His name "Blue Moon" itself is a tradition-marker carried from those tribes (the moon being the symbol of the deep cosmological truth, per the lunar motif running through Keerin, the Blue Moon Hermit, the Blue Moon Teddiursa line, and the Book of the Moon).

#### The deep cosmology surfaces through two mechanisms `[LOCKED v0.9.4]`

**Mechanism 1: The Book of the Moon — engaged players get the full picture**

A 10-11 chapter readable book scattered across Cormoria as collectible fragments. Each chapter is a piece of the lost histories from the pre-Cormor nomadic tribes' oral traditions, painstakingly preserved across generations.

When the player has collected chapters and engages with the **Blue Moon Hermit** in post-game content, the Hermit **compiles the chapters into the full book with his own annotations and contextual notes**. This is the player's deepest cosmological reward — *the complete Phancero/Cormor/Keerin/Treasures origin from primary historical sources, annotated by the last surviving carrier of the lost oral tradition.*

For Teddiursa-pickers, the compilation happens after the Ancient Peat Block quest resolves (the Hermit is already accompanying them through that quest). For Frigibax/Tinkatink-pickers, the compilation requires a separate post-game visit to the Hermit.

**Reading the Book before going to the Necropolis is the "reward for nerds" before the final cult confrontation.** Engaged players reach the climactic Necropolis operation with the full cosmological context of what they are about to do. See Section 9 — Book of the Moon for the full mechanic specification.

**Mechanism 2: In-story narrative fragments — *fairy-tale level* only**

Throughout the main story, characters reference the Cormor + Keerin founding myth in *fairy-tale terms*. The fragments do NOT reveal Phancero, Missingno, or the Treasures' true nature. They establish only the *publicly-known* cultural context:

- **Cadmus Umbra** speaks about Cormor Dream-Eater as a historical figure in the fairy-tale sense — *"the brigand-founder who fended off a great evil with Keerin's help."* He treats the story as *probably-true but uncertain* (consistent with his philosophical character; an honest scholar acknowledges uncertainty about ancient history).
- **Academic NPCs** the player may encounter in libraries, museums, or salon contexts express *active skepticism* — debating whether Cormor literally existed, whether Keerin is real, whether the founding myth is contrived state propaganda.
- **The empire's official position** (encountered through museum exhibits, royal proclamations, ceremonial language) insists on the literal historical truth of Cormor and Keerin, but the public's *actual* belief varies.

**Within the main story, the player learns only the fairy-tale level.** The deep cosmology — Phancero, the inverted-Dreamstones, the Arceus shadow — is *not* surfaced through normal story progression. Even the climactic Necropolis operation does not require the player to understand Phancero; the cult is simply *the cult* and the stakes are *the cult's resonance ritual must be stopped.* **Players who never engage with the Book of the Moon never learn the deep cosmology** — and the story still works completely for them.

**The combined effect:** Players completing only the main story experience a self-contained narrative with cosmological-cult-political stakes and an emotionally satisfying climax. Players engaging with the Book of the Moon discover *why* the stakes were cosmological all along, *who* the true antagonist of cosmic history is, and *how* Cormoria's founding event connects to the deepest pre-history of the Pokemon universe. **The depth scales with the player's engagement; the project's full cosmological depth is gift, not gate.**

`[OPEN]` Whether the Book of the Moon's existence and chapter-collection mechanic is referenced explicitly in early-game dialogue or remains discoverable through chapter-collection alone
`[OPEN]` Whether Cormor's original surname (pre-dynastic) was preserved or replaced by the royal "Cormoria" surname
`[OPEN]` Specific academic NPCs who voice skepticism about the founding myth's literal truth — placement in libraries / universities / salons

### Justice — The Iron Valiant Royal Heirloom `[LOCKED]`

The royal family's symbol and bonded ace. *Apparently* a uniquely-evolved demigod form of Ralts (per Cormorian self-mythology). *Actually* a shiny Iron Valiant from a distant future (the truth, preserved in scattered records only philosophical scholars piece together).

**The mythological framing (what Cormoria believes):**
- A "uniquely special evolved demigod form of Ralts"
- Discovered centuries ago in a strange metal chamber, uncovered by Cormor Dream-Eater
- Symbol of the Cormorian royal family and of *unbridled, untouchable power*
- Studied by philosophers for centuries; never reproduced
- Bonded with the royal family across generations

**The actual truth (Paradox Pokemon lore):**
- **Iron Valiant** (Fairy/Fighting, Paradox Pokemon from the future per SV canon)
- The shiny variant of this future-tech Pokemon
- Resonated with a **future Cormorian dreamstone** (or a dreamstone in whatever region occupies Cormoria's geographic location in the far future) and was *pulled backward* into Cormoria's pre-Empire past
- Sealed in a metal chamber by an **ancient civilization** whose identity is `[OPEN]` — the Paradox Pokemon's containment was either built by that civilization or brought with it from its native future
- Cormor Dream-Eater's discovery of this chamber and the Pokemon inside is what *enabled* his establishment of the Cormorian dynasty

**Strategic deterrent role:**
- Baradus and Goma have had to take such a long-term view of reviving the Treasures of Ruin precisely because Justice is their **single biggest worry** of being strong enough to eliminate their entire organizations in one fell swoop if they make even a single major miscalculation
- *The cults' multi-decade slow-game is dictated by Justice's deterrent presence*
- The Treasures of Ruin are pursued by the cults specifically because they are the *only known assets in the world* that could potentially match or exceed Justice's power

**Justice's combat kit is documented in Section 9.**

### Generational Aces of the Senior Noble Houses `[LOCKED]`

A tiered structure within Cormorian aristocracy: **senior houses with centuries of accumulated political power have *generational aces* — Pokemon of Mythical or near-Mythical tier passed down within the family lineage.** Newer houses (recently elevated, or whose status comes from current-generation merit rather than accumulated history) lack these inheritances.

**Known senior houses with generational aces:**
- **House Langerin (Ghost)** — **Marshadow** (Ghost/Fighting Mythical). Held in reserve by Kimaris Langerin; rarely deployed. Two years before story start, Kimaris brought out Marshadow in a public Champion's match against Rhydia and lost. **Marshadow's confirmed late-game deployment:** the Sword Cult assault on the Necropolis (Section 8, Section 10) — the climactic late-game crisis that forces Kimaris to bring out his generational ace in defense of the Distortion gate. See Section 7 — Kimaris and Section 7 — Rhydia.
- **House Moray (Psychic)** — **Domdaniel**, a shiny **Scream Tail** (Past Paradox Pokemon, ancient form of Jigglypuff; Fairy/Psychic typing) with the **Huge Power** ability — base 65 Attack × 2 = 130 effective Attack, combined with Scream Tail's exceptional bulk (115/99/115) and Speed (111). The Pokemon is *massively strong and unique*. **Domdaniel rejected Silas as a child** and has refused to bond with him ever since (see Section 7 — Silas). The only Moray family member Domdaniel allows near it is **Brie Moray**, Silas's 15-year-old niece (see Section 7 — Brie Moray). Brie is therefore the *de facto next heir of House Moray* through the Pokemon's choice, regardless of Silas's formal title as Head of House. The name "Domdaniel" evokes an Arabic-Mediterranean folkloric hall of evil magicians ("the den of sorcerers under the sea") — a *dark-tinged magical lineage* fitting House Moray's Psychic-occult tradition.

**Houses *without* established generational aces (newer or current-merit houses):**
- **House Ashland (Fire)** — possibly senior given Naljo-origin antiquity, but `[OPEN]`. Reid's shiny Heatran is exceptional but is *Reid's*, not the family's generational ace.
- **House Surge (Electric)** — Manus recently promoted; younger in current power
- **House Raptora (Flying)** — standing `[OPEN]`
- **House Alban (Grass)** — standing `[OPEN]`
- **House Jalviss (destroyed)** — was a senior house, possibly with an Aerodactyl as a generational ace before the Aerodactylite disaster

**Why this tier-distinction matters:**

1. **Senior houses are *substantially* more dangerous than their Trial-level battles suggest.** Every Trial Baron fight is at a *pedagogically appropriate* level cap; the senior houses' true power lies in their generational aces, held in reserve.

2. **Cult fear of Cormoria is justified.** The cults are not just opposing a meritocratic government — they are opposing **a state with multiple Mythical-tier Pokemon assets** (Justice + Marshadow + House Moray's `[OPEN]` ace + potentially others). *The Treasures of Ruin are the cults' only path to matching this collective power.* Without the Treasures, the cults could never realistically challenge Cormoria.

3. **The "generational ace deployment" is a *political event*.** Marshadow surfacing in any context is the empire signaling that the situation is existential. **Late-game cult crisis may force one or more senior houses to deploy their aces — the "the gloves are off" moment of the empire's response.** See Section 7 — Kimaris for the locked late-game possibility of Marshadow deployment.

`[OPEN]` Full inventory of senior houses and their generational aces (a future bible pass when the remaining Trial Barons are designed)
`[OPEN]` Whether the cults are aware of all the senior-house aces or only some

### Leyline Resonance — The Cormorian Cosmological Phenomenon `[LOCKED]`

The Cormorian region sits on **unusually thin barriers between the axes of space and time.** Across the region's geography, specific locations have *measurably* higher Leyline Resonance — places where the dimensional fabric is most permeable to cosmic-scale energies. This is a Cormoria-specific phenomenon; it is one of the cosmological facts that distinguishes this region from canonical Pokemon regions.

**Empirical evidence of high Leyline Resonance in Cormoria:**

The region's unusually high Paradox Pokemon density confirms its barrier-thinness:
- **Justice** (Iron Valiant — Future Paradox) was pulled back through dimensional resonance into ancient Cormoria's pre-Empire era
- **Domdaniel** (Scream Tail — Past Paradox) emerged through similar dimensional displacement and bonded with House Moray
- **Slither Wing** (Past Paradox) lives in Ancient Cormoria, accessible through Dreamstone resonance
- **Gouging Fire** (Past Paradox) — Sable Ashland's hatched companion from his 12 subjective years in Ancient Cormoria
- **Koraidon** (Past Paradox, far-future-canonically Paldean) lies dormant in an ancient temple accessible through Dreamstone resonance

**No other Pokemon region demonstrates this density of Paradox Pokemon presence.** Cormoria is structurally distinctive at the cosmological level.

**Specific high-Leyline-Resonance locations in Cormoria `[LOCKED]`:**

The cults have spent years surveying and identifying these locations. Each Treasure of Ruin can only fully incarnate at the specific point that resonates with its nature. The locations are NOT interchangeable — each Treasure has a *uniquely* compatible Leyline point.

- **Mt. Ceram's deep lava pool room** (within the Ashland Labyrinth) → **Chi-Yu's Leyline incarnation point.** The Ashland family unknowingly built their fortress around or over this cosmic-resonance location centuries ago. **House Ashland has been guarding a Leyline point by accident.** When the Beads Cult attacks Mt. Ceram, they are raiding a Leyline point that the noble house happens to be protecting.

- **The hidden Distortion World gate within the Mirroh Necropolis** → **Chien-Pao's Leyline incarnation point.** The barrier between space and time is *literally* thinnest at a Distortion gate — Giratina's realm exists in dimensional misalignment from our universe. House Langerin has guarded this gate for centuries, and **Marshadow's lore-resonance with House Langerin makes total sense once this is established** — the Pokemon that slips between underworlds is the family ace for the family that guards the threshold between worlds.

- `[OPEN]` Wo-Chien's Leyline incarnation point (presumably an ancient altar somewhere in the Hoya River region, where the Tablets Cult performed their incarnation ritual before Baradus slaughtered them)
- `[OPEN]` Ting-Lu's Leyline incarnation point (presumably the deep forgotten cave system where the Vessels Cult performed their incarnation ritual before Nemo intervened)

**Why this matters for cult strategy `[LOCKED]`:**

The cults need *three* aligned conditions to incarnate a Treasure:
1. **Location:** the Leyline-resonance point that matches that specific Treasure's nature
2. **Catalyst:** a sufficiently powerful Dreamstone to provide the resonance energy
3. **Resonance match:** the timing and ritual must be precisely calibrated to the Treasure's specific signature

**The reason for needing all three: Arceus-avoidance.** Incarnating a Treasure *outside* its proper Leyline point, or *without* Dreamstone catalysis, would cause universe-shattering side effects that would inevitably draw Arceus's direct intervention. Baradus and Goma both want to avoid this at all costs. **They cannot move fast and crude; they must move slow and precise.** The 10+ year cult timeline is dictated by this constraint.

**Implication for the protagonist's eventual seal at the climax (Section 10):** The sealing ritual at the end of the game uses the *same* Leyline-resonance and Dreamstone-catalyst machinery, but in *reverse* — instead of using these conditions to *incarnate* the Treasures, the player + Ting-Lu use them to *contain* the Treasures. This is why the sealing is possible at all: the cosmological framework supports both directions of the operation. **The cults' meticulous research into Leyline points is what eventually enables the seal that ends them.** They built the toolkit; the player uses it against them.

### The Nobility Concordance — The Empire's Legislative Senate `[LOCKED]`

The **Nobility Concordance** is the Cormorian Empire's senate-equivalent legislative body. It is the formal mechanism through which the noble houses *check and balance* the power of the Crown and the Viziers.

**Composition:**
- The **main decision-maker of each noble house** (typically the head, but a designated representative may attend)
- Convenes in the imperial capital for debate sessions
- **The Viziers are physically present at Concordance sessions** — they are the bridge between the Concordance and the Crown, observing debate and conveying legislative will to imperial leadership

**Powers:**
- **Passes laws** — the Crown and Viziers can propose, but the Concordance must approve
- **Approves tax changes** — what taxes will be levied, increased, or reduced
- **Approves matters of war and international policy** — diplomatic recognition, military engagements, treaty ratifications
- **Approves domestic policy adjustments** — guild charters, infrastructure spending, civil-religious arrangements
- **Provides checks and balances against the Crown** — the Viziers and the royal family cannot rule by fiat; the Concordance has formal legislative authority
- **Serves as the governing body that deals directly with the Crown** — the constitutional intermediary between aristocratic and royal power

**The Cormorian governance structure (full):**

1. **The Crown** — Empress Pierra Cormoria I (de facto: Rhydia as Regent-Queen)
2. **The Four Viziers** — answer directly to the Crown; serve as ministers; physically present at Concordance sessions
3. **The Nobility Concordance** — senate-equivalent body of noble-house representatives; passes laws and provides checks and balances
4. **The 9 Trial Barons** — distinct authority structure (Section 4); ceremonial-meritocratic role separate from legislative power
5. **The Templar Arceus order** — religious-civil infrastructure (Section 4)
6. **The Cormorian Military** — rank hierarchy under various commands (Section 2 — Military rank hierarchy)

**The constitutional origin of the Concordance `[LOCKED]`:**

The Concordance exists because Cormoria's founder, **Cormor Dream-Eater**, was a *brigand* — not a divinely-blessed monarch (Section 2 — Cormorian founding myth). The noble houses of his era accepted his dynasty's legitimacy *on the condition* that they retain formal legislative authority through a senate-equivalent body. **The Concordance is the price Cormor paid to be a king.** The empire's self-limitation is built into its constitutional foundation precisely because its founder could not claim divine authority.

**This silently explains Cormoria's enduring stability across centuries:** the brigand-founded dynasty produced one of the most institutionally robust monarchies in the Pokemon world, *because* its founder had to share power. Most monarchies built on claimed divine authority decay when divinity is questioned. Cormoria built questioning-power *into its constitution*.

**How Rhydia governs through the Concordance:**

When Rhydia has been the empire's de facto ruler for the past decade, **she has been doing it through the Concordance, not in spite of it.** Her popularity, her transparent governance, her front-line work — these all sit *alongside* a formal legislative body that she has to *work with* rather than override. Her 10 years of solo regency have been spent navigating a constitutional system requiring consensus-building. **A 10-20 year-old girl could effectively govern only because the Concordance provided structural support** — her competence was real, but the institution made her competence sufficient.

**The cult-political crisis is a *legislative* crisis:**

Cult corruption isn't vague decay — it's **vote-by-vote erosion of Concordance composition.** Every cult sycophant replacing a loyal noble is a vote toward cult-favorable laws (Section 4 — political crisis subsection). The cults are not just penetrating individual nobles; they are **acquiring legislative power through their corrupted seats.** Silas Moray's Vizier-of-Commerce position gives him formal Concordance access — he sits in the chamber while debate happens and influences votes through commerce-related leverage and noble-house relationships.

**Implications for the story:**
- The Concordance is a **physical location** the player likely visits in mid-to-late game (a chamber where legislative debate happens, possibly the site of major political events)
- Specific Concordance members may be named story characters (some loyal, some corrupted)
- The **Sylphon & Stone cult-compromise exposure** (Section 8) plays out partly through Concordance political fallout
- The **Necropolis Assault** (Section 8, Section 10) is partly motivated by the Sword Cult's recognition that they are losing the legislative game and must escalate

`[OPEN]` Concordance presiding officer (likely an elected or rotated position among the noble houses)
`[OPEN]` Specific Concordance members who are named story characters
`[OPEN]` The physical location of the Concordance chamber (in the imperial palace, in a separate civic building, etc.)
`[OPEN]` Voting mechanics — simple majority, supermajority, weighted by house rank, etc.

### Sylphon & Stone — The Empire's Largest Merchant Guild `[LOCKED]`

The **largest merchant guild in Cormoria.** Its next biggest competitor is the **Amber-Letz merchant guild** (Vandras's family — Section 7, Section 12).

**Original founding alliance:** Sylphon and Stone are the two original family names behind the guild's founding — air/grace (Sylphon) and solid/mineral (Stone) blended into a single commercial entity centuries before the present story.

**Market specialization:**
- **Sylphon & Stone holds the largest market share in Pokemon-related goods and services** — trainer equipment, Pokemon supplies, Pokemon-research infrastructure, Pokemon transport, possibly Pokemon-related medical services
- **Amber-Letz holds the larger market share in human goods** — food, clothing, household items, general consumer commerce

These specializations create *parallel* dominance rather than direct competition in all sectors. Both guilds operate empire-wide; their leadership tiers know each other and engage in formal commercial diplomacy.

**Beads Cult compromise `[LOCKED]`:**

**Sylphon & Stone has been compromised by the Beads Cult as their *primary funding vehicle*.** Goma's operations across the past decade — including the failed Royal Palace assassination plot and the Mt. Ceram lava-pool operation — have been funded through Sylphon & Stone's commercial network. The cult-funds move as legitimate-appearing commercial transactions through the guild's accounts.

**This gives the Beads Cult *political leverage against Baradus's approach*.** Baradus's path runs through:
- Converting Silas Moray (Section 7)
- Subverting the nobility through the Concordance (this section, above)

Goma's path runs through:
- Compromising Sylphon & Stone for funding and commercial cover
- Independent action that does not coordinate with Baradus

**The two cult-political strategies do not overlap.** This is why Goma operates so independently — she has her own institutional vehicle (Sylphon & Stone) that gives her resources and political reach without needing to coordinate with the Sword Cult. **The cults' disunity is partly an institutional fact, not just a personality clash.**

**Mid-to-late-game exposure beat `[LOCKED]`:**

**The Sylphon & Stone cult-compromise is exposed during the game**, causing political fallout. Likely placement: **late Act III / early Act IV**, after Mt. Ceram (where Goma's escape exposes evidence of her funding pipeline) and before the climactic late-game beats.

**Political fallout includes:**
- **Beads Cult loses its primary funding pipeline** — Goma is forced to operate on residual resources for the rest of the story
- **The Concordance is shaken** — if Sylphon & Stone leadership had Concordance seats (the largest merchant guild presumably does), those seats are now compromised or vacated
- **Amber-Letz benefits commercially** — Vandras's family is positioned to pick up market share as Sylphon & Stone is investigated and partially dismantled. *Two thousand years later, this commercial shift is part of why the Berlitz family becomes dominant.* The seeds of canon's mercantile landscape are planted here.
- **Silas Moray may be implicated** by association — his Vizier-of-Commerce role oversaw the guild; he is partially responsible for not catching the cult-funding pipeline. This adds pressure to Silas leading up to his Vizier defeat and unmasking.

`[OPEN]` Who specifically exposes the compromise — Rhydia's intelligence network? Eden's defection-era knowledge? Nemo Korolev's pre-death intel? A combination?
`[OPEN]` The specific scripted-event structure of the exposure beat — investigation sequence, public revelation moment, political-fallout scenes

**Descendants — Sylph Co. and Devon Corporation `[LOCKED — soft canon]`:**

After Cormoria fades across the centuries, **the descendants of the main Sylphon and Stone shareholders settle in Kanto and Hoenn:**
- **Kanto descendants** → eventually found **Silph Co.** (canonical Kanto Pokemon-tech corporation)
- **Hoenn descendants** → eventually found **Devon Corporation** (canonical Hoenn Pokemon-tech corporation)

**The two major Pokemon-tech corporations in modern canon descend from a Cormorian merchant guild that was compromised by the Beads Cult during our story.** Two thousand years later, neither Silph Co. nor Devon Corp knows their origin — but their dominance in their respective regions reflects generations of accumulated Cormorian commercial expertise and the Pokemon-goods specialization that began with Sylphon & Stone.

**The Sylphon → Silph linguistic evolution:**
- Sylphon → Sylph → Silph (across millennia of pronunciation drift)
- The "sylph" (air spirit) etymology resonates with Silph Co.'s Pokemon-research focus (delicate, technical, ethereal)

**The Stone → Devon linguistic evolution:**
- Stone → Stoneward / Stowne / Stove → Devon (geographic-derived eventual name change as descendants settled in regions whose place-names absorbed the family identity)
- The "stone" (solid foundation) etymology resonates with Devon Corp's hardware-focused product line (Devon Goods, including the Devon Scope and various Hoenn-region Pokemon technologies)

`[OPEN]` Specific named Sylphon and Stone family heads in the present story
`[OPEN]` Whether the player can encounter post-exposure dialogue acknowledging the future of these families (subtle hints to canon-aware players)

### Amber-Letz — The Empire's Second Merchant Guild `[LOCKED]`

The **second largest merchant guild in Cormoria**, smaller competitor to Sylphon & Stone. **Vandras's family** — the merchant guild Osrid will eventually be adopted into post-cataclysm as Veddev.

**Market specialization:**
- **Amber-Letz holds the larger market share in human goods** — food, clothing, household items, general consumer commerce
- Smaller presence in Pokemon-related goods compared to Sylphon & Stone

**Founding alliance:** Amber and Letz are the two original family names behind the guild — Vandras's birth-Amber family merged with his wife's Letz merchant family generations ago.

**Long-term commercial trajectory:**
- During the present story, Amber-Letz is the **smaller competitor**
- Following Sylphon & Stone's cult-compromise exposure, Amber-Letz picks up market share
- **Across ~1,800 years**, the Amber-Letz family name evolves: Amber-Letz → Amberletz → ... → **Berlitz**
- The Berlitz family eventually produces **Volo** (PLA) and **Cynthia** (Gen 4)
- *Cynthia's canonical gravitas tracks with two millennia of bloodline carrying unspoken Cormorian historical depth* — including the commercial generational ascendance from the empire-era smaller competitor to the modern Sinnohian elite line

**The thematic charge of the Amber-Letz / Sylphon & Stone rivalry:**

The empire-era commercial rivalry casts a 2000-year shadow across canon Pokemon's commercial landscape. **The smaller competitor that took in the renounced prince eventually outlasts the larger guild that was compromised by the cult.** This is the project's broader thesis applied to commerce: institutions built on integrity (and on accidental partnership with morally significant figures) outlast institutions built on corruption (and on cult-funding compromise). **Cynthia descends from the guild that adopted a stranger; Silph and Devon descend from the guild that funded the Beads Cult.** Both succeed — they're modern canon's dominant corporations — but the project's protagonist-bloodline runs through the *smaller, more honest* commercial line.

### The Royal Secret Villa `[LOCKED]`

The Cormorian royal family's secluded retreat — **physically far from the imperial capital, geographically near House Moray's estate.** Pierra has been residing here in self-imposed seclusion for most of the 10 years since Eldred's assassination.

**Geographic significance:**
- The Villa's location near House Moray's estate **explains how Silas's daily psychic manipulation of Pierra has been logistically possible** — they are essentially neighbors. Silas can visit Pierra on a near-daily basis to maintain his memory-erasure manipulation reinforcement (Section 9 — Silas's memory-erasure mechanics requires sustained reinforcement).
- **Pierra is physically alone except for Villa staff and Silas's visits.** Rhydia is in the capital running the empire and rarely visits her mother — the geographic distance is real.
- **Geographic poignancy:** Pierra retreated to her family Villa for safety and privacy after her husband's assassination; in doing so, she unknowingly placed herself in *the worst possible location for her emotional safety*. The Villa is the trap. The geography is the manipulation infrastructure.

**Story-beat implications:**
- The Villa may be a location the player eventually visits — likely in a late-game beat where Silas's manipulation is exposed
- A late-game pilgrimage to the Villa could be the moment Pierra learns the truth about Silas and (separately) the moment she might or might not learn about Osrid's survival
- `[OPEN]` Whether the player visits the Villa in the main game; whether Pierra ever learns the full truth

---

