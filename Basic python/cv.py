import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break  # if frame not captured, exit loop

    cv2.imshow("my cam", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
