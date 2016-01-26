__author__ = 'Manuel Bordes'
# https://www.hackerrank.com/challenges/byte-the-correct-apple
# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
# http://zacstewart.com/2015/04/28/document-classification-with-scikit-learn.html
# coding:utf-8
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

train={}
train['text']=[]
train['class']=[]

with open('apple-computers.txt', 'r') as f:
    for line in f:
        train['text'].append(line)
        train['class'].append(0)

with open('apple-fruit.txt', 'r') as f:
    for line in f:
        train['text'].append(line)
        train['class'].append(1)

pipeline = Pipeline([
    ('vectorizer',  CountVectorizer(ngram_range=(1, 2),stop_words='english')),
    ('classifier',  MultinomialNB()) ])

text_clf = pipeline.fit(train['text'], train['class'])

test=[]
for i in range(int(raw_input())):
	s=raw_input()
	test.append(s)

test_label=text_clf.predict(test)
for e in test_label: print('computer-company' if e==0 else 'fruit')

