from elasticsearch import Elasticsearch
import time
import datetime

es = Elasticsearch(hosts=['35.172.3.21:39200'])

def main():
    index_name = 'userevent'
    type_name = 'userevent'

    ##########################################
    # 查看所有索引
    alias = es.indices.get_alias()
    #print(alias)

    # 查询所有index名称
    result = es.indices.get_alias().keys()
    #print(result)

    # 查询index信息,包含mapping  settings信息
    result = es.indices.get(index_name)
    #print(result)

    # 查询所有数据
    result = es.search(index=index_name, doc_type=type_name)
    #print(result)
    #print(result['hits']['hits'])

     # 指定条件查询
    #query_body = {'query': {'term': {'from': 'NULL'}}}

    ts = int(round(time.time()*1000))

    query_body = {'query': {'range': {'createtime': {"gte":ts-1000*60*6,'lte':ts}}}}
    result = es.search(index=index_name, doc_type=type_name, body=query_body)
    #print(result)
    print(result['hits']['hits'])

if __name__ == '__main__':
    main()