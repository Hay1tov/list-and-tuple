l = list([1,"salom dunyo",True, 1.2, "hello world", 3, False])
s = []
for i in l:
    if isinstance(i, str):
        if i.islower():
            s.append(i.upper())
        else:
            s.append(i)

print(s)   