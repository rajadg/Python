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
        if item.endswith(".log") or ("drive" in item) or\
            (os.stat(full_path).st_size > 0):
            valid_logs.append(os.path.join(location, item))
        else:
            rejected.append(full_path)
            continue
    return valid_logs, rejected


def is_non_ascii(text, encoding):
    converted = text.decode(encoding, errors='ignore').encode('ascii', errors='ignore')
    return text != str(converted)


def import_log(es, log_file, index_name="public", app="drive", encoding="utf-8", **std_attrs):
    if not es.indices.exists(index_name):
        es.indices.create(index_name) 
    logs = ClientLog(log_file=log_file, encoding=encoding)
    file_name = os.path.basename(log_file)
    log("entries: %d" % len(logs.entries))
    for item in logs.entries:
        data = item.as_dict()
        data["file"] = file_name
        if std_attrs:
            data.update(std_attrs)
        data["app"] = app
        try:
            es.create(index=index_name, doc_type=app, body=data)
        except Exception as e:
            log("Exception: %r", str(e))
            log("data: %r", data)
            


def main():
    index_name = datetime.now().strftime("%Y%m%d%H%M%S")
    index_name = "sample-index"
    location = r"E:\test\logs"
    valid, invalid = find_log_files(location)
    print "valid files: %r" % valid
    print "invalid files: %r" % invalid
    
    log("staring to read")
    es = Elasticsearch(["127.0.0.1:9200"])

    # Clean-up already existing index
    if es.indices.exists(index_name):
        print "deleting index " + index_name
        print es.indices.delete(index_name)
    
    for log_file in valid:
        log("importing log file: %s ..." % log_file)
        import_log(es, 
                   log_file=log_file, 
                   index_name=index_name, 
                   source="local-pc", 
                   user="raja",
                   os="Windows",
                   stack="up2",
                   deviceid="123456",
                   encoding="ascii")
    log("completed read")


if __name__ == '__main__':
    main()
    pass
