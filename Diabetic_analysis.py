# Diabetes Data Analysis Project
# By Priyanka Palai

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Basic Analysis
print("=== DIABETES DATA ANALYSIS ===")
print(f"Total Patients: {len(df)}")
print(f"Diabetic Patients: {df['Outcome'].sum()}")
print(f"Non-Diabetic Patients: {len(df) - df['Outcome'].sum()}")
print(f"Average Age: {df['Age'].mean():.2f}")
print(f"Average Glucose: {df['Glucose'].mean():.2f}")
print(f"Average BMI: {df['BMI'].mean():.2f}")
# Chart 1 - Pie Chart (Diabetic vs Non Diabetic)
labels = ['Non-Diabetic', 'Diabetic']
sizes = [500, 268]
colors = ['#66b3ff', '#ff6666']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Diabetic vs Non-Diabetic Patients')
plt.savefig('chart1_pie.png')
plt.show()
print("Chart 1 saved!")
# Chart 2 - Bar Chart (Average Glucose by Outcome)
plt.figure(figsize=(8,5))
sns.barplot(x='Outcome', y='Glucose', data=df, palette='coolwarm')
plt.title('Average Glucose Level - Diabetic vs Non-Diabetic')
plt.xlabel('Outcome (0 = Non-Diabetic, 1 = Diabetic)')
plt.ylabel('Average Glucose Level')
plt.savefig('chart2_bar.png')
plt.show()
print("Chart 2 saved!")
# Chart 3 - Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Outcome', bins=20, palette='coolwarm')
plt.title('Age Distribution - Diabetic vs Non-Diabetic')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.savefig('chart3_age.png')
plt.show()
print("Chart 3 saved!")