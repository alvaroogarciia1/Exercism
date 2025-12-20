def isEven(number):
    return number % 2 == 0

def checkNumber(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
def steps(number):
    steps = 0
    while number != 1:
        checkNumber(number)
        if isEven(number):
            number/=2
        else:
            number*=3
            number+=1
        steps+=1
    return steps