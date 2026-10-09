import cv2
from ultralytics import YOLO


def main():
    # Load the pretrained YOLO object detection model
    model = YOLO("yolo11n.pt")

    # Open the laptop webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Object Detection Started!")
    print("Press Q to quit.")

    while True:
        # Read one frame from the webcam
        success, frame = camera.read()

        if not success:
            print("Error: Could not read webcam frame.")
            break

        # Detect objects in the frame
        results = model(frame, conf=0.40, verbose=False)

        # Draw object labels and boxes on the frame
        annotated_frame = results[0].plot()

        # Display the result
        cv2.imshow("AI Real-Time Object Detection", annotated_frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera and close windows
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()