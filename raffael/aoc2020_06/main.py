import functools

with open('aoc2020_06_input.txt', 'r') as f:
    data = f.read().split('\n')

p1, p2 = 0, 0
q_set = set()
q_buf = []

for line in data:
    if line != '':
        q_set.update(set(line))
        q_buf.append(set(line))
    else:
        p1 += len(q_set)
        p2 += len(functools.reduce(lambda q1, q2: q1 & q2, q_buf))
        q_set.clear()
        q_buf.clear()

print('Part 1: ', p1)
print('Part 2: ', p2)
