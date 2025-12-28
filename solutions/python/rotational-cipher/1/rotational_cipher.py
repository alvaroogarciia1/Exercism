alphabet:str = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text:str, key:int):
    rot:str = ''
    key = key % 26
    for ch in text:
        if ch.lower() in alphabet:
            i = alphabet.index(ch.lower())
            if ch.isupper():
                rot_ch = alphabet[(i + key) % 26].capitalize()
            else:
                rot_ch = alphabet[(i + key) % 26]
            rot+=rot_ch
        else:
            rot+=ch
    return rot