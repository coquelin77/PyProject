from elasticsearch import Elasticsearch
es = Elasticsearch([{"host":"localhost","port":9200}])
find=es.get(index='bank', doc_type='typeName', id='idValue')
print(find)