from itertools import groupby
inp_str = '1222311'
print(*[(len(list(c)), int(k)) for k, c in groupby(inp_str)])

for k, c in groupby(inp_str):
	print(k)
	print(list(c))