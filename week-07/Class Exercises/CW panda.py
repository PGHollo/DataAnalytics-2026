import pandas as pd

data = {
"Student":["Amy","Bob","Cara","Dan","Eva"],
"Score": [85,92,78,95,100]

}

df = pd.DataFrame(data)
print(df)
print()

print("SUM:", df["Score"].sum())
print("COUNT:", df["Score"].count())
print("MEAN:", df["Score"].mean())
print("MEDIAN:", df["Score"].median())
print("MIN:", df["Score"].min())
print("MAX:", df["Score"].max())

print("\nAggregate Results:")
print(df["Score"].agg(["sum","mean","median","min","max"]))

data = {
"Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
"Employee": ["Amy", "Bob", "Cara", "Dan", "Eva", "Frank"],
"Salary": [70000, 50000, 80000, 60000, 55000, 65000]
}

df2 = pd.DataFrame(data)
print(df2)

grouped = df2.groupby("Department")

print("SUM")
print(grouped["Salary"].sum())

print("\nMEAN")
print(grouped["Salary"].mean())

print("\nCOUNT")
print(grouped["Employee"].count())

print("\nMULTIPLE AGGREGATES")
print(grouped["Salary"].agg(["sum", "mean", "min", "max"]))
