from assistant.speaker import speak
from assistant.listener import listen

speak("Hello. I am Jarvis.")

while True:

    command = listen()

    if command == "":
        continue

    if "exit" in command:
        speak("Goodbye.")
        break

    speak(f"You said {command}")