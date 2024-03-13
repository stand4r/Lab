def Sum(S, n):
    if n >= 100:
        return S
    S+=n+1
    return Sum(S, n+1)
print(Sum(10, 10))