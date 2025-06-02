import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 2\Dataset .csv')
print("Dataset loaded successfully.")

# Keep only relevant columns and remove rows with missing cuisines
df_cuisine = df[['Cuisines', 'Aggregate rating']].dropna()

# Count most common cuisine combinations
top_combinations = df_cuisine['Cuisines'].value_counts().head(10)
print("\nTop 10 Most Common Cuisine Combinations:")
print(top_combinations)

# Calculate average rating for each of these combinations
avg_ratings = df_cuisine.groupby('Cuisines')['Aggregate rating'].mean()

# Create a summary DataFrame with count and average rating
summary_df = pd.DataFrame({
    'Count': top_combinations,
    'Average Rating': avg_ratings[top_combinations.index].round(2)
}).reset_index().rename(columns={'index': 'Cuisine Combination'})

# Display the summary
print("\nTop Cuisine Combinations with Average Ratings:")
print(summary_df)
