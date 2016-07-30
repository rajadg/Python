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

def get_stats(es):
    print dir(Elasticsearch().cat)
    display("nodes", es.cat.nodes(format='json'))
    display("indices", es.cat.indices(format='json'))
    display("aliases", es.cat.aliases(format='json'))
    display("plugins", es.cat.plugins(format='json'))
    display("shards", es.cat.shards(format='json'))
    display("master", es.cat.master(format='json'))
    display("segments", es.cat.segments(format='json'))
    display("fielddata", es.cat.fielddata(format='json'))
    display("allocation", es.cat.allocation(format='json'))


def main():
    es = Elasticsearch(["127.0.0.1:9200",])
    get_stats(es)
    return


if __name__ == '__main__':
    main()
    pass