def find_number_length(number):
    return len(str(number))

def sumDigits(number):
    r = 0
    length = find_number_length(number)
    for c in str(number):
        c = int(c)
        r+=pow(c, length)
    return r    

def is_armstrong_number(number):
    return number == sumDigits(number)