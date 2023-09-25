from timeit import Timer, timeit

def is_anagram1(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            found = False
            for j in range(len(s1)):
                if s1[i] == s2[j]:
                    found = True
                    break
            if not found:
                return False
            return True

def is_anagram2(s1,s2):
    if len(s1) != len(s1):
        return False
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def is_anagram3(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    for j in range(len(c1)):
        if c1[j] != c2[j]:
            return False
    return True

t1 = Timer("is_anagram1('abc','cba')", "from __main__ import is_anagram1")
print("anagram1:", t1.timeit(number=100), "miliseconds")
t2 = Timer("is_anagram2('abc','cba')", "from __main__ import is_anagram2")
print("anagram2:", t2.timeit(number=100), "miliseconds")
t3 = Timer("is_anagram3('abc','cba')", "from __main__ import is_anagram3")
print("anagram3:", t3.timeit(number=100), "miliseconds")

'''
print(is_anagram1('abcd', 'dcba'))
print(is_anagram2('abcde', 'edcba'))
print(is_anagram3('apple', 'pleap'))
'''
