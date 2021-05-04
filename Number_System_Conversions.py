import csv

class Converter:

    def __init__(self):
        pass

    def decimal_to_binary(self, raw_decimal_input):
        decimal_input = int(raw_decimal_input) #replace this with actual user input

        if (decimal_input - 128) > 0 or (decimal_input - 128) == 0:
            decimal_input = (decimal_input - 128)
            position_1 = '1' #position 1 represents the MSB in the binary sequence
        else:
            position_1 = '0'

        if (decimal_input - 64) > 0 or (decimal_input - 64) == 0:
            decimal_input = (decimal_input - 64)
            position_2 = '1'
        else:
            position_2 = '0'
        
        if (decimal_input - 32) > 0 or (decimal_input - 32) == 0:
            decimal_input = (decimal_input - 32)
            position_3 = '1'
        else:
            position_3 = '0'

        if (decimal_input - 16) > 0 or (decimal_input - 16) == 0:
            decimal_input = (decimal_input - 16)
            position_4 = '1'
        else:
            position_4 = '0'

        if (decimal_input - 8) > 0 or (decimal_input - 8) == 0:
            decimal_input = (decimal_input - 8)
            position_5 = '1'
        else:
            position_5 = '0'

        if (decimal_input - 4) > 0 or (decimal_input - 4) == 0:
            decimal_input = (decimal_input - 4)
            position_6 = '1'
        else:
            position_6 = '0'

        if (decimal_input - 2) > 0 or (decimal_input - 2) == 0:
            decimal_input = (decimal_input - 2)
            position_7 = '1'
        else:
            position_7 = '0'

        if (decimal_input - 1) > 0 or (decimal_input - 1) == 0:
            decimal_input = (decimal_input - 1)
            position_8 = '1' #position 8 represents the LSB in the binary sequence
        else:
            position_8 = '0'

        binary_output = f'{position_1}{position_2}{position_3}{position_4}{position_5}{position_6}{position_7}{position_8}'
        print (f'Decimal input: {raw_decimal_input}\nBinary output (8 bit): {binary_output}')

    def decimal_to_octal(self):
        pass

    def decimal_to_hex(self):
        pass
    
    def decimal_to_BCD(self):
        pass

    def binary_to_decimal(self):
        pass

    def binary_to_octal(self, raw_binary_input):
        binary_input = list(raw_binary_input)

        if len(binary_input) in [3, 6, 9]:
            print('good')

        elif len(binary_input) in [2, 5, 8]:
            binary_input.insert(0, '0')
            print(binary_input)

        elif len(binary_input) in [1, 4, 7]:
            binary_input.insert(0, '0')
            binary_input.insert(0, '0')
            print(binary_input)

        else:
            print('bad, extraneous value') #delete this later, only here for testing

        

    def binary_to_hex(self):
        pass

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

class Controller:
    pass

Converter().binary_to_octal('1111')