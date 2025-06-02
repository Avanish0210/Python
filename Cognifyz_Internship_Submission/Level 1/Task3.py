import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 1\Dataset .csv')

print("Dataset loaded successfully.")

# Count number of restaurants in each price range
price_range_counts = df['Price range'].value_counts().sort_index()
print("Price range counts calculated successfully.")
print(price_range_counts)

total_restaurants = len(df)
print("Total number of restaurants:", total_restaurants)

# Calculate percentage for each price range
price_percentages = (price_range_counts / total_restaurants * 100).round(2)
print("Price range percentages calculated successfully.")
print(price_percentages)

# Plotting the distribution
plt.figure(figsize=(10, 6))
plt.bar(price_range_counts.index, price_range_counts.values, color='skyblue')
plt.title('Distribution of Restaurants by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()