# https://open.kattis.com/problems/morsecodepalindromes

def is_palindrome(word):
    l = len(word)
    for i in range(l // 2):
        if word[i] != word[l - i - 1]:
            return False
    return l > 0

def main():
    morse_code = {
        "A": "10", "B": "0111", "C": "0101", "D": "011", "E": "1", "F": "1101", "G": "001", "H": "1111", "I": "11", "J": "1000", "K": "010", "L": "1011",
        "M": "00", "N": "01", "O": "000", "P": "1001", "Q": "0010", "R": "101", "S": "111", "T": "0", "U": "110", "V": "1110", "W": "100", "X": "0110",
        "Y": "0100", "Z": "0011", "0": "00000", "1": "10000", "2": "11000", "3": "11100", "4": "11110", "5": "11111", "6": "01111", "7": "00111", "8": "00011", "9": "00001"
    }

    word = input()
    
    morse = ""

    for c in word:
        if c.upper() in morse_code:
            morse += morse_code[c.upper()]

    if is_palindrome(morse):
        print(1)
    else:
        print(0)

main()