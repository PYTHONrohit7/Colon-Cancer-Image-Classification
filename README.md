# 🧬 Colon Cancer Image Classification

This project is part of **COSC2673 Assignment 2** at RMIT University. It builds an end-to-end machine learning system to classify histopathology images of colon cells into:

- **Cancerous vs Non-Cancerous** (binary classification)
- **Cell Type** (e.g., fibroblast, epithelial, inflammatory) *(optional extension)*

The dataset is a prepared version of the **CRCHistoPhenotypes** dataset.

---

## 📁 Project Structure

. ├── mainData.csv # Label data for 60 patients ├── extraData.csv # Label data for 39 patients (isCancerous only) ├── images/ # Folder containing 27x27 RGB colon cell images ├── model_isCancerous.py # Python script for binary classification ├── README.md # Project documentation ├── requirements.txt # List of required packages