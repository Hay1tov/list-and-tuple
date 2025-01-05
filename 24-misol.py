list_1 = [(1, 0, 2), (0, 3, 5), (0, 3, 4), (1, 0, 3), (0, 6, 3)]

tuples_1 = []

for tuples in list_1:
    tuples_1.append([element for element in set(tuples)])

elements = [element for lists in tuples_1 for element in lists]

for i in set(elements):
    if elements.count(i) == len(list_1):
        print(i)