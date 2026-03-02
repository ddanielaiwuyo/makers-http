from dataclasses import dataclass, field
import time


@dataclass
class Albums:
    """Represents album entity in database"""
    id: int
    title: str
    release_year: str


@dataclass
class Artist:
    """Represents artist entity in database"""

    id: int
    name: str
    genre: str
    albums: list[Albums] = field(default=None)


def get_all_artists(delay) -> list[Artist]:
    sugar_hill = Artist(None, "SugarHill Keem", "UK-RAP")
    bill_evans = Artist(None, "Bill Evans", "Jazz")
    radio_head = Artist(None, "Radiohead", "Alternative-Rock")

    time.sleep(float(delay))
    print("delay over")

    return [sugar_hill, bill_evans, radio_head]
