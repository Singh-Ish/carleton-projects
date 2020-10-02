from scholarly import scholarly
import pandas as pd
import json
from datetime import date
import time

#author = scholarly.search_author_id('iM8ssiUAAAAJ')
# single professor

'''
search_query = scholarly.search_author('Mostafa Taha')
author = next(search_query).fill()
print(author)

'''
# multiple professor response

authors= ['Mostafa Taha','Andy Adler','Halim Yanikomeroglu','Yvan Labiche'] # name of professors to consider


#defining the dataframes
publication_df = pd.DataFrame(columns=['id','name', 'title','cites','year'])
author_df = pd.DataFrame(columns=['id','name','affiliation','interest','citedby','citedbyyear','hindex','hindex5y','i10index','i10index5y'])

for a in authors:
    search_query = scholarly.search_author(a)
    author = next(search_query).fill()

    print("reading the " + author.name + "from google scholar")
    # assigning id and name
    id = author.id
    name = author.name


    # author details
    a = author.affiliation
    b = author.citedby
    c = author.cites_per_year
    h = author.hindex
    h5 = author.hindex5y
    i = author.i10index
    i10 = author.i10index5y
    interest = author.interests

    author_df = author_df.append(
        {'id': id, 'name': name, 'affiliation': a, 'interest': interest, 'citedby': b, 'citedbyyear': c, 'hindex': h,
         'hindex5y': h5, 'i10index': i, 'i10index5y': i10}, ignore_index=True)

    author_df.sort_values(by=['name'])

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

        publication_df = publication_df.append({'id': id, 'name': name, 'title': title, 'cites': cites, 'year': year},
                                         ignore_index=True)


    publication_df.sort_values(by=['cites'])

    # time to sleep for 30 minutes
    time.sleep(1800)

# export author and publication database
today = str(date.today())
author_file = "author" + today +".xlsx"
author_df.to_excel(author_file)
print(" exporting the author dataframe")

publication_file= "publication" + today+ ".xlsx"
publication_df.to_excel(publication_file)
print("exporting the publciation dataframe")