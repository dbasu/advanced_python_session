len_arr = int(input())
arr = input().split()
min = int(arr[0])
max = min
sum = min
for i in range(1, len_arr):
    x = int(arr[i])
    sum = sum + x
    if x < min:
        min = x
    if x > max:
        max = x
print('{:d} {:d}'.format(sum - max, sum - min))