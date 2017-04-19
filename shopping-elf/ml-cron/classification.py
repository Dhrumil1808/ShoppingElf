from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB


from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

with open("data-set.txt","r") as text_file:
    lines = text_file.read().split("\n")

lines= [line.split("|") for line in lines if ((len(line.split("|"))==2) and (line.split("|")[1]<> ''))]
training_documents = [line[0] for line in lines]
#print training_documents
training_labels = [line[1] for line in lines]
#print  training_labels
# fit a k-nearest neighbor model to the data
model = KNeighborsClassifier()
count_vectorizer = CountVectorizer(binary='true')

training_documents = count_vectorizer.fit_transform(training_documents)

model.fit(training_documents, training_labels)


print(model)
# make predictions
expected = "1"
predicted = model.predict(count_vectorizer.transform(["bread"]));
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


with open("data-set.txt","r") as text_file:
    lines = text_file.read().split("\n")

lines= [line.split("|") for line in lines if ((len(line.split("|"))==2) and (line.split("|")[1]<> ''))]
training_documents = [line[0] for line in lines]
#print training_documents
training_labels = [line[1] for line in lines]
#print  training_labels
count_vectorizer = CountVectorizer(binary='true')

training_documents = count_vectorizer.fit_transform(training_documents)
#print  training_documents
baker_classfier= BernoulliNB().fit(training_documents,training_labels)
print baker_classfier.predict(count_vectorizer.transform(["bread"]))
print count_vectorizer.transform(["bread"])


with open("data-set0.txt","r") as text_file:
    lines = text_file.read().split("\n")

lines= [line.split("|") for line in lines if ((len(line.split("|"))==2) and (line.split("|")[1]<> ''))]
training_documents1 = [line[0] for line in lines]
#print training_documents
training_labels1 = [line[1] for line in lines]
#print  training_labels
count_vectorizer = CountVectorizer(binary='true')

training_documents1 = count_vectorizer.fit_transform(training_documents1)
#print  training_documents
oil_classfier= BernoulliNB().fit(training_documents1,training_labels1)
print oil_classfier.predict(count_vectorizer.transform(["bread"]))
print count_vectorizer.transform(["bread"])




with open("data-set1.txt","r") as text_file:
    lines = text_file.read().split("\n")

lines= [line.split("|") for line in lines if ((len(line.split("|"))==2) and (line.split("|")[1]<> ''))]
training_documents2 = [line[0] for line in lines]
#print training_documents
training_labels2 = [line[1] for line in lines]
#print  training_labels
count_vectorizer = CountVectorizer(binary='true')

training_documents2 = count_vectorizer.fit_transform(training_documents2)
#print  training_documents
cerial_classfier= BernoulliNB().fit(training_documents2,training_labels2)
print cerial_classfier.predict(count_vectorizer.transform(["bread"]))
