"""Skill: control system volume (Windows only, via pycaw)."""

from pycaw.pycaw import AudioUtilities


def _get_volume_interface():
    device = AudioUtilities.GetSpeakers()
    return device.EndpointVolume


def run(command: str) -> str:
    volume = _get_volume_interface()

    if "mute" in command:
        volume.SetMute(1, None)
        return "Muted."

    if "unmute" in command:
        volume.SetMute(0, None)
        return "Unmuted."

    if "up" in command or "increase" in command:
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(min(current + 0.5, 1.0), None)
        return "Volume increased."

    if "down" in command or "decrease" in command:
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(max(current - 0.5, 0.0), None)
        return "Volume decreased."

    return "Say volume up, volume down, mute, or unmute."