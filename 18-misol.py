s = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
i = 0
s2 = []

while i < 3:
    s2.append(s[i])
    i+=1

while i:
    s2.append(s[len(s) - i])
    i-=1

print(s2)
print(s2[::-1])