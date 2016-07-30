'''
Created on 19-May-2016

@author: dgraja
'''


def get_pre(arr):
    *pre, _ = arr
    return pre


def get_post(arr):
    _, *post = arr
    return post


def get_mid(arr):
    _, *mid, _ = arr
    return mid


def mid_mid_sample():
    arr = [1, 2, 3, 4, (5, 6, 7, 8), 9, 10]
    *_, (mid), _, _ = arr
    print ("-"*40)
    print ("arr:", arr)
    print ("mid:", mid)
    return


def main():
    print("-"*40, "\n", "            unpacking sample\n", "-"*40)
    container = [1,2,3,4,5,6]
    print ("container:", container)
    print ("pre:" , get_pre(container))
    print ("mid:" , get_mid(container))
    print ("post:" , get_post(container))
    
    text = "hello world"
    print ("text:", text)
    print ("pre:" , "".join(get_pre(text)))
    print ("mid:" , "".join(get_mid(text)))
    print ("post:" , "".join(get_post(text)))
    
    mid_mid_sample()
    return


if __name__ == '__main__':
    main()
    pass