import string
import collections

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint


def reduce_words (text):
    text = text.translate(string.punctuation)



def process_text(text, stem=True):
    print text
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(string.punctuation)

    print text

    tokens = word_tokenize(text)
    if len(tokens)!=0:
        if stem:
            stemmer = PorterStemmer()
            tokens = [stemmer.stem(t.lower()) for t in tokens]
    else:
        tokens=[]
        tokens.append(text)
    print "**********************"

    print text

    print tokens
    print "**********************"


    return tokens


def find_all_products(allProducts,allClusters,product):
        productsInCluster =[];
        if product in allProducts:
            index = allProducts.index(product);
            for c in allClusters:
                eachClusterProducts =allClusters[c]
                if index in eachClusterProducts:
                    output = eachClusterProducts

            for eachIndex in output:
                productsInCluster.append(allProducts[eachIndex])

        return productsInCluster

def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)

    print texts

    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans()
    km_model.fit(tfidf_model)


    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    return clustering



def testclustering():
    articles = []
    with open("data/product-data.txt","r") as text_file:
        lines = text_file.read().split("\n")

    articles =['YELLOW MANGOS', 'LARGE NAVEL ORANGES', 'CANTAIOUPE MELONS', 'CANTALOUPE MELONS', "\\'J ELLOW BANANAS", 'HALF PT BLUEBERRIES', 'I:! T T in', 'X LG HASS AVOCADOS', 'HALF RT BLUEBERRIES', 'CUCUMBERS', 'CLUSTER TOMATOES', 'YELLOW BANANAS', 'MINI HATERHELON', 'ORG STRAWBERRIES', 'REDUCED FAT MILK', 'LIMES', 'DANJOU PEARS', 'RASPBERRIES', 'PURPLE SWEET POTATO', 'X LG HASSlAggCADOS'];

    #for i in lines:
        #print i
        #articles.append(i)


    clusters = cluster_texts(articles, 10)
    pprint(dict(clusters))

    for c in clusters:
        #print clusters[c]
        print "cluster-----****"
        print  c
        a =clusters[c]
        for p in a:
            #print p
            print articles[p]


    products = find_all_products(articles,clusters,"PURPLE SWEET POTATO")
    print products

testclustering()