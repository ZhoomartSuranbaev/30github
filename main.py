def inputData():
    print("Enter the name, age, location, and current balance (space-separated): ")
    data = input().split()
    return displayData(data)

def displayData(data):
    name = data[0]
    age = int(data[1])
    location = data[2]
    current_balance = float(data[3])

    year = 2025 + (100 - age)  # Год, когда исполнится 100 лет
    future_balance = current_balance * (1.05 ** (10 * 12))  # Сложные проценты за 10 лет

    print(f"Hello {name} from {location}!")
    print(f"In {year}, you will turn 100 years old.")
    print(f"If you save 5% of your current balance every month, in 10 years you will have ${future_balance:.2f}.")

inputData()
