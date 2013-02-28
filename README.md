# Starrify

'Star' [Spotify](http://spotify.com) tracks from the command line.

# Requirements

Install libspotify and pyspotify, e.g.

```bash
brew install libspotify
pip install pyspotify
```

Create a [libspotify API key](http://dev.spotify.com/technologies/libspotify/keys/) and copy the `spotify_appkey.key` file to the same directory containing `starrify.py`.

# Usage

```bash
python starrify.py -t [SPOTIFY_TRACK_URI] -u [SPOTIFY_USERNAME] -p [SPOTIFY_PASSWORD]
```

# TODO

* Use in conjunction with the Spotify AppleScript dictionary to grab what's currently playing, and star it using an [Alfred](http://www.alfredapp.com/) keyboard shortcut.

# Contact

@[steveWINton](https://twitter.com/steveWINton)
