from dataclasses import dataclass, field
from entities.album import Album

@dataclass
class Artist:
    """Represents artist entity in database"""
    id: int
    name: str
    genre: str
    albums: list[Album] = field(default=None)
