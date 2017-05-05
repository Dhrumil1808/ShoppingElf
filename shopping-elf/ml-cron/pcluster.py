import string
import collections

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint


def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t.lower()) for t in tokens]
    return tokens


def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
    print articles;
    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans()
    km_model.fit(tfidf_model)
    #pred= vectorizer.fit_transform(["bread","whole-wheat","help","oats","pita"])
    #print pred
    #out = km_model.predict(pred)
    #print "ssssss";
    #print out;

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    return clustering


if __name__ == "__main__":
    articles = []
    with open("data/product-data.txt","r") as text_file:
        lines = text_file.read().split("\n")

    for i in lines:
        #print i
        articles.append(i)
    clusters = cluster_texts(articles, 10)
    pprint(dict(clusters))

    for c in clusters:
        #print clusters[c]
        print "cluster-----****"
        a =clusters[c]
        for p in a:
            #print p
            print articles[p]
