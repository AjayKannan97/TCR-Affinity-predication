# TCR Affinity Prediction

## Overview

This repository contains the implementation of a TCR-Epitope Binding Affinity Prediction model using Few-Shot Learning. The project focuses on enhancing the accuracy of predicting TCR (T-cell receptor) binding affinities using contrastive loss in a Siamese Network framework.

### Features

Few-Shot Learning Approach: Utilizes a Siamese network to predict TCR-epitope affinity with limited labeled data.

Contrastive Loss Optimization: Improves model performance by better distinguishing between similar and dissimilar TCR-epitope pairs.

Data Preprocessing: Handles sequence alignment and feature extraction for TCR and epitope representations.

Evaluation Metrics: Uses accuracy, precision, recall, and F1-score to assess the model’s performance.

Visualization: Plots embedding spaces and affinity score distributions for insights.

### Project Structure

├── data/                 # Preprocessed TCR-epitope dataset
├── models/               # Implementation of Siamese Network with contrastive loss
├── notebooks/            # Jupyter notebooks for EDA and model training
├── scripts/              # Utility scripts for data processing and model evaluation
├── results/              # Performance metrics and visualization outputs
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies

## Installation

### Clone the repository:

git clone https://github.com/AjayKannan97/TCR-Affinity-predication.git
cd TCR-Affinity-predication

### Create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### Install dependencies:

pip install -r requirements.txt

## Usage

### Train the Model:

python scripts/train_model.py --epochs 50 --batch_size 32

### Evaluate the Model:

python scripts/evaluate.py --model_path models/best_model.pth

Run Exploratory Data Analysis (EDA):
Open and run notebooks/EDA.ipynb in Jupyter Notebook.

### Results

The model demonstrated a 30% improvement in prediction accuracy over traditional approaches by leveraging Few-Shot Learning with contrastive loss. More details can be found in the results/ directory.

### References

Contrastive Loss in Siamese Networks - Used for learning discriminative TCR-epitope embeddings.

Few-Shot Learning Techniques - Helps in learning with limited labeled data.

TCR Binding Prediction Literature - Incorporates domain-specific knowledge in immunoinformatics.

### Contact

For queries or collaborations, feel free to reach out:

Author: Ajay Kannan

Email: ajaykannan@gmail.com

LinkedIn: [Ajay Kannan](https://www.linkedin.com/in/ajay-kannan-34a04013b/)
