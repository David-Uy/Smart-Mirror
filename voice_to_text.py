# voice_to_text.py

import speech_recognition as sr
from text_to_speech import text_to_speech

def speech_to_text():
    """
    Listens for speech input from the user and converts it to text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        text_to_speech("How can I assist you?")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            text_to_speech("Sorry, I didn't catch that. Could you repeat?")
            return ""
        except sr.RequestError as e:
            text_to_speech("There seems to be a problem with the speech recognition service.")
            print(f"Request error from Google Speech Recognition service; {e}")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

if __name__ == "__main__":
    response = speech_to_text()
    print("Received input:", response)

