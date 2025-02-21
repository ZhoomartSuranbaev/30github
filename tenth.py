#1. Уникальные элементы списка
#Задача: Дан список чисел nums. Верни новый список, в котором удалены все дубликаты, но порядок сохранён.
def remove_duplicates(nums:list)->list:
    result =[]
    for i in nums:
        if i not in result:
            result.append(i)
    return result

nums = [4, 2, 2, 3, 1, 4, 5, 1]
result = remove_duplicates(nums)
print(f'список, в котором удалены все дубликаты, но порядок сохранён: {result}')


