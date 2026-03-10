cols = 9
rows = 7

for i in range(0, rows):
    for j in range(0, cols):
        if i == 0:
            if j == 1 or j == 2 or j == 6 or j == 7:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 1:
            if j == 4:
                print(" ", end="")
            else:
                print("*", end="")
        elif i == 2 or j >= i - 2 and j <= rows + 3 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

