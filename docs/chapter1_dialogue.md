# Dreamstone Ruination: Chapter 1 script, up to Eden's imprisonment

Generated from the game scripts (tools: see commit). Speakers as the player sees them; narration in italics.
In game, a name is shown only when a new speaker starts talking.

## Opening narration (Professor Tenebris)

> From the notes of Professor Tenebris - XX-XX-29

> To my favourite lab assistant-turned-Champion,

> I hope this finds you well! I know you've got a lot on your plate these days, but I thought you'd appreciate an update since our last chat at the lab.

> I finished rummaging through my old family home and... I can barely believe it. I found writings from over two thousand years ago that actually document the lost age of the Cormorian Empire!

> Try to wrap your mind around this.

> Two thousand years before Red became Champion of the Indigo League in Kanto, the world of Pokémon was a very different place, and Cormoria most of all. It was almost unrecognisable.

> You and I are no strangers to travelling into the distant past, but even so, this period in history was like a black hole. Even I knew almost nothing about it. Until now.

> It was an age of empires and of stranger faiths, when every nation vied for supremacy over the others. It paints quite a picture, doesn't it?

> But those who wrote the histories that came after did their best to bury every trace of what happened. And now I have the proof.

> I've barely begun to piece it all together, but if what these papers say is true, everything we thought we knew about the modern world is going to change.

> My ancestor, Cadmus Umbra, was a Vizier of the Cormorian Empire in its waning years, and he was extremely thorough in recording what he saw. So brace yourself, kiddo. It's pretty fantastic.

> It all starts with his own copy of a letter he sent to someone very important...

## Cold open (letter and reply)
*(Installed 2026-11-18, user-revised. Source of truth: data/maps/PellucaReflection/scripts.pory.)*

*A sealed letter. Plain wax, no crest.*

**Cadmus:** Nomad Alban,  The surgeon's report from Sevii reached my desk a week before your commander's did. A commander proud of his decisions does not take a week to report them.  Burns to the face and neck, taken holding a beach that needed twice the men. Commander Surge split his forces across two fronts, and you paid for his folly.

**Cadmus** *(smile)***:** The Commander has since been invited to explain his judgement to people who outrank us both. He will be explaining it for some time, from a cell that has never seen daylight.

**Cadmus:** I am told the army gave you a rare mending mask from the Athanto kingdom while your burns heal. Such masks hasten healing and ward off evil. None have been made since the kingdom fell, and one is now worth more than most noble estates, so expect a few stares.  Wear it well. I suspect it will serve you longer than the burns require.  I am pleased to inform you that, for your actions on that beach and in light of your injuries, you have been granted an honorable discharge from further military service, with lifetime benefits.  You have also been raised to the rank of Rainhawk. At twenty, you are the youngest in Cormorian history to hold it. The rank carries the right to challenge the Trials, should you choose to, a right the Empire rarely extends beyond its noble houses. I suspect you will choose to. Word of all this has travelled faster than any ship. Criers have carried the tale of Sevii through every square from Silversun to Rivetshore: the beach, the burns, and the masked soldier made Rainhawk at twenty. Notices bearing a likeness of your mask hang in half the taverns of the Empire, so do not be surprised when strangers know you on sight.  As of the day this letter reaches you, you will serve under me in the Ministry of Education.

**Cadmus:** Your immediate orders are as follows. The Pale Veluza waits in the harbor south of your barracks. You are to board her and return home. She sails for Pelluca Valley, where I will meet you at the docks.  Write your reply and leave it with the Templar chaplain at your barracks. It will reach me quickly. Sign it with the name you were born with, not the one I gave you a decade ago, and I will know it is truly you.

**Cadmus** *(smile)***:** Then burn this. These days, too many people in Cormoria read letters never meant for them.  C.

*[Signing screen: pre-filled "Osrid", editable.]*

**Osrid:** Received and acknowledged. I will be aboard the Veluza when she sails.  It... will be good to be home again.

*[The letter burns in the lamp: flame sound, no narration.]*

## Arrival at the Pelluca dock

**Dockhand:** A Rainhawk, in a mask? Like something out of the old stories.

**Sailor:** That's the one who held the beach at Sevii. Burned for it, they say.

**Cadmus:** Rainhawk Alban. Welcome to Pelluca Valley.

**Cadmus:** And the burns? Are they healing?

**“Nomad”:** Slowly. The mask helps.

**Cadmus:** Good. Walk with me. We will talk somewhere quieter.

## Umbra's lab: the briefing

**Cadmus:** Welcome home, my Prince. Forgive the dust. Nobody comes down here but me.

*Cadmus raises a hand toward your mask.*

**Cadmus:** Let me see.

**Osrid:** No.

**Cadmus:** Of course.  The last time you were in Pelluca, you and your sister were ten years old. You fell out of the Academy's apple tree in front of half the faculty. Do you remember?

**Osrid:** I remember the tree.

**Cadmus:** Then let us talk about who you are while you're here.  To the Empire, you are Nomad Alban, a Rainhawk lately discharged and now my personal assistant. The Academy has also named you its head of security, which mostly means no door in this valley is closed to you.

**Cadmus:** There is a small house down in the valley with your cover name on the lease. It isn't much, but the door locks.

**Osrid:** And the real work?

**Cadmus:** For now, the real work and the cover are the same. Earn the Trial Badges. All of them.  A Rainhawk who holds every badge has the right to challenge the Champion.

**Osrid:** My sister.

**Cadmus:** Your sister. Rhydia has held the title for five years now, and she rules the Empire in your mother's name besides.  A man who beats the Champion in front of the whole Empire can tell everyone who he really is, and no one will dare touch him.

**Osrid:** Does she know I'm here?

**Cadmus:** No.

**Cadmus:** Tell me something. What are Pokémon, to you?

**Osrid:** Assets. You keep them fed, you keep them sharp, and you spend them carefully.

**Cadmus:** Surge's words.

**Osrid:** They kept me alive.

**Cadmus:** They did. They also put you on that beach.

**Osrid:** Starter Pokémon? I thought those were only given to noble children.

**Cadmus:** Usually. These three are different.  Read the note beside each one before you choose. I wrote them myself, so forgive the handwriting.

**Cadmus:** Before you choose, take this. You'll be meeting a great many Pokémon from here on, and you should keep a record of them.

*{PLAYER} received the PokéLog!*

**Cadmus:** Paper and ink. It isn't elaborate, but it will get the job done. Write down each one you meet, what it is and how it fights, in your own hand.  In the army, someone else wrote the reports and you read them. This time, you see each Pokémon for yourself.

**Osrid:** Understood.

## Starter note: Frigibax

*Heraldic Frigibax.  I hatched this one from an egg I found on Mt. Mirroh. Note its coloring. In all my years I have never seen another like it.  It favors Dragon and Ice moves, and it hits harder than anything else here, though it is slow to come into its own. Be patient with it.  Its final form, Baxcalibur, is so rare that only one other has been recorded on this continent in two hundred years.  One old text claims it can grow stronger still with the help of a special stone. I have found nothing to confirm it.*

*Take the Heraldic Frigibax as your partner?*

## Starter note: Teddiursa

*Blue Moon Teddiursa.  Tales of a Blue Moon line have circulated for over a century. I found this cub by pure chance a year ago, in the woods near the Blue Moon Monastery.  Much about it is still a mystery. It has a gift for special attacks, and it seems able to learn a wider range of moves than either of the others.  An old story claims the line can grow stronger still from something buried in ancient peat. I took it for folklore.*

*Take the Blue Moon Teddiursa as your partner?*

## Starter note: Tinkatink

*Dragonmaul Tinkatink.  I came across this egg in the Seregmorn Desert, north of Mt. Ceram, a few months ago, and I still can scarcely believe my luck.  A clan of Tinkatink in that desert is said to share this coloring, and to hunt dragons.  It is small, but it takes a blow better than anything twice its size.  A colleague tells me a Tinkaton of that clan can grow stronger still with some rare material worked into its gear. I have not been able to confirm it.*

*Take the Dragonmaul Tinkatink as your partner?*

## The theft and the battle

**Cadmus:** Who put out the lamps?

**Thief:** Don't mind me, gentlemen. I'll only be a moment.

**Cadmus:** Put that down.

**Thief:** Mm, no. I came a long way for this one.

**Cadmus:** Neptune.

**Thief:** So the stories about your Jousteel are true. He's bigger than I was told.  Fine. I'll find another way out.

**Thief:** Is that a mending mask? From Athanto? That's worth more than this whole cellar. Who are you supposed to be?

**“Nomad”:** Put it back.

**Thief:** You'll have to take it off me. Pilfer, up!

**Thief:** Who are you?

**“Nomad”:** Nomad Alban.

**Thief:** Never heard of you.

**“Nomad”:** Good.

**Thief:** Ha! All right, Nomad Alban. I want a rematch, the minute I get out of whatever hole they're about to put me in.

**Cadmus:** You'll find it a very deep hole.

## Eden's defeat line (in battle)

*Five minutes with that Pokémon and you fight like you've had it for years. Who taught you that?*

## The Templar holding cell

*Later, in a holding cell beneath the Templar monastery.*

*(Foreshadowing, user 2026-11-19; DRAFT lines: the church's old foundation fault that Eden's escape blast will expose.)*

**Cadmus:** These walls have seen better days. That crack runs halfway up to the ceiling.

**Templar:** The monastery is old, Vizier. Old stone settles. A few cracks are only its age showing, nothing to trouble yourself over.

**Cadmus:** ...As you say. Then let us begin.

**Templar:** Name.

**Thief:** Eden.

**Templar:** Eden of where?

**Eden:** Of here, apparently.

**Templar:** The Pokémon you took will stay in the Order's keeping.

**Eden:** For now.

**“Nomad”:** Who sent you?

**Eden:** Nobody sends me anywhere. I go where the good things are.

**Eden:** Your little one did all the work back there, you know. And you never said a word to it. Just orders.

**Eden:** Just saying.

**Templar:** Vizier. Rainhawk. If you would leave her with me.

**Cadmus:** Of course. Rainhawk, with me.

## Back at the lab: the shard briefing

**Cadmus:** She knew where to look, and she knew exactly what to take. Someone told her both.

**Osrid:** Someone who knew I was coming.

**Cadmus:** Or someone who knew I was preparing for someone. Either way, I can't put off telling you about the other half of your work.

**Cadmus:** Cormoria once had a Dreamstone. The old tales call it the heart of the Empire. I understand it less than I would like, but I am certain it matters.  It was shattered long ago. A friend of mine, whose name you don't need, has found where nine of the pieces came to rest.

**Cadmus:** There are cults in Cormoria, more of them every year, and two of them want those pieces as badly as I do. If they reach them first, I don't think either of us will like what they wake up.

**Osrid:** And the badges?

**Cadmus:** The badges are why no one will ask what you are doing on a mountain. A Rainhawk chasing Trials can go anywhere he likes.  Bring the pieces to me. I know someone who can make the stone whole again.

**Osrid:** Where do I start?

**Cadmus:** West, past Route 11, toward Mirroh. Kimaris Langerin oversees the first Trial there, and there are rumors of a piece on the mountain above it.  But take a day in the valley first. Learn your partner's habits before someone tests them for you.

## Cadmus, if you talk to him

**Cadmus:** The valley first, then Mirroh. And sleep, if you can manage it.

**Cadmus:** Take your time. They have waited this long.
