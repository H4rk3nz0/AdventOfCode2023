import sys
import numpy

few_set = {}

for line in open(sys.argv[1],'r').read().split('\n')[:-1]:
	game_split = line.split(':')
	game_id = game_split[0][5:]

	game_rounds = game_split[1].strip().split(';')
	game_rounds = [game.strip() for game in game_rounds]

	rgb = [0] * 3

	for game in game_rounds:

		gaame = map(lambda x: x.split(' '), game.split(', '))

		for block in gaame:
			block_dict = {block[1]: int(block[0])}
			for set in block_dict:
				match set:
					case 'red':
						if (rgb[0] < block_dict[set]):
							rgb[0] = block_dict[set]
					case 'green':
						if (rgb[1] < block_dict[set]):
							rgb[1] = block_dict[set]
					case 'blue':
						if (rgb[2] < block_dict[set]):
							rgb[2] = block_dict[set]

	few_set[game_id] = numpy.prod(rgb)

print(few_set)

total = 0
for set in few_set:
	total += few_set[set]

print(total)
