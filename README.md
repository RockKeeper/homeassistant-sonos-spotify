# homeassistant-sonos-spotify

### NOT INSTALLABLE! PLACEHOLDERS HAVE TO BE REPLACED AT media_player.py

this project is intended to work around the problem that sonos players 
are not listed via the soptify connect api. For this I have modified 
the Sonos integration so that it gets the data such as playlists, 
albums, etc. from the Spotify integration, and can then play them 
via Sonos.

Only missing part is the possibility to choose the spotify-media player 
and unique-id at the setup of this integration. At the moment those values 
are hardcoded at media_player.py and in this repo replaced by placeholders...

Status: Work in progress