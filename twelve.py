# 3. Два числа дают сумму (Two Sum)
# 📌 Задача: Дан список чисел nums и число target. Найди два индекса, сумма элементов которых равна target.
def twoSum(target:int, numbers:list) :
    for i in range(len(numbers)):
        if target - numbers[i] in numbers:
            return [numbers.index(numbers[i]), numbers.index(target - numbers[i], numbers.index(numbers[i]) + 1)]
print(twoSum(6, [3, 3, 4]))

def TwoSum(target: int, numbers: list):
    seen = {}  # {число: индекс}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Возвращаем индексы найденной пары
        seen[num] = i  # Запоминаем текущий элемент
    return []  # Если пары нет

print(TwoSum(9, [2, 7, 11, 15]))
