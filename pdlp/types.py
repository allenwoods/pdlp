from contextlib import contextmanager
from pydantic import BaseModel

class _Graph:
    def __init__(self) -> None:
        pass
    
    def source(self):
        pass
    
@contextmanager
def Graph(name):
    yield None

class Subgraph(BaseModel):
    pass

class Node(BaseModel):
    pass