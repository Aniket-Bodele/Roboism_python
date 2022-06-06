def test(lis):
    l = []
    for i in range(len(lis)):
        l.append(lis.count(lis[i]))

    index = l.index(max(l))
    return lis[index]


l = [1, 2, 3, 2, 2, 3, 2, 3, 5]
print(test(l))

l = [2, 3, 3, 8, 3, 6, 8, 8, 8]
print(test(l))