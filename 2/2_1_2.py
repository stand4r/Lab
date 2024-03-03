from time import perf_counter
def NumberOfOdds(n: int) -> int:
    S = 0
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 1:
            S+=1
    return S

start = perf_counter()
for _ in range(1_000_000):
    NumberOfOdds(223_234_234)
print(NumberOfOdds(223_234_234))
end = perf_counter()

print("Время выполнения: ", round(end-start, 2), "с")

