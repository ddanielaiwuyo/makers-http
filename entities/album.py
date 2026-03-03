from dataclasses import dataclass, field

@dataclass
class Album:
    """Represents album entity in database"""
    id: int
    title: str
    release_year: str
    artist_id: int = field(default=None)

