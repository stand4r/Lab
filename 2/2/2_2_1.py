def rec(num, step):
    if step == 1:
        return num
    return a * rec(num, step-1)
    
a = int(input("a = "))
n = int(input("n = "))
print(f"{a}**{n} = ", rec(a, n))