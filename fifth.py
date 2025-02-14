orders = [
    {"id": 101, "customer": "Айбек", "amount": 2500, "status": "delivered"},
    {"id": 102, "customer": "Алина", "amount": 5000, "status": "pending"},
    {"id": 103, "customer": "Бекзат", "amount": 3200, "status": "delivered"},
    {"id": 104, "customer": "Диана", "amount": 1500, "status": "canceled"},
    {"id": 105, "customer": "Ерлан", "amount": 4200, "status": "pending"},
    {"id": 106, "customer": "Жанна", "amount": 1800, "status": "delivered"},
    {"id": 107, "customer": "Канат", "amount": 6000, "status": "canceled"},
    {"id": 108, "customer": "Лейла", "amount": 7000, "status": "delivered"},
]

# 1. Посчитать сумму заказов по статусам
delivered_sum = sum(order["amount"] for order in orders if order["status"] == "delivered")
pending_sum = sum(order["amount"] for order in orders if order["status"] == "pending")
canceled_sum = sum(order["amount"] for order in orders if order["status"] == "canceled")

print(f"Sum of delivered: {delivered_sum}")
print(f"Sum of pending: {pending_sum}")
print(f"Sum of canceled: {canceled_sum}")

# 2. Найти клиента с наибольшей суммой доставленных заказов
from collections import defaultdict

customer_totals = defaultdict(int)
for order in orders:
    if order["status"] == "delivered":
        customer_totals[order["customer"]] += order["amount"]

best_customer = max(customer_totals, key=customer_totals.get)
print(f"Customer with max delivered amount: {best_customer} (${customer_totals[best_customer]})")

# 3. Отфильтровать и отсортировать pending-заказы
pending_orders = sorted(
    [order for order in orders if order["status"] == "pending"], 
    key=lambda x: x["amount"], 
    reverse=True
)
print("Pending orders sorted by amount:", pending_orders)

# 4. Вывести топ-3 самых дорогих заказов
top3_orders = sorted(orders, key=lambda x: x["amount"], reverse=True)[:3]
print("Top 3 most expensive orders:", top3_orders)
