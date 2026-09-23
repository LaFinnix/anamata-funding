# Method annex

## Supporting method documentation for the Creative Fellowship Fund 2026, Round 2 application

## Practice brief

Working document for the Creative Fellowship 2026 R2 programme. The application is at
`the application document`.
This file is the music side: what to build, what to test, and how to write with it.

Status: draft v0.1, 2026-09-21. Prices marked TO QUOTE have not been verified, and no number in this
file should go onto a funder form until it has a quote behind it.

---

### 1. The rig

Three outputs, not one. Every piece of hardware below serves either the audible path, the tactile path,
or the bone conduction path. Keeping them on separate amplifiers and separate buses is the whole trick,
because a tactile pass that reads on the body is far too loud to judge by ear.

| Part | Example product class | Why it is there | Cost |
|---|---|---|---|
| Tactile transducers (2 to 4) | Dayton Audio TT25-8 puck transducers for chair and backrest | Small, mountable, 8 ohm, happy in the 20 to 200 Hz band | TO QUOTE |
| Large tactile transducer (1 to 2) | Dayton Audio BST-1 or AuraSound AST-2B-4 class bass shaker | Moves a platform or a floor panel, for feet and sternum | TO QUOTE |
| Amplifier, dedicated | Class D or pro amp, 50 to 150 W per channel into 4 or 8 ohm | Drives the tactile path separately from the monitor amp | TO QUOTE |
| Wearable haptic vest | Woojer Vest Edge or bHaptics TactSuit X40 class | Body-location work while composing, and a second surface to compare against the chair | TO QUOTE |
| Bone conduction | Shokz OpenRun class | Carries the mid and upper band to a Deaf or hard of hearing collaborator through the skull | TO QUOTE |
| Measurement mic | Dayton iMM-6 or miniDSP UMIK-1 class, calibrated | Frequency response of the tactile path, measured not guessed. Works with Room EQ Wizard | TO QUOTE |
| Contact measurement | Contact mic or a small accelerometer on the mounting surface | What the body actually receives, which is the honest reference. Amplifier output is not evidence | TO QUOTE |
| Mounting and isolation | Plywood platform, rubber isolation pads, bolts | Rigid coupling to the transducer, isolation from the building. Both matter: rigid coupling so energy moves, isolation so it moves into the body and not the floor | TO QUOTE |

Build two surfaces, because they behave differently and the tests compare them.
1. **Tactile chair.** Two puck transducers bolted to a rigid back panel and one under the seat. Reads on
   the upper back, lower back and thighs.
2. **Tactile platform.** One large shaker under a plywood board with isolation feet. Reads through the
   feet and, standing close, the sternum.

Budget envelope in the application is $6,800 for this line. Get quotes before the annex goes anywhere.

---

### 2. Phase one test protocol

Twelve tests. Each one has a purpose, a method, and a result that changes what I write. Run them in this
order; the later tests assume the earlier ones have defined the working range.

Record every test as an entry with the date, the setup, the level, and the result. That log becomes the
protocol document's evidence section, and it is also what makes the failures publishable.

| # | Test | Method | What it decides |
|---|---|---|---|
| T1 | Usable range | Sweep 20 to 250 Hz in third octave steps on each surface, note where the surface stops responding and where it feels like heat rather than vibration | The working band per surface |
| T2 | Perceptibility threshold | At each of six frequencies, raise level until the participant reports feeling it, then note the level. Repeat with hearing blocked | The dynamic floor. Defines how quiet a detail can be |
| T3 | Envelope vocabulary | Same frequency, four envelopes: fast attack fast decay, fast attack slow decay, slow attack slow decay, gated sustain. Ask what each one means | Which envelope reads as impact, as pulse, as swell, as tension |
| T4 | Polyrhythm legibility | 3:2 and 5:4 patterns at 40, 60 and 80 Hz. Two lines, separated in frequency, then the same pattern with both lines in one band | The core technical result. Where two rhythms stay two rhythms and where they become one rumble |
| T5 | Masking distance | Two simultaneous tones, 10 to 40 Hz apart, and find the spacing where they merge | How far apart two tactile lines must sit to stay separate |
| T6 | Onset marker | Click, short sine burst, and noise burst at the same energy | Which transient reads as an onset through fabric and clothing |
| T7 | Body map | The same eight event types delivered to sternum, upper back, lower back, thighs, feet, palms, forearms, skull | The location vocabulary the notation uses |
| T8 | Vest against platform | The same material on both surfaces | Which surface carries rhythm and which carries pitch and level. Likely different answers |
| T9 | Bone crossover | Raise frequency until the skull path takes over from the tactile path | Where the two-channel split sits. Expect the crossover somewhere above the tactile band |
| T10 | Te reo prosody | Take a spoken reo phrase, extract its stress pattern, test whether that pattern reads as a rhythm tactilely | Whether vocal cadence survives the translation to touch |
| T11 | NZSL cadence | With a Deaf collaborator, sign a line from the same waiata and time the signing cadence against the sung meter | Whether the signed and sung versions share a pulse, which is what makes the co-composition real rather than decorative |
| T12 | Fatigue and comfort | Thirty minutes of continuous exposure at working level on each surface | Safe session length, and where discomfort starts. Log it, keep sessions short, and stop when it stops being pleasant |

T4, T9, T10 and T11 are the tests that produce something the sector does not already have.

---

### 3. The workflow

#### Session architecture

One session, three output buses, one source.

- **AUDIBLE** goes to the monitors as normal.
- **TACTILE** goes to the transducer amplifier. Separate amp, separate level.
- **BONE** goes to the bone conduction path, band-limited to the range the skull carries.

The tactile bus processing order is fixed, because reordering it changes the result:
1. Source split. Either a dedicated low layer written for touch, or the low content extracted from the
   mix. Both are valid, and the tests decide which reads better per waiata.
2. High pass at roughly 20 to 25 Hz. This protects the transducer and removes energy nothing can feel.
3. Low pass at 200 to 250 Hz, adjusted per surface after T1.
4. Transient shaping. The attack is the message. If it is soft, the rhythm disappears.
5. Dynamic control, slow, so it does not flatten the attack it just shaped.
6. Limiter as protection, not as tone.

#### Phase alignment

The tactile path arrives late. The transducer has mass, the amplifier has a delay, and the coupling has
give. Measure it with an impulse through both paths and align the tactile bus to the audible one. Then
write the waiata so that a felt onset and a heard onset are the same event, not two events 30 ms apart.

#### Writing rules to test, not to assume

- Rhythm carries in the tactile layer. Pitch is weak below 50 Hz, so melody is carried by rhythm, level
  and location rather than by pitch. Test this rather than believe it.
- Two rhythmic lines need separation in band and in body location. T4 and T5 set the numbers.
- Repetition is not boring in the tactile register; it is legibility. A hook that cannot be felt twice
  the same way is not a hook.
- Sections are marked by change in location or band, not by change in harmony. A chorus can be one event
  moving from the chair to the sternum.
- Never judge the tactile mix by ear. Use the measurement path and the collaborator.

---

### 4. The works

Six waiata in te reo Māori, each with a tactile layer composed alongside the vocal line rather than after
it. Three recorded to release standard with English, te reo Māori and NZSL assets, each with its tactile
score published.

Prototype first. Build one work as the tactile prototype before committing the others, so the notation and
the workflow are tested on a real piece rather than on test signals.

Recommendation for the prototype: a slow, sparse waiata. Low tempo and a single line is where tactile
legibility is easiest to prove, and where a polyrhythm has room to stay two rhythms. A dense, fast waiata
is the harder second piece, once T4 has produced the separation figures.

### 5. Roles

| Role | Who | Paid from |
|---|---|---|
| Composer, programme lead | Ngaika Smith | Artist time, $31,200 |
| Deaf artists, NZSL poets, tāngata whaikaha Māori performers | To be selected within 30 days of award from networks we already work with | Collaborator fees and koha, $7,500 |
| Cultural review at draft stage | Maurea, Precious Clark, engaged since 2024 | Collaborator fees and koha |
| NZSL interpreters | WordsWorth Interpreting | Access and interpretation, $3,000 |
| Accessibility and haptic advice | Access Advisors and Arts Access Aotearoa | In kind, existing relationship |
| Taonga pūoro mentor | To be selected with the cultural reviewer | Collaborator fees and koha |

### 6. What this brief produces for the fellowship

- The tactile notation, tested on real works, released as an open document.
- The protocol document, built from the test log rather than from opinion.
- The DAW template, exported as a session template with the three buses pre-routed.
- The evidence section of both, which is the test log itself.

### 7. Open items
1. Quotes for every item in section 1. Nothing in the budget annex is real until it has one.
2. Vest choice. Consumer vest roadmaps change quickly, so confirm the current model, its latency, its
   software support and whether it accepts an external transducer feed before buying.
3. Which waiata is the prototype.
4. Collaborators, once approached.
5. Session length and level limits, confirmed with the collaborators rather than assumed.

## Tactile notation

Draft notation for waiata where the primary version is felt. Tested in phase two, revised as the tests
change it, released as an open document at the end of the fellowship.

The audible score and the tactile score share bar numbers, so the two can be read together. The tactile
score must also stand alone: a performer who has never heard the work should be able to rehearse and
perform from it.

### Event fields

Every event carries seven fields. Nothing is optional except duration on an instantaneous event.

| Field | Values | Notes |
|---|---|---|
| Time | bar.beat.tick, or seconds for a standalone tactile work | Follows the audible score |
| Channel | CH1 to CH8, the body location codes below | Location is the melodic axis |
| Character | impact, pulse, swell, rumble, tick, sustain | The six characters established in test T3 |
| Band | A 20 to 40 Hz, B 40 to 80 Hz, C 80 to 140 Hz, D 140 to 250 Hz, E above 250 Hz via bone conduction | Band boundaries move after test T1 per surface |
| Intensity | 0 to 5 | 3 is the working level from test T2, 5 is the ceiling from test T12, 0 is written silence |
| Duration | milliseconds, or a note value | |
| Grouping | bracket over a phrase | Where two events group as one gesture |

### Body location codes

| Code | Location | Delivered by |
|---|---|---|
| CH1 | sternum and chest | platform, standing close |
| CH2 | upper back | chair back, upper transducer |
| CH3 | lower back and hips | chair back, lower transducer |
| CH4 | left thigh | seat transducer left |
| CH5 | right thigh | seat transducer right |
| CH6 | feet and legs | platform shaker |
| CH7 | palms and forearms | vest arm channels, or a held transducer |
| CH8 | skull | bone conduction path |

Bilingual labels for each location are an open item. Te reo names for the body areas should come from the
cultural reviewer rather than from me, and then sit alongside the codes rather than replacing them, so the
notation stays readable to performers outside te ao Māori.

### Worked example, one bar of 4/4

| Beat | Channel | Character | Band | Intensity | Duration |
|---|---|---|---|---|---|
| 1 | CH2 | impact | A | 5 | 120 ms |
| 1.5 | CH2 | pulse | B | 3 | 80 ms |
| 2 | CH6 | rumble | A | 4 | 400 ms |
| 2.5 | CH7 | tick | C | 2 | 40 ms |
| 3 | CH2 | impact | A | 5 | 120 ms |
| 4 | CH1 | swell | B | 3 | 800 ms |

Read it as: two impacts on the upper back at beats one and three, a lower pulse between them, a long low
rumble through the feet from beat two, a tick in the palms to mark the off beat, and a swell on the chest
that opens the next bar. The melodic contour of the bar is CH2 to CH6 to CH7 to CH1.

### Reading rules
1. A line is followed by channel, not by pitch. Movement between channels is the contour.
2. Two events that share a channel and a band merge into one sensation. They must be re-notated to
   different channels or different bands, and the separation figures come from tests T4 and T5.
3. Intensity 0 is written, not omitted. Knowing where nothing happens is part of the score.
4. Characters are established by test, not by taste. If T3 says a slow attack reads as tension rather
   than as swell, the vocabulary changes.
5. The performance test for the notation: hand the score to a performer who cannot hear the recording. If
   they cannot rehearse from it, the notation has failed and the fields are wrong, not the performer.

### Versioning

| Version | Trigger | Changes |
|---|---|---|
| 0.1 | drafted 2026-09-21 | fields, channels, characters, worked example |
| 0.2 | after T1, T2, T3 | band boundaries, working level, character vocabulary |
| 0.3 | after T7 | location codes confirmed against the body map |
| 0.4 | after the first waiata is scored | grouping, phrase marks, whatever the first real work exposes |
| 1.0 | released | open document with the changelog, published with the protocol |

The changelog is part of the deliverable. It shows the method was tested rather than asserted.
