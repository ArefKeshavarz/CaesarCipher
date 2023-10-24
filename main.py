import Letters
import functions

print(" ----> Hello , welcome to the Caesar Cipher :) <---- ")
# receive word :
word = input(" >> please enter your word : ")
word = word.lower()
# for manage exceptions :
while (not word.isalpha()):
    if (not word.isalpha()):
        print(" >>> word is wrong , please enter only a word contain alphba : ")
        word = input(">> please enter your word : ")
        word = word.lower()
# receive shift number :
number_is_wrong = True
# for manage exceptions :
while (number_is_wrong):
    try:
        number = int(input(" >> please enter shift number : "))
        number_is_wrong = False
    except:
        print(" >>> input is wrong . ")
        number_is_wrong = True
# receive activity :
activity = input(" >> please enter your activity :  'encode' to encrypt , 'decode' to decrypt :")
# for manage exceptions :
while (not (activity == "encode" or activity == "decode")):
    print(" >>> input is wrong .")
    activity = input(" >> please enter your activity :  'encode' to encrypt , 'decode' to decrypt :")
word = functions.encode_decode(word, Letters.alphabet, number, activity)
print(word)
