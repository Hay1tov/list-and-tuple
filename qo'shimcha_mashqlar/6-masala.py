t = list([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
n = 0
s = []

for i in t:
    length = len(t[n]) - 1
    s.append(t[n][length])
    n += 1
    
print(tuple(s))