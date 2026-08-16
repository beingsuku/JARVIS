import os
import re
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SCOPE = "user-modify-playback-state user-read-playback-state user-read-currently-playing"

_sp = None


def _get_client():
    """Lazy-init spotipy client so OAuth/browser popup only happens on first real use,
    not on JARVIS startup / import."""
    global _sp
    if _sp is None:
        _sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope=SCOPE,
            cache_path=".spotify_cache",
        ))
    return _sp


def _active_device_id(sp):
    """Returns the id of the first active device, or None if Spotify app isn't open/no device found."""
    devices = sp.devices().get("devices", [])
    if not devices:
        return None
    # Prefer a device already marked active; otherwise fall back to the first available.
    for d in devices:
        if d.get("is_active"):
            return d["id"]
    return devices[0]["id"]


def run(command: str) -> str:
    command = command.lower().strip()

    try:
        sp = _get_client()
    except Exception:
        return "Spotify isn't set up correctly. Check your client ID, secret, and redirect URI in the .env file."

    device_id = _active_device_id(sp)
    if device_id is None:
        return "I can't find an active Spotify device. Make sure the Spotify app is open on this PC."

    try:
        # Play a specific song: "play <song name>" (but not bare "play" or "play music")
        match = re.search(r"play (.+)", command)
        if match and match.group(1).strip() not in ("", "music", "song", "spotify"):
            query = match.group(1).strip()
            results = sp.search(q=query, type="track", limit=1)
            tracks = results.get("tracks", {}).get("items", [])
            if not tracks:
                return f"I couldn't find a song called {query} on Spotify."
            track = tracks[0]
            uri = track["uri"]
            name = track["name"]
            artist = track["artists"][0]["name"] if track["artists"] else "unknown artist"
            sp.start_playback(device_id=device_id, uris=[uri])
            return f"Playing {name} by {artist}."

        if "pause" in command or "stop" in command:
            sp.pause_playback(device_id=device_id)
            return "Paused."

        if "resume" in command or "continue" in command or command.strip() == "play":
            sp.start_playback(device_id=device_id)
            return "Resuming playback."

        if "next" in command or "skip" in command:
            sp.next_track(device_id=device_id)
            return "Skipped to next track."

        if "previous" in command or "back" in command or "last song" in command:
            sp.previous_track(device_id=device_id)
            return "Went back to previous track."

        return "I didn't understand that Spotify command."

    except spotipy.exceptions.SpotifyException as e:
        return f"Spotify error: {str(e)}"
    except Exception as e:
        return f"Something went wrong controlling Spotify: {str(e)}"