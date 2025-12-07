s = 'bmudsiluhar'

def reverse_string(s):
    rev =""
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    return rev
        
print(reverse_string(s))

s = 'orpsiluhar'

def reverse_string(s):
    rev =""
    i = len(s) - 1
    while i >= 0:
        rev = rev + s[i]
        i -= 1
    return rev

print(reverse_string(s))

