import json

import click

from .api.spotify import Spotify


@click.command()
@click.argument("songs", nargs=-1)
def main(songs):
    spotify = Spotify()
    spotify.connect()
    for song in songs:
        songs = spotify.search(song)
        sample_track_id = songs.tracks.items[0].item_id
        features = spotify.get_tracks_audio_features(sample_track_id)
        print(f"Features for {song}:\n{json.dumps(features, indent=4)}")


if __name__ == "__main__":
    main()
