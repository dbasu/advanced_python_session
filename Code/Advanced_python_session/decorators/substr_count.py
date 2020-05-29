from functools import lru_cache

@lru_cache(maxsize=256)
def tokenize(left, right):
    if left == right:
        return [s[right]]
    else:
        _substr = tokenize(left, right-1).copy()
        _substr.extend([s[start:(right+1)] for start in range(left, right+1) if s[start:right+1] not in _substr])
        return _substr 

if __name__ == '__main__':
	s = 'aabaa'
	for q in [(1,1),(1,4),(1,1),(1,4),(0,2)]:
		print(len(tokenize(q[0], q[1])))
	print(tokenize.cache_info())


