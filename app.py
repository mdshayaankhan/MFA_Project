from flask import Flask, render_template, request
from deepface import DeepFace
import cv2
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

def capture_live_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        img_path = "static/uploads/temp_login.jpg"
        cv2.imwrite(img_path, frame)
        cam.release()
        return img_path
    else:
        cam.release()
        raise Exception("Webcam not accessible")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    user_id = request.form["userid"]
    saved_img = f"static/uploads/{user_id}.jpg"

    try:
        live_img = capture_live_image()
        result = DeepFace.verify(img1_path=saved_img, img2_path=live_img)
        if result["verified"]:
            return render_template("result.html", message="Login Success ✅")
        else:
            return render_template("result.html", message="Face Not Verified ❌")
    except Exception as e:
        return render_template("result.html", message=f"Error: {str(e)}")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_id = request.form["userid"]
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Register - Press Space to Capture")

        while True:
            ret, frame = cam.read()
            if not ret:
                break
            cv2.imshow("Register - Press Space to Capture", frame)

            k = cv2.waitKey(1)
            if k % 256 == 32:  # SPACE pressed
                filename = f"static/uploads/{user_id}.jpg"
                cv2.imwrite(filename, frame)
                break

        cam.release()
        cv2.destroyAllWindows()
        return render_template("result.html", message=f"Registered {user_id} ✅")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
