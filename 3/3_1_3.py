from random import randint


class CustomList(list):
    def negativeCount(self):
        S = 0
        for i in self:
            if i < 0:
                S+=1
        return S

    def evenSum(self):
        S = 0
        for i in self:
            if i % 2 == 0:
                S+=i
        return S

    def maxIndex(self):
        return self.index(max(self))

    def evenPrint(self):
        for i in range(0, len(self), 2):
            print(f"a[{i}] = {self[i]}")

a = CustomList(randint(-150, 150) for _ in range(15))
print(a)
print(a.negativeCount())
print(a.evenSum())
print(a.maxIndex())
a.evenPrint()
