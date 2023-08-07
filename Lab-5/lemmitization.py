import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt') 
nltk.download('wordnet')  

def perform_lemmatization(text):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)

text = "Lemmatization is the process of reducing words to their base or root form."

lemmatized_text = perform_lemmatization(text)
print("Original Text:")
print(text)
print("\nLemmatized Text:")
print(lemmatized_text)
