
# Real-Time Object Classification using CNN


---

#Project Structure

```
Real-Time-Digit-CNN
 model.py         # Trains and saves MNIST CNN model
 main.py          # Real-time digit prediction from webcam
 saved_model/
 mnist_cnn.h5 # Trained CNN model
 requirements.txt # Python dependencies
 README.txt        # This file
```

---

Features

-Digit recognition (0-9) using webcam input
-Trained CNN model on MNIST dataset
-Real-time prediction and visualization

---


### 1. Clone the repo

```bash
git clone https://github.com/your-username/real-time-digit-cnn.git
cd real-time-digit-cnn

### 2. Install dependencies

```bash
pip install -r requirements.txt

If `requirements.txt` is missing, manually install:

```bash
pip install numpy tensorflow opencv-python matplotlib

---

### 3.Train the CNN

To train a digit recognition CNN using the MNIST dataset:

```bash
python model.py
```

This will generate a file `saved_model/mnist_cnn.h5`.

---

### 4.Run Real-Time Digit Recognition

After training:

```bash
python main.py

Draw a number on a white paper and hold it up to your webcam.
The predicted digit will be printed live.

---

