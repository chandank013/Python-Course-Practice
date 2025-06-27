# Telegram: string to Morse code   # text = defence

codes = ['._','_...','_._','_..','.','.._.','__.','....','..','.___']

# # . short press
# # __ long press
morse_str = ''
text = 'deface'
for x in text:
    morse_str += codes[ord(x) - 97] + " "

print(morse_str)

