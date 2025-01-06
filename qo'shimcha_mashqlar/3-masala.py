l = [1, True, "salom dunyo", 3, False, 6, "hello world", 3.9, "uzbekistan", 1]

new_l = []
new_l += l[::3]

t = tuple(new_l)

print(f"1 -> {t.index(1)}")