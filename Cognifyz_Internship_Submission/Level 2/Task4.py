import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 2\Dataset .csv')

print("Dataset loaded successfully.")

# Count restaurant occurrences by name
restaurant_counts = df['Restaurant Name'].value_counts()

# Filter those appearing more than once (chains)
chains = restaurant_counts[restaurant_counts > 1]

# Display top chains
print("Top Restaurant Chains:")
print(chains.head(10))

# Filter original data for just chains
chain_data = df[df['Restaurant Name'].isin(chains.index)]

# Analyze average rating and total votes per chain
chain_summary = chain_data.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',
    'Votes': 'sum',
    'Restaurant ID': 'count'
}).rename(columns={'Restaurant ID': 'Total Outlets'})

# Round the rating
chain_summary['Aggregate rating'] = chain_summary['Aggregate rating'].round(2)

# Sort by total outlets
chain_summary = chain_summary.sort_values(by='Total Outlets', ascending=False)

print("\nChain Analysis (Top 10):")
print(chain_summary.head(10))
