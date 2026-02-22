# String exercises

# Longest word
words = ["a", "bb", "ccc"]
if words:
    longest = max(words, key=len)
    print(longest, len(longest))

# Replace 'not...poor' with 'good'
def replace_not_poor(text):
    words = text.split()
    if "not" in words and "poor" in words:
        n, p = words.index("not"), words.index("poor")
        if n < p:
            words[n:p+1] = ["good"]
    return " ".join(words)

# Swap first 2 chars of strings
def swap_strings(a, b):
    return b[:2]+a[2:] + " " + a[:2]+b[2:]

# String length
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Char frequency
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Insert string in middle
def insert_string_middle(original, to_insert):
    mid = len(original)//2
    return original[:mid] + to_insert + original[mid:]

# Repeat last 2 chars 4 times
def repeat_last_two_chars(s):
    if len(s) < 2:
        return "String too short"
    return s[-2:] * 4
