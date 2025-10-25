#import library 
from googlesearch import search

#write your query
query = "best course for python"

# displaying 10 results from the search
for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)
#you will notice the 10 search results(website links) in the output.