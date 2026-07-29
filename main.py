from assistant.speaker import speak
from assistant.listener import listen
from assistant.audio.wake_word import WakeWordDetector
from assistant.brain.processor import process
 

detector = WakeWordDetector()

speak("Hello. I am Jarvis.")

while True:

    detector.wait_for_wake_word()
    speak("Yes?")

    while True:
        command = listen()

        if command == "":
            continue

        if "exit" in command:
            speak("Going to sleep.")
            break

        response = process(command)
        speak(response)