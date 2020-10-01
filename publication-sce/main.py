from scholarly import scholarly

#author = scholarly.search_author_id('iM8ssiUAAAAJ')
# single professor

'''
search_query = scholarly.search_author('Mostafa Taha')
author = next(search_query).fill()
print(author)

'''
# multiple professor response

authors= ['Mostafa Taha']#,'Andy Adler'] # name of professors to consider


#defining the dataframes
publication_df = pd.DataFrame(columns=['id','name', 'title','cites','year'])
author_df = pd.DataFrame(columns=['id','name','affiliation','interest','citedby','citedbyyear','hindex','hindex5y','i10index','i10index5y'])

for a in authors:
    search_query = scholarly.search_author(a)
    author = next(search_query).fill()
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
    for z in author.publications:

        data = z.bib
        # print(data)
        pub_json = json.dumps(data)
        pj = json.loads(pub_json)
        if ("year" in pj):
            year = pj['year']
        else:
            year = 0

        title = pj['title']
        cites = pj['cites']

        publication_df = publication_df.append({'id': id, 'name': name, 'title': title, 'cites': cites, 'year': year},
                                         ignore_index=True)

    publication_df.sort_values(by=['cites'])

# export author and publication database
author_df.to_excel('author.xlsx',engine='xlsxwriter')

publication_df.to_excel('publications.xlsx',engine='xlsxwriter')
