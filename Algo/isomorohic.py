def is_isomorohic(s1: str, s2: str) -> bool:
    assert len(s1) == len(s2) and s1 != ''
    mapping = {}
    values = set()
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        try:
            if mapping[c1] == c2:
                continue
            else:
                print ("Not isomorohic")
                return False
        except KeyError:
            if c2 in values:
                print ("Not isomorohic")
                return False
            else:
                mapping[c1] = c2
                values.add(c2)

    print ("Isomorohic")
    return True

is_isomorohic('abbc', 'cdde')
is_isomorohic('abc', 'etd')
is_isomorohic('aggron', 'daaake')