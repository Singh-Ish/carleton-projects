import pandas as pd
from scholarly import scholarly



# scholarly tests

# check if a professor is present or not

noAccount=[]

############### Getting scholar Names from Id

df = pd.read_csv("profScholarId.csv")

#authorId = df.values.tolist()

authorId = df.stack().tolist()

#print(authorId)
noAuthorId=[]
authorNames= pd.DataFrame(columns=['name','id'])


for a in authorId:

    try:
        print("reading the author id")
        print(a)
        author = scholarly.search_author_id(a)
        name = author.name
        id = author.id
        #print(name)
        authorNames = authorNames.append({'name':name,'id':id}, ignore_index=True)
        time.sleep(300)

    except:
        noAuthorId.append(a)
        #print(" author id " + a + "is not present" )


#authorNames.to_json('scholarNames.json')
authorNames.to_csv("sNames.csv",index=False)
print(" exported the names to a csv file ")