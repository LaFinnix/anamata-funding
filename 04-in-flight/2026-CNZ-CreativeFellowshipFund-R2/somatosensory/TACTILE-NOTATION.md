# TACTILE-NOTATION, version 0.1

Draft notation for waiata where the primary version is felt. Tested in phase two, revised as the tests
change it, released as an open document at the end of the fellowship.

The audible score and the tactile score share bar numbers, so the two can be read together. The tactile
score must also stand alone: a performer who has never heard the work should be able to rehearse and
perform from it.

## Event fields

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

## Body location codes

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

## Worked example, one bar of 4/4

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

## Reading rules

1. A line is followed by channel, not by pitch. Movement between channels is the contour.
2. Two events that share a channel and a band merge into one sensation. They must be re-notated to
   different channels or different bands, and the separation figures come from tests T4 and T5.
3. Intensity 0 is written, not omitted. Knowing where nothing happens is part of the score.
4. Characters are established by test, not by taste. If T3 says a slow attack reads as tension rather
   than as swell, the vocabulary changes.
5. The performance test for the notation: hand the score to a performer who cannot hear the recording. If
   they cannot rehearse from it, the notation has failed and the fields are wrong, not the performer.

## Versioning

| Version | Trigger | Changes |
|---|---|---|
| 0.1 | drafted 2026-09-21 | fields, channels, characters, worked example |
| 0.2 | after T1, T2, T3 | band boundaries, working level, character vocabulary |
| 0.3 | after T7 | location codes confirmed against the body map |
| 0.4 | after the first waiata is scored | grouping, phrase marks, whatever the first real work exposes |
| 1.0 | released | open document with the changelog, published with the protocol |

The changelog is part of the deliverable. It shows the method was tested rather than asserted.
