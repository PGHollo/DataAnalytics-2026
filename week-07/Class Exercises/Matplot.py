import matplotlib.pyplot as plt

# 1. Data
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [1200, 1500, 1100, 1800]

# 2. Create chart
plt.plot(months, sales)

# 3. Add labels and title
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# 4. Show chart
plt.show()

# Bar chart
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [1200, 1500, 1100, 1800]

plt.bar(months, sales)


plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()