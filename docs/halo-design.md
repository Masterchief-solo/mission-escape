# Halo Design Notes

How the *Mission Python* "Escape" game maps onto the Master Chief Edition.
Phase 1 keeps the book's mechanics and only reskins names, text and art.
Phase 2 adds original Halo features.

## Theme mapping

| Book (Escape)                    | Master Chief Edition                               |
|----------------------------------|----------------------------------------------------|
| Mars space station               | UNSC *Pillar of Autumn*                            |
| Astronaut player                 | Master Chief (Spartan-117)                         |
| Mission control / radio messages | Cortana                                            |
| Air supply running out           | MJOLNIR shield / armor power                       |
| Hazards (moving dangers)         | Sentinels / Flood spores                           |
| Objects and props                | Keycards, MA5B, plasma pistol, Cortana's data chip |
| Escape pod goal                  | Reach the Longsword / Warthog run                  |

## Asset rules

- Pygame Zero loads from `images/` and `sounds/`. Filenames are lowercase with no spaces.
- We are starting with the book's provided assets, then will replace them gradually with Halo-style art.
- Don't commit ripped official Halo assets. This is a personal project.
- The per-image replacement plan, sourcing options and credits live in `halo-assets.md`.

## Phase 2 backlog

- [ ] Custom Master Chief sprites: hand-draw the 20 walk-cycle frames and their 20 shadows, with the helmet and torso locked across frames, replacing the recoloured book astronaut used in Phase 1
- [ ] Cortana dialogue system (dicts, JSON data files)
- [ ] Shield recharge mechanic (timers, `clock.schedule`)
- [ ] Covenant enemy AI (classes / OOP)
- [ ] Split `escape.py` into modules (imports, packages)
- [ ] Save / load (file I/O)
- [ ] Tests with `pytest`, linting with `ruff`
