str = input()
for c in str:
    c = ord(c)
    if 65 <= c <= 90:
        print(chr(c + 32), end="")
    else:
        print(chr(c - 32), end="")
print()