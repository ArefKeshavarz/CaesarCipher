# function for encode word :
def encode(word, alphabet, number):
    word = list(word)
    for letter_of_word in word:
        new_letter_of_word = alphabet[int(alphabet.index(letter_of_word)) + number]
        word[int(word.index(letter_of_word))] = new_letter_of_word
    word = "".join(word)
    return word
# function for decode word :

