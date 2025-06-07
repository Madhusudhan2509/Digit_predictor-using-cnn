# main.py
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('saved_model/mnist_cnn.h5')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    roi = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (28, 28))
    roi = roi.reshape(1, 28, 28, 1) / 255.0

    pred = np.argmax(model.predict(roi), axis=1)
    cv2.putText(frame, f'Predicted: {pred[0]}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    
    cv2.imshow('Live Classification', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
