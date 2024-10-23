import os
import threading
import tkinter as tk
import requests
from datetime import datetime
from dotenv import load_dotenv
from PIL import Image, ImageTk
from voice_assistance import main as voice_assistant_main
from emotion_detection import run_emotion_detection
from play_music import play_audio
from get_news import get_news
from affirmations import get_affirmations
from text_to_speech import text_to_speech

# Load API keys from .env file
load_dotenv()

def start_voice_assistant():
    print("Starting Voice Assistant...")
    # Show "Listening..." label
    listening_label.config(text="Listening...")
    listening_label.update()

    def voice_assistant_thread():
        voice_assistant_main()
        # Hide "Listening..." label after completion
        listening_label.config(text="")

    threading.Thread(target=voice_assistant_thread).start()

def start_emotion_detection():
    print("Starting Emotion Detection...")
    threading.Thread(target=run_emotion_detection).start()

def start_music_player(emotion="neutral"):
    print(f"Playing music for emotion: {emotion}")
    threading.Thread(target=play_audio, args=(emotion,)).start()

def display_news():
    print("Fetching News...")
    # Hide affirmation label
    affirmation_label.config(text="")
    # Fetch and display news
    news = get_news()
    news_label.config(text=news)

def display_weather():
    print("Fetching Weather Data...")
    api_key = os.getenv("weather_api")
    city = "Cairns"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"].capitalize()
        }
        weather_message = (f"{weather_data['city']}: {weather_data['temperature']}°C,\n"
                           f"Feels like: {weather_data['feels_like']}°C,\n{weather_data['description']}")
        weather_label.config(text=weather_message)
    else:
        error_message = data.get("message", "Unable to fetch weather data.")
        print(f"Error: {error_message}")
        weather_label.config(text="Weather unavailable")
        text_to_speech("I'm sorry, I couldn't retrieve the weather data.")

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Update every second

def display_affirmation(emotion="neutral"):
    print("Displaying Affirmation...")
    # Hide news label
    news_label.config(text="")
    # Fetch and display affirmation
    affirmation = get_affirmations("affirmations_dataset.csv", emotion)
    affirmation_label.config(text=affirmation)

def main():
    root = tk.Tk()
    root.title("Smart Mirror Application")
    root.geometry("1200x800")
    root.configure(bg="black")

    # Top-left: Time and Weather
    global time_label, weather_label, listening_label
    time_label = tk.Label(root, font=("Arial", 16), fg="white", bg="black")
    time_label.place(x=20, y=20)
    weather_label = tk.Label(root, font=("Arial", 16), fg="white", bg="black")
    weather_label.place(x=20, y=50)
    update_time()
    display_weather()  # Initial call to display weather

    # Top-center: Logo
    logo_image = Image.open("jcu_logo.png")  # Replace with the path to your logo
    logo_image = logo_image.resize((250, 100), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg="black")
    logo_label.image = logo_photo  # Keep a reference
    logo_label.place(relx=0.5, y=20, anchor="n")

    # Center: News and Affirmation Displays
    global news_label, affirmation_label
    news_label = tk.Label(root, font=("Arial", 16), fg="white", bg="black", wraplength=600, justify="center")
    news_label.place(relx=0.5, rely=0.5, anchor="center")

    affirmation_label = tk.Label(root, font=("Arial", 16), fg="white", bg="black", wraplength=600, justify="center")
    affirmation_label.place(relx=0.5, rely=0.7, anchor="center")

    # Top-right: Listening Label (for voice assistant status)
    listening_label = tk.Label(root, font=("Arial", 16), fg="yellow", bg="black")
    listening_label.place(relx=0.8, rely=0.2, anchor="center")

    # Right side: Control Buttons
    button_frame = tk.Frame(root, bg="black")
    button_frame.place(relx=0.95, rely=0.5, anchor="e")

    voice_assistance_button = tk.Button(button_frame, text="Voice Assistant", font=("Arial", 14), command=start_voice_assistant)
    voice_assistance_button.pack(pady=10, anchor="e")

    emotion_button = tk.Button(button_frame, text="Emotion Detection", font=("Arial", 14), command=start_emotion_detection)
    emotion_button.pack(pady=10, anchor="e")

    music_button = tk.Button(button_frame, text="Play Music", font=("Arial", 14), command=lambda: start_music_player("happy"))
    music_button.pack(pady=10, anchor="e")

    news_button = tk.Button(button_frame, text="Display News", font=("Arial", 14), command=display_news)
    news_button.pack(pady=10, anchor="e")

    affirmation_button = tk.Button(button_frame, text="Show Affirmation", font=("Arial", 14), command=lambda: display_affirmation("happy"))
    affirmation_button.pack(pady=10, anchor="e")

    close_button = tk.Button(button_frame, text="Close Application", font=("Arial", 14), command=root.quit)
    close_button.pack(pady=10, anchor="e")

    root.mainloop()

if __name__ == "__main__":
    main()
