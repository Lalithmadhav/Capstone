# Hybrid CNN-RNN for Handwritten Text Recognition (HTR)

## Project Overview
A deep learning pipeline designed to recognize and transcribe handwritten text from images. This project implements a hybrid architecture combining **Convolutional Neural Networks (CNN)** for feature extraction and **Recurrent Neural Networks (RNN)** with LSTMs for sequence modeling.

## Tech Stack
* **Language:** Python
* **Deep Learning:** TensorFlow/Keras
* **Numerical Processing:** NumPy, Pandas
* **Computer Vision:** OpenCV

## Architecture Details
1. **Feature Extraction:** A multi-layer CNN to capture spatial features of characters.
2. **Sequence Mapping:** A Bridge layer to reshape CNN output for sequential processing.
3. **Temporal Modeling:** Bi-directional LSTMs to capture context from both directions of the text.
4. **Loss Function:** CTC Loss for training on unaligned sequence data.

## Key Achievements
* **Built from Scratch:** Implemented the data pipeline and model architecture without high-level automated wrappers.
* **Preprocessing Pipeline:** Developed custom scripts for noise reduction and image normalization to improve OCR accuracy.
* **Generalization:** Designed to handle various handwriting styles by resizing and grayscaling the images.
