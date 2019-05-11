from elasticsearch import Elasticsearch
es = Elasticsearch([{"host":"localhost","port":9200}])
es.delete(index='bank', doc_type='typeName', id='idValue')