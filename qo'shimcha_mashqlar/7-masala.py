text = "Python anD data STRuctures are interesting!"

text_list = list(text)
lower = []

for alpha in text_list:
    if alpha.islower():
        lower.append(alpha)

print(lower)