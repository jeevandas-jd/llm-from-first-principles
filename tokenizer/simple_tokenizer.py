import re

class SimpleTokenizer:
    def __init__(self, vocab):
        self.token_to_id = vocab
        self.id_to_token = {i: t for t, i in vocab.items()}
        self.unk_token = "<UNK>"

    def encoder(self, text: str):
        tokens = re.split(r"[,.:;!_()?'\"]|--|\s", text)
        tokens = [t.strip() for t in tokens if t.strip()]
        return [self.token_to_id.get(t, self.token_to_id[self.unk_token]) for t in tokens]

    def decoder(self, ids):
        return " ".join(self.id_to_token[i] for i in ids)
