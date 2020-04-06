# Valerie Nayak
# 4/6/2020
# Cracking the Coding Interview, p. 90
# 1.5: One Away

def one_away(word1, word2):
    if word1 == word2:
        return True
    size_diff = abs(len(word1) - len(word2))
    if size_diff > 1:
        return False
    temp1 = word1[:]
    temp2 = word2[:]
    found_diff = False
    while len(temp1) > 0 and len(temp2) > 0:
        if temp1[0] != temp2[0]:
            if found_diff == True:
                return False
            elif len(temp1) > len(temp2):
                temp1 = temp1[1:]
            elif len(temp2) > len(temp1):
                temp2 = temp2[1:]
            else:
                temp1 = temp1[1:]
                temp2 = temp2[1:]
            found_diff = True
        else:
            temp1 = temp1[1:]
            temp2 = temp2[1:]
    return True

word1 = 'pale'
word2 = 'apale'
print(one_away(word1, word2))