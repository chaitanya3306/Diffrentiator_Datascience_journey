# Week 4 — Prerequisites & Recap Checklist

Welcome! This README covers what you need before starting Week 4 of this machine learning course, featuring technical skills, mindset prep, and dataset setup. Follow this checklist for a strong start.

---

## ✅ Technical Prerequisites

### Python & Libraries
- You should already be comfortable with:
  - pandas
  - numpy
  - matplotlib
  - seaborn

- **Core skills:**
  - Data cleaning, preprocessing, and transformation
  - Handling missing values
  - Categorical data encoding
  - Feature scaling and selection

- **Required libraries:**  
  Run this before starting:
pip install scikit-learn matplotlib seaborn numpy pandas


### Math & Stats Basics
- Statistics: mean, median, mode, variance, standard deviation
- Probability: basics, independent/conditional events
- Linear Algebra (conceptual): vectors, matrices
- Calculus (basic intuition): slope/rate of change (for regression)

---

## ✅ Mindset Preparation

- ML ≠ just code:  
Be ready to solve problems with data, not just write scripts.
- Focus areas:
- Use train/test splits instead of "fit all data"
- Evaluate models with multiple metrics (don’t just look at accuracy)
- Compare different models to understand why one outperforms another

---

## ✅ Dataset Setup

- Start with sample datasets:
- load_boston (regression)
- load_iris (classification)
- load_digits (classification)

Example usage:

from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target


- Real-world mini-project dataset:
- Titanic (classification) — available via Kaggle or seaborn:
  ```
  import seaborn as sns
  titanic = sns.load_dataset("titanic")
  ```
- California Housing (regression)

---

## ✅ Skills to Revise Before Week 4

- Loading datasets (with pandas/sklearn)
- Exploratory Data Analysis (EDA):
- Data shape, info, describe
- Null/missing values
- Data preprocessing:
- Scaling, encoding, handling nulls
- Review your Week 3 Feature Engineering notes — remember: good features = half of ML success!

---

## 📦 Ready to Start?

- Check your environment and skills
- Install necessary packages
- Review dataset loading and EDA
- Refresh feature engineering concepts

Happy Learning! 🚀


