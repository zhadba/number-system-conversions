import csv

class Number:
    
    def __init__(self, numerical_input):
        self.numerical_input = numerical_input

    def __str__(self):
        return f'Numeric input: {self.numerical_input}' 

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
        print(self.numeric_output)

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
        print (self.numeric_output)

        return self.numeric_output

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
        print(sum(self.numeric_output))
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

        self.numeric_output = (int(octal_input[0]) * (8**2)) + (int(octal_input[1]) * (8**1)) + (int(octal_input[2]) * (8**0))
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
            for conversion in conversions:
                if digit in conversion['value']:
                    

    def hex_to_binary(self, user_input):
        pass

    def BCD_to_decimal(self, user_input):
        pass

    def alpha_to_ASCII(self, user_input):
        pass

    def ASCII_to_alpha(self, user_input):
        pass

class Menu:
    pass

class View:
    pass

class Controller:
    pass

SystemConverter().hex_to_decimal('ABCD')