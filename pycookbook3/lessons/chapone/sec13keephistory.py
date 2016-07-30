'''
Created on 19-May-2016

@author: dgraja
'''


from collections import deque


history = deque(maxlen=5)


def keep_history(item):
    history.append(item)
    print (history)
    return history


def main():
    print (keep_history("one")[0])
    print (keep_history("two"))
    print (keep_history("three"))
    print (keep_history("four"))
    print (keep_history("five"))
    print (keep_history("six"))
    print (keep_history("seven"))
    print (keep_history("eight"))
    
    print(dir(history))

    
    return


if __name__ == '__main__':
    main()
    pass