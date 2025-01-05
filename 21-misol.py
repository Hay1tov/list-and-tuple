text = text = input("matnni kiriting >> ")

text2 = text.split()

word = ''
for i in text2:
    word += i[0]

print(word)