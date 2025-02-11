lst = []
for i in range (1,4):
    lst.append(list(map(float, input(f'Введите оценки {i}-го студента через пробел: ').split())))

results = []
for i in lst:
    results.append(sum(i)/len(i))
print(f'Лучший студент: №{results.index(max(results)) + 1} со средним баллом {max(results)}')