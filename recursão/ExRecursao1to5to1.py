def printn(n):
    if n >= 1:
        print(n)
        printn(n-1)
        if n != 1:
            print(n)
n = 5
printn(n)