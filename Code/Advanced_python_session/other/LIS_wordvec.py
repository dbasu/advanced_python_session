def differByOne(word1,word2):
	subsequence = True
	for c in word1:
		if c not in word2:
			subsequence = False
			break
	return subsequence
			

def longest_chain(w):
    words = {}
    for i in range(len(w)):
        if w[i] not in words:
            words[w[i]] = True
    print(words)
    sol = [1 for i in range(len(w))]
    w.sort(key=lambda s: len(s))
    # print(w)
    for i in range(len(w)):
    	maxcnt = 0
    	for j in range(i):
    		if len(w[i]) - len(w[j]) == 1:
    			if differByOne(w[j],w[i]):
    				maxcnt = max(maxcnt, sol[j])
    	sol[i] = 1 + maxcnt
    return max(sol)
    

a = ["a", "b", "bda", "ba", "bca",  "bdca"] # longest chain is 4
a.sort(key = lambda s: len(s))
print (longest_chain(a))