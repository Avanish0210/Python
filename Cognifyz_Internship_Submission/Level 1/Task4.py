import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 1\Dataset .csv')

print("Dataset loaded successfully.")

# 1. Count how many offer online delivery
online_delivery_counts = df['Has Online delivery'].value_counts()

# 2. Calculate percentages
total_restaurants = len(df)
online_yes = online_delivery_counts.get("Yes", 0)
online_no = online_delivery_counts.get("No", 0)

online_delivery_percentage = round((online_yes / total_restaurants) * 100, 2)
no_online_delivery_percentage = round((online_no / total_restaurants) * 100, 2)

print(f"Percentage with online delivery: {online_delivery_percentage}%")
print(f"Percentage without online delivery: {no_online_delivery_percentage}%")

# 3. Compare average ratings
avg_rating_online = round(df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean(), 2)
avg_rating_no_online = round(df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean(), 2)

print(f"Average rating (with online delivery): {avg_rating_online}")
print(f"Average rating (without online delivery): {avg_rating_no_online}")
