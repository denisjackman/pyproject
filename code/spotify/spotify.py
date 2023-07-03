#!/usr/bin/python
"""
    Spotify API example
"""
import tekore as tk
from djgamemodule import security as sec


def main():
    """ This is the main function """
    credid = sec.credscheck('y:/pyproject/secrets/secrets.json')
    # client_id = cred_id["SpotifyClientID"]
    # client_secret = cred_id["SpotifyClientSecret"]
    # redirect_uri = "https://github.com/denisjackman/pyproject"
    # conf = (client_id, client_secret, redirect_uri)
    token = credid["SpotifyToken"]
    spotify = tk.Spotify(token)
    tracks = spotify.current_user_top_tracks()
    count = 1
    for track in tracks.items:
        print(count, track.name)
        count = count + 1
        user = spotify.user
        print(user.display_name())
    # spotify.playback_start_tracks([t.id for t in tracks.items])


if __name__ == '__main__':
    main()
