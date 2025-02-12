import random

names = ["Айбек", "Алина", "Бекзат", "Диана", "Ерлан", "Жанна", "Канат", "Лейла", "Медер", "Нурбек",
         "Омар", "Пери", "Рустам", "Саида", "Тимур", "Улан", "Фариза", "Хан", "Чолпон", "Ширин"]

country_codes = ["+996", "+998", "+777", "+374", "+992", "+993"]

contacts = [
    (random.choice(names), random.choice(country_codes) + str(random.randint(1000000, 9999999)))
    for _ in range(100)
]

kg_contacts = [contact for contact in contacts if contact[1].startswith("+996")]
kg_contacts_sorted = sorted(kg_contacts, key=lambda x: x[0])

print("\nКыргызские контакты (отсортированные по имени):")
for name, number in kg_contacts_sorted:
    print(f"{name}: {number}")
