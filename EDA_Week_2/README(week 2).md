# 🛒 Week 2 Retail Dataset (Modified for Advanced EDA)

## 📌 Overview  
This dataset is part of my **12-Week Differentiator Data Science Journey**.  
It is a **modified version** of the original Week 2 Retail dataset to simulate **real-world messy data**.  
The modifications allow practicing **data cleaning, EDA, and preprocessing** at a professional level.

---

## 🔍 Modifications Introduced  
To make the dataset more realistic, the following changes were applied:  
1. **Missing Values** — Introduced `NaN` in random places across numeric and categorical columns.  
2. **Duplicate Rows** — Added duplicate records for testing deduplication techniques.  
3. **Outliers** — Created extreme values in `Sales`, `Discount`, and `Profit` columns to practice outlier detection and handling.  
4. **String Inconsistencies** — Added inconsistencies in `Region` and `Category` (e.g., extra spaces, different casing, typos).  

---

## 📂 Columns  
- **Order ID** – Unique ID for each order  
- **Order Date** – Date of order (contains inconsistencies and missing values)  
- **Region** – Region name (contains inconsistencies)  
- **Category** – Product category (contains inconsistencies)  
- **Sales** – Sales amount (contains outliers)  
- **Discount** – Discount percentage (contains outliers)  
- **Profit** – Profit amount (contains outliers)  

---

## 🎯 Objective  
The purpose of this dataset is to:  
- Practice **data cleaning techniques** (handling missing values, fixing strings, removing duplicates).  
- Apply **EDA techniques** (detecting patterns, relationships, and anomalies).  
- Simulate **real-world messy dataset challenges** faced by top data scientists.

---

## 🚀 How to Use  
1. **Load the dataset**  
```python
import pandas as pd
df = pd.read_csv('Week2_Retail_Dataset_Modified.csv')
