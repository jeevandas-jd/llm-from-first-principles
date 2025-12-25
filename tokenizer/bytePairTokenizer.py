


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


#haracterBasedTokenizer("hello world")


import tiktoken 


text=("hello world this is jeevandas welcome to my youtube channel")

tokenizer=tiktoken.get_encoding("gpt2")

encoded=tokenizer.encode(text=text)

print(encoded)

decoded=tokenizer.decode(encoded)

print(f"decoded text : \n {decoded}")