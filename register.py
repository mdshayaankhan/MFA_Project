import cv2
import os


def register_user(user_id):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Register Face")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Register Face", frame)

        k = cv2.waitKey(1)
        if k % 256 == 32:  # SPACE pressed
            img_name = f"static/uploads/{user_id}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"[INFO] Saved face for user: {user_id}")
            break

    cam.release()
    cv2.destroyAllWindows()

# Example usage:
# register_user("john")
