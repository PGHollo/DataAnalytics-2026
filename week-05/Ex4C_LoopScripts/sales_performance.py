"""Display sales records and identify top performers."""


def main():
    """Print each salesperson's monthly sales summary."""
    sales_data = [
        ("Marcus Webb", "East", 4250.00),
        ("Priya Sharma", "West", 5875.50),
        ("DeShawn Carter", "East", 3100.75),
        ("LaTonya Rivers", "South", 6420.00),
        ("Bob Nguyen", "West", 4980.25),
    ]

    total_sales = 0

    print("Monthly Sales Summary")
    print("---------------------")

    for name, region, sales in sales_data:
        print(f"{name} ({region}): ${sales:,.2f}")

        if sales > 5000:
            print(" ^ Top performer!")

        total_sales += sales

    print()
    print(f"Overall total sales: ${total_sales:,.2f}")


main()