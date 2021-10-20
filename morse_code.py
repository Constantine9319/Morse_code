MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', ' ': ' '}


def convert_str_to_code(string: str):
    """ converts string into morse code"""
    returning_string = ''
    for char in string:
        try:
            returning_string += MORSE_CODE[char] + ' '
        except KeyError: # for some chars that not in the MORSE_CODE dict
            continue
    return returning_string


def convert_code_to_str(string: str):
    """ converts morse code into string"""
    code_list = string.split('  ')
    returning_string = ''
    for item in code_list:
        for q in item.split():
            returning_string += str(list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(q)]) #this one finds a key by it's value
        returning_string += " "
    return returning_string[:-1].capitalize()
convert_to = '0'
while convert_to != 'S' or "M":
    convert_to = input(f'Press "M" to convert string to Morse code, or press "S" to convert Morse code to string\n').upper()
    if convert_to == "M":
        inp_str = input("The string to convert:\n").upper()
        string_in_code = convert_str_to_code(inp_str)
        print('Your string in Morse Code:')
        print(string_in_code)
    elif convert_to == "S":
        inp_str = input("The string to convert (use triple space to separate words):\n").upper()
        not_code = False
        for char in inp_str:
            if char not in {"-", ' ', '.'}:
                not_code = True
        if not_code:
            print("This is not Morse code")
        else:
            string_in_code = convert_code_to_str(inp_str)
            print("Your code in string:")
            print(string_in_code)
