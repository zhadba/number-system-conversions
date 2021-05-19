import csv

class Converter:

    def __init__(self):
        pass

    def read_cheat_sheet(self, directory):
        conversion_map = []
        with open(directory, newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                conversion_map.append({'key': row[0], 'value': row[1]})
            
        return conversion_map

    def decimal_to_binary(self, raw_decimal_input):
        base_2_iterations = [128, 64, 32, 16, 8, 4, 2, 1]
        decimal_input = int(raw_decimal_input)
        binary_output = []

        for iteration in base_2_iterations:
            position_x = ''
            if (decimal_input - iteration) > 0 or (decimal_input - iteration) == 0:
                decimal_input = (decimal_input - iteration)
                position_x = '1'
            else:
                position_x = '0'

            binary_output.append(position_x)
        
        return ''.join(binary_output)

    def decimal_to_octal(self, raw_decimal_input):
        binary_representation = self.decimal_to_binary(raw_decimal_input)
        octal_output = self.binary_to_octal(binary_representation)
        print(octal_output)

    def decimal_to_hex(self, raw_decimal_input):
        binary_representation = self.decimal_to_binary(raw_decimal_input) 
        hex_output = self.binary_to_hex(binary_representation)
        print(hex_output)

    def decimal_to_BCD(self):
        pass

    def binary_to_decimal(self):
        pass

    def binary_to_octal(self, raw_binary_input):
        conversions = self.read_cheat_sheet('CSV Files\Octal_Cheat_Sheet.csv')
        raw_binary_input = list(raw_binary_input)
        binary_input = [] 

        for binary_digit in raw_binary_input:
            if (binary_digit != ' '):
                binary_input.append(binary_digit)

        if len(binary_input) in [2, 5, 8]:
            binary_input = ['0'] + binary_input
        elif len(binary_input) in [1, 4, 7]:
            binary_input = ['0', '0'] + binary_input

        binary_string = ''
        binary_split_string = []
        octal_output = []

        binary_string = (binary_string.join(binary_input))
        for index in range(0, len(binary_string), 3):
            binary_split_string.append(binary_string[index : index + 3])

        for binary_group in binary_split_string:
            for conversion_pair in conversions:
                if str(binary_group) in conversion_pair['key']:
                    octal_output.append(conversion_pair['value'])
            
        return ''.join(octal_output)
            
    def binary_to_hex(self, raw_binary_input):
        conversions = self.read_cheat_sheet('CSV Files\Hex_Cheat_Sheet.csv')
        raw_binary_input = list(raw_binary_input)
        binary_input = []

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
        hex_output = []

        binary_string = (binary_string.join(binary_input))
        for index in range(0, len(binary_string), 4):
            binary_split_string.append(binary_string[index : index + 4])

        for binary_group in binary_split_string:
            for conversion_pair in conversions:
                if binary_group in conversion_pair['key']:
                    hex_output.append(conversion_pair['value']) 

        return ''.join(hex_output)  

    def octal_to_decimal(self):
        pass

    def octal_to_binary(self):
        pass

    def hex_to_decimal(self):
        pass

    def hex_to_binary(self):
        pass

    def BCD_to_decimal(self):
        pass

    def alpha_to_ASCII(self):
        pass

    def ASCII_to_alpha(self):
        pass

class Menu:
    pass

class View:
    pass

class Controller:
    pass

Converter().decimal_to_hex('121')