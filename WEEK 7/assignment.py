# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Use seaborn style for better aesthetics
sns.set(style="whitegrid")

# Error handling when loading dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset file not found. Please check the path.")
except Exception as e:
    print("An error occurred while loading the dataset:", e)

# Preview dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# Example of handling missing values (not needed for iris, but included for instructions)
if df.isnull().values.any():
    df.fillna(df.mean(), inplace=True)
    print("Missing values handled by filling with column mean.\n")

# Map target column to species names for readability
df["species"] = df["target"].map(dict(zip(range(3), iris.target_names)))


# Task 2: Basic Data Analysis

# Basic statistics
print("\nBasic Statistics of Numerical Columns:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby("species").mean()
print("\nMean values grouped by species:")
print(grouped)

print("\nObservations:")
print("- Setosa species has smaller petal size compared to Versicolor and Virginica.")
print("- Virginica species generally has the largest petal and sepal measurements.")


# Task 3: Data Visualization

# 1. Line chart – show sepal length trend (index as pseudo-time)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="green")
plt.title("Line Chart: Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart – average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="viridis")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram – distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=12, color="skyblue", edgecolor="black")
plt.title("Histogram: Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot – sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# 5. Box plot – petal width distribution by species
plt.figure(figsize=(8,5))
sns.boxplot(x="species", y="petal width (cm)", data=df, palette="Set2")
plt.title("Box Plot: Petal Width Distribution by Species")
plt.xlabel("Species")
plt.ylabel("Petal Width (cm)")
plt.show()          

