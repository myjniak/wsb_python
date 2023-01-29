from enum import Enum
from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class ItemType(Enum):
    track = "track"
    artist = "artist"


class ExternalUrls(BaseModel):
    spotify: str


class Artist(BaseModel):
    external_urls: ExternalUrls
    href: str
    item_id: str = Field(..., alias="id")
    name: str
    item_type: Literal["track", "artist", "album"] = Field(..., alias="type")
    uri: str


class Album(BaseModel):
    album_type: str
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    item_id: str = Field(..., alias="id")
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    item_type: Literal["track", "artist", "album"] = Field(..., alias="type")
    uri: str


class Item(BaseModel):
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    item_id: str = Field(..., alias="id")
    is_local: bool
    name: str
    popularity: int
    item_type: Literal["track", "artist", "album"] = Field(..., alias="type")
    uri: str


class Tracks(BaseModel):
    href: str
    items: List[Item]
    limit: int
    next_page: str = Field(..., alias="next")
    offset: int
    previous: Optional[str]
    total: int


class SearchResult(BaseModel):
    tracks: Tracks
