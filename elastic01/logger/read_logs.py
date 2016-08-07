'''
Created on 06-Aug-2016

@author: dgraja
'''

from elasticsearch import Elasticsearch
from logger.client_log_reader import ClientLog
import os
from datetime import datetime

def log(msg, *args):
    text = msg % args
    print "%s   %s" % (datetime.now().strftime("%Y-%m-%d %X.%f")[:-3], text)


def find_log_files(location):
    contents = os.listdir(location)
    valid_logs = []
    rejected = []
    for item in contents:
        full_path = os.path.join(location, item)
        if os.path.splitext(item)[-1] != ".log" or os.stat(full_path).st_size <= 0:
            rejected.append(full_path)
            continue
        valid_logs.append(os.path.join(location, item))
    return valid_logs, rejected


def import_log(es, log_file, index_name="public", app="drive", **std_attrs):
    if not es.indices.exists(index_name):
        es.indices.create(index_name) 
    log = ClientLog(log_file=log_file)
    for item in log.entries:
        data = item.as_dict()
        if std_attrs:
            data.update(std_attrs)
        data["app"] = app
        es.create(index=index_name, doc_type=app, body=data)


def main():
    index_name = datetime.now().strftime("%Y%m%d%H%M%S")
    location = r"E:\temp\elastic-log\.cpo-drive\logs"
    valid, invalid = find_log_files(location)
    print "valid files: %r" % valid
    print "invalid files: %r" % invalid
    
    log("staring to read")
    es = Elasticsearch(["127.0.0.1:9200"])
    import_log(es, 
               log_file=valid[0], 
               index_name=index_name, 
               source="localhost", 
               user="dgraja", 
               deviceid="459103005a2511e6969ec018858486ec")
    log("completed read")


if __name__ == '__main__':
    main()
    pass
