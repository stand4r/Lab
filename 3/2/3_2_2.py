from random import randint
def rotate_right(lst) -> list:
    lst.insert(0, lst.pop())
    return lst

arr = [randint(1, 9) for _ in range(10)]
print(arr)
print(rotate_right(arr))