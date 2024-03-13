from random import randint


class CustomList(list):
    def count3(self):
        S = 0
        for i in self:
            if i % 3 == 0:
                S+=1
        return S

    def positiveSum(self):
        S = 0
        for i in self:
            if i > 0:
                S+=i
        return S

    def maxIndex(self):
        return self.index(max(self))

    def evenPrint(self):
        for i in range(0, len(self), 2):
            print(f"a[{i}] = {self[i]}")

a = CustomList(randint(-150, 150) for _ in range(15))
print(a)
print(a.count3())
print(a.positiveSum())
print(a.maxIndex())
a.evenPrint()