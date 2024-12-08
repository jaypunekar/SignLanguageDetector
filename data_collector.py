import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'ILoveYou', 'Please']

number_of_images = 5


def main():
    # Create label directories
    for label in labels:
        img_path = os.path.join(IMAGE_PATH, label)
        os.makedirs(img_path, exist_ok=True)  # Handle existing directory

    # Open camera
    try:
        cap = cv2.VideoCapture(1)
        if not cap.isOpened():
            print("Error opening camera!")
            return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    for label in labels:
        print(f"Collecting images for {label}")
        time.sleep(3)

        for imgnum in range(number_of_images):
            ret, frame = cap.read()
            if not ret:
                print("Error capturing frame!")
                continue

            imagename = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imagename, frame)

            print(f"Image {imgnum+1} captured for {label}")
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()