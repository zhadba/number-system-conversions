import csv

class SystemConverter:
    
    def __init__(self):
        self.numeric_output = []

    def read_cheat_sheet(self, directory):
        conversion_map = []
        with open(directory, newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                conversion_map.append({'key': row[0], 'value': row[1]})

        return conversion_map

    def decimal_to_binary(self, user_input):
        base_2_iterations = [128, 64, 32, 16, 8, 4, 2, 1]
        decimal_input = int(user_input)
        self.numeric_output = []

        for iteration in base_2_iterations:
            position_x = ''
            if (decimal_input - iteration) > 0 or (decimal_input - iteration) == 0:
                decimal_input = (decimal_input - iteration)
                position_x = '1'
            else:
                position_x = '0'

            self.numeric_output.append(position_x)
        
        return ''.join(self.numeric_output)

    def decimal_to_octal(self, user_input):
        self.numeric_output = []
        binary_representation = self.decimal_to_binary(user_input)
        self.numeric_output = self.binary_to_octal(binary_representation)

        return self.numeric_output

    def decimal_to_hex(self, user_input):
        self.numeric_output = []
        binary_representation = self.decimal_to_binary(user_input) 
        self.numeric_output = self.binary_to_hex(binary_representation)

        return self.numeric_output

    def decimal_to_BCD(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\BCD_Cheat_Sheet.csv')
        decimal_input = list(user_input)
        self.numeric_output = []
        
        for digit in decimal_input:
            for conversion_pair in conversions:
                if digit in conversion_pair['key']:
                    self.numeric_output.append(conversion_pair['value'])

        return ''.join(self.numeric_output)

    def binary_to_decimal(self, user_input):
        raw_binary_input = list(user_input)
        binary_input = []
        self.numeric_output = []

        for binary_digit in raw_binary_input:
            if (binary_digit != ' '):
                binary_input.append(binary_digit)

        if len(binary_input) in [3, 7]:
            binary_input = ['0'] + binary_input
        elif len(binary_input) in [2, 6]:
            binary_input = ['0', '0'] + binary_input
        elif len(binary_input) in [1, 5]:
            binary_input = ['0','0','0'] + binary_input

        if len(binary_input) == 4:
            conversion_map = {'8': binary_input[0], '4': binary_input[1], '2': binary_input[2], '1': binary_input[3]}
            for k, v in conversion_map.items():
               conversion = (int(k) * int(v))
               self.numeric_output.append(conversion)
                          
        elif len(binary_input) == 8:
            conversion_map = {'128': binary_input[0], '64': binary_input[1], '32': binary_input[2],'16': binary_input[3], '8': binary_input[4], '4': binary_input[5], '2': binary_input[6], '1': binary_input[7]}
            for k, v in conversion_map.items():
                conversion = (int(k) * int(v))
                self.numeric_output.append(conversion)

        return sum(self.numeric_output)

    def binary_to_octal(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\Octal_Cheat_Sheet.csv')
        raw_binary_input = list(user_input)
        binary_input = [] 
        self.numeric_output = []

        for binary_digit in raw_binary_input:
            if (binary_digit != ' '):
                binary_input.append(binary_digit)

        if len(binary_input) in [2, 5, 8]:
            binary_input = ['0'] + binary_input
        elif len(binary_input) in [1, 4, 7]:
            binary_input = ['0', '0'] + binary_input

        binary_string = ''
        binary_split_string = []

        binary_string = (binary_string.join(binary_input))
        for index in range(0, len(binary_string), 3):
            binary_split_string.append(binary_string[index : index + 3])

        for binary_group in binary_split_string:
            for conversion_pair in conversions:
                if str(binary_group) in conversion_pair['key']:
                    self.numeric_output.append(conversion_pair['value'])
            
        return ''.join(self.numeric_output)
            
    def binary_to_hex(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\Hex_Cheat_Sheet.csv')
        raw_binary_input = list(user_input)
        binary_input = []
        self.numeric_output = []

        for binary_digit in raw_binary_input:
            if (binary_digit != ' '):
                binary_input.append(binary_digit)

        if len(binary_input) in [3, 7, 11, 15]:
            binary_input = ['0'] + binary_input
        elif len(binary_input) in [2, 6, 10, 14]:
            binary_input = ['0', '0'] + binary_input
        elif len(binary_input) in [1, 5, 9, 13]:
            binary_input = ['0', '0', '0'] + binary_input

        binary_string = ''
        binary_split_string = []

        binary_string = (binary_string.join(binary_input))
        for index in range(0, len(binary_string), 4):
            binary_split_string.append(binary_string[index : index + 4])

        for binary_group in binary_split_string:
            for conversion_pair in conversions:
                if binary_group in conversion_pair['key']:
                    self.numeric_output.append(conversion_pair['value']) 

        return ''.join(self.numeric_output)  

    def octal_to_decimal(self, user_input):
        octal_input = list(user_input)
        self.numeric_output = []
        
        if len(octal_input) == 2:
            octal_input = ['0'] + octal_input
        elif len(octal_input) == 1:
            octal_input = ['0','0'] + octal_input

        self.numeric_output = (int(octal_input[0]) * (8**2)) + (int(octal_input[1]) * (8)) + (int(octal_input[2]))
        return self.numeric_output

    def octal_to_binary(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\Octal_Cheat_Sheet.csv')
        octal_input = list(user_input)
        self.numeric_output = []

        if len(octal_input) == 2:
            octal_input = ['0'] + octal_input
        elif len(octal_input) == 1:
            octal_input = ['0','0'] + octal_input

        for digit in octal_input:
            for conversion_pair in conversions:
                if str(digit) in conversion_pair['value']:
                    self.numeric_output.append(conversion_pair['key'])
                    
        return ''.join(self.numeric_output)
        
    def hex_to_decimal(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\Alpha_Hex_Cheat_Sheet.csv')
        raw_hex_input = list(user_input)
        hex_input = []
        self.numeric_output = []

        if len(raw_hex_input) == 3:
            raw_hex_input = ['0'] + raw_hex_input
        elif len(raw_hex_input) == 2:
            raw_hex_input = ['0', '0'] + raw_hex_input
        elif len(raw_hex_input) == 1:
            raw_hex_input = ['0', '0', '0'] + raw_hex_input

        for digit in raw_hex_input:
            if digit in ['0','1','2','3','4','5','6','7','8','9']:
                hex_input.append(digit)
            for conversion in conversions:
                if digit in conversion['value']:
                    hex_input.append(conversion['key'])
        
        self.numeric_output = (int(hex_input[0]) * (16**3)) + (int(hex_input[1]) * (16**2)) + (int(hex_input[2]) * (16)) + (int(hex_input[3]))
        return self.numeric_output
        
    def hex_to_binary(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\Hex_Cheat_Sheet.csv')
        hex_input = list(user_input)
        self.numeric_output = []

        for digit in hex_input:
            for conversion in conversions:
                if digit in conversion['value']:
                    self.numeric_output.append(conversion['key'])

        return ''.join(self.numeric_output)

    def BCD_to_decimal(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\BCD_Cheat_Sheet.csv')
        raw_BCD_input = list(user_input)
        BCD_input = []
        self.numeric_output = []

        for BCD_digit in raw_BCD_input:
            if (BCD_digit != ' '):
                BCD_input.append(BCD_digit)

        if len(BCD_input) in [3, 7, 11, 15]:
            BCD_input = ['0'] + BCD_input
        elif len(BCD_input) in [2, 6, 10, 14]:
            BCD_input = ['0', '0'] + BCD_input
        elif len(BCD_input) in [1, 5, 9, 13]:
            BCD_input = ['0', '0', '0'] + BCD_input

        BCD_string = ''
        BCD_split_string = []

        BCD_string = (BCD_string.join(BCD_input))
        for index in range(0, len(BCD_string), 4):
            BCD_split_string.append(BCD_string[index : index + 4])

        for BCD_group in BCD_split_string:
            for conversion_pair in conversions:
                if BCD_group in conversion_pair['value']:
                    self.numeric_output.append(conversion_pair['key'])

        return ''.join(self.numeric_output)

    def alpha_to_ASCII(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\ASCII_Cheat_Sheet.csv')
        raw_alpha_input = list(user_input)
        alpha_input = []
        self.numeric_output = []

        for letter in raw_alpha_input:
            if (letter == ' '):
                alpha_input.append('blank')
            else:
                alpha_input.append(letter)

        for letter in alpha_input:
            for conversion in conversions:
                if letter in conversion['key']:
                    self.numeric_output.append(conversion['value'])

        return ''.join(self.numeric_output)

    def ASCII_to_alpha(self, user_input):
        conversions = self.read_cheat_sheet('CSV Files\ASCII_Cheat_Sheet.csv')
        ASCII_input = user_input
        self.numeric_output = []
        
        for conversion in conversions:
            if ASCII_input in conversion['value']:
                self.numeric_output.append(conversion['key'])

        return ''.join(self.numeric_output)


class Menu:
    
    def __init__(self, menu_options):
        self.options = menu_options

    def show_menu(self):
        for number,choice in self.options.items():
            if (number != ' '):
                print(f"{number}: {choice['description']}")
            else:
                print(f"{choice['description']}")    

    def receive_menu_choice(self):
        choice_validity = False
        while not choice_validity:
            menu_choice = input('Please input the number that corresponds with your choice: ')
            if menu_choice in self.options.keys():
                choice_validity = True
                return menu_choice
            else: 
                print('That choice does not exist')

    def capitalize_alpha_characters(self, user_input):
        capitalized_input = []
        for item in list(user_input):
            if item.isalpha():
                capitalized_input.append(item.upper())
            elif item.isdigit():
                capitalized_input.append(item)
        
        return ''.join(capitalized_input)

    def receive_decimal_input(self, length_limitation, content_limitation):
        input_validity = False
        while not input_validity:
            user_input = input('Please enter a decimal/octal input to convert: ')
            if len(list(user_input)) <= length_limitation:
                if user_input in content_limitation:
                    input_validity = True
                    return user_input
                else:
                    print('Invalid content. Please check that the appropriate system is chosen')
            else:
                print('Invalid length. Please check parameters for input')
    
    def receive_non_decimal_input(self, length_limitation, content_limitation):
        input_validity = False
        while not input_validity:
            user_input = input('Please enter an alphanumeric/binary/mixed input to convert: ')
            user_input = self.capitalize_alpha_characters(user_input)
            extraneous_input = []
            for item in list(user_input):
                if item in content_limitation:
                    pass   
                else:
                    extraneous_input.append(item)
              
            if len(list(user_input)) <= length_limitation:
                if extraneous_input:
                    print('Invalid content. Please check that the appropriate system is chosen')
                else:
                    input_validity = True
                    return user_input
            else:
                print('Invalid length. Please check parameters for input')
                    
class View:
    
    def __init__(self):
        self.printable_input = []
        self.printable_output = []

    def print_output(self, printable_input, printable_output):
        if printable_output and printable_input:
            self.printable_output = printable_output
            print(f'\nINPUT: {printable_input}\nOUTPUT: {printable_output}')
        else:
            print('\nNo input, therefore no output')


class Controller:
    
    def __init__(self):
        self.menu = Menu({})
        self.view = View()
        self.converter = SystemConverter()
        self.running = True
    
        self.menu_options = {
            ' ': {'description': '\nSelect the parent system of the number you wish to input:', 'action': None},
            '1': {'description': 'Decimal', 'action': lambda: self.show_decimal_menu()},
            '2': {'description': 'Binary', 'action': lambda: self.show_binary_menu()},
            '3': {'description': 'Octal', 'action': lambda: self.show_octal_menu()},
            '4': {'description': 'Hexadecimal', 'action': lambda: self.show_hex_menu()},
            '5': {'description': 'BCD', 'action': lambda: self.show_BCD_menu()},
            '6': {'description': 'Alphanumeric', 'action': lambda: self.show_alpha_menu()},
            '7': {'description': 'ASCII', 'action': lambda: self.show_ASCII_menu()},
            '8': {'description': 'Quit', 'action': lambda: self.terminate_program()}}

        self.decimal_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'Decimal --> Binary', 'action': lambda: self.convert_decimal_to_binary()},
            '2': {'description': 'Decimal --> Octal', 'action': lambda: self.convert_decimal_to_octal()},
            '3': {'description': 'Decimal --> Hexadecimal', 'action': lambda: self.convert_decimal_to_hex()},
            '4': {'description': 'Decimal --> BCD', 'action': lambda: self.convert_decimal_to_BCD()},
            '5': {'description': 'Return to Menu', 'action': lambda: self.run()}}

        self.binary_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'Binary --> Decimal', 'action': lambda: self.convert_binary_to_decimal()},
            '2': {'description': 'Binary --> Octal', 'action': lambda: self.convert_binary_to_octal()},
            '3': {'description': 'Binary --> Hexadecimal', 'action': lambda: self.convert_binary_to_hex()},
            '4': {'description': 'Return to Menu', 'action': lambda: self.run()}}

        self.octal_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'Octal --> Decimal', 'action': lambda: self.convert_octal_to_decimal()},
            '2': {'description': 'Octal --> Binary', 'action': lambda: self.convert_octal_to_binary()},
            '3': {'description': 'Return to Menu', 'action': lambda: self.run()}}

        self.hex_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'Hexadecimal --> Decimal', 'action': lambda: self.convert_hex_to_decimal()},
            '2': {'description': 'Hexadecimal --> Binary', 'action': lambda: self.convert_hex_to_binary()},
            '3': {'description': 'Return to Menu', 'action': lambda: self.run()}}

        self.BCD_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'BCD --> Decimal', 'action': lambda: self.convert_BCD_to_decimal()},
            '2': {'description': 'Return to Menu', 'action': lambda: self.run()}}

        self.alpha_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'Alphanumeric --> ASCII', 'action': lambda: self.convert_alpha_to_ASCII()},
            '2': {'description': 'Return to Menu', 'action': lambda: self.run()}}

        self.ASCII_menu_options = {
            ' ': {'description': '\nSelect the system that you wish to convert to:', 'action': None},
            '1': {'description': 'ASCII --> Alphanumeric', 'action': lambda: self.convert_ASCII_to_alpha()},
            '2': {'description': 'Return to Menu', 'action': lambda: self.run()}}

    def run(self):
        self.menu = Menu(self.menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.menu_options.get(menu_choice)['action']()

    def show_decimal_menu(self):
        self.menu = Menu(self.decimal_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.decimal_menu_options.get(menu_choice)['action']()

    def show_binary_menu(self):
        self.menu = Menu(self.binary_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.binary_menu_options.get(menu_choice)['action']()

    def show_octal_menu(self):
        self.menu = Menu(self.octal_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.octal_menu_options.get(menu_choice)['action']()

    def show_hex_menu(self):
        self.menu = Menu(self.hex_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.hex_menu_options.get(menu_choice)['action']()

    def show_BCD_menu(self):
        self.menu = Menu(self.BCD_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.BCD_menu_options.get(menu_choice)['action']()

    def show_alpha_menu(self):
        self.menu = Menu(self.alpha_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.alpha_menu_options.get(menu_choice)['action']()

    def show_ASCII_menu(self):
        self.menu = Menu(self.ASCII_menu_options)
        while self.running:
            self.menu.show_menu()
            menu_choice = self.menu.receive_menu_choice()
            self.ASCII_menu_options.get(menu_choice)['action']()

    def convert_decimal_to_binary(self):
        length_limitation = 3
        content_limitation = []
        for number in list(range(256)):
            content_limitation.append(str(number))

        user_input = self.menu.receive_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.decimal_to_binary(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_decimal_to_octal(self):
        length_limitation = 3
        content_limitation = []
        for number in list(range(512)):
            content_limitation.append(str(number))

        user_input = self.menu.receive_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.decimal_to_octal(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_decimal_to_hex(self):
        length_limitation = 5
        content_limitation = []
        for number in list(range(255)):
            content_limitation.append(str(number))

        user_input = self.menu.receive_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.decimal_to_hex(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_decimal_to_BCD(self):
        length_limitation = 4
        content_limitation = []
        for number in list(range(10000)):
            content_limitation.append(str(number))

        user_input = self.menu.receive_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.decimal_to_BCD(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_binary_to_decimal(self):
        length_limitation = 9
        content_limitation = [' ', '0', '1']

        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.binary_to_decimal(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_binary_to_octal(self):
        length_limitation = 11
        content_limitation = [' ', '0', '1']

        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.binary_to_octal(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_binary_to_hex(self):
        length_limitation = 19
        content_limitation = [' ', '0', '1']

        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.binary_to_hex(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_octal_to_decimal(self):
        length_limitation = 3
        content_limitation = []
        for number in list(range(778)):
            content_limitation.append(str(number))

        user_input = self.menu.receive_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.octal_to_decimal(user_input)
        self.view.print_output(user_input, printable_output) 

    def convert_octal_to_binary(self):
        length_limitation = 3
        content_limitation = []
        for number in list(range(778)):
            content_limitation.append(str(number))

        user_input = self.menu.receive_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.octal_to_binary(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_hex_to_decimal(self):
        length_limitation = 4
        content_limitation = ['A', 'B', 'C', 'D', 'E', 'F']
        for number in range(10):
            content_limitation.append(str(number))
    
        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.hex_to_decimal(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_hex_to_binary(self):
        length_limitation = 2
        content_limitation = ['A', 'B', 'C', 'D', 'E', 'F']
        for number in range(10):
            content_limitation.append(str(number))

        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.hex_to_binary(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_BCD_to_decimal(self):
        length_limitation = 19
        content_limitation = [' ', '0', '1']

        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.BCD_to_decimal(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_alpha_to_ASCII(self):
        length_limitation = 1
        content_limitation = []
        conversions = self.converter.read_cheat_sheet('CSV Files\ASCII_Cheat_Sheet.csv')
        for conversion in conversions:
            content_limitation.append(conversion['key'])

        print(content_limitation)
        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.alpha_to_ASCII(user_input)
        self.view.print_output(user_input, printable_output)

    def convert_ASCII_to_alpha(self):
        length_limitation = 7
        content_limitation = ['0', '1']

        print(content_limitation)
        user_input = self.menu.receive_non_decimal_input(length_limitation, content_limitation)
        printable_output = self.converter.ASCII_to_alpha(user_input)
        self.view.print_output(user_input, printable_output)        
        
    def terminate_program(self):
        self.running = False

if __name__ == '__main__':
    conversion_program = Controller()
    conversion_program.run()