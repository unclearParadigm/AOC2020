import time

begin = time.time()

with open('aoc2020_03_input.txt', 'r') as f:
    game_map = [line * 100 for line in f.read().split('\n') if line != '']

tree_map = []
for y_index, _ in enumerate(game_map):
    for x_index, position_value in enumerate(game_map[y_index]):
        if position_value == '#':
            tree_map.append((x_index, y_index))


def count_hits_for_angle(delta_x, delta_y):
    hit_counter = 0
    previous_x_index = 0
    for y in range(0, len(game_map), delta_y):
        for x in range(previous_x_index, len(game_map[0]), delta_x):
            if (x, y) in tree_map:
                hit_counter += 1
            previous_x_index += delta_x
            break
    return hit_counter


part1 = count_hits_for_angle(3, 1)
part2 = count_hits_for_angle(1, 1) \
        * part1 * count_hits_for_angle(5, 1) \
        * count_hits_for_angle(7, 1) \
        * count_hits_for_angle(1, 2)

print("Part 1: ", part1)
print("Part 2: ", part2)
print("Both parts took: {0}s".format(time.time() - begin))

