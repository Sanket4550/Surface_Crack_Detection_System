# Industrial Surface Crack Detection Using CNN

## Overview

This project uses a Convolutional Neural Network (CNN) built with TensorFlow and Keras to detect cracks on industrial surfaces from images. It classifies images into two categories: Crack and NoCrack.

## Features

- Automated Crack Detection
- Image Preprocessing and Data Augmentation
- CNN Model Training
- Model Evaluation and Performance Analysis
- Confusion Matrix and Classification Report
- Prediction on New Images
- Model Checkpoint Saving

## Technologies Used

Python, TensorFlow, Keras, NumPy, Matplotlib, Scikit-learn, Pillow

## Dataset

The dataset contains two categories:

- `Positive/` – Images containing cracks.
- `Negative/` – Images without cracks.

Dataset split:

| Training | Validation | Testing |
|---|---|---|
| 70% | 15% | 15% |

## CNN Model Architecture

The CNN model consists of:

- Convolutional Layers (Conv2D)
- Batch Normalization
- Max Pooling
- Flatten Layer
- Dense Layers
- Dropout
- Sigmoid Output Layer

## Model Configuration

| Parameter | Value |
|---|---|
| Image Size | 128 × 128 |
| Batch Size | 32 (original configuration) |
| Epochs | 15 (original configuration) |
| Output Activation | Sigmoid |
| Classification | Binary |

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Execution

**Train the model:**

```bash
python Marvellous_CNN_Surface_Crack_Detection.py
```

**Predict on a new image:**

```bash
python Surface_Crack_Predict.py
```

## Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

## Output

- Best Trained Model
- Final CNN Model
- Model Evaluation Results
- Crack / NoCrack Predictions

## Future Improvements

- Real-Time Crack Detection
- Streamlit GUI Integration
- Model Optimization
- Cloud Deployment

## Disclaimer

This project is developed for educational purposes. Predictions should be verified before use in actual industrial quality-control applications.
