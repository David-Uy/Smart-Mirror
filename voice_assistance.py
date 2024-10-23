# app_voice_assistant.py

import os
from api_key import API_KEY
from langchain_community.llms import OpenAI
from text_to_speech import text_to_speech
from voice_to_text import speech_to_text
import time

def main():
    # Set the OpenAI API key
    os.environ['OPENAI_API_KEY'] = API_KEY
    llms = OpenAI(temperature=0.9)

    print("Voice Assistant: Say 'bye' to end the conversation.")
    while True:
        prompt = speech_to_text()  # Capture voice input

        if not prompt:  # Skip if no input detected
            print("No input detected. Waiting for user input...")
            continue

        if "bye" in prompt.lower():  # Exit condition
            text_to_speech("Goodbye! Have a great day!")
            break

        try:
            # Generate response from OpenAI
            openai_response = llms.invoke(prompt)
            print("Voice Assistant:", openai_response)
            text_to_speech(openai_response)  # Speak the response
        except Exception as e:
            print(f"An error occurred with OpenAI API: {e}")
            text_to_speech("I'm sorry, I'm having trouble responding right now. Please try again.")

        # Small delay to avoid overlapping commands
        time.sleep(1)

if __name__ == "__main__":
    main()
