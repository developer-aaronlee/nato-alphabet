import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# nato_dict = {}
# for (x, y) in nato_df.iterrows():
#     nato_dict[y.letter] = y.code

nato_dict = {y.letter: y.code for (x, y) in nato_df.iterrows()}

# output = []
# for x in user_input:
#     word = nato_dict[x]
#     output.append(word)

def generate():
    user_input = input("What's the word to spell out? ").upper()
    try:
        output = [nato_dict[x] for x in user_input]
    except KeyError:
        print("Please enter letters in the alphabets.")
        generate()
    else:
        print(output)

generate()