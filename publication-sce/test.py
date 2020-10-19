from datetime import date
import pandas as pd
import os
from scholarly import scholarly
import json


# scholarly tests

# check if a professor is present or not





######### ending scholar names from scholar ID

####### when the name is same for scholarly erro handling
#author = scholarly.search_author_id('Ni6CAs8AAAAJ')

#search_query = scholarly.search_author('Mostafa Taha')

#print(next(search_query))


###### getting the author names from the excel sheet

df = pd.read_csv('sNames.csv')

#author = df['name'].tolist()
for row in df.index:
    author = df['name'][row]
    id = df['id'][row]

    print(author , " ", id)



'''

############ extract from google scholarly and compare it to verify

search_query = scholarly.search_author(a)
author = next(search_query).fill()
#print([pub.bib['title'] for pub in author.publications])
publication_df = pd.DataFrame(columns=['id', 'name', 'title', 'cites', 'year'])
author_df = pd.DataFrame(columns=['id', 'name', 'affiliation', 'interest', 'citedby', 'citedbyyear', 'hindex', 'hindex5y', 'i10index',
                 'i10index5y','email'])

#print(type(author))
# scrapping google scholarly results and saving them

if author.id == id:
    #print(author)

    # author details
    name = author.name
    a = author.affiliation
    b = int(author.citedby)
    c = author.cites_per_year
    h = float(author.hindex)
    h5 = float(author.hindex5y)
    i = float(author.i10index)
    i10 = float(author.i10index5y)
    interest = author.interests
    e = author.email

    author_df = author_df.append(
        {'id': id, 'name': name, 'affiliation': a, 'interest': interest, 'citedby': b, 'citedbyyear': c, 'hindex': h,
         'hindex5y': h5, 'i10index': i, 'i10index5y': i10 , 'email':e}, ignore_index=True)

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

        query = scholarly.search_pubs(title)
        pub = next(query)
        data = pub.bib

        abstract = data['abstract']
        url = data['url']

        publication_df = publication_df.append({'id': id, 'name': name, 'title': title, 'cites': cites, 'year': year},
                                         ignore_index=True)

        # add a time delay for extracting a publication details

    publication_df.sort_values(by=['cites'])

else:
    print('false')

print(author_df)
print(publication_df)


###### extracting publications
query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
pub = next(query)


data = pub.bib
abstract = data['abstract']
url = data['url']

print(abstract)
print(url)




'''
'''
# other test
today = date.today()
today = str(today)
print("Today's date:", today)

print(type(today))

Bike = {
        'bikes': ['Yamaha R1','Hero Hunk','KTM RC','Kawasaki Ninja'],
        'Price': [220000,251000,270400,350500]
        }
df = pd.DataFrame(Bike)
today = str(date.today())

# exporting the files
cwd = os.getcwd()

path = os.path.join(cwd , "data")
author_file = "author" + today +".xlsx"
path = os.path.join(path , author_file)

print(path )


df.to_excel(path, index=False)
print("exported the file ")

'''