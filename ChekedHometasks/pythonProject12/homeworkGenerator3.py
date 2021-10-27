
sentence = "thequick brown fox jumps over the lazy dog"
newline = [len(word) for word in sentence.split(' ') if word != "the"]
print(newline)

