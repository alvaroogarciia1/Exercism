vowels = "aeiou"

def rule_1(word):
    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"
    return ""

def rule_2(word):
    vowels = "aeiou"
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + "ay"
    return word + "ay"

def rule_3(word):
    vowels = "aeiou"
    for i in range(len(word) - 1):
        if word[i:i+2] == "qu":
            return word[i+2:] + word[:i+2] + "ay"
        if word[i] in vowels:
            break
    return ""

def rule_4(word):
    vowels = "aeiou"
    for i in range(1, len(word)):
        if word[i] == "y":
            return word[i:] + word[:i] + "ay"
        if word[i] in vowels:
            break
    return ""

def translate(text):
    words = text.lower().split()
    translated_list = []
    for word in words:
        result = rule_1(word)
        if result == "":
            result = rule_3(word)
        if result == "":
            result = rule_4(word)
        if result == "":
            result = rule_2(word)
        translated_list.append(result)
    return " ".join(translated_list)