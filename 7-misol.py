l = [("salom", 2, 2.1, True),("hello world", 2, 2.0, 2),("hello", True, "Max", 12)]

temp = list(l[0])
temp[2] = "change"
l[0] = tuple(temp)
print(l[0][2])
