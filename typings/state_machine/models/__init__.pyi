"""
This type stub file was generated by pyright.
"""

class InvalidStateTransition(Exception):
    ...


class State:
    def __init__(self, initial=..., **kwargs) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class Event:
    def __init__(self, **kwargs) -> None:
        ...
    

