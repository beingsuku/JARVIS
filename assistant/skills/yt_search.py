"""Skill: search YouTube — either show results, or auto-play the first result.

Uses yt-dlp's search extraction (ytsearch:) rather than scraping directly,
since yt-dlp is actively maintained and handles YouTube's page changes
far more reliably than raw scraping libraries.
"""

import webbrowser

import yt_dlp

_YDL_OPTS = {
    "quiet": True,
    "no_warnings": True,
    "extract_flat": "in_playlist",  # metadata only, don't resolve full video info
    "skip_download": True,
}


def _search_first_result(query: str):
    with yt_dlp.YoutubeDL(_YDL_OPTS) as ydl:
        info = ydl.extract_info(f"ytsearch1:{query}", download=False)
        entries = info.get("entries", [])
        if not entries:
            return None
        entry = entries[0]
        video_id = entry.get("id")
        title = entry.get("title", query)
        return f"https://www.youtube.com/watch?v={video_id}", title


def run(command: str) -> str:
    command = command.lower()

    # "play <query> on youtube" -> auto-play first result
    if "on youtube" in command:
        query = command.replace("play", "", 1).replace("on youtube", "").strip()

        if not query:
            return "What do you want me to play on YouTube?"

        try:
            result = _search_first_result(query)
        except Exception:
            return f"Something went wrong searching YouTube for {query}."

        if result is None:
            return f"I couldn't find anything for {query} on YouTube."

        video_url, title = result
        webbrowser.open(video_url)
        return f"Playing {title} on YouTube."

    # "search youtube for <query>" / "youtube search <query>" -> show results page
    for trigger in ["search youtube for", "youtube search for", "search youtube", "youtube search"]:
        if trigger in command:
            query = command.split(trigger, 1)[1].strip()
            if not query:
                return "What do you want me to search for on YouTube?"
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Searching YouTube for {query}."

    return "Say either 'play something on YouTube' or 'search YouTube for something'."