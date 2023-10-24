import Letters
import functions

print("Hello , welcome to the Caesar Cipher :) ")
word = input("please enter your word : ")
number = int(input("please enter your number : "))
word = functions.encode(word, Letters.alphabet, number)
print(word)
