from __future__ import annotations
import typing


class ABBenPy:
    
    def __init__(self):
        self.value: str = ""
        self.izq: typing.Optional[ABBenPy] = None
        self.der: typing.Optional[ABBenPy] = None
    
    def esVacio(self) -> bool:
        return self.value == ""
    
    def insertar(self, valor: str, left: bool):
        if self.esVacio():
            self.value = valor
        else:
            if left:
                self.izq = ABBenPy()
                self.izq.insertar(valor, True) 
                # En este punto no importa si le paso True o False a "left", porque siempre va a ser vacio ese arbol asi que nunca checkea la variable "left"
            else:
                self.der = ABBenPy()
                self.der.insertar(valor, True)
        
    
    def imprimir_arbol_binario(self, lvl: int):
        print(" " * lvl, self.value)
        if self.izq != None:
            self.izq.imprimir_arbol_binario(lvl + 1)
        if self.der != None:
            self.der.imprimir_arbol_binario(lvl + 1)
    
    
def generate_ABB_from_filter_string(filter_string_split: list[str], arbol_hasta_ahora: ABBenPy) -> ABBenPy:
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
    
    # TODO: Ver que onda con los punteros aca, como puedo agregarle al arbol y al mismo tiempo pasar un nuevo arbol
    
    return 
    


if __name__ == "__main__":
    miArbol = ABBenPy()
    miArbol.insertar("1", True)
    miArbol.insertar("je", True)
    miArbol.insertar("what", False)
    
    # nuevoarbol = ABBenPy("no")
    # otroarbolito = ABBenPy("der")
    
    # nuevoarbol.insertar(miArbol, True)
    
    
    miArbol.imprimir_arbol_binario(0)
    