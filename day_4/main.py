def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

class PartOne:
    def __init__(self, txt_file) -> None:
        self.file = read_file(txt_file)
        self.point_sum = 0

    def get_point_sum(self) -> int:
        for single_card in self.file:
            self.point_sum += self.calculate_card_points(single_card)
        return self.point_sum

    def calculate_card_points(self, string) -> int:
        card_points = 0
        card_numbers = string.split(' | ')

        winning_numbers = self.get_winning_numbers(card_numbers[0])
        your_numbers = self.get_numbers_you_have(card_numbers[1])

        for num in your_numbers:
            if num in winning_numbers and card_points == 0:
                card_points = 1
            elif num in winning_numbers and card_points >= 1:
                card_points *= 2

        return card_points

    def get_winning_numbers(self, string) -> list:
        winning_numbers = string.split()
        winning_numbers.pop(0)
        winning_numbers.pop(0)
        return winning_numbers

    def get_numbers_you_have(self, string) -> list:
        return string.split()

class PartTwo:
    def __init__(self, txt_file) -> None:
        self.txt_file = txt_file
        self.file = read_file(txt_file)
        self.card_total = 0
    


part_one = PartOne('real_input.txt')
sum_one = part_one.get_point_sum()
print('Part One:', sum_one)
