# affirmations.py

import pandas as pd
import random


def load_data(file_path="affirmations_dataset.csv"):
    """
    Loads the affirmations dataset from a CSV file.
    """
    return pd.read_csv(file_path)


def get_affirmations(file_path, emotion_tag):
    """
    Retrieves a random affirmation based on the specified emotion tag.
    """
    data = load_data(file_path)

    # Filter rows based on the emotion tag/category
    filtered_data = data[data["Category"].str.lower() == emotion_tag.lower()]

    if not filtered_data.empty:
        # Pick a random affirmation from the filtered rows
        affirmation = random.choice(filtered_data["Affirmation"].tolist())
        return affirmation
    else:
        return "Stay positive and keep going!"


if __name__ == "__main__":
    print(get_affirmations("affirmations_dataset.csv", "happy"))
