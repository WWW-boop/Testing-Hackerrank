def funnyString(s):
    a,b=[],[]
    s0=list(reversed(s))
    for i in range(len(s)-1):
        a.append(abs(ord(s[i]) - ord(s[i + 1])))
        b.append(abs(ord(s0[i]) - ord(s0[i + 1])))
    return "Funny " if a==b else "Not Funny"