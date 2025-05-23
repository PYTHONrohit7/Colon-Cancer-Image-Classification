# 🧬 Colon Cancer Image Classification

This project is part of **ICAIMLH** at online mode. It builds an end-to-end machine learning system to classify histopathology images of colon cells into:

The dataset is a prepared version of the **CRCHistoPhenotypes** dataset.

---

## 📁 Project Structure

├── mainData.csv # Label data for 60 patients

├── extraData.csv # Label data for 39 patients (isCancerous only)

├── images/ # Folder containing 27x27 RGB colon cell images

├── model_isCancerous.py # Python script for binary classification

├── README.md # Project documentation

├── requirements.txt # List of required packages

# How to Run

## STEPS:

**Clone the repository**
```bash
git clone https://github.com/PYTHONrohit7/Colon-Cancer-Image-Classification.git
```
... *navigate into the cloned repository directory* ...

# STEP 01- Create a conda environment after opening the repository
```bash
conda create -n cnncls python=3.8 -y
```
*Then activate evn *
```bash
conda activate cancer
```
# STEP STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
**Note:**

1.  I used the repository URL from the second image (`PYTHONrohit7/Colon-Cancer-Image-Classification.git`).
2.  I added the `git clone` command, as just the URL isn't executable.
3.  I added a placeholder comment about navigating into the directory, which is usually the next implicit step after cloning.
4.  I kept the structure and commands exactly as shown in the second image otherwise.
