'''
Created on 08-Aug-2016

@author: dgraja
'''

from logger.client_log_reader import ClientLog


target = r"E:\Temp\unicode\test01.txt"


def test():
    logs = ClientLog(target, "shift-jis")
    data = logs.entries[0]
    return data.text


def display_ord(data):
    try:
        print "Raw data: %s" % data
    except Exception:
        print "raw data not printable"
    print "Ordinal:"
    print ["0x%x" % ord(chr) for chr in data]
    print "\n"
    

def main():
    text = ""
    with open(target, 'rb') as fp:
        raw_text = fp.readline()
        text = raw_text
    display_ord(text[80:])
    text = test()
    print text[80:]
    display_ord(text[80:])
    
    sample = raw_text.decode("shift-jis")
    sample = sample.encode("utf-8")
    display_ord(sample[80:])
#     utf8 = unicode.decode(raw_text[182:], "utf-8")
#     display_ord(utf8)


if __name__ == '__main__':
    main()
    pass
