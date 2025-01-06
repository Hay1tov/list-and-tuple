t = (1, 2, 3, 4, 5, 6, 7)

i = ""
o = 0 
for a in t:
    if o == 2 or o == 5:
        i += str(a)
    o += 1
    
print(i)