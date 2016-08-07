'''
Created on 23-Feb-2016

@author: dgraja
'''
import os
from datetime import datetime
import time


class LogEntry(object):
    ''' An entry log file '''
    def __init__(self, text, count):
        self.text = text
        self.index = count
        self.time_stamp = datetime.min
        self.pid = self.thread_id = 0
        self.log_type = 'extension'
        self.cname = self.message = ''
        self.parse()
        self.more = []

    def parse(self):
        ''' Parse the log entry'''
        if not self.text or len(self.text) < 30:
            return
        try:
            stamp = self.text[:24]
            self.time_stamp = datetime.strptime(stamp[:-1], '%Y-%m-%d %H:%M:%S,%f')
            remaining = self.text[24:].split(' ', 3)
            self.pid = int(remaining[0])
            self.thread_id = int(remaining[1])
            self.log_type = remaining[2]
            msg = remaining[3].strip().split(' ', 1)
            self.cname = msg[0].strip()
            self.message = msg[1].strip()
        except Exception:
            pass
        return

    def extend(self, entry):
        self.more.append(entry)

    def time_string(self):
        tm = self.time_stamp
        if not self.time_stamp or self.time_stamp == datetime.min:
            tm = datetime.now()
            time.sleep(0.001)
        return tm.strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]

    def as_dict(self):
        return {"full_text": self.text,
               "time": self.time_string(),
               "process": self.pid,
               "thread": self.thread_id,
               "level": self.log_type,
               "class": self.cname,
               "message": self.message,
               "sequence": self.index}

    def __repr__(self):
        return str(self.as_dict())

    def __str__(self):
        if self.log_type == 'extension':
            return self.text
        result = "[%06d]: %s %d %d %8s %s %s" % (self.index, self.time_string(), self.pid, self.thread_id,
                                                 self.log_type, self.cname, self.message)
        if self.more:
            result = result + '\n' + ''.join([str(entry) for entry in self.more])
        return result


class ClientLog(object):
    def __init__(self, log_file='test.log'):
        self.log_file = log_file
        self.entries = []
        self.read_logs()

    def read_logs(self):
        with open(self.log_file, 'r') as fp:
            count = 0
            line = fp.readline()
            active_entry = None
            while line:
                count = count + 1
                entry = LogEntry(line, count)
                if entry.log_type != 'extension':
                    active_entry = entry
                    self.entries.append(entry)
                else:
                    active_entry.extend(entry)
                line = fp.readline()
        return

    def write_log(self, out_file, logs=None):
        directory = os.path.dirname(out_file)
        if not os.path.exists(directory):
            os.mkdir(directory)
        if not logs:
            logs = self.entries
        with open(out_file, 'w') as fp:
            for entry in sorted(logs, key=lambda entry: entry.index):
                fp.write(str(entry) + "\n")

    def get_classes(self):
        return set([entry.cname for entry in self.entries])

    def get_threads(self):
        return set([entry.thread_id for entry in self.entries])

    def get_levels(self):
        return set([entry.log_type for entry in self.entries])

    def filter(self, criteria=(lambda item: item.log_type == 'ERROR')):
        return filter(criteria, self.entries)

    def filter_by_thread(self, thread_id):
        thread_filter = lambda entry: entry.thread_id == thread_id
        return self.filter(criteria=thread_filter)

    def filter_by_class(self, cname):
        cname_filter = lambda entry: entry.cname == cname
        return self.filter(criteria=cname_filter)

    def filter_by_level(self, level):
        avail = ['FATAL', 'CRITICAL', 'ERROR', 'WARNING', 'WARN', 'DEBUG', 'INFO', 'TRACE']
        target = []
        for l in avail:
            target.append(l)
            if l == level:
                break
        level_filter = lambda entry: entry.log_type in target
        return self.filter(criteria=level_filter)

    def filter_by_message(self, message):
        message_filter = lambda entry: message in entry.message
        return self.filter(criteria=message_filter)

    def filter_by_keywords(self, keywords):
        def keyword_filter(entry):
            for item in keywords:
                if item not in entry.message:
                    return False
            return True
        return self.filter(criteria=keyword_filter)


if __name__ == '__main__':
    pass
