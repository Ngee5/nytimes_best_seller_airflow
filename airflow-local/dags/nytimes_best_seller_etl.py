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
print(data_convert)

# json_df = pd.read_json(data)
# print(json_df.to_string())

print(r.json())

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




