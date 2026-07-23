import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)      # Speaking speed
engine.setProperty("volume", 1.0)    # Max volume

voices = engine.getProperty("voices")

# Select a female voice if available
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()