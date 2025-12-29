def score(x:int, y:int):
    distance:int = pow(pow(x,2) + pow(y,2), 1/2)
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0