import re
n = int(input())
for i in range(n):
    name = input()
    matches_suvo = len(re.findall(r'SUVO', name))
    matches_suvojit = len(re.findall(r'SUVOJIT', name))
    print('SUVO = {:d}, SUVOJIT = {:d}'.format(matches_suvo - matches_suvojit, matches_suvojit))