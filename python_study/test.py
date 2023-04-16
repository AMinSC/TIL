clothes = ["skirt", "red sock", "blue sock"]
newClothes = []
for clothing in clothes:
    if "sock" in clothing:
        print("Appending:", clothing)
        newClothes.append(clothing)

print(newClothes)
clothes.extend(newClothes)
print(clothes)

clothes2 = ["skirt", "red sock", "blue sock"]
newClothes = []
for clothing in clothes2:
    if "sock" in clothing:
        print("Appending:", clothing)
        clothes2.append(clothing)
        break

print(clothes2)
