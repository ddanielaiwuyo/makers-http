from dataclasses import dataclass, field
from entities.album import Album

# @dataclass
# class Album:
#     """Represents album entity in database"""
#     id: int
#     title: str
#     release_year: str


@dataclass
class Artist:
    """Represents artist entity in database"""
    id: int
    name: str
    genre: str
    albums: list[Album] = field(default=None)
