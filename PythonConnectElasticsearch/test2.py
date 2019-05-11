from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "127.0.0.1", "port": 9200, "timeout": 15000}])
es_Test = Elasticsearch([{"host": "127.0.0.1", "port": 9200}])

# p=es.search(index="douban_movie")
# print(p)
body = {
    "query":{
        "match_all":{}
    }
}
p=es.search(index="douban_movie",body=body)
print(p)