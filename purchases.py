purchases = [
    {"item": "apple",  "category": "fruit",  "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit",  "price": 0.5, "quantity": 5},
    {"item": "milk",   "category": "dairy",  "price": 1.5, "quantity": 2},
    {"item": "bread",  "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(data):
    return sum(d["price"] * d["quantity"] for d in data)

def items_by_category(data):
    result = {}
    for d in data:
        result.setdefault(d["category"], set()).add(d["item"])
    return {k: sorted(v) for k, v in result.items()}

def expensive_purchases(data, min_price):
    return [d for d in data if d["price"] >= min_price]

def average_price_by_category(data):
    totals, counts = {}, {}
    for d in data:
        cat = d["category"]
        totals[cat] = totals.get(cat, 0) + d["price"]
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: round(totals[cat] / counts[cat], 2) for cat in totals}

def most_frequent_category(data):
    volumes = {}
    for d in data:
        volumes[d["category"]] = volumes.get(d["category"], 0) + d["quantity"]
    return max(volumes, key=volumes.get)

if __name__ == "__main__":
    min_price = 1.0

    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
