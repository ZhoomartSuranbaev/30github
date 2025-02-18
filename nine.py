import json

# Данные для записи
data = [
    {"id": 1, "name": "Айбек", "age": 25, "city": "Бишкек"},
    {"id": 2, "name": "Алина", "age": 22, "city": "Ош"},
    {"id": 3, "name": "Бекзат", "age": 30, "city": "Нарын"}
]

# Записываем в файл
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Данные записаны в data.json")

# Читаем JSON
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("Считанные данные:", loaded_data)

# Добавляем нового человека
new_person = {"id": 4, "name": "Диана", "age": 28, "city": "Талас"}
loaded_data.append(new_person)

# Перезаписываем файл
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(loaded_data, file, ensure_ascii=False, indent=4)

print("Добавлена Диана. JSON обновлён!")
