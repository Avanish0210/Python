import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 2\Dataset .csv')

print("Dataset loaded successfully.")

Aggregate_rating_data = df['Aggregate rating'].dropna()
print("Aggregate rating data extracted successfully.")
rating_count = Counter(Aggregate_rating_data)
common_rating = rating_count.most_common(10)
print("Most common ratings:", common_rating)


average_votes = round(df['Votes'].mean(), 2)
print("Average votes:", average_votes)

