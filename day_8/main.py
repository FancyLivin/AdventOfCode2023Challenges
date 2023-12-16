def read_directions(file_name):
    with open(file_name, 'r') as file:
        return file.readline().strip()

def read_network(file_name):
    with open(file_name, 'r') as file:
        # Skip first 2 lines for network map
        for _ in range(2):
            next(file)

        dictionary = {}
        for line in file:
            key, value = line.strip().split(' = ')
            dictionary[key] = tuple(value.lstrip('(').rstrip(')').split(', '))
    return dictionary

direction_map = {'L': 0, 'R': 1}

class PartOne:
    def __init__(self, file_name) -> None:
        self.directions = read_directions(file_name)
        self.network = read_network(file_name)
        self.steps = self.find_total_steps()

    def find_total_steps(self) -> int:
        steps = 0
        node = 'AAA'
        while node != 'ZZZ':
            direction = direction_map[self.directions[steps % len(self.directions)]]
            node = self.network[node][direction]
            steps+=1
        return steps

class PartTwo:
    pass

p_one = PartOne('real.txt')
print('Part One:', p_one.steps)