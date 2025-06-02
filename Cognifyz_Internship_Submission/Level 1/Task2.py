import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 1\Dataset .csv')

print("Dataset loaded successfully.")

# 1. City with the highest number of restaurants
city_counts = df['City'].value_counts()
print("City counts calculated successfully.")
highest_restaurants_city = city_counts.idxmax()
highest_restaurants_count = city_counts.max()
print('City with the highest number of restaurants:', highest_restaurants_city)
print('Number of restaurants in', highest_restaurants_city, ':', highest_restaurants_count)

# 2. Average rating per city
group_data = df.groupby('City')
average_rating_per_city = group_data['Aggregate rating'].mean()
print("Average rating per city calculated successfully.")
# Sort the result in descending order
average_rating_by_city = average_rating_per_city.sort_values(ascending=False)


#city with the highest rating
highest_rating_city = average_rating_by_city.idxmax()
highest_avg_rating_value = round(average_rating_by_city.max(), 2)
print(f"City with the highest average rating: {highest_rating_city} (Rating: {highest_avg_rating_value})")