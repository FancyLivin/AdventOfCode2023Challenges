def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

SYMBOL_LIST = ['*', '-', '+', '@', '#', '$', '%', '&', '=', '/']
GEAR = '*'
OFFSET = 1

class PartOne:
    def __init__(self, txt_file) -> None:
        self.file = read_file(txt_file)
        self.engine_map = []
        self.part_number_sum = 0
    
    def populate_engine_map(self) -> None:
        for line in self.file:
            line = line.strip('\n')
            self.engine_map.append(line)

    def get_part_number_sum(self) -> int:
        for y in range(len(self.engine_map)):
            for x in range(len(self.engine_map[y])):
                if self.is_symbol(self.engine_map[y][x]):
                    self.part_number_sum += self.get_sum_around_symbol(x, y)

        return self.part_number_sum

    def is_symbol(self, char) -> bool:
        if char in SYMBOL_LIST:
            return True
        return False
    
    def get_sum_around_symbol(self, x, y) -> int:
        max_x = len(self.engine_map) - OFFSET
        max_y = len(self.engine_map[0]) - OFFSET
        sum_around_symbol = 0

        if y != 0:
            if x != 0:
                sum_around_symbol += self.extract_part_number(x - OFFSET, y - OFFSET) # top left
            sum_around_symbol += self.extract_part_number(x, y - OFFSET) # top middle
            if x != max_x:
                sum_around_symbol += self.extract_part_number(x + OFFSET, y - OFFSET) # top right

        if x != 0:
            sum_around_symbol += self.extract_part_number(x - OFFSET, y) # middle left
        if x != max_x:
            sum_around_symbol += self.extract_part_number(x + OFFSET, y) # middle right

        if y != max_y:
            if x != 0:
                sum_around_symbol += self.extract_part_number(x - OFFSET, y + OFFSET) # bottom left
            sum_around_symbol += self.extract_part_number(x, y + OFFSET) # bottom middle
            if x != max_x:
                sum_around_symbol += self.extract_part_number(x + OFFSET, y + OFFSET) # bottom right

        return sum_around_symbol
    
    def extract_part_number(self, x, y) -> int:
        if self.engine_map[y][x].isdigit() == False:
            return 0
        initial_x = x

        x = self.go_to_part_number_start_index(x, y)
        part_number = self.get_part_number(x, y)
        self.delete_part_number(initial_x, y)

        return part_number

    def go_to_part_number_start_index(self, x, y) -> int:
        while (self.engine_map[y][x].isdigit()):
            x -= OFFSET
        x += OFFSET
        return x

    def get_part_number(self, x, y) -> int:
        max_x = len(self.engine_map)
        part_number = ''

        while (self.engine_map[y][x].isdigit()):
            part_number += self.engine_map[y][x]
            x += OFFSET
            if x == max_x:
                break
        return int(part_number)

    def delete_part_number(self, x, y) -> None:
        x = self.go_to_part_number_start_index(x, y)
        self.replace_part_number_with_filler(x, y)
    
    def replace_part_number_with_filler(self, x, y) -> None:
        max_x = len(self.engine_map)

        while (self.engine_map[y][x].isdigit()):
            self.engine_map[y] = self.engine_map[y][:x] + '.' + self.engine_map[y][x + OFFSET:]
            x += OFFSET
            if x == max_x:
                break

class PartTwo:
    def __init__(self, txt_file) -> None:
        self.txt_file = txt_file
        self.file = read_file(txt_file)
        self.engine_map = []
        self.gear_ratio_sum = 0

    def populate_engine_map(self) -> None:
        for line in self.file:
            line = line.strip('\n')
            self.engine_map.append(line)

    def get_gear_ratio_sum(self) -> int:
        for y in range(len(self.engine_map)):
            for x in range(len(self.engine_map[y])):
                if self.is_gear(self.engine_map[y][x]):
                    self.gear_ratio_sum += self.get_gear_ratio(x, y)
        return self.gear_ratio_sum

    def is_gear(self, char) -> bool:
        if char == '*':
            return True
        return False

    def get_gear_ratio(self, x, y):
        gear_parts = []

        max_x = len(self.engine_map) - OFFSET
        max_y = len(self.engine_map[0]) - OFFSET

        if y != 0:
            if x != 0:
                gear_parts.append(self.extract_part_number(x - OFFSET, y - OFFSET)) # top left
            if self.engine_map[y - OFFSET][x - OFFSET].isdigit() == False:
                gear_parts.append(self.extract_part_number(x, y - OFFSET)) # top middle
            if x != max_x and self.engine_map[y - OFFSET][x].isdigit() == False:
                gear_parts.append(self.extract_part_number(x + OFFSET, y - OFFSET)) # top right

        if x != 0:
            gear_parts.append(self.extract_part_number(x - OFFSET, y)) # middle left
        if x != max_x:
            gear_parts.append(self.extract_part_number(x + OFFSET, y)) # middle right

        if y != max_y:
            if x != 0:
                gear_parts.append(self.extract_part_number(x - OFFSET, y + OFFSET)) # bottom left
            if self.engine_map[y + OFFSET][x - OFFSET].isdigit() == False:
                gear_parts.append(self.extract_part_number(x, y + OFFSET)) # bottom middle
            if x != max_x and self.engine_map[y + OFFSET][x].isdigit() == False:
                gear_parts.append(self.extract_part_number(x + OFFSET, y + OFFSET)) # bottom right
        
        gear_parts = list(filter(lambda x: x != None, gear_parts))
        adjacent_part_numbers = len(gear_parts)
        if adjacent_part_numbers == 2:
            return gear_parts[0] * gear_parts[1]
        return 0
    
    def extract_part_number(self, x, y) -> int:
        if self.engine_map[y][x].isdigit() == False:
            return None
        gear = PartOne(self.txt_file)
        gear.populate_engine_map()

        x = gear.go_to_part_number_start_index(x, y)
        part_number = gear.get_part_number(x, y)

        return part_number

part_one = PartOne('real_input.txt')
part_one.populate_engine_map()
part_one_sum = part_one.get_part_number_sum()

part_two = PartTwo('real_input.txt')
part_two.populate_engine_map()
part_two_sum = part_two.get_gear_ratio_sum()

print('Part One:', part_one_sum)
print('Part Two:', part_two_sum)
