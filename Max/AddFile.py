from elasticsearch import Elasticsearch
es = Elasticsearch([{"host":"localhost","port":9200}])
print(es.cluster.state())
b= {"name": 'lu', 'sex':'female', 'age': 10}
es.index(index='bank', doc_type='typeName',body=b,id=None)
print(es.cluster.state())