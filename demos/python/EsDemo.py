#coding='UTF-8'
from elasticsearch import Elasticsearch
import time
#import datetime
from datetime import datetime
import json

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

    #ts = int(round(time.time()*1000))

    ts = int(getTimeStamp('2018-10-02'))
    print("test-->")

    query_body = {'query': {'range': {'createtime': {"gte":ts-1000*60*60*24,'lte':ts}}}}
    result = es.search(index=index_name, doc_type=type_name, body=query_body)
    print(result)
    print(result['hits']['hits'])



def getTimeStamp(vdate_str):
    #vdate_str = '2018-10-02'
    vdate = datetime.strptime(vdate_str, '%Y-%m-%d').date()
    un_time = time.mktime(vdate.timetuple())
    #print(un_time)
    return un_time



def   testEs():

    query_body = {"bool":{"must":{"match":{"eventType":"event_start_show"}}}}

    ts = int(getTimeStamp('2018-10-03'))
    print("test-->")

    query_body = {'query': {'range': {'createtime': {"gte":ts-1000*60*60*24,'lte':ts}}}}

    #res = es.index(index="userevent", doc_type="userevent", id=0, body={"any": "data", "timestamp": datetime.now()})

    query_body = {"size":0,"query":{"constant_score":{"filter":{"terms":{"eventType.keyword":["event_first_visit"]}}}},"aggs":{"user_status":{"filter":{"range":{"createtime":{"gte":0,"lte":1636128296935}}},"aggs":{"uv":{"cardinality":{"field":"userId.keyword"}}}}}}
    res = es.search(index='userevent',doc_type='userevent' , body=query_body)
    #print(res)
    print(json.dumps(res))
    for item in res["hits"]["hits"]:
        print(item["_source"])

if __name__ == '__main__':
    testEs()