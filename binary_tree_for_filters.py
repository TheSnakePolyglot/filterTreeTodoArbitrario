from __future__ import annotations
import typing


class ABBenPy:
    
    def __init__(self):
        self.value: str = ""
        self.izq: typing.Optional[typing.Self] = None
        self.der: typing.Optional[typing.Self] = None
    
    
    def insertar(self, valor: str):
        pass
        
    
    
def generate_ABB_from_filter_string(filter_string: str)
        