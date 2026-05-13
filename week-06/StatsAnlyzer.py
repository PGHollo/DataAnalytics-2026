import statistics


def analyze_sales(sales):
    mean = statistics.mean(sales)
    median = statistics.median(sales)
    mode = statistics.mode(sales)
    stdev = statistics.stdev(sales)
    total = sum(sales)
    high = max(sales)
    low = min(sales)

    return mean, median, mode, stdev, total, high, low


analyst = input("Analyst name: ")
region = input("Region: ")

print("Enter daily sales for 7 days:")

sales = []

for day in range(1, 8):
    sale = float(input(f"Day {day}: $"))
    sales.append(sale)

mean, median, mode, stdev, total, high, low = analyze_sales(sales)

print(f"""
======= Weekly Sales Statistics Report =======

Analyst: {analyst}
Region: {region}
Data: {sales}

Total Revenue: ${total:.2f}
Mean Average: ${mean:.2f}
Median: ${median:.2f}
Mode: ${mode:.2f}
Standard Deviation: ${stdev:.2f}
Highest Day: ${high:.2f}
Lowest Day: ${low:.2f}

==============================================
""")