import pickle
import random

import markovify

with open("title_pickle", "rb") as load_file:
    load_dict = pickle.load(load_file)
    title_list = list(load_dict["title_set"])
    title_text = '\n'.join(title_list)

text_model = markovify.NewlineText(title_text)

print(len(title_text))

# sentence = text_model.make_sentence()
# while sentence is None or not sentence.startswith("I was Reincarnated as"):
#     sentence = text_model.make_sentence()
# print(sentence)

while True:
    real = random.getrandbits(1)
    print("Is this real or fake? ", end=None)
    if real:
        _ = input(f"{random.choice(title_list)}")
    else:
        _ = input(f"{text_model.make_sentence()}")
    print(f"It's {'real' if real else 'fake'}\n")