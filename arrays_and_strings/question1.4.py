# Valerie Nayak
# 4/2/2020
# Cracking the Coding Interview, p. 90
# 1.4: Palindrome Permutation

def make_dict(my_str):
    letters = {}
    count = 0
    for c in my_str:
        if c.isalpha() == False:
            continue
        else:
            if c.lower() in letters:
                letters[c.lower()] += 1
            else:
                letters[c.lower()] = 1
            count += 1
    return letters, count

def check_dict(letters, count):
    if count % 2 == 1:
        found_odd = False
        for c in letters:
            if letters[c]%2 == 1:
                if found_odd == False:
                    found_odd = True
                else:
                    return False
    else:
        for c in letters:
            if letters[c]%2 == 1:
                return False
    return True

def pal_permute(my_str):
    letters, count = make_dict(my_str)
    return check_dict(letters, count)

print(pal_permute('Tact Coa'))