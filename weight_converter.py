weight = int(input("Enter weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
	converter = weight * 0.45
	print(f"You are {converter} kilos")
else:
	converter = weight / 0.45
	print(f"You are {converter} pounds")

