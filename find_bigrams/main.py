
def find_bigrams(sentence):

    def format_word(word):
        return word.strip().lower()

    bigrams = []
    words = sentence.split(' ')
    for i in range(len(words) - 1):
        bigramsItem = (format_word(words[i]), format_word(words[i+1].strip()))
        bigrams.append(bigramsItem)

    return bigrams

sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""

result = find_bigrams(sentence)

print(result)

