"""
Shared microphone audio stream.
Used by wake word detection (Stage 2) and later by STT (Stage 3),
so both stages consume the same raw audio source instead of
fighting over the microphone device.
"""

import queue
from typing import Generator

import numpy as np
import sounddevice as sd


class MicStream:
    """Continuously captures microphone audio in fixed-size chunks."""

    def __init__(self, sample_rate: int = 16000, chunk_size: int = 1280):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self._audio_queue: "queue.Queue[np.ndarray]" = queue.Queue()
        self._stream: sd.InputStream | None = None

    def _callback(self, indata, frames, time_info, status):
        if status:
            print(f"[MicStream] status: {status}")
        # Copy is required: sounddevice reuses the buffer
        self._audio_queue.put(indata.copy().flatten())

    def start(self) -> None:
        self._stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self.chunk_size,
            callback=self._callback,
        )
        self._stream.start()

    def stop(self) -> None:
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None

    def frames(self) -> Generator[np.ndarray, None, None]:
        """Yields audio chunks as they arrive. Blocks until stream is started."""
        while True:
            yield self._audio_queue.get()