import streamlit as st
import numpy as np
import cv2
from keras.models import load_model

# Load model
model = load_model('saved_model/mnist_cnn.h5')

st.title("Real-Time Digit Recognition using CNN")

run = st.checkbox('Run Webcam')
FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(gray, (28, 28))
    roi = roi.astype("float32") / 255.0
    roi = roi.reshape(1, 28, 28, 1)

    prediction = model.predict(roi)
    digit = np.argmax(prediction)

    # Display digit on frame
    cv2.putText(frame, f'Predicted: {digit}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Convert BGR to RGB and display
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

cap.release()
