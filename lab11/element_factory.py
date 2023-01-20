from __future__ import annotations

from enum import Enum


class ElemType(Enum):
    Html = "html"
    Head = "head"
    Title = "title"
    Body = "body"
    B = "b"
    Div = "div"


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

class AbstractNodeFactory:
    def make_node(self, type: ElemType, content: str):
        pass

class StandardNodeFactory(AbstractNodeFactory):
    def make_node(self, type: ElemType, content: str, attr: Dict):
        c = None
        if type == ElemType.Html.value:
            c = Html(content, attr)
        elif type == ElemType.Head.value:
            c = Head(content, attr)
        elif type == ElemType.Body.value:
            c = Body(content, attr)
        elif type == ElemType.Title.value:
            c = Title(content, attr)
        elif type == ElemType.Div.value:
            c = Div(content, attr)
        elif type == ElemType.B.value:
            c = B(content, attr)
        
        return c

class DebugNodeFactory(StandardNodeFactory):
    def make_node(self, type: ElemType, content: str, attr: Dict):
        print(f"{ElemType[type.capitalize()].name} node is created.")
        return StandardNodeFactory.make_node(self, type, content, attr)