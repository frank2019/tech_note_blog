#coding='UTF-8'
from elasticsearch import Elasticsearch
import time
import datetime

es = Elasticsearch(hosts=['35.172.3.21:39200'])

def main():
    index_name = 'userevent'
    type_name = 'userevent'

    ##########################################
    # get index name
    alias = es.indices.get_alias()
    #print(alias)

    # get index name
    result = es.indices.get_alias().keys()
    #print(result)

    #  mapping  settings
    result = es.indices.get(index_name)
    #print(result)

    # 
    result = es.search(index=index_name, doc_type=type_name)
    #print(result)
    #print(result['hits']['hits'])

     # 
    #query_body = {'query': {'term': {'from': 'NULL'}}}

    ts = int(round(time.time()*1000))

    print("test-->")

    query_body = {'query': {'range': {'createtime': {"gte":ts-1000*60*60*24,'lte':ts}}}}
    result = es.search(index=index_name, doc_type=type_name, body=query_body)
    #print(result)
    print(result['hits']['hits'])

if __name__ == '__main__':
    main()