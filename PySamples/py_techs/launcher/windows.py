'''
Created on Mar 23, 2015

@author: dgraja
'''

import subprocess
import os
import tempfile
from datetime import datetime, timedelta, time
from win32process import STARTUPINFO

def start_process(app, arg):
    if str(app).find(" ")>=0:
        app = '"%s"' % app
    cmdline = '%s %s && exit' % (app, arg)
    print "start_process: %s" % cmdline
    start = datetime.now()
    try:
        with tempfile.TemporaryFile('w+') as rec:
            si = subprocess.STARTUPINFO()
            si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = 5
            si.hStdOutput = 1
            proc = subprocess.Popen(cmdline, stdout=rec, shell=True, startupinfo=si)
            print "start_process : %s" % str(proc)
            proc.wait()
            print "start_process : %s exited" % str(proc)
            rec.seek(0)
            return rec.read()
    finally:
        dur = (datetime.now() - start)
        print "Duration : " + str(dur)
        print "start_process: completed"

def simple_run(app, arg):
    cmdline = '"%s" %s && exit' % (app, arg)
    print "simple_run: %s" % cmdline
    os.system(cmdline)
    print "simple_run complete"
    return


def main():
    folder = "K:\\Java\\nuxeo-server\\nuxeo"
    nuxeoctl = os.path.join(folder, "bin", "nuxeoctl.bat")
    args = ' --gui=false restart'
#     simple_run(nuxeoctl, args)
    print start_process(nuxeoctl, args)


    return

if __name__ == '__main__':
    main()
    pass