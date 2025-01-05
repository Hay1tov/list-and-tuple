l = [23, 1, 45, -54, -5456 -56.56, True, False, "Salom dunyo"]
l_musbat = []

for i in l:
    if isinstance(i, int) and i > 0:
        l_musbat.append(i)
print(l_musbat)