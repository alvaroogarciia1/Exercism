def classify(number:int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<0:
        raise ValueError("Classification is only possible for positive integers.")
    elif number == 1:
        return 'deficient'
    else:
        factors:list = [1]
        i:int = 2
        divided = False
        while i * i <= number:
            if number % i == 0:
                factors.append(i)
                if i != number // i:
                    factorsappend(number // i)
            i += 1
        total = sum(factors)
        if total == number:
            return "perfect"
        elif total > number:
            return "abundant"
        else:
            return "deficient"