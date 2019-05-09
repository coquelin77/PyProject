from datetime import datetime
import io
import elasticsearch
from elasticsearch import Elasticsearch
es = Elasticsearch([{"host":"localhost","port":9200}])
#with open('./accounts.json','r',encoding='utf-8') as file:
#    s =file.read()
    #print(s)
#    es.bulk(index='bank',doc_type='typeName',body=s)

#b= {"name": 'lucy', 'sex':'female', 'age': 10}
#es = Elasticsearch(['localhost:9200'])
#es.index(index='bank', doc_type='typeName',body=b,id=None)

#es.delete(index='bank', doc_type='typeName', id='idValue')

#es.get(index='bank', doc_type='typeName', id='idValue')

#es.update(index='bank', doc_type='typeName', id='idValue', body={待更新字段})


print(es.cluster.state())

print(es.cluster.health())