from scholarly import scholarly

#author = scholarly.search_author_id('iM8ssiUAAAAJ')

search_query = scholarly.search_author('Mostafa Taha')
author = next(search_query).fill()
print(author)
