import re

# To convert a word string to a number 
def words_to_number(word_str :str) -> int:

    # Mapping from words to numbers
    word_to_digit = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
        }

    # Defining a regular expression pattern to match any of the number words
    pattern = r"(zero|one|two|three|four|five|six|seven|eight|nine)"
    
    # Replace all occurrences of the words with their corresponding digits
    return int(re.sub(pattern, lambda match: word_to_digit[match.group(0)], word_str))

# Optimal solution by recursively calculating gcd to not use for loop
def gcd(a,b):

    # Termination condition based on euclidean algorithm
    if b == 0:
        return a
    
    # Recursive call to set a = b and b = a%b 
    return gcd(b,a%b)

# To convert a number to word string 
def number_to_word(ans :int) -> str:
    
    # Mapping from numbers to words
    digit_to_word = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
        }
    
    result = str(ans)
    
    # Defining a regular expression pattern to match any of the digits
    pattern = r"(0|1|2|3|4|5|6|7|8|9)"

    return re.sub(pattern, lambda match: digit_to_word[match.group(0)], result)  
    
def main():
    
    try:
        
        input1 = input("Enter input 1: ")
        if not input1.isalpha():
            raise Exception

        input2 = input("Enter input 2: ")
        if not input2.isalpha():
            raise Exception
        
        num1 = words_to_number(input1)
        num2 = words_to_number(input2)
    except:
        print('''Invalid input! Make sure your input follows the constraints:
              1. Numbers in words only in between 'zero' to 'nine' 
              2. No spaces between words
              3. Only in lowercase''')
        return


    print(number_to_word(gcd(num1,num2)))

if __name__ == '__main__':
    main()

