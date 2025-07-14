# 🚢 Titanic Dataset – Exploratory Data Analysis (EDA)

This repository contains my submission for **Task 02** of the **SkillCraft Technology Internship**, which focuses on **data cleaning and exploratory data analysis (EDA)** using the classic Titanic dataset from Kaggle.

---

## 📌 Objective

- Perform data cleaning and transformation
- Explore patterns and relationships between features
- Visualize survival trends based on demographics and ticketing details

---

## 🧰 Tools & Libraries

- Python 🐍  
- pandas  
- numpy  
- matplotlib  
- seaborn  

---

## 📁 Dataset

- Source: [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
- File: `Titanic-Dataset.csv`

---

## 🔍 Data Cleaning Steps

1. Dropped rows with missing values in the **`Embarked`** column.
2. Handled outliers in the **`Fare`** column using **IQR** method.
3. Created new feature **`Has_Cabin`** to indicate presence of cabin info.
4. Categorized passengers into **`Age_Group`**:
   - `Child`: 0–12  
   - `Teen`: 13–18  
   - `Young Adult`: 19–35  
   - `Adult`: 36–60  
   - `Senior`: 60+

---

## 📊 EDA Visualizations

- 📦 **Boxplot** of `Fare` distribution
- 👩‍🦱 **Survival count by Gender**
- 👶 **Survival count by Age Group**
- 🔥 **Correlation heatmap** of numeric features

All visuals are generated using **Seaborn** and **Matplotlib** with proper formatting and labels.

---

## 📸 Sample Outputs

| Plot | Description |
|------|-------------|
| 🎯 Boxplot | Outlier detection for fare |
| 📊 Countplot | Gender-wise survival analysis |
| 🧒 Age Group Plot | Age group and survival comparison |
| 🔥 Correlation Heatmap | Insight into inter-feature relationships |

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/titanic-eda-skillcraft.git
cd titanic-eda-skillcraft
