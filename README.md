﻿# MFA_Project


python -m venv .venv

pip install deepface opencv-python flask numpy==1.26.4

mfa_project/
│
├── app.py              # Flask backend for login verification
├── register.py         # Captures face during registration
├── static/
│   └── uploads/        # Stores registered face images
├── templates/
│   ├── index.html      # Login page
│   ├── register.html   # Registration page
│   └── result.html     # Success/Failure page


pip install deepface opencv-python flask numpy==1.26.4

//pip uninstall numpy
//pip install numpy==1.26.4

pip install tensorflow-cpu==2.11.0

python app.py
