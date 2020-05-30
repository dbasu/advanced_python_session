l0 = [1, 2, 3, 4]
l1 = [5, 6, 7, 8]
big_l = l0 + l1
print(big_l)
l2 = l1.copy()
l0.append(l1)
l2.extend(l1)
print(l0)
print(l2)

m1 = [l1 for _ in range(4)]
m2 = l1 * 4
print(m1)
print(m2)

l1
print(m1)
print(m2)


print(l1==l1[:])
print(l1[1:10])
# print(l1[10])
print(l1[1:10:2])
print(l2[-4::-2])
print(l2[-4:6:-1])





