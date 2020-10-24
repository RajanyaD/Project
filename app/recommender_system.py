# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:56:49 2020

@author: rajan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class BookDetails:
    def __init__(self,user_id,isbn,rating):
        self.user_id = user_id
        self.isbn = isbn
        self.rating = rating
      
import csv

with open('Book reviews/BX-Book-Ratings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    array=[]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]}, {row[1]}, {row[2]}.')
            ob = BookDetails(int(row[0]), {row[1]}, {row[2]})
            array.append(ob)

        line_count += 1
    print(f'Processed {line_count} lines.')
    
newarr = sorted(array,key=lambda x:x.user_id)

from collections import defaultdict
data=defaultdict(list)
#previd=2

for i in range(1149780):
    print(str(newarr[i].user_id)+"  "+repr(newarr[i].isbn)[2:-2])
    data[str(newarr[i].user_id)].append(repr(newarr[i].isbn)[2:-2])

values=[]
for key in data:
    values.append(data[key])

from apyori import apriori
rules = apriori(values,min_support=0.001,min_confidence=0.01,min_lift=4)

result = list(rules)    

val=[]
for i in range(99):
    a = repr(result[i].items)[12:-3].split("', '")
    val.append(a)

dataset = pd.read_csv('book1000k-1100k.csv') 

books = defaultdict(list)

for i in range(39705):
    arr = [dataset['Name'][i],dataset['Authors'][i],dataset['Rating'][i],dataset['PublishYear'][i],dataset['Publisher'][i],
            dataset['Language'][i],dataset['pagesNumber'][i],dataset['Description'][i]]
    books[dataset['ISBN'][i]].append(arr) 
    
dictval=defaultdict(list)
for i in range(99):
    dictval[i].append(val[i])

    
import flask
import werkzeug

app = flask.Flask(__name__)
@app.route("/")
def post_val():
    return dictval
if __name__=="__main__":
    app.run()