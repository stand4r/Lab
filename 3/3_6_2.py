s = input("Введите фразу: ")
st = ""
m = 0
m_st = ""
for i in s:
    if i != " ":
        st += i
    else:
        if len(st) > m:
           m = len(st)
           m_st = st
        st = ""
if len(st) > m:
    m = len(st)
    m_st = st

print(f"Самое длинное слово: {m_st}\nДлина слова: {m}")

