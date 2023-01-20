from abc import ABC, abstractmethod, abstractproperty
from typing import List, Dict
from element_factory import DebugNodeFactory

def main():
    factory = DebugNodeFactory()
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = factory.make_node('div', 'This is a test A', divAtts)
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = factory.make_node('div', 'This is a test B', divAtts)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = factory.make_node('div', 'This is a test C', divAtts)
    b = factory.make_node('b', 'This is a simple HTML file', {})
    divC.appendChild(b)
    body = factory.make_node('body', '', {})
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    title = factory.make_node('title', 'Example', {})
    head = factory.make_node('head', '', {})
    head.appendChild(title)
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = factory.make_node('html', '', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())
if __name__ == "__main__":
    main()