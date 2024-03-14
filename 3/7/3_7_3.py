from random import choice

s = "qrstuvwxyz56789?!;"
print("".join(arr:=[choice(s) for _ in range(int(input("Длина массива = ")))]))

print("".join(["_" if i == "?" else i for i in arr]))