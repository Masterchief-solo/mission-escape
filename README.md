# Mission Escape
Mission Python, Masterchief Edition. A space adventure game built with Python! Based on *Mission Python* by Sean McManus.
Built with [Pygame Zero](https://pygame-zero.readthedocs.io/).

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Run

```bash
uv run pgzrun escape.py
```

## Layout

- `escape.py` - the main game (grows chapter by chapter)
- `images/`, `sounds/` - game assets (Pygame Zero requires these folder names; music is played from `sounds/`)
- `docs/halo-design.md` - Halo theme mapping and feature backlog

## Credits

- Game code and sound effects from *Mission Python* by Sean McManus ([sean.co.uk](http://www.sean.co.uk/books/mission-python/)).
- Original art by Rafael Pimenta. Some images are recoloured or replaced with AI-generated Halo-style art; see `docs/halo-assets.md` for each asset's source.
- The book's assets are used with credit, for non-commercial purposes only, as their licence requires. This project is free and not for sale.

Mission Escape: Master Chief Edition was created under Microsoft's "[Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules)" using assets from Halo, and it is not endorsed by or affiliated with Microsoft.
