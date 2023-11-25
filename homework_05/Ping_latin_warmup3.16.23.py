# return a string where str is converted into pig latin
# move the first letter to the end and add "ay"
# examples: 
# pig --> igpay
# latin --> atinlay
def to_pig_latin(str):
    return str[1:] + str[0] + "ay"

# take a string that's in pig latin already and convert it back to English
# think about what letter from the end gets moved to the front
# example: eversalray -> reversal
def decode_pig_latin(str):
    return str[len(str)-3:len(str)-2] + str[0:len(str)-3]

# You can test your code using:
print(to_pig_latin("pig"))   # igpay
print(to_pig_latin("latin"))  # atinlay

print(decode_pig_latin("eversalray"))  # reversal
print(decode_pig_latin("igpay")) # pig