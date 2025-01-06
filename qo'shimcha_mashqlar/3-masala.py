t = [1, True, "salom dunyo", 3, False, 6, "hello world", 3.9, "uzbekistan", 1]

s = []
s += t[::3]

t = tuple(s)

print(f"1 -> {t.index(1)}")