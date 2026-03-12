import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


def preprocess(text):

    stop_words = set(stopwords.words('english'))

    tokens = word_tokenize(text.lower())

    words = [w for w in tokens if w.isalnum() and w not in stop_words]

    return " ".join(words)