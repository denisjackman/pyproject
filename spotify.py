"""
    Spotify API example
"""

import tekore as tk
from jackmanimation import credscheck

cred_id = credscheck()
client_id = cred_id["SpotifyClientID"]
client_secret = cred_id["SpotifyClientSecret"]
redirect_uri = "https://github.com/denisjackman/pyproject"
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
