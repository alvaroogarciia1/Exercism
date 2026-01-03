
def rebase(input_base:int, digits:list, output_base:int):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    num:int = 0
    maxP:int = len(digits) - 1
    for n in digits:
        if n < 0 or n >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        num += (n * (input_base ** maxP))
        maxP -= 1
    rem:int = 0
    l:list = [] 
    while num >= output_base:
        rem = num % output_base
        l.append(rem)
        num//=output_base
    l.append(num)
    return l[::-1]
         
rebase(10, [5], 2)
