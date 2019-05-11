from elasticsearch import Elasticsearch
es = Elasticsearch([{"host":"localhost","port":9200}])
es.update(index='bank', doc_type='typeName', id='idValue', body={待更新字段})