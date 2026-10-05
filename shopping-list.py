shopping_list = [
    {"item": "Notebook", "price": 150, "purchased": True},
    {"item": "Pen", "price": 30, "purchased": True},
    {"item": "USB Drive", "price": 900, "purchased": False},
]

still_need = [item["item"] for item in shopping_list if not item["purchased"]]
remaining_cost = sum(item["price"] for item in shopping_list if not item["purchased"])

print("Still need to buy:", still_need)
print("Remaining cost:", remaining_cost)