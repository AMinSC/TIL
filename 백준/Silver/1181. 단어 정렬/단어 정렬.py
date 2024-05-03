char_set = set()
for _ in range(int(input())):
    char_set.add(input())
char_set = sorted(char_set, key=lambda x: (len(x), x))
for c in char_set:
    print(c)