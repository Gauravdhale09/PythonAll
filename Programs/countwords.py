
def countwords(sentence):
    words = sentence.split()
    return len(words)

sentence = "This is a sample sentence."
word_count = countwords(sentence)
print(word_count)