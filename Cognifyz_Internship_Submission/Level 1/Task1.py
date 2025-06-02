# Level 1 - Task 1: Top Cuisines
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 1\Dataset .csv')

print("Dataset loaded successfully.")
cuisine_data = df['Cuisines'].dropna()
print("Cuisines data extracted successfully.")

# Count the occurrences of each cuisine
cuisine_counts = Counter(cuisine_data)
top_cuisines = cuisine_counts.most_common(3)
print("Top 3 cuisines:", top_cuisines)

total_restaurants = len(cuisine_data)
print("Total number of restaurants:", total_restaurants)

# Calculate percentage for each top cuisine
top_3_percentages = [(cuisine, round(count / total_restaurants *100, 2)) for cuisine, count in top_cuisines]
print("Top 3 cuisines with percentages:", top_3_percentages)
