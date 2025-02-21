def multiply(a:int, b:int) -> int:
    result = 0
    if a > 0 and b > 0 or a < 0 and b < 0:
        for _ in range(abs(b)):
            result += a
        return result
    else:
        for _ in range(abs(b)):
            result += a
        return -result

a = int(input('a:'))
b = int(input('b:'))
print(f'a * b = {multiply(a,b)}')