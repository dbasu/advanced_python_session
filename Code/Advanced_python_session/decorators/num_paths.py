from functools import lru_cache

@lru_cache(maxsize=64)
def count_path(i, j):
	if (i == 1) or (j==1):
		return 1
	else:
		return count_path(i-1, j) + count_path(i, j-1)

def test():
	return (count_path(8,8), 2*count_path(4,5))
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1000))
    print(test())

