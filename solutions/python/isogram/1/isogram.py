def is_isogram(string:str):
    string = string.replace(' ', '').replace('-', '').lower()
    for ch in string:
        if string.count(ch)>1:
            return False
    return True