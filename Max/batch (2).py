from elasticsearch import Elasticsearch
es = Elasticsearch([{"host":"localhost","port":9200}])
with open('./accounts.json','r',encoding='utf-8') as file:
    s =file.read()
    print(s)
    es.bulk(index='bank',doc_type='typeName',body=s)