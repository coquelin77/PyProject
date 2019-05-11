from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "127.0.0.1", "port": 9200, "timeout": 15000}])
es_Test = Elasticsearch([{"host": "127.0.0.1", "port": 9200}])

#创建index索引
#创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
#这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
es.indices.create(index='my-index',ignore)

#插入数据
#插入数据,(这里省略插入其他两条数据，后面用)
es.index(index="my-index",doc_type="test-type",id=01,body={"any":"data01","timestamp":datetime.now()})

#get获取数据
#查询数据，两种get and search
#get获取
res = es.get(index="my-index", doc_type="test-type", id=01)
es.get(index='indexName', doc_type='typeName', id='idValue')

#删除数据
#delete：删除指定index、type、id的文档
es.delete(index='indexName', doc_type='typeName', id='idValue')

#条件删除
#delete_by_query：删除满足条件的所有数据，查询条件必须符合DLS格式
query = {'query': {'match': {'sex': 'famale'}}}# 删除性别为女性的所有文档
query = {'query': {'range': {'age': {'lt': 11}}}}# 删除年龄小于11的所有文档
es.delete_by_query(index='indexName', body=query, doc_type='typeName')

#条件更新
#update_by_query：更新满足条件的所有数据，写法同上删除和查询

#批量写入、删除、更新
doc = [
    {"index": {}},
    {'name': 'jackaaa', 'age': 2000, 'sex': 'female', 'address': u'北京'},
    {"index": {}},
    {'name': 'jackbbb', 'age': 3000, 'sex': 'male', 'address': u'上海'},
    {"index": {}},
    {'name': 'jackccc', 'age': 4000, 'sex': 'female', 'address': u'广州'},
    {"index": {}},
    {'name': 'jackddd', 'age': 1000, 'sex': 'male', 'address': u'深圳'},
]
doc = [
    {'index': {'_index': 'indexName', '_type': 'typeName', '_id': 'idValue'}}
    {'name': 'jack', 'sex': 'male', 'age': 10}
    {'delete': {'_index': 'indexName', '_type': 'typeName', '_id': 'idValue'}}
    {"create": {'_index': 'indexName', "_type": 'typeName', '_id': 'idValue'}}
    {'name': 'lucy', 'sex': 'female', 'age': 20}
    {'update': {'_index': 'indexName', '_type': 'typeName', '_id': 'idValue'}}
    {'doc': {'age': '100'}}
]
es.bulk(index='indexName',doc_type = 'typeName', body = doc)

# 批量更新也可以采用如下的方式进行json拼装，最后写入
for line in list:
    action = {
        "_index": self.index_name,
        "_type": self.index_type,
        "_id": i,  # _id 也可以默认生成，不赋值
        "_source": {
            "date": line['date'],
            "source": line['source'].decode('utf8'),
            "link": line['link'],
            "keyword": line['keyword'].decode('utf8'),
            "title": line['title'].decode('utf8')}
    }
    i += 1
    ACTIONS.append(action)
success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)

#搜索所有数据
es.search(index="my_index",doc_type="test_type")
# 或者
body = {
    "query":{
        "match_all":{}
    }
}
es.search(index="my_index",doc_type="test_type",body=body)

#term与terms
#term
body = {
    "query":{
        "term":{
            "name":"python"
        }
    }
}
# 查询name="python"的所有数据
es.search(index="my_index",doc_type="test_type",body=body)
#terms
body = {
    "query":{
        "terms":{
            "name":[
                "python","android"
            ]
        }
    }
}
# 搜索出name="python"或name="android"的所有数据
es.search(index="my_index",doc_type="test_type",body=body)

# match:匹配name包含python关键字的数据
body = {
    "query":{
        "match":{
            "name":"python"
        }
    }
}
# 查询name包含python关键字的数据
es.search(index="my_index",doc_type="test_type",body=body)

# multi_match:在name和addr里匹配包含深圳关键字的数据
body = {
    "query":{
        "multi_match":{
            "query":"深圳",
            "fields":["name","addr"]
        }
    }
}
# 查询name和addr包含"深圳"关键字的数据
es.search(index="my_index",doc_type="test_type",body=body)

body = {
    "query":{
        "ids":{
            "type":"test_type",
            "values":[
                "1","2"
            ]
        }
    }
}
# 搜索出id为1或2d的所有数据
es.search(index="my_index",doc_type="test_type",body=body)

body = {
    "query":{
        "bool":{
            "must":[
                {
                    "term":{
                        "name":"python"
                    }
                },
                {
                    "term":{
                        "age":18
                    }
                }
            ]
        }
    }
}
# 获取name="python"并且age=18的所有数据
es.search(index="my_index",doc_type="test_type",body=body)
