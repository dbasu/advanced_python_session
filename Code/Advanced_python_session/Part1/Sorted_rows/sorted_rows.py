N, M = 5, 3
rows = [[10,  2,  5],
		[ 7,  1,  0],
		[ 9,  9,  9],
		[ 1, 23, 12],
		[ 6,  5,  9]]
K = 2


for row in sorted(rows, key=lambda row: row[K]):
    print(row)