name = input()
number = int(input())
print("Группа №", number // 100, ".", sep="")
print(number % 10, ". ", name, ".", sep="")
print("Шкафчик: ", number, ".", sep="")
print("Кроватка: ", (number % 100) // 10, ".", sep="")