dot1 = {3, 8, 6, 15, 42, 1, 31, 9, 67, 74}
dot2 = {'key1': [], 'key2': []}
for i in dot1:
    if i <= 10:
        dot2['key1'].append(i)
    else:
        dot2['key2'].append(i)
print(dot2)
