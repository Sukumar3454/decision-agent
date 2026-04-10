import json
import random

products = []

for i in range(1, 101):
    product = {
        "product": f"Product {i}",
        "revenue": random.randint(20000, 100000),
        "growth_rate": random.randint(5, 20),
        "cost": random.randint(10000, 80000),
        "customer_satisfaction": random.randint(60, 95)
    }
    products.append(product)

with open("data/products.json", "w") as f:
    json.dump(products, f, indent=4)

print("100 products generated ✅")