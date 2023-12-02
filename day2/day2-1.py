import sys

red = 12
green = 13
blue = 14

working_games = []

for line in open(sys.argv[1],'r').read().split('\n'):
	works = 1
	game_split = line.split(':')
	game_id = game_split[0][4:]
	if len(game_split) <= 1: continue

	game_rounds = game_split[1].strip().split(';')

	for game in game_rounds:
		if works == 0: continue
		game = game.strip()
		game_dict = dict(map(lambda x: x.split(' '), game.split(', ')))
		game_dict = {v: int(k) for k, v in game_dict.items()}
		for set in game_dict:
			match set:
				case 'red':
					if game_dict[set] > red:
						works = 0
				case 'blue':
					if game_dict[set] > blue:
						works = 0
				case 'green':
					if game_dict[set] > green:
						works = 0

	if works:
		working_games.append(game_id.strip())


total = 0
for val in working_games:
	total += int(val)

print(total)
