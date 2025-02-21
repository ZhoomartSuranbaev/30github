# 2. Сжатие строки (Run-Length Encoding)
# 📌 Задача: Дан строка s, состоящая только из букв. Сожми её, заменяя повторяющиеся символы на букву + количество повторений.
def strCompress(s: str) -> str:
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))  # Добавляем последний символ
    return "".join(compressed)


print(strCompress("aaabbcddd"))  # ✅ "a3b2c1d3"
