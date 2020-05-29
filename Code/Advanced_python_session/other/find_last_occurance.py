x = raw_input()
y = x.split()
x = raw_input()
arr = x.split()
len_arr = int(y[0])
search_int = int(y[1])
found = -1
for i in range(len_arr):
    if int(arr[-i]) == search_int:
        found = len_arr -i
        break
    
print (found)