# Frequent Character

def char_frequency(s):
    freq = {}
    for ch in s.lower():
        if ch == " ":
            continue
        if ch in freq:
            freq[ch] = freq[ch] +  1
        else:
            freq[ch] = 1
    char = max(freq, key=freq.get)
    return char, freq[char]
print(char_frequency("BilliE EllisH"))
print(char_frequency("Mississippi"))

# No Duplicates

def org_char(s):
    seen = set()
    new_string = ""
    for ch in s.lower():
        if ch not in seen:
            new_string += ch
            seen.add(ch)
    return new_string

print(org_char("PrograMming"))