def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-9):  # Corrected range from (1, n-10) to (1, n-9)
            out *= i
    else:
        lim = n - 20
        out = sum(range(1, lim+1))  # Corrected calculation to sum the range from 1 to lim+1
    print(out)


n = int(input("Enter an integer: "))
compute(n)

