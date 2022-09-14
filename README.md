# These are some of my favorite chord progressions

## NOTE:
- Circlular nodes are chords that start songs
- songs must be added in the following format (in the mermaid block):
    - `<artist> - <title>`

### Songlist

- Jack Johnson - Sitting Waiting Wishing
- Ashley Eriksson - Island Song
- Radiohead - Creep
- Sam's Riff 1

```mermaid
graph LR;
    %% Jack Johnson - Sitting Waiting Wishing
    Am((Am))-->Am7
    Am7-->G
    G-->G7
    G7-->F
    F-->F7
    F7-->C
    C-->C7
    C7-->E
    E-->E7
    E7-->Am
    
    %% Ashley Eriksson - Island Song
    A((A))-->D
    D-->G
    G-->Bm
    D-->A
    A-->G
    Bm-->G
    G-->D
    G-->A
    A-->D
    D-->F#7
    F#7-->G
    G-->E7
    E7-->A

    %% Radiohead - Creep
    G((G))-->B
    B-->C
    C-->Cm
    Cm-->Cm
    Cm-->G

    %% Sam - Riff 1
    C7((C7))-->B7
    B7-->Em7
    Em7-->D7
    D7-->Cm7
    Cm7-->C7
```

---

# TODO
- figure out how to make graph bigger
- Write a utility script for:
    - adding new songs
    - checking for duplicate lines
    - removing songs
    - searching for songs