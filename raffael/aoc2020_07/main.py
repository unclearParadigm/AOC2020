import time


class Bag(object):
    def __init__(self, color: str, quantity: int = 0) -> None:
        self.quantity = int(quantity)
        self.quantity_carrying = 0
        self.contents = []
        self.color = str(color)

    def __repr__(self):
        return self.color

    def contains(self, bag_to_search, root_bags: list) -> bool:
        if len(self.contents) == 0:
            return bag_to_search.color == self.color

        for b, q in self.contents:
            rbs_without_b = list(filter(lambda ib: ib.color != b.color, root_bags))
            if b.contains(bag_to_search, list(filter(lambda ib: ib.color != b.color, rbs_without_b))):
                return True
            if len([rb for rb in root_bags if rb.color == b.color and rb.contains(bag_to_search, rbs_without_b)]) > 0:
                return True

    def count_contains(self, bag_to_search) -> int:
        count = 1
        for name, items in self.contents:
            if name.contains(bag_to_search, []):
                for c, bag_count in name.contents:
                    count += int(bag_count) * self.count_contains(c)

        return count

    def add_bag(self, bag, quantity: int) -> None:
        self.contents.append((bag, int(quantity)))
        self.quantity_carrying += quantity

    @staticmethod
    def create_from(line: str):
        split = line \
            .replace(' bags contain ', ';') \
            .replace(' bag, ', ';') \
            .replace(' bags.', '') \
            .replace(' bags, ', ';') \
            .replace(' bag.', '') \
            .replace('no other ', '') \
            .split(';')

        bag = Bag(str(split[0]).strip())
        for containing_bag in split[1:]:
            if containing_bag != 'no other':
                q, attr, color = containing_bag.split(' ')
                bag.add_bag(Bag(attr + ' ' + color, int(q)), int(q))
        return bag


start = time.time()
with open('aoc2020_07_input.txt', 'r') as f:
    rules = [Bag.create_from(b) for b in f.read().split('\n') if b != '']
print('parsing took {0}s'.format(time.time() - start))

SEARCH_COLOR = 'shiny gold'

start = time.time()
p1 = len([b for b in rules if b.contains(Bag(SEARCH_COLOR), rules) and b.color != SEARCH_COLOR])
print('Part 1:', p1, 'took {0}s'.format(time.time() - start))

start = time.time()
p2 = sum([b.count_contains(Bag(SEARCH_COLOR)) for b in rules])
print('Part 2:', p2, 'took {0}s'.format(time.time() - start))
