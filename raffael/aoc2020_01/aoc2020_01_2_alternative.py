import itertools

with open('aoc2020_01_input.txt', 'r') as f:
	numbers = [int(n) for n in f.read().split('\n') if n != '']

a, b, c = list(filter(lambda x: sum(x) == 2020, itertools.combinations(numbers, 3)))[0]
print(a * b * c)
