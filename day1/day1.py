import sys

D = open(sys.argv[1]).read().strip()
part_1 = 0
part_2 = 0

for line in D.split('\n'):
	part1_digits = []
	part2_digits = []
	for index1,cha in enumerate(line):
		if cha.isdigit():
			part1_digits.append(cha)
			part2_digits.append(cha)
		for index2,val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
			if line[index1:].startswith(val):
				part2_digits.append(str(index2+1))
	part_1 += int(part1_digits[0]+part1_digits[-1])
	part_2 += int(part2_digits[0]+part2_digits[-1])

print(part_1)
print(part_2)
