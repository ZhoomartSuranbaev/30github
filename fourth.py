# Требуется:
# Рассчитать среднюю оценку по каждому предмету.
# Определить лучшего студента (у кого максимальный средний балл).
# Вывести список студентов, у кого хотя бы один предмет ниже 60 (не сдали).
# Отсортировать студентов по среднему баллу и вывести Топ-3.
students = {
    "Айбек": {"Математика": 75, "Физика": 80, "История": 90},
    "Алина": {"Математика": 90, "Физика": 85, "История": 95},
    "Бекзат": {"Математика": 82, "Физика": 78, "История": 88},
    "Диана": {"Математика": 95, "Физика": 92, "История": 89},
    "Ерлан": {"Математика": 60, "Физика": 65, "История": 70},
    "Жанна": {"Математика": 88, "Физика": 79, "История": 85},
    "Канат": {"Математика": 45, "Физика": 55, "История": 50},
    "Лейла": {"Математика": 100, "Физика": 98, "История": 99},
    "Медер": {"Математика": 55, "Физика": 60, "История": 65},
    "Нурбек": {"Математика": 78, "Физика": 82, "История": 80}
}

# 1. Рассчитать среднюю оценку по каждому предмету
subjects = ["Математика", "Физика", "История"]
average_scores = {subject: sum(st[subject] for st in students.values()) / len(students) for subject in subjects}

print("Средние оценки по предметам:")
for subject, avg in average_scores.items():
    print(f"{subject}: {avg:.2f}")

# 2. Определить лучшего студента
student_avg_scores = {name: sum(grades.values()) / len(grades) for name, grades in students.items()}
best_student = max(student_avg_scores, key=student_avg_scores.get)
print(f"\nЛучший студент: {best_student} (средний балл {student_avg_scores[best_student]:.2f})")

# 3. Вывести список студентов, у кого хотя бы один предмет ниже 60
failed_students = {name: {subj: score for subj, score in grades.items() if score < 60}
                   for name, grades in students.items() if any(score < 60 for score in grades.values())}

print("\nСтуденты, которые не сдали хотя бы один предмет:")
for name, failed_subjects in failed_students.items():
    failed_list = ", ".join(f"{subj} - {score}" for subj, score in failed_subjects.items())
    print(f"{name}: {failed_list}")

# 4. Отсортировать студентов по среднему баллу и вывести Топ-3
sorted_students = sorted(student_avg_scores.items(), key=lambda x: x[1], reverse=True)[:3]

print("\nТоп-3 студентов по среднему баллу:")
for i, (name, avg) in enumerate(sorted_students, 1):
    print(f"{i}. {name} - {avg:.2f}")

