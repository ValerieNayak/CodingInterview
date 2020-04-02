# Valerie Nayak
# 4/2/2020
# Cracking the Coding Interview, p. 90
# 1.2: Check Permutation

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    chars1 = {}
    chars2 = {}
    for c in str1:
        if c in chars1:
            chars1[c] += 1
        else:
            chars1[c] = 1
    for c in str2:
        if c in chars2:
            chars2[c] += 1
        else:
            chars2[c] = 1
    if chars1 == chars2:
        return True
    else:
        return False

print(check_permutation('abc', 'cab'))
print(check_permutation('dog', 'go'))
print(check_permutation('dad', 'daa'))