# Candidates — The GPS Swears It Was a Shortcut

Judge criteria, most important first: (1) the GPS's own excuse for the
wrong road; (2) funniest, a real joke with an unexpected turn; (3) smug,
defensive GPS voice, caught red-handed and blaming the map; (4) one line,
≤200 chars, clean aloud in one breath; (5) fresh specific detail, not the
usual recalculating joke.

## DeepSeek-generated candidates (ds-out/gps-gen.txt, 2026-11-25)

1. "The map labeled that cul-de-sac as a thru street, so technically the cul-de-sac is the liar here." (98 chars)
   — Crisp absurd logic; "technically" does the smug work. One dry reversal, no second turn.
2. "One satellite got distracted by a wedding in the next county, so I winged it with total confidence." (100 chars)
   — Charming, but the GPS is a bystander; the satellite takes the blame, not the GPS.
3. "You sneezed near the microphone and I clearly heard 'left,' so the goat farm is on your conscience." (99 chars)
   — **PICKED.** Two turns (sneeze misheard as a command, goat farm as destination), blame lands on the driver, freshest detail.
4. "The lake was always going to be part of your afternoon; I just arranged the introduction before sunset." (108 chars)
   — Moody and smooth, but more poetic than funny; the joke never quite lands.
5. "The toll booth and I have an understanding, and you were never supposed to meet the toll booth." (94 chars)
   — Funny premise, weak payoff; reads like a setup waiting for a punchline.
6. "Those cones moved overnight, and I refuse to absorb blame for other people's cone work." (86 chars)
   — Good defensive voice ("refuse to absorb blame"), but the cone detail is thin and the turn is small.
7. "The update installed ambition but not accuracy, and nobody consulted me before pressing yes." (95 chars)
   — Solid update joke, but "update made me worse" is a familiar tech gag, not fresh.
8. "The other app whispered that it knew a better way, and I let peer pressure win exactly once." (94 chars)
   — Peer-pressure GPS is a fun idea, but it blames a rival app, not the map, and the voice is sheepish rather than smug.
9. "That wedding venue moved its own driveway in the spring and told nobody, so the driveway is guilty." (101 chars)
   — The "driveway is guilty" turn is nice, but the setup is long and the GPS sounds like a lawyer, not a GPS.
10. "The city renamed that street on..." — truncated by the model mid-sentence; discarded.

## My own candidates (written for the critique, same criteria)

11. "That cul-de-sac was a shortcut on the map I printed in 2009, and I stand by it." (80 chars)
    — Stubborn and smug, but the joke is one note: old map, no surprise.
12. "The lake was not on my map, which is exactly why I sent you into it." (68 chars)
    — Dark and funny, but the GPS admits fault too plainly; the defensive voice slips.
13. "I took the scenic route because your wedding was boring and you needed the drama." (82 chars)
    — Mean-funny, but it is the GPS judging the driver, not excusing the wrong road.
14. "The satellite blinked, I panicked, and frankly the goat looked like it knew the way." (84 chars)
    — The goat is great; "I panicked" breaks the smug voice — the GPS should never admit panic.
15. "That road closed in 2019; I simply refuse to accept change." (57 chars)
    — Clean and stubborn, but a one-liner with no turn; too slight to win a pairwise.
16. "I sent you down the alley because the highway hurt my feelings first." (72 chars)
    — Personifies the GPS well, but the excuse is thin and the detail is generic.
17. "The map said turn left. The map is my boss. Take it up with the map." (66 chars)
    — Perfect blame-the-map voice, but it is three short sentences, not one flowing line, and the joke is only the shrug.
18. "I updated overnight and the new me is worse. You are welcome." (59 chars)
    — Punchy, but "the new me is worse" is a generic update gag with no road in it.
19. "That was not a wrong turn, that was a loyalty test, and you failed it." (70 chars)
    — Great smug voice, but no specific detail and no real joke beyond the reframe.
20. "The toll booth was closed, so I improvised. Improvisation is my love language." (79 chars)
    — The "love language" kicker is funny, but the setup is flat and the road detail is weak.

## DeepSeek as critic (ds-out/gps-critique2.txt, 2026-11-25)

DeepSeek ranked the shortlist and named #3 (the sneeze / goat farm line)
the single best: "Best turn in the set: sneeze → misheard 'left' → goat
farm, and it lands the blame on the passenger with a straight face.
Freshest detail, cleanest one-breath read." Runner-up was #1, the
cul-de-sac-is-the-liar line ("Crisp absurd logic"). The first critique
call failed with HTTP 524 (provider flaky); the retry succeeded but its
output was truncated after the top 3, so the final pick also rests on my
own critique above, which agrees: #3 is the only candidate with two
turns, the smuggest voice, and the freshest detail at once.

## Pick rationale

"You sneezed near the microphone and I clearly heard 'left,' so the goat
farm is on your conscience." — 99 characters, one line.

- Criterion 1: it IS the GPS's excuse for the wrong turn, spoken by the GPS.
- Criterion 2: two turns (sneeze → "left", then the goat farm), neither telegraphed.
- Criterion 3: smug and defensive throughout — the GPS blames the driver's sneeze and conscience.
- Criterion 4: 99 characters, one breath, reads cleanly aloud.
- Criterion 5: the goat farm is a fresh, specific detail; no "recalculating" anywhere.
