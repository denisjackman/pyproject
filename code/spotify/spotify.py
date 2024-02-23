#!/usr/bin/python
"""
    Spotify API example
"""
import os
import sys
import tekore as tk

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck # noqa: E402


def main():
    """ This is the main function """
    credid = credscheck('y:/pyproject/secrets/secrets.json')
    token = credid["SpotifyToken"]
    spotify = tk.Spotify(token)
    tracks = spotify.current_user_top_tracks()
    count = 1
    for track in tracks.items:
        print(count, track.name)
        count = count + 1
        user = spotify.user
        print(user.display_name())


if __name__ == '__main__':
    main()
