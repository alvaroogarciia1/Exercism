def convert(number):
    r = str(number)
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        r = ''
        if number % 3 == 0:
            r += 'Pling'
        if number % 5 == 0:
            r += 'Plang'
        if number % 7 == 0:
            r += 'Plong'
    return r
