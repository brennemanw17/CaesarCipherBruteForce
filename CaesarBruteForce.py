# Caesar Cipher Brute force
# Written by William S Brenneman
# CSCI 4190 assng 1

#message to be decoded
msg = input('Paste the text you would like cracked:')
msg = msg.upper()

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#loops through all possible keys
for key in range(26):
    decoded = ""

    #decodes message with given key
    for i in msg:
        if i.isspace():
            decoded = decoded + i
        else:
            letter = alph.index(i)
            letter = letter - key
            letter = letter % 26
            decoded = decoded + alph[letter]

    print('Key: %s  Decoded: %s' % (key, decoded))