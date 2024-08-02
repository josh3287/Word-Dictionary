# Collect input from user
def main():
    word_dictionary = {
        'Zeus': 'God of The Sky and Thunder',
        'Poseidon': 'God of The Sea',
        'Hades': 'God of the Underworld',
        'Hera': 'Goddess of Marriage and Childbirth',
        'Hestia': 'Goddess of the Hearth'
    }
    while True:
        word = input("Which Greek god would you like to know about?: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()