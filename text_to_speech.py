# text_to_speech.py
import pyttsx3


def text_to_speech(text):
    """
    Converts the given text to speech.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use voices[1] or adjust based on preference
    engine.setProperty('rate', 150)  # Set speech speed
    engine.setProperty('volume', 1.0)  # Set volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text_to_speech("Hello! I am your smart mirror assistant.")
