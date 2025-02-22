n = int(input())
total = n
if n <= 0:
    print(1, end="")
else:
    while n > 1:
        total = total * (n-1)
        n -= 1
    print(total, end="")