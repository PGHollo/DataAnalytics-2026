import pandas as pd

# Create DataFrame
df = pd.DataFrame ({
    "Student": ["Amy", "Bob", "Cara", "Dan"],
    "Score": [88, 95, 79, 91]
}, index=[3,1,2,0])

print("ORIGINAL DATAFRAME")
print(df)

# Sort by index
print("\nSORTED INDEX")
print(df.sort_index())

# Rank scores
df["Rank"] = df["Score"].rank(ascending=False)

print("\nWITH RANKINGS")
print(df)

print("\nSORTED INDEX (Highest to Lowest)")
sorted_df = df.sort_index(ascending=False)

print(sorted_df)

df["Rank"] = df["Score"].rank(ascending=False)
ranked_df = df.sort_values(by="Rank")
print("\nRANKINGS (Highest to Lowest)")
print(ranked_df)