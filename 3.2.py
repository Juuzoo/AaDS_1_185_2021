def fact(k):
    if k <= 1:
        return 1
    else:
        return k * fact(k-1)


def sum(n):
    s = 0
    for k in range(1, n+1):
        s += -1 * k * ((5-k)/fact(k))
    print('{:.2f}'.format(s))

sum(5)
