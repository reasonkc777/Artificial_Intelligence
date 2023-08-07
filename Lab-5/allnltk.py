import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')  
nltk.download('stopwords')  
nltk.download('wordnet')  

def process_text(text):
    # Tokenization
    words = word_tokenize(text)
    

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    

    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]
    
    return lemmatized_words


text = "Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language."

processed_words = process_text(text)
print("Original Text:")
print(text)
print("\nProcessed Words:")
print(processed_words)
