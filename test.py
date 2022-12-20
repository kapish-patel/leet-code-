a = [1, 5, 3, 7, 3, 8, 6, 4, 6, 2, 7, 9, 4, 5, 2, 5, 0]
temp = []
for i in range(len(a)):
    if a[i] in temp:
        print(f"Found duplicate at {i} and value is: {a[i]}")
    if a[i] not in temp:
        temp.append(a[i])
