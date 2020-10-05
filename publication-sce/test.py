from datetime import date
import pandas as pd
import os
from scholarly import scholarly
import json


# scholarly tests

# check if a professor is present or not



############### Getting scholar Names from Id
'''
noAccount=[]
df = pd.read_csv("profScholarId.csv")

#authorId = df.values.tolist()

authorId = df.stack().tolist()

#print(authorId)
noAuthorId=[]
authorNames= pd.DataFrame(columns=['name'])


for a in authorId:

    try:
        print("reading the author id")
        print(a)
        author = scholarly.search_author_id(a)
        name = author.name
        print(name)
        authorNames = authorNames.append({'name':name}, ignore_index=True)
        time.sleep(300)

    except:
        noAuthorId.append(a)
        print(" author id " + a + "is not present" )


#authorNames.to_json('scholarNames.json')
authorNames.to_csv("sNames.csv",index=False)
print(" exported the names to a csv file ")

'''
######### ending scholar names from scholar ID

####### when the name is same for scholarly erro handling
#author = scholarly.search_author_id('Ni6CAs8AAAAJ')

search_query = scholarly.search_author('Mostafa Taha')

print(next(search_query))



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