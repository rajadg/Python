'''
Created on 08-Aug-2016

@author: dgraja
'''
from elasticsearch import Elasticsearch
import json


es = Elasticsearch(["127.0.0.1:9200"])
index_name = "9327"


def query_by_thread_get(thread_id=4512):
    result = es.search(index=index_name, doc_type="drive", q="thread:%s" % str(thread_id))
    print json.dumps(result, indent=2)
    for item in result["hits"]["hits"]:
        print (item["_source"]["full_text"]).strip()


def query_by_thread(thread_id=3160):
    body = {"query": {"match_all": {}},
            "filter": {"term": {"thread": thread_id}}}
    result = es.search(index=index_name, doc_type="drive", body=body)
#     print json.dumps(result, indent=2)
    for item in result["hits"]["hits"]:
        print (item["_source"]["full_text"]).strip()


def filter_by_parms(es, index, **filters):
    """
        Query the Elasticsearch only by filters
    """
    # An empty body with match_all and no filter
    body = {"query": {"match_all": {}},
            "filter": {"term": {}},
            "from":0, "size": 50}
    if "size" in filters:
        body["size"] = filters["size"]
        filters.pop("size")
    if "page" in filters:
        body["from"] = filters["page"]
        filters.pop("page")
    # add all filter criteria from arguments to body
    for key, val in filters.iteritems():
        body["filter"]["term"][key] = val
    
    print "body: " + json.dumps(body, indent=4)
    
    # Query the elastic search
    result = es.search(index=index_name, doc_type="drive", body=body)
    
    # print each log entry line by line
    for item in result["hits"]["hits"]:
        print (item["_source"]["full_text"]).strip()


def main():
#     query_by_thread(thread_id=123145303453696)
    filter_by_parms(es=es, index=index_name, page=1, size=5, process=554)
    
    return


if __name__ == '__main__':
    main()
    pass
