def caesarCipher(s, k):
    ls = []
    allower = "abcdefghijklmnopqrstuvwxyz"
    alupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s:
        if x.isupper():
            ls.append(alupper[(alupper.index(x) + k) % 26])
        elif x.islower():
            ls.append(allower[(allower.index(x) + k) % 26])
        else:
            ls.append(x)
    return ''.join(ls)