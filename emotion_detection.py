# emotion_detection.py
import time

import cv2
from deepface import DeepFace
from play_music import play_audio
from affirmations import get_affirmations


def detect_faces_and_expressions(frame):
    result = DeepFace.analyze(img_path=frame, actions=['emotion'], enforce_detection=False)

    # Check if result is a list or a dictionary
    if isinstance(result, list):
        # Assuming the list contains one dictionary result
        result = result[0]

    # Now extract the dominant emotion
    dominant_emotion = result.get('dominant_emotion', None)

    if dominant_emotion:
        return dominant_emotion
    else:
        print("No dominant emotion detected.")
        return "neutral"  # Return a default emotion if detection fails


def run_emotion_detection():
    print("Starting Emotion Detection...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        # Detect emotion
        emotion = detect_faces_and_expressions(frame)
        # print(f"Detected Emotion: {emotion}")

        # time.sleep(2)

        # Display emotion on frame
        cv2.putText(frame, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion Detection', frame)


        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_emotion_detection()
