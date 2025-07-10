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
        
    
    def imprimir_arbol_binario(self, lvl: int):
        print(" " * lvl, self.value)
        if self.izq != None:
            self.izq.imprimir_arbol_binario(lvl + 1)
        elif self.der != None:
            self.der.imprimir_arbol_binario(lvl + 1)
    
    
def generate_ABB_from_filter_string(filter_string_split: list[str]) -> ABBenPy:
    """ 
    This function parses strings like ( ( ( Prop < 15 ) AND Booly ) OR ( Num == 5 ) ) AND ( OtherBool OR ( realy > 0 ) ) that have already been .split()
    """
    
    count_paren: int = 1 if filter_string_split[0] == "(" else 0
    
    i: int = 0
    while ((count_paren != 0) and (i < len(filter_string_split))):
        
        if (filter_string_split[i] == "("):
            count_paren += 1
        elif (filter_string_split[i] == ")"):
            count_paren -= 1
        
        i += 1
    
    
    
        