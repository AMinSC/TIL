alphabet = input()
END = len(alphabet) - 1
MID = alphabet[END // 2]

for i in alphabet:
    if i != alphabet[END]:
        print(0)
        break
    if i == MID:
        print(1)
        break
    END -= 1
