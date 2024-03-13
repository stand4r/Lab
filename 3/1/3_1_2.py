from random import randint


class CustomList(list):
    def positiveCount(self):
        S = 0
        for i in self:
            if i > 0:
                S+=1
        return S

    def negativeSum(self):
        S = 0
        for i in self:
            if i < 0:
                S+=i
        return S

    def minIndex(self):
        return self.index(min(self))

    def evenPrint(self):
        for i in range(1, len(self), 2):
            print(f"a[{i}] = {self[i]}")

a = CustomList(randint(-100, 100) for _ in range(15))
print(a)
print(a.positiveCount())
print(a.negativeSum())
print(a.minIndex())
a.evenPrint()