'''
Created on 30-Jul-2016

@author: dgraja
'''
import json
from elasticsearch import Elasticsearch


def display(name, data):
    line = "-" * 80
    print line 
    print "%s: %s" % (name, json.dumps(data, indent=2))
    print line + "\n\n"


def create_index(es):
    '''
        create a new index
    '''
    es.indices.create("client_stats")


def main():
    es = Elasticsearch(["127.0.0.1:9200",])
    create_index(es)
    return


if __name__ == '__main__':
    main()
    pass