# play_music.py

import pygame


def play_audio(emotion):
    """
    Plays an audio file corresponding to the specified emotion.
    """
    pygame.init()
    mixer = pygame.mixer
    mixer.init()

    # Dictionary with paths to the audio files based on emotions
    audio_files = {
        "happy": "songs/Bruno Mars - The Lazy Song (Official Music Video).mp3",
        "sad": "songs/Maroon 5 - Payphone ft. Wiz Khalifa (Explicit) (Official Music Video).mp3",
        "angry": "songs/The Kid LAROI, Justin Bieber - STAY (Official Video).mp3",
        "neutral": "songs/Lil Nas X - Old Town Road (Official Video) ft. Billy Ray Cyrus.mp3",
        "surprise": "songs/Maroon 5 - Sugar (Official Music Video).mp3",
    }

    # Get the file to play; default to 'neutral' if emotion is not recognized
    file_to_play = audio_files.get(emotion, audio_files["neutral"])

    # Load and play the audio file
    mixer.music.load(file_to_play)
    mixer.music.play()

    # Keep playing until the song finishes
    while mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    mixer.quit()


if __name__ == "__main__":
    play_audio("happy")
