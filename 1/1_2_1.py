def rec(S: int, i: int, st: str):
    if i == 6:
        ar = [S*6, S/6, S+6, S-6]
        if 35 in ar:
            st=st+str(ar.index(35)+1)
            return st
        else:
            return 
    return rec(S*i, i+1, st+"1"), rec(S/i, i+1, st+"2"), rec(S+i, i+1, st+"3"), rec(S-i, i+1, st+"4")
#1: *;  2: /; 3: +; 4: -;
print(rec(1, 2, ""))

