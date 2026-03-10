number = int(input("Введите ваше число: "))
print(f"number = {number:0b}")  # number = 101

x = int(input("Введите число, которое нужно зашифровать: "))
key = int(input("Введите ключ: "))
encrypt = x ^ key
print(f"Зашифрованное число: {encrypt:0b}")
decrypt = encrypt ^ key
print(f"Расшифрованное число: {decrypt}")

x = 9  # 1001
y = 5  # 0101
x = x ^ y
y = x ^ y
x = x ^ y

print(f"x = {x}")  # x = 5
print(f"y = {y}")  # y = 9