# Industrial_Surface_Crack_Detection_System

## About the Project

Industrial Surface Crack Detection is a deep learning project that uses a **Convolutional Neural Network (CNN)** to identify cracks on industrial surfaces from images.

The model classifies input images into two categories:

- **Crack:** The image contains a visible surface crack.
- **NoCrack:** The image does not contain a visible surface crack.

The main objective is to automate surface defect detection using computer vision and deep learning techniques.

## Project Objectives

- Detect cracks on industrial surfaces using image classification.
- Build and train a CNN model using TensorFlow and Keras.
- Apply image preprocessing and data augmentation.
- Evaluate model performance using test data.
- Predict whether a new input image contains a crack.

## Technologies Used

- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow, Keras
- **Numerical Computing:** NumPy
- **Data Visualization:** Matplotlib
- **Model Evaluation:** Scikit-learn
- **Image Processing:** Pillow (PIL)

## Project Structure

```text
Industrial_Crack_Detection/
│
├── CrackDataset/
│   ├── Positive/
│   └── Negative/
│
├── Processed_CrackDataset/
│   ├── train/
│   │   ├── Crack/
│   │   └── NoCrack/
│   │
│   ├── validation/
│   │   ├── Crack/
│   │   └── NoCrack/
│   │
│   └── test/
│       ├── Crack/
│       └── NoCrack/
│
├── Input_Images/
│
├── CNN_Surface_Crack_Detection.py
├── Surface_Crack_Predict.py
├── requirements.txt
└── README.md
```
**Note:** `Processed_CrackDataset/` and `CrackDataset/`cannot be added because of large size.
**Note:** `Processed_CrackDataset/` is generated automatically by the training script. `Input_Images/` is an optional folder for testing new images.

## Dataset

The original dataset contains two categories:

- `Positive/` – Images containing surface cracks.
- `Negative/` – Images without surface cracks.

The dataset is divided into three parts:

| Dataset | Percentage |
|---|---:|
| Training | 70% |
| Validation | 15% |
| Testing | 15% |

In my reported dataset run, there were 40,000 images in total:

- 20,000 positive images.
- 20,000 negative images.

The actual number of images may vary depending on the dataset used.

## CNN Model Architecture

The project uses a Convolutional Neural Network to learn visual features from industrial surface images.

## Model Training

The training script performs the following operations:

1. Loads crack and non-crack images.
2. Splits the dataset into training, validation, and testing sets.
3. Preprocesses images.
4. Applies image augmentation.
5. Builds the CNN architecture.
6. Trains the model.
7. Monitors validation performance.
8. Evaluates the model using test data.
9. Generates a confusion matrix and classification report.
10. Saves the trained model.

### Saved Models

The training script saves:

- `Best_Crack_Detection_Model.keras`
- `Final_Crack_Detection_Model.keras`

The final model is saved when the training script reaches its final saving statement. If training is interrupted, this file may not be created or updated.

## Installation and Setup

### 1. Install Python

Install a compatible Python version on your system.

Check the installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd Surface_Crack_Detection_System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Required Libraries

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Train the Model

Run the training script:

```bash
python Marvellous_CNN_Surface_Crack_Detection.py
```

Allow training to finish so that the final model can be saved.

## Predict on New Images

To classify a new industrial surface image:

1. Place the image inside the `New_Images/` folder.
2. Open `Surface_Crack_Predict.py`.
3. Set the image path and model path correctly.
4. Run the prediction script.

```bash
python Surface_Crack_Predict.py
```

The prediction script loads the trained model, preprocesses the input image, and predicts whether it contains a crack.

### Image Preprocessing

The prediction image must use the same preprocessing as the training images:

- Resize to 128 × 128 pixels.
- Convert the image into a numerical array.

### Class Label Mapping

The training output reported the following class mapping:

```python
{'Crack': 0, 'NoCrack': 1}
```

For a sigmoid output:

- Prediction greater than 0.5 → NoCrack
- Prediction less than or equal to 0.5 → Crack

Always verify the class mapping if the dataset folder order changes.

## Model Evaluation

The model is evaluated using a separate test dataset.

The evaluation includes:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

Actual evaluation results should be added here after a completed training run.

## Conclusion

This project demonstrates how deep learning and computer vision can be applied to industrial surface defect detection.

Using a CNN built with TensorFlow and Keras, the system learns image features and classifies industrial surface images into crack and non-crack categories.

The project provides practical experience with image preprocessing, CNN architecture design, model training, evaluation, and image prediction.

## Disclaimer

This project is developed for educational and experimental purposes.
