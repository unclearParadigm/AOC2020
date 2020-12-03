with open('aoc2020_01_input.txt', 'r') as f: 
	numbers = [int(n) for n in f.read().split('\n') if n != '']

for n in numbers:
	for j in numbers:
		if n + j == 2020:
			print(n * j)