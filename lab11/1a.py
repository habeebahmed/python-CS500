from abc import ABC, abstractmethod, abstractproperty
from typing import Dict, List


class Node(ABC):
    def __init__(self, content:str = "", attributes:Dict = {}):
        self.__children = []
        self.__attributes = attributes
        self.__content = content
    @property
    def content(self):
        return self.__content
    @property
    def children(self):
        return self.__children
    @property
    def attribites(self):
        return self.__attributes
    @abstractmethod
    def html(self):
        pass
    def appendChild(self, child):
        self.__children.append(child)
    def static_html_generator(self, tag):
        str = f'<{tag}'
        for k, v in self.attribites.items():
            str += ' ' + k + '="' + v + '"'
        str += '>'
        # children
        for elem in self.children:
            str += elem.html()
        str += self.content
        str += f'</{tag}>'
        return str

class Html(Node):
    def html(self):
        str = '<!DOCTYPE html>'
        # str = '<!DOCTYPE html><html'
        # for k, v in self.attribites.items():
        #     str += ' ' + k + '="' + v + '"'
        # str += '>'
        # # children
        # for elem in self.children:
        #     str += elem.html()
        # str += self.content
        # str += '</html>'
        str += self.static_html_generator("html")
        return str

class Head(Node):
    def html(self):
        str = self.static_html_generator("head")
        return str

class Body(Node):
    def html(self):
        str = self.static_html_generator("body")
        return str

class Title(Node):
    def html(self):
        str = self.static_html_generator("title")
        return str

class Div(Node):
    def html(self):
        str = self.static_html_generator("div")
        return str

class B(Node):
    def html(self):
        str = self.static_html_generator("b")
        return str

def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = Div('This is a test B', divAtts)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = Div('This is a test C', divAtts)
    b = B('This is a simple HTML file', {})
    divC.appendChild(b)
    body = Body('', {})
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    title = Title('Example', {})
    head = Head('', {})
    head.appendChild(title)
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = Html('', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())
if __name__ == "__main__":
    main()