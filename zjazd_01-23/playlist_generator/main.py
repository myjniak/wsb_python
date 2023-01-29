from api.spotify import Spotify


spotify = Spotify()
spotify.connect()
songs = spotify.search("Kawałek do tańca")
sample_track_id = songs.tracks.items[0].item_id
features = spotify.get_tracks_audio_features(sample_track_id)
print(features)
