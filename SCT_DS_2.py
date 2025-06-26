# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style='whitegrid')

# Load the dataset
url = 'Titanic-Dataset.csv'
data = pd.read_csv(url)

# Display first and last 5 rows
print(data.head())
print(data.tail())

# Show all column names to avoid any typo issues
print("\nColumn names in the dataset:")
print(data.columns)

# Overview of dataset structure and datatypes
print("\nDataset Info:")
data.info()

# Summary statistics for numerical features
print("\nSummary Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Drop rows where 'Embarked' is missing
data.dropna(subset=['Embarked'], inplace=True)

# Handle 'Fare' outliers using IQR method
Q1 = data['Fare'].quantile(0.25)
Q3 = data['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['Fare'] >= lower_bound) & (data['Fare'] <= upper_bound)]

# Extract information from 'Cabin'
data['Has_Cabin'] = data['Cabin'].notnull().astype(int)
data.drop(columns=['Cabin'], inplace=True)

# Categorize passengers into age groups
data['Age_Group'] = pd.cut(
    data['Age'],
    bins=[0, 12, 18, 35, 60, np.inf],
    labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
)

# Show Age and Age Group
print(data[['Age', 'Age_Group']].head())

# Save cleaned data
data.to_csv('cleaned_titanic.csv', index=False)

# -------------------- EDA Visualizations --------------------

# Fare distribution boxplot
plt.figure(figsize=(8, 4))
sns.boxplot(x=data['Fare'])
plt.title("Fare Distribution")
plt.show()

# Check actual column names to avoid plotting error
print("\nUpdated Column Names:")
print(data.columns)

# Use correct column names (make sure 'Sex' and 'Survived' exist)
if 'Sex' in data.columns and 'Survived' in data.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Sex', hue='Survived', data=data)
    plt.title('Survival Count by Gender')
    plt.show()
else:
    print("Column 'Sex' or 'Survived' not found. Please check dataset.")

# Survival by Age Group
if 'Age_Group' in data.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Age_Group', hue='Survived', data=data)
    plt.title('Survival Count by Age Group')
    plt.show()
else:
    print("Column 'Age_Group' not found.")

# Correlation heatmap for numeric columns
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
