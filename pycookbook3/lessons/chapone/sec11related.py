'''
Created on 19-May-2016

@author: dgraja
'''

def show_vargs(*args, **kwargs):
    print ("*args:", args)
    print ("*kwargs:", kwargs)
    print("-"*40)


def main():
    print ("show_vargs(1,2,3,4)")
    show_vargs(1,2,3,4)
    print ("show_vargs(\"hello world\")")
    show_vargs("hello world")
    print ("show_vargs(list(\"hello world\"))")
    show_vargs(list("hello world"))
    
    print("show_vargs(a=1, b=2)")
    show_vargs(a=1, b=2)
    print("show_vargs(1, b=2)")
    show_vargs(1, b=2)
    
    tpl = (1,2,3,4)
    print("show_vargs(tpl)")
    show_vargs(tpl)
    print("show_vargs(*tpl)")
    show_vargs(*tpl)
    
    maps = { "one": 1, "two": 2, "three": 3, "four": 4}
    print("show_vargs(maps)")
    show_vargs(maps)
    print("show_vargs(*maps)")
    show_vargs(*maps)
    print("show_vargs(**maps)")
    show_vargs(**maps)
    return


if __name__ == '__main__':
    main()
    pass
