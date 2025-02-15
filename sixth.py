# Рассчитать среднюю зарплату по каждому отделу (department).
# Найти самого высокооплачиваемого сотрудника.
# Сформировать список сотрудников старше 30 лет, отсортировав их по возрасту (по убыванию).
# Вывести 3 самых молодых сотрудников.

employees = [
    {"id": 1, "name": "Айбек", "age": 35, "salary": 1200, "department": "IT"},
    {"id": 2, "name": "Алина", "age": 29, "salary": 1500, "department": "HR"},
    {"id": 3, "name": "Бекзат", "age": 40, "salary": 2000, "department": "IT"},
    {"id": 4, "name": "Диана", "age": 25, "salary": 1000, "department": "Marketing"},
    {"id": 5, "name": "Ерлан", "age": 38, "salary": 1800, "department": "Finance"},
    {"id": 6, "name": "Жанна", "age": 32, "salary": 1700, "department": "HR"},
    {"id": 7, "name": "Канат", "age": 27, "salary": 900, "department": "Marketing"},
    {"id": 8, "name": "Лейла", "age": 45, "salary": 2200, "department": "IT"},
    {"id": 9, "name": "Медер", "age": 30, "salary": 1300, "department": "Finance"},
    {"id": 10, "name": "Нурбек", "age": 28, "salary": 1100, "department": "HR"},
]


def average_salary_by_department(employees):
    department_salaries = {}
    department_employees = {}
    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]
        if department in department_salaries:
            department_salaries[department] += salary
            department_employees[department] += 1
        else:
            department_salaries[department] = salary
            department_employees[department] = 1
    for department in department_salaries:
        department_salaries[department] /= department_employees[department]
    return department_salaries


def highest_paid_employee(employees):
    highest_paid = max(employees, key=lambda x: x["salary"])
    return highest_paid


def employees_over_30_sorted(employees):
    employees_over_30 = [employee for employee in employees if employee["age"] > 30]
    employees_over_30_sorted = sorted(
        employees_over_30, key=lambda x: x["age"], reverse=True
    )
    return employees_over_30_sorted


def display_youngest_employees(employees, n=3):
    employees_sorted = sorted(employees, key=lambda x: x["age"])
    for employee in employees_sorted[:n]:
        print(employee)


print("Средняя зарплата по отделам:", average_salary_by_department(employees))
print("Самый высокооплачиваемый сотрудник:", highest_paid_employee(employees))
print(
    "Сотрудники старше 30 лет (отсортированные по возрасту):",
    employees_over_30_sorted(employees),
)
print("3 самых молодых сотрудника:", display_youngest_employees(employees))
