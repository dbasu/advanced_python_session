#Crating two lists
l0 = [1, 2, 3, 4]
l1 = [5, 6, 7, 8]
# Joining two lists
print('List 0 = ' + str(l0))
print('List 1 = ' + str(l1))
big_l = l0 + l1
print('List 0 + List 1 = ' + str(big_l))
# changing big_l does not change the merged lists
big_l[0] = 5
print('List 0 = ' + str(l0))


# Difference Between Extend and append
l2 = l0.copy()

l0.append(l1)
l2.extend(l1)
print('List 0 .apend( List 1)= ' + str(l0))
print('List 0 .extend( List 1)= ' + str(l2))

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





