'''
Created on 23-Jun-2015

@author: dgraja
'''


class Node(object):
    '''
    classdocs
    '''

    def __init__(self, tag_name='p', node_type='node', attrs=None, children=None):
        '''
        Constructor
        '''
        self.attrs = {}
        if attrs and isinstance(attrs, dict):
            for key, val in attrs.iteritems():
                self.attrs[key] = val
        self.children = []
        if children and isinstance(children, (list, tuple, set)):
            self.children = list(children)
        self.type = str(node_type)
        self.tag_name = str(tag_name)

    def append(self, child):
        self.children.append(child)
        return self

    def __str__(self):
        result = ""
        if self.type == 'node':
            attr_text = "" if not self.attrs else (" " + " ".join(["%s='%s'" % (key, value) for key, value in self.attrs]))
            content_text = "" if not self.children else "".join([str(child) for child in self.children])
            result = "<%s%s>%s</%s>" % (self.tag_name, attr_text, content_text, self.tag_name)
        return result


class Html(Node):
    def __init__(self, attrs=None, children=None, head=None, body=None, title=None):
        '''
        Constructor for Html Node
        '''
        super(Html, self).__init__(tag_name='html', node_type='node', attrs=attrs, children=children)
        self.__title__ = Node(tag_name='title', children=[title, ])
        self.__head__ = head if head else Node(tag_name='head', children=[self.__title__, ])
        self.__body__ = body if body else Node(tag_name='body')
        self.children = [self.__head__, self.__body__]
        return

    def title(self):
        return self.__title__

    def head(self):
        return self.__head__

    def body(self):
        return self.__body__
    pass


class Content(Node):

    def __init__(self, tag_name='p', attrs=None, children=None):
        ''' Constructor for generic content tag '''
        super(Content, self).__init__(tag_name=tag_name, node_type='node', attrs=attrs, children=children)
        return
    pass


def h1(attrs=None, children=None):
    return Content(tag_name='h1', attrs=attrs, children=children)


def h2(attrs=None, children=None):
    return Content(tag_name='h2', attrs=attrs, children=children)


def h3(attrs=None, children=None):
    return Content(tag_name='h3', attrs=attrs, children=children)


def h4(attrs=None, children=None):
    return Content(tag_name='h4', attrs=attrs, children=children)


def h5(attrs=None, children=None):
    return Content(tag_name='h5', attrs=attrs, children=children)


def h6(attrs=None, children=None):
    return Content(tag_name='h6', attrs=attrs, children=children)


def span(attrs=None, children=None):
    return Content(tag_name='span', attrs=attrs, children=children)


def para(attrs=None, children=None):
    return Content(tag_name='p', attrs=attrs, children=children)


def div(attrs=None, children=None):
    return Content(tag_name='div', attrs=attrs, children=children)


def tag(attrs=None, children=None):
    return Content(tag_name='p', attrs=attrs, children=children)


def test1():
    response = Html(title='Basic Sample 01')
    response.body().\
        append(h1().append('basic sample 01')).\
        append(para().append('Hello World !!'))
    print str(response)


if __name__ == '__main__':
    test1()
    pass
