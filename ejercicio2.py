def isPar(a):
    if len(a) % 2 == 0:
        return True
    else:
        return False


def dictConvert(sentence):
    dictionary = {}
    for i in sentence.split():
        dictionary.setdefault(str(len(i)), isPar(i))
    return dictionary


print(dictConvert("Las flores bailan en el campo").items())
