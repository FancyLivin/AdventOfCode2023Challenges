import time

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.rstrip('\n') for line in lines]

pipe_map = {
    '|' : 'NS',
    '-' : 'EW',
    'L' : 'NE',
    'J' : 'NW',
    '7' : 'SW',
    'F' : 'SE',
    '.' : 'X',
    'S' : 'X'
}
# direction is based on what side you come from
dir_map = {
    'S' : 1,
    'N' : -1,
    'E' : -1,
    'W' : 1,
    'X' : 0
}
NS = {
    'N' : -2,
    'S' : 2,
    'X' : 0
}
LR = {
    'W' : -2,
    'E' : 2,
    'X' : 0
}

def get_start_coords(map) -> tuple:
    for x, row in enumerate(map):
        for y, point in enumerate(row):
            if point == 'S':
                return (x, y)
    return (-1, -1)

class PartOne:
    def __init__(self, file_name):
        self.p_map = read_file(file_name)
        self.start = get_start_coords(self.p_map)
        self.farthest = 0
    
    def get_farthest_point(self) -> int:
        self.farthest = 0
        current = self.start
        previous = None
        while self.p_map[current[0]][current[1]] != 'S' or self.farthest == 0:
            if self.farthest >= 20:
                break

            print(self.p_map[current[0]][current[1]], current)
            time.sleep(1)

            top = self.p_map[current[0] - 1][current[1]]
            if 'S' in pipe_map[top] and current[0] - 1 >= 0:
                current, previous = self.change_coordinates('S', current, previous, top)

            right = self.p_map[current[0]][(current[1] + 1) % len(self.p_map[0])]
            if 'W' in pipe_map[right] and current[1] + 1 < len(self.p_map[0]):
                current, previous = self.change_coordinates('W', current, previous, right)

            left = self.p_map[current[0]][current[1] - 1]
            if 'E' in pipe_map[left] and current[1] - 1 >= 0:
                current, previous = self.change_coordinates('E', current, previous, left)

            bottom = self.p_map[current[0] + 1][current[1]]
            if 'N' in pipe_map[bottom] and current[0] + 1 < len(self.p_map[0]):
                current, previous = self.change_coordinates('N', current, previous, bottom)

        return self.farthest // 2
    
    def change_coordinates(self, excluded_char, current, previous, direction) -> (tuple, tuple):
        if self.p_map[current[0]][current[1]] == 'S' and self.farthest != 0:
            return current, previous

        remaining = self.exclude_character(pipe_map[direction], excluded_char)
        if direction == '|':
            print(direction, current)
            temp = (current[0] + NS[remaining], current[1])
        elif direction == '-':
            temp = (current[0], current[1] + LR[remaining])
        else:
            print(dir_map[pipe_map[direction][0]], dir_map[pipe_map[direction][1]])
            temp = (current[0] + dir_map[pipe_map[direction][0]], current[1] + dir_map[pipe_map[direction][1]])

        if previous == temp:
            print('fail',temp, previous, current, direction, remaining)
            previous = temp
            return current, previous
        print('pass',temp, previous, current, direction, remaining)
        self.farthest+=2
        previous = current
        return temp, previous
    
    def exclude_character(self, original_string, excluded_char) -> str:
        return original_string.replace(excluded_char, '')

class PartTwo:
    pass
