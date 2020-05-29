
from itertools import combinations 
def func_str(s):
	n = len(s)
	p = len(set(s))
	return (n ** p) % 1000000007
def sum_substr(s):
	x = sum([func_str(s[i:j]) for i, j in combinations(range(len(s) + 1), r = 2)])
	x += len(set(s))
	return x
def all_substr(s):
	return [s[i:j] for i, j in combinations(range(len(s) + 1), r = 2)]

print([(i,j) for i, j in combinations(range(2 + 1), r=2)])
print(sum_substr('aa'))