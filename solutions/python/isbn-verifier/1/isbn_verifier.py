alphabet = '0123456789X-'

def is_valid(isbn:str):
    val:int = 0
    num:int = 10
    for ch in isbn:
        if ch in alphabet:
            if ch.isdigit():
                val+=(int(ch)*num)
                num-=1
            elif ch == 'X' and isbn.index('X') == len(isbn)-1:
                val+=(10*num)
                num-=1
        else:
            return False
    if num == 0:
        return val % 11 == 0
    else:
        return False