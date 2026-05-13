class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity} units")

    def inventory_value(self):
        total = self.price * self.quantity
        print(f"Inventory Value: ${total:.2f}")
        print("-----------------------------")


products = []

for number in range(1, 3):
    print(f"\n=== Enter Product {number} ===")
    name = input("Product name: ")
    category = input("Category: ")
    price = float(input("Price $: "))
    quantity = int(input("Quantity: "))

    products.append(Product(name, category, price, quantity))


for number, product in enumerate(products, start=1):
    print(f"\n===== Product {number}: {product.name} =====")
    print(f"Product {number}: {product.name} {product.category}")

    product.display_info()
    product.inventory_value()