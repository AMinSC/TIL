from collections import Counter

string = list(map(str, str(input())))
string = [val.upper() for val in string]
string = Counter(string)

# print(max(string))
print(string)
# cnt = 0
# for i in arr:
#     if max(arr.values()) == arr[i]:
#         cnt += 1
# if 1 < cnt:
#     print("?")
# else:
#     print([key for key, val in arr.items() if val == max(arr.values())][0])