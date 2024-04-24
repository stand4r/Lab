# вариант 3
import time

def Reverse(n):
    n_str = str(n)
    reversed_n = int(n_str[::-1])
    return reversed_n

print(Reverse(17962))

start_time = time.time()

for _ in range(1000000):
    result = Reverse(17962)  
    
end_time = time.time()

print("Время выполнения:", end_time - start_time, "секунд")
