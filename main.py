import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name:").upper()

nato_list = [nato_dict[letter] for letter in name]
print(nato_list)
