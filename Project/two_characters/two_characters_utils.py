def alternate(s):
    c = tuple(set(s))
    if len(c) < 2:
        return 0
    lengths = []
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            test = "".join([a for a in s if a in (c[i], c[j])])
            if any(test[k] == test[k+1] for k in range(len(test) - 1)):
                continue
            else:
                lengths.append(len(test))
    if lengths:
        return max(lengths)
    return 0