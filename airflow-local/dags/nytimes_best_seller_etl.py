import os
import json
import secrets
import time
import requests
from requests import api
from requests.auth import HTTPBasicAuth
import datetime
import pandas as pd

#authenication to access the api
api_key = "HuJ1SA6Xh3QU48PtwRCcpaO303K8idOD"
secrets = "UwuXpO2vCkyXIT5Y"

#requirement for type of book extraction
books = ["combined-print-and-e-book-fiction", "combined-print-and-e-book-nonfiction"]

#download the list of books 
for book in books:
    url = f"https://api.nytimes.com/svc/books/v3/lists/current/{book}.json?api-key={api_key}"
    r = requests.get(url)

data = r.json()
data_convert = json.dumps(data)
# print(data_convert)

#use pandas to read the json file & add column names
times = pd.read_json(data_convert)
times.columns = ['data_type','status','copyright','last_modified','results']
times['last_modified'] = pd.to_datetime(times['last_modified']).dt.tz_convert(None)
times['today'] = datetime.datetime.now()
# print(days_convert)

times['days_diff'] = times['today'].dt.date - times['last_modified'].dt.date

times['days_diff'] = times['days_diff'].dt.days.astype('int16')

success = 0
for time in times['days_diff']:
    if int(time) > 7:
        success += 1
    else:
        success = 1

print(success)



# print(last_modified)
    

# json_df = pd.read_json(data)
# print(json_df.to_string())

# print(r.json())

'''
title = []
description = []
author = []
price = []
publisher = []
primary_isbn10 = []

#extracting only the relevant bits of data from the json object
for details in data["results"]:
    title.append(details["title"])
    description.append(details["description"])
    author.append(details["author"])
    price.append(details["price"])
    publisher.append(details["publisher"])
    primary_isbn10.append(details["primary_isbn10"])

print(title)

book_dict = { 

        "title" : title,
        "description" : description,
        "author" : author,
        "price" : price,
        "publisher" : publisher,
        "primary_isbn10" : primary_isbn10
}

book_df = pd.DataFrame(book_dict, columns = ["title", "description","author", "price","publisher","primary_isbn10"])

book_df.to_csv("NyTimes_Bestseller.csv")
'''




