from __future__ import annotations
import typing


class ABBenPy:
    
    def __init__(self):
        self.value: str = ""
        self.izq: typing.Optional[ABBenPy] = None
        self.der: typing.Optional[ABBenPy] = None
    
    def esVacio(self) -> bool:
        return self.value == ""
    
    def insertar(self, valor: str):
        if self.esVacio():
            self.value = valor
            self.izq = ABBenPy()
            self.der = ABBenPy()
        else:
            raise ValueError("Cant insert to Tree that isnt empty")

    
    def imprimir_arbol_binario(self, lvl: int):
        print(" " * lvl, self.value)

        print(" " * lvl, "r: ")
        if self.der != None:
            self.der.imprimir_arbol_binario(lvl + 1)
        print(" " * lvl, "l:")
        if self.izq != None:
            self.izq.imprimir_arbol_binario(lvl + 1)
    
    
    
def generate_ABB_from_filter_string(filter_string_split: list[str], arbol_hasta_ahora: ABBenPy):
    """ 
    This function parses strings like ( ( ( ( Prop ) < ( 15 ) ) AND ( Booly ) ) OR ( ( Num ) == ( 5 ) ) ) AND ( ( OtherBool ) OR ( ( realy ) > ( 0 ) ) ) that have already been .split()
    Easier example: ( ( This ) > ( 0 ) ) OR ( SomeBool )

    Por como esta escrito "insertar()", esta funcion siempre genera hojas que apunten a ABBs vacios (o sea que self.esVacio() == True) en vez de que las hojas apunten a NULL (None)
    """

    if filter_string_split[0] == "(":
        count_paren: int = 1

        i: int = 1
        while ((count_paren != 0) and (i < len(filter_string_split))):
            
            if (filter_string_split[i] == "("):
                count_paren += 1
            elif (filter_string_split[i] == ")"):
                count_paren -= 1
            
            i += 1
        
        arbol_hasta_ahora.insertar(filter_string_split[i])


        # On each list slice, I remove the binary operator that was inserted to the tree and also 1 set of parentheses
        generate_ABB_from_filter_string(filter_string_split[1: i-1], arbol_hasta_ahora.izq)
        generate_ABB_from_filter_string(filter_string_split[i+2: len(filter_string_split) - 1], arbol_hasta_ahora.der)

    else:
        arbol_hasta_ahora.insertar(filter_string_split[0])




ACCEPTED_OPERATORS = [">", "<", "==", "AND", "OR"]

def is_accepted_operator(aStr: str) ->  bool:
    return aStr in ACCEPTED_OPERATORS

def mapStringOperatorToFunction(x: typing.Union[float, bool], y: typing.Union[float, bool], binaryOperator: str) -> bool:
    if is_accepted_operator(binaryOperator):
        match binaryOperator:
            case ">":
                return x > y,
            case "<":
                return x < y,
            case "==":
                return x == y,
            case "AND": 
                return x and y,
            case "OR": 
                return x or y
    else:
        raise ValueError("Operator '" + binaryOperator + "' is not on the accepted list of binary operators: " + ACCEPTED_OPERATORS)


def is_float(aStr: str) -> bool:
    try:
        float(aStr)
        return True
    except ValueError:
        return False

def evaluateBinaryFilterTree(valuesForVariables: dict[str: typing.Union[float, bool]], arbol_de_filtro: ABBenPy) -> bool:
    # PRE: ABBenPy no es vacio

    if (arbol_de_filtro.esVacio):
        return True
    
    else:
        # Deal with Constants and Variables
        # The only Constants accepted are floats    
        
        # The only place where non bool elements can appear is on leafs. Despues todo lo otro son bools, y por lo tanto solo AND u OR
        # Los operadores de las leafs pueden incluir los demas tmb (>, <, ==)

    




if __name__ == "__main__":

    arbolGenerado = ABBenPy()
    miFiltro = "( ( ( ( Prop ) < ( 15 ) ) AND ( Booly ) ) OR ( ( Num ) == ( 5 ) ) ) AND ( ( OtherBool ) OR ( ( realy ) > ( 0 ) ) )"
    generate_ABB_from_filter_string(miFiltro.split(), arbolGenerado)

    arbolGenerado.imprimir_arbol_binario(0)
    