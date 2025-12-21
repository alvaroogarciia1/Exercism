def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        square = 1
        i = 1
        while i != number:
            square*=2
            i+=1
    return square

def total():
    total = 0
    i = 1
    while i != 65:
            total+=square(i)
            i+=1
    return total
        

print(square(1))