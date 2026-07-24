"""
Wake word detection using openWakeWord.

wait_for_wake_word() blocks until "Hey Jarvis" is heard, then
releases the microphone and returns. It does NOT keep listening
in the background — this keeps mic ownership simple: only one
component (wake word OR STT) ever holds the device at a time.
"""

from openwakeword.model import Model
from assistant.audio.mic_stream import MicStream


class WakeWordDetector:
    def __init__(
        self,
        model_name: str = "hey_jaarvis",
        threshold: float = 0.5,
        sample_rate: int = 16000,
    ):
        self.threshold = threshold
        self.model = Model(
            wakeword_models=[model_name],
            inference_framework="onnx",
        )
        self.mic = MicStream(sample_rate=sample_rate)

    def wait_for_wake_word(self) -> None:
        """Blocks until wake word detected. Releases mic before returning."""
        self.mic.start()
        print("[WakeWord] Listening for 'Hey Jarvis'...")
        try:
            for chunk in self.mic.frames():
                predictions = self.model.predict(chunk)
                for name, score in predictions.items():
                    if score > self.threshold:
                        print(f"[WakeWord] Detected '{name}' ({score:.2f})")
                        return
        finally:
            self.mic.stop()  # always release the mic, even on error