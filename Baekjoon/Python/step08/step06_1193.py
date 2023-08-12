denominator = int(input())

molecule = 1

while denominator > molecule:
    denominator -= molecule
    molecule += 1

if molecule % 2 == 0:
    print(f"{denominator}/{molecule + 1 - denominator}")
else:
    print(f"{molecule - denominator + 1}/{denominator}")
