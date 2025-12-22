


import re


def characterBasedTokenizer(text):
    words=[]

    for i in text:
        if i!=" ":
            words.append(i)
    words=sorted(set(words))

    vocab={a:i for i,a in enumerate(words)}
    print(vocab)
    return vocab


characterBasedTokenizer("hello world")

