# Valerie Nayak
# 4/6/2020
# Cracking the Coding Interview, p. 90
# 1.6: String Compression

def compress(original):
    comp = ''
    current = original[0]
    count = 1
    for letter in original[1:]:
        if letter == current:
            count += 1
        else:
            comp += current + str(count)
            current = letter
            count = 1
    comp += current + str(count)
    if len(comp) < len(original):
        return comp
    else:
        return original

my_str = 'aabcccccaaad'
print(compress(my_str))