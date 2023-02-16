string = list(map(str, str(input())))
for idx, val in enumerate(string):
    if 97 <= ord(val) <= 122:
        string[idx] = chr(ord(val) - 32)
arr = {}
for i in set(string):
    arr[i] = string.count(i)
cnt = 0
for i in arr:
    if max(arr.values()) == arr[i]:
        cnt += 1
if 1 < cnt:
    print("?")
else:
    print([key for key, val in arr.items() if val == max(arr.values())][0])