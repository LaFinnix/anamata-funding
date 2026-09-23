# Ngā Wiri o te Tinana: somatosensory composition practice brief

Working document for the Creative Fellowship 2026 R2 programme. The application is at
`/opt/data/anamata/funding/applications/2026-CNZ-CreativeFellowshipFund-R2/APPLICATION.md`.
This file is the music side: what to build, what to test, and how to write with it.

Status: draft v0.2, 2026-09-24. Prices in section 1 are indicative envelopes held for planning, not
quotes, and the quote plan in section 1 sets out who is asked and by when. Nothing here is a price claim
and none of it belongs on a funder form until a quote sits behind it.

---

## 1. The rig

Three outputs, not one. Every piece of hardware below serves either the audible path, the tactile path,
or the bone conduction path. Keeping them on separate amplifiers and separate buses is the whole trick,
because a tactile pass that reads on the body is far too loud to judge by ear.

| Part | Example product class | Why it is there | Envelope |
|---|---|---|---|
| Tactile transducers (2 to 4) | Dayton Audio TT25-8 puck transducers for chair and backrest | Small, mountable, 8 ohm, happy in the 20 to 200 Hz band | Indicative, quote pending |
| Large tactile transducer (1 to 2) | Dayton Audio BST-1 or AuraSound AST-2B-4 class bass shaker | Moves a platform or a floor panel, for feet and sternum | Indicative, quote pending |
| Amplifier, dedicated | Class D or pro amp, 50 to 150 W per channel into 4 or 8 ohm | Drives the tactile path separately from the monitor amp | Indicative, quote pending |
| Wearable haptic vest | Woojer Vest Edge or bHaptics TactSuit X40 class | Body-location work while composing, and a second surface to compare against the chair | Indicative, quote pending |
| Bone conduction | Shokz OpenRun class | Carries the mid and upper band to a Deaf or hard of hearing collaborator through the skull | Indicative, quote pending |
| Measurement mic | Dayton iMM-6 or miniDSP UMIK-1 class, calibrated | Frequency response of the tactile path, measured not guessed. Works with Room EQ Wizard | Indicative, quote pending |
| Contact measurement | Contact mic or a small accelerometer on the mounting surface | What the body actually receives, which is the honest reference. Amplifier output is not evidence | Indicative, quote pending |
| Mounting and isolation | Plywood platform, rubber isolation pads, bolts | Rigid coupling to the transducer, isolation from the building. Both matter: rigid coupling so energy moves, isolation so it moves into the body and not the floor | Indicative, quote pending |

Build two surfaces, because they behave differently and the tests compare them.

1. **Tactile chair.** Two puck transducers bolted to a rigid back panel and one under the seat. Reads on
   the upper back, lower back and thighs.
2. **Tactile platform.** One large shaker under a plywood board with isolation feet. Reads through the
   feet and, standing close, the sternum.

Budget envelope in the application is $6,800 for this line, held as a planning figure. The fund does not
ask for a budget and the $50,000 is fixed, so the envelope exists for acquittal and for the next round
rather than for assessment. What follows is how it becomes real.

### Quote plan

Every line is quoted before purchase, and each one is replaced by the real figure in the next revision of
this brief.

| Line | Where the quote comes from | Due |
|---|---|---|
| Puck and shaker transducers | The manufacturer's New Zealand distributor, or the export route where no local stock exists | before purchase |
| Amplifier | New Zealand pro audio suppliers, quoted for the transducer load rather than for a nominal wattage | before purchase |
| Wearable vest | The vendor direct, quoted only after the routing questions below are answered in writing | before purchase |
| Bone conduction | New Zealand retail for the OpenRun class, or whatever the reviewer prefers | before purchase |
| Measurement chain | Calibrated USB measurement microphone plus a small accelerometer, quoted with its calibration file | before purchase |
| Mounting and isolation | Local timber and hardware, priced as a bill of materials rather than as one item | before purchase |

If quotes come back above the envelope, the deliverable changes rather than the arithmetic: the second
large transducer and the second surface are the items that can wait a phase.

### Vest routing and latency

A consumer vest is the least predictable device in the rig. Most process audio internally and many reach
the body over Bluetooth, and a thirty millisecond buffer would break the alignment step in section 3
before the work starts. The vest is therefore specified by its routing, not by its marketing.

- **Preferred path:** analog auxiliary input, or USB audio treated as an ordinary sound card. Analog is
  preferred because it removes a codec stage that cannot be inspected.
- **Not accepted as the scored path:** Bluetooth, or any mode where the vest's own processing cannot be
  switched off. A vest in that state is a composition reference, and the measurement path with the chair
  and platform stays the reference surfaces.
- **Measured, not assumed:** the vest's own round-trip latency is measured with the same impulse method
  used for the other surfaces and logged beside the chair and platform figures. Whatever it adds is
  compensated like any other delay, and the residual error is reported rather than tuned out by feel.
- **Answered in writing before the purchase decision:** whether the internal processing can be bypassed,
  whether the vest accepts an external transducer feed, and what its latency is on the analog path.

---

## 2. Phase one test protocol

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
| T12 | Fatigue, comfort and exposure | Thirty minutes of continuous exposure at working level on each surface, with acceleration measured at the contact surface and logged as a time weighted figure. Screened participants only, check in at ten and twenty minutes, stop rule in force | Safe session length, the level ceiling the notation writes as intensity 5, and the exposure record the acquittal needs |

T4, T9, T10 and T11 are the tests that produce something the sector does not already have.

### Participant care and safeguarding

Vibration is a physical exposure and a research rig is not a playground. The programme runs on the terms
below, and they are protocol rather than good intentions.

- **Screening before the first session.** No participant enters the rig without being asked about
  pacemakers and other implanted devices, pregnancy, vestibular conditions, recent surgery or injury,
  epilepsy, and circulatory or nerve conditions in the areas the rig loads. A yes starts a conversation
  about whether this work is right for that person, not an automatic no.
- **Informed consent that names the sensory experience.** Consent states what will be felt, where, at
  what level, for how long, and that vibration can cause numbness, tingling, fatigue or nausea. It is
  taken per session, in the participant's first language, with NZSL interpretation where that is their
  language.
- **Exposure referenced to published guidance.** Thresholds are set against ISO 2631-1 for whole-body
  vibration and ISO 5349-1 for hand-arm vibration, measured with an accelerometer at the contact surface
  rather than inferred from amplifier output. Exposure is logged per session, and the level ceiling in
  the notation is capped by what the log supports rather than by what sounds good.
- **Opt out at any point, and the work still counts.** Any participant may stop a test, a session or the
  programme at any stage without giving a reason, and nothing they contributed is used afterwards unless
  they say so. The log records a stop as a stop.
- **Fees for time, agreed before the session.** Collaborators are paid for their time rather than
  reimbursed for attending, with the rate agreed in writing first.
- **Data sovereignty.** Session recordings, body-map responses and test results belong to the people who
  produced them. The programme holds them under the CARE principles already documented for the platform:
  collective benefit, authority to control, responsibility, ethics. Nothing from a session is published,
  sampled or released without consent to that specific use, and consent for one use is not consent for
  another.
- **Cultural review of the protocol before any session runs.** The reviewer sees the screening
  questions, the consent wording and the exposure protocol, and sessions do not begin until that review
  is returned.

---

## 3. The workflow

### Session architecture

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

### Phase alignment

The tactile path arrives late. The transducer has mass, the amplifier has a delay, the coupling has give,
and a wearable adds its own buffer on top. Alignment is a measurement, not an adjustment by feel.

1. Send an impulse out of both paths at once and capture both with one interface: the audible path on the
   measurement microphone, the tactile path on the accelerometer or contact microphone fixed to the
   mounting surface. One pass, two channels, so the difference between the onsets is a number rather than
   an impression.
2. Read the offset in samples. A sample delay on the audible bus, set to that figure, is the
   compensation. Where the tactile path runs late by more than the audible bus can carry, the delay moves
   to the tactile bus and the monitors come forward instead.
3. Confirm against a loopback and against an oscilloscope view of the two channels, then confirm by hand
   on a click train. Sampled figure, scope figure and felt result should agree, and where they do not
   agree, the disagreement is the finding.
4. Hold residual error under five milliseconds and log the figure per surface, because the chair, the
   platform and the vest will not match. Anything larger is written into the score as a deliberate
   gesture rather than left as a defect.

### Writing rules to test, not to assume

- Rhythm carries in the tactile layer. Pitch is weak below 50 Hz, so melody is carried by rhythm, level
  and location rather than by pitch. Test this rather than believe it.
- Two rhythmic lines need separation in band and in body location. T4 and T5 set the numbers.
- Repetition is not boring in the tactile register; it is legibility. A hook that cannot be felt twice
  the same way is not a hook.
- Sections are marked by change in location or band, not by change in harmony. A chorus can be one event
  moving from the chair to the sternum.
- Never judge the tactile mix by ear. Use the measurement path and the collaborator.

---

## 4. The works

Six waiata in te reo Māori, each with a tactile layer composed alongside the vocal line rather than after
it. Three recorded to release standard with English, te reo Māori and NZSL assets, each with its tactile
score published.

Prototype first. Build one work as the tactile prototype before committing the others, so the notation and
the workflow are tested on a real piece rather than on test signals.

Recommendation for the prototype: a slow, sparse waiata. Low tempo and a single line is where tactile
legibility is easiest to prove, and where a polyrhythm has room to stay two rhythms. A dense, fast waiata
is the harder second piece, once T4 has produced the separation figures.

## 5. Roles

| Role | Who | Paid from |
|---|---|---|
| Composer, programme lead | Ngaika Smith | Artist time, $31,200 |
| Deaf artists, NZSL poets, tāngata whaikaha Māori performers | To be selected within 30 days of award from networks we already work with | Collaborator fees and koha, $7,500 |
| Cultural review at draft stage | Maurea, Precious Clark, engaged since 2024 | Collaborator fees and koha |
| NZSL interpreters | WordsWorth Interpreting | Access and interpretation, $3,000 |
| Accessibility and haptic advice | Access Advisors and Arts Access Aotearoa | In kind, existing relationship |
| Taonga pūoro mentor | To be selected with the cultural reviewer | Collaborator fees and koha |

## 6. What this brief produces for the fellowship

- The tactile notation, tested on real works, released as an open document.
- The protocol document, built from the test log rather than from opinion.
- The DAW template, exported as a session template with the three buses pre-routed.
- The evidence section of both, which is the test log itself.

## 7. Open items

1. Quotes for every item in section 1, by the route in the quote plan. Nothing in the budget annex is a
   price until a quote sits behind it, and the envelope holds as a planning figure until then.
2. Vest choice, pending the vendor's written answer on processing bypass, external feed and analog
   latency.
3. Accelerometer choice and calibration, so exposure is logged in metres per second squared rather than
   in amplifier settings.
4. Cultural review of the screening, consent and exposure protocol before the first session, and te reo
   terms for the body location codes in the notation.
5. Which waiata is the prototype.
6. Collaborators, once approached.
7. Session length and level limits, confirmed with the collaborators rather than assumed.
