num = range(5)
alp = map(chr, range(ord('a'),ord('e')))
alpbet = list(alp)
print(type(num))
print(type(alp))
print(type(enumerate(alp)))


for index, value in enumerate(alpbet):
    print(f'{index}: {value}')

for index in range(len(alpbet)):
	value = alpbet[index]
	print(f'{index}: {value}')





