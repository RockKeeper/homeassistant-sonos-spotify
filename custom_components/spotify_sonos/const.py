"""Const for Sonos."""

DOMAIN = "spotify_sonos"
DATA_SPOTIFY_SONOS = "spotify_sonos_media_player"

SONOS_ARTIST = "artists"
SONOS_ALBUM = "albums"
SONOS_PLAYLISTS = "playlists"
SONOS_GENRE = "genres"
SONOS_ALBUM_ARTIST = "album_artists"
SONOS_TRACKS = "tracks"
SONOS_COMPOSER = "composers"

DATA_SPOTIFY_CLIENT = "spotify_client"
DATA_SPOTIFY_ME = "spotify_me"
DATA_SPOTIFY_SESSION = "spotify_session"

SPOTIFY_SCOPES = [
    # Needed to be able to control playback
    "user-modify-playback-state",
    # Needed in order to read available devices
    "user-read-playback-state",
    # Needed to determine if the user has Spotify Premium
    "user-read-private",
    # Needed for media browsing
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-library-read",
    "user-top-read",
    "user-read-playback-position",
    "user-read-recently-played",
    "user-follow-read",
]