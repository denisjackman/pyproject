#!/usr/bin/python
"""
    Spotify API example
"""
import os
import sys

#pylint: disable=wrong-import-position
MODULE_PATH = "../jackmanimation/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import credscheck
#pylint: enable=wrong-import-position

import tekore as tk


def main():
    """ This is the main function """
    cred_id = credscheck('../secrets/credentials.json')
    # client_id = cred_id["SpotifyClientID"]
    # client_secret = cred_id["SpotifyClientSecret"]
    # redirect_uri = "https://github.com/denisjackman/pyproject"
    # conf = (client_id, client_secret, redirect_uri)
    token = cred_id["SpotifyToken"]
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
