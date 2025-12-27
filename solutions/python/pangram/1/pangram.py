def is_pangram(sentence:str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    for ch in alphabet:
        if ch.isalpha():
            if ch not in sentence:
                return False
    return True