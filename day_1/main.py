def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

class DayOne:
    def __init__(self, file_name) -> None:
        self.file = read_file(file_name)
        self.sum = 0

    def calculate_sum_of_strings(self) -> None:
        for string in self.file:            
            first_num = self.get_first_number(string)
            last_num = self.get_last_number(string)
            combined_num = str(first_num) + str(last_num)
            self.sum += int(combined_num)

    def get_first_number(self, string) -> int:
        first_num = None
        for char in string:
            try:
                first_num = int(char)
                break
            except:
                continue
        return first_num

    def get_last_number(self, string) -> int:
        last_num = None
        for char in string:
            try:
                last_num = int(char)
            except:
                continue
        return last_num

class DayTwo:
    pass
