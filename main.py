import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

# new_key = {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry you can only enter letters')
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
