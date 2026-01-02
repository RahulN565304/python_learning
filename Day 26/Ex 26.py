# Reverse in String

def reverse_string(s):
    return s[::-1]
print(reverse_string("Rahul"))

# Reverse w/o Slicing

def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
print(reverse_string("Rahul"))

# Palindrome in String

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("Rahul"))
print(is_palindrome("sees"))

# Frequency Count

def char_frequency(s):
    freq = {}
    for ch in s.lower():
        if ch == " ":
            continue
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    return freq
print(char_frequency("Billie Ellish"))
print(char_frequency("Hello World"))
print(char_frequency("BANANA banana"))

