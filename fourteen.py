# Задача: Разворот целого числа (Reverse Integer)
# 📌 Условие:
# Дано целое число x. Необходимо развернуть его цифры. Если число становится больше 32-битного диапазона со знаком (-2³¹ до 2³¹ - 1), вернуть 0.

def reverseInteger(num: int) -> int:
    if num < -2 ** 31 or num > 2 ** 31 - 1:
        return 0

    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1]) * sign

    return reversed_num if -2 ** 31 <= reversed_num <= 2 ** 31 - 1 else 0


print(reverseInteger(100))  # 1
print(reverseInteger(-456))  # -654
print(reverseInteger(1534236469))  # 0 (слишком большое)
