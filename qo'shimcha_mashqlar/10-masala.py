l = [1, False, 4.3, "salom dunyo", 4, True, "hello world", 6, 5, False, 3.2, "new year"]

s = []
for i in l:
    if isinstance(i, (int, float)):
        s.append(i)

s.sort()
print(s[len(s) - 3:])