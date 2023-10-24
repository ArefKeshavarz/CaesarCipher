# function for encode word :
def encode_decode(word, alphabet, number, activity):
    word = list(word)
    for letter_of_word in word:
        if (activity == "encode"):
            new_letter_of_word = alphabet[int(alphabet.index(letter_of_word)) + number]
        elif (activity == "decode"):
            new_letter_of_word = alphabet[int(alphabet.index(letter_of_word)) - number]
        word[int(word.index(letter_of_word))] = new_letter_of_word
    word = "".join(word)
    return word
