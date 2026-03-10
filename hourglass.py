def hourglass():
    try:
        n = int(input("Чтобы нарисовать песочные часы,\nведите любое, желательно, нечетное число: "))
        if n >= 3:
            for i in range(0, n):
                for j in range(0, n):
                    if i == 0 or i == n-1 or j==i or j == n-i-1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
        elif 0 < n < 3:
            print("Заданное число слишком маленькое.")
        elif n < 0:
            print("Заданное число отрицательное, ничего не сработает")
    except ValueError:
        print("Заданное число не допустимо. Попробуйте еще раз.")

hourglass()