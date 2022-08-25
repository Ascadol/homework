# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів.
# На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.


def first(a, b):
    c = a ** 2 + b
    return (c)


def second(a, b):
    d = b ** 2 + a
    return (d)


print("Введіть числа a i b")
a = float(input("Введіть ціле число a: "))
b = float(input("Введіть ціле число b: "))

x_1 = first(a, b)
print(x_1)

x_2 = second(a, b)
print(x_2)

sort_list = [x_1, x_2]
sort_list.sort()
minimum = sort_list[0]
maximum = sort_list[-1]

if minimum < -5 or maximum > 5:
    print("Результат поза діапазоном (-5 : 5)")
else:
    while minimum < maximum:

        print(minimum)
        minimum += 0.5 # трохи мозок вивіхнув, поки додумався = поставити xD











