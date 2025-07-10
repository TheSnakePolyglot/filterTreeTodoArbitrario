from __future__ import annotations
import typing


class ABBenPy:
    
    def __init__(self, value: str):
        self.value: str = value
        self.izq: typing.Optional[ABBenPy] = None
        self.der: typing.Optional[ABBenPy] = None
    
    
    def insertar(self, valor: str, left: bool):
        if left:
            self.izq = ABBenPy(valor)
        else:
            self.der = ABBenPy(valor)
        
    
    
def generate_ABB_from_filter_string(filter_string_split: list[str]) -> ABBenPy:
    """ 
    This function parses strings like ( ( ( Prop < 15 ) AND Booly ) OR ( Num == 5 ) ) AND ( OtherBool OR ( realy > 0 ) ) that have already been .split()
    """
    
    
        