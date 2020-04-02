# Valerie Nayak
# 4/2/2020
# Cracking the Coding Interview, p. 90
# 1.3: URLify

def urlify(start): # start is the starting str
    words = start.split(' ')
    url = ''
    for w in words[:-1]:
        url += w + '%20'
    url += words[-1]
    return url

print(urlify('Mr John Smith'))
print(urlify('Mr'))