This is a repository designed for the purpose of easing the conversion between commonly
applicational number systems. There should exist two primary python files that contain functionality for
conversions between:

 - Any decimal number between 0 and 255 into binary (8 bit).
 - Any decimal number between 0 and 511 into octal (16 bit).
 - Any decimal number between 0 and 255 into hex (8 bit).
 - Any decimal number between 0 and 9999 into BCD (16 bit).
 - Any binary number between 0 and 1111 1111 into decimal (8 bit).
 - Any binary number between 0 and 111 111 111 into octal (9 bit).
 - Any binary number between 0 and 1111 1111 1111 1111 into hex (16 bit).
 - Any octal number between 0 and 777 into decimal (16 bit).
 - Any octal number between 0 and 777 into binary (16 bit).
 - Any hex number between 0 and FFFF into decimal (16 bit).
 - Any hex number between 0 and FF into binary (8 bit).
 - Any BCD representation from 0 to 1001 1001 1001 1001 into decimal (16 bit).
 - Any Alphanumeric representation from A-Z and 0-9 into ASCII 7-bit code.
 - Any ASCII 7-bit code into Alphanumeric representation.

The second primary file is designed to employ a parity error detection method for any 
7-bit code. Accepts odd or even parity.

The remaining files in this repository are designed to aid the conversion/error detection process.
