import requests as req
import sys

query = sys.argv[1]
engine = sys.argv[2]


def search(query, engine):
    engines = {'ddg': 'https://duckduckgo.com/?q='}
    url_query = engines[engine] + query
    response = req.get(url_query).text
    return url_query


print(search(query, engine))
