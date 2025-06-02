import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset 
df=pd.read_csv(r'C:\Users\LENOVO\OneDrive\Documents\Python\Cognifyz_Internship_Submission\Level 2\Dataset .csv')

print("Dataset loaded successfully.")

# Drop rows with missing coordinates
geo_df = df[['Longitude', 'Latitude']].dropna()

# Plot geographic distribution
plt.figure(figsize=(10, 6))
plt.scatter(geo_df['Longitude'], geo_df['Latitude'], alpha=0.3, s=10, color='teal')
plt.title("Geographic Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()