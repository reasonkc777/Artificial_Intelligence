import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')  

def perform_stemming(text):
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

text = "Stemming is an important step in natural language processing. It helps to reduce words to their root form."

stemmed_text = perform_stemming(text)
print("Original Text:")
print(text)
print("\nStemmed Text:")
print(stemmed_text)
