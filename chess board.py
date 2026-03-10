n = 5
counter = 1

for i in range(0, n):
    for j in range(0, n):
        if i % 2 == 0 and j % 2 == 0:
            print("*", end=" ")
        elif i % 2 != 0 and j % 2 != 0:
            print("*", end=" ")
        else:
            print(f"{counter}", end=" ")
            counter += 1
    print()  