n = 4
row = 1

while row <= n:
    # 1. Inner loop for leading spaces
    space = 1
    while space <= (n - row):
        print(" ", end=" ")
        space += 1

    # 2. Inner loop for ascending numbers
    num = 1
    while num <= row:
        print(num, end=" ")
        num += 1

    # 3. Inner loop for descending numbers
    num = row - 1
    while num >= 1:
        print(num, end=" ")
        num -= 1

    print()  # Move to the next line
    row += 1
