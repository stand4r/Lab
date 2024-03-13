def recursion(n, count, P):
    if n < P:
        print("Количество множителей:", count)
        if count==2:
            return "простое"
        else:
            return "не простое"
    if n%P == 0:
        count += 1
    P+=1
    return recursion(n, count, P)

N = 17

print(recursion(N, 0, 1))