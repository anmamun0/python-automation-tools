import cv2
import matplotlib.pyplot as plt

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame using matplotlib
    plt.imshow(frame)
    plt.show()

    # Save the frame to a file
    cv2.imwrite("captured_image.jpg", frame)

    # Wait for user input
    points = plt.ginput(1)
    if points:
        break

# When everything is done, release the capture
cap.release()
