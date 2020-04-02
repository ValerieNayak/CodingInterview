# Valerie Nayak
# 4/2/2020
# Cracking the Coding Interview, p. 90
# 1.1: Is Unique

def is_unique(my_str):
    chars = set()
    for c in my_str:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True

print(is_unique('abcd'))
print(is_unique('apricot'))
print(is_unique('hello'))