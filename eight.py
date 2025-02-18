# Прочитай файл и преобразуй данные в список словарей (orders).
# Посчитай общую сумму заказов по каждому статусу (delivered, pending, canceled).
# Определи клиента с наибольшей суммой доставленных заказов.
# Найди три самых дорогих заказа.
# Запиши результат в новый файл orders_report.txt
orders = []
with open('orders_txt_8.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst = line.strip().split(',')
        ix_dict = {
            'id': lst[0],
            'customer': lst[1],
            'amount': float(lst[2]),  # Преобразуем в число
            'status': lst[3]
        }
        orders.append(ix_dict)

# Подсчёт общей суммы заказов по статусам
amount_delivered = sum(order['amount'] for order in orders if order['status'] == 'delivered')
amount_pending = sum(order['amount'] for order in orders if order['status'] == 'pending')
amount_canceled = sum(order['amount'] for order in orders if order['status'] == 'canceled')

# Определяем клиента с наибольшей суммой доставленных заказов
customer_totals = {}
for order in orders:
    if order['status'] == 'delivered':
        customer_totals[order['customer']] = customer_totals.get(order['customer'], 0) + order['amount']

max_customer = max(customer_totals, key=customer_totals.get)  # Клиент с макс. суммой доставленных заказов
max_customer_amount = customer_totals[max_customer]

# Три самых дорогих заказа
top_orders = sorted(orders, key=lambda x: x['amount'], reverse=True)[:3]

# Запись в файл
with open('orders_report.txt', 'w', encoding='utf-8') as f:
    f.write(f'Сумма заказов по каждому статусу:\n')
    f.write(f'delivered: {amount_delivered}\n')
    f.write(f'pending: {amount_pending}\n')
    f.write(f'canceled: {amount_canceled}\n\n')

    f.write(f'Клиент с наибольшей суммой доставленных заказов: {max_customer} ({max_customer_amount})\n\n')

    f.write('Три самых дорогих заказа:\n')
    for order in top_orders:
        f.write(
            f'ID: {order["id"]}, Customer: {order["customer"]}, Amount: {order["amount"]}, Status: {order["status"]}\n')
