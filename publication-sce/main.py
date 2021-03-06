from scholarly import scholarly
import pandas as pd
import json
from datetime import date
import time
import os

#author = scholarly.search_author_id('iM8ssiUAAAAJ')
# single professor
today = str(date.today()) # todays date
'''
search_query = scholarly.search_author('Mostafa Taha')
author = next(search_query).fill()
print(author)

'''
# multiple professor response

#authors= ['Mostafa Taha','Andy Adler','Halim Yanikomeroglu','Yvan Labiche'] # name of professors to consider

df = pd.read_csv('sNames.csv') # reading author names from the csv list
#authors = df.stack().tolist()
#print(authors)

#defining the dataframes
publication_df = pd.DataFrame(columns=['id','name', 'title','cites','year'])
author_df = pd.DataFrame(columns=['id','name','affiliation','interest','citedby','citedbyyear','hindex','hindex5y','i10index','i10index5y'])
notSameAuthor = pd.DataFrame(columns=['name'])


for row in df.index:
    a = df['name'][row]
    oid = df['id'][row]

    #print(a , " ", id)

    search_query = scholarly.search_author(a)
    author = next(search_query).fill()

    print("reading the " + author.name + "from google scholar")
    # assigning id and name
    id = author.id
    name = author.name

    if id == oid:  # its the same author if that we want to scrap
        aff = author.affiliation
        b = int(author.citedby)
        c = author.cites_per_year
        h = float(author.hindex)
        h5 = float(author.hindex5y)
        i = float(author.i10index)
        i10 = float(author.i10index5y)
        interest = author.interests

        author_df = author_df.append( {'id': id, 'name': name, 'affiliation': a, 'interest': interest, 'citedby': b, 'citedbyyear': c, 'hindex': h, 'hindex5y': h5, 'i10index': i, 'i10index5y': i10}, ignore_index=True)

        # iterating all publications
        print("reading the publications for " + author.name)
        for z in author.publications:

            data = z.bib
            # print(data)
            pub_json = json.dumps(data)
            pj = json.loads(pub_json)
            if ("year" in pj):
                year = int(pj['year'])
            else:
                year = 0

            title = str(pj['title'])
            cites = int(pj['cites'])

            publication_df = publication_df.append( {'id': id, 'name': name, 'title': title, 'cites': cites, 'year': year}, ignore_index=True)

        # can add a step to add the author to the database or export it to an excel

        # time to sleep for 15 minutes
        time.sleep(900)

    else:
        print("author id did not match to the name")
        notSameAuthor = notSameAuthor.append({'name':name},ignore_index=True)




# sorting the values based on name an publication cites
publication_df.sort_values(by=['cites'])
author_df.sort_values(by=['name'])

# adding the last updated coloum to the dataframes
author_df['lastUpdated'] = today
publication_df['lastUpdated'] = today


# export author and publication database

cwd = os.getcwd()

path = os.path.join(cwd , "data")
author_file = "author" + today +".xlsx"

pathAuth = os.path.join(path , author_file)

author_df.to_excel(pathAuth, index=False)
author_df.to_csv("author.csv",index=False) # exporting to author csv
print(" exporting the author dataframe to author csv and /data/author-date")

publication_file= "publication" + today+ ".xlsx"
pathPub = os.path.join(path , publication_file)
publication_df.to_excel(pathPub, index=False)
publication_df.to_csv("publications.csv",index=False)
print("exporting the publciation dataframe to publication csv and /data/publication-date ")



print("can't find the below author details ")
print(notSameAuthor)
notSameAuthor.to_csv("notScrappedAuthor.csv",index=False)

