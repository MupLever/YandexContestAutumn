def closeness(arr1, arr2, rgr):
    while rgr >= 0 and arr1[rgr] != arr2[rgr]:
        rgr -= 1
    return rgr + 1

def exp_search(arr1, arr2) -> int:
    if arr1[0] != arr2[0]:
        return 0

    min_size = min(len(arr1), len(arr2))
    rgr = 1
    while (rgr < min_size and arr1[rgr] == arr2[rgr]):
        rgr = rgr << 1
    if rgr > min_size - 1:
        rgr = min_size - 1

    return closeness(arr1, arr2, (rgr + 1) >> 1)
    
array_count = int(input())
array_of_arrays = []
for _ in range(array_count):
    _ = input()
    array_of_arrays.append(list(map(int, input().split(' '))))
    
sum = 0

for i in range(len(array_of_arrays)):
    for j in range(i + 1, len(array_of_arrays)):
        sum += exp_search(array_of_arrays[i], array_of_arrays[j])
print(sum)
