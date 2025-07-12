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




OPERATORS_BOOL_BOOL = ["AND", "OR"]
OPERATORS_REAL_BOOL = [">", "<", "=="]
OPERATORS_REAL_REAL = ["+", "-", "*", "/"]

def is_bool_bool_operator(aStr: str) ->  bool:
    return aStr in OPERATORS_BOOL_BOOL
def is_real_bool_operator(aStr: str) ->  bool:
    return aStr in OPERATORS_REAL_BOOL
def is_real_real_operator(aStr: str) ->  bool:
    return aStr in OPERATORS_REAL_REAL

def mapStringOperatorToFunctionBoolBool(x: bool, y: bool, binaryOperator: str) -> bool:
    if is_bool_bool_operator(binaryOperator):
        match binaryOperator:
            case ">":
                return x > y
            case "<":
                return x < y
            case "==":
                return x == y
            case "AND": 
                return x and y
            case "OR": 
                return x or y
    else:
        raise ValueError("Operator '" + binaryOperator + "' is not on the accepted list of binary operators: " + OPERATORS_BOOL_BOOL)
    
def mapStringOperatorToFunctionRealBool(x: float, y: float, binaryOperator: str) -> bool:
    if is_real_bool_operator(binaryOperator):
        match binaryOperator:
            case ">":
                return x > y
            case "<":
                return x < y
            case "==":
                return x == y
    else:
        raise ValueError("Operator '" + binaryOperator + "' is not on the accepted list of binary operators: " + OPERATORS_REAL_BOOL)


def mapStringOperatorToFunctionRealReal(x: float, y: float, binaryOperator: str) -> float:
    if is_real_real_operator(binaryOperator):
        match binaryOperator:
            case "+":
                return x+y
            case "-":
                return x-y
            case "*":
                return x*y
            case "/":
                return x/y
    else:
        raise ValueError("Operator '" + binaryOperator + "' is not on the accepted list of binary operators: " + OPERATORS_REAL_REAL)
    
def is_float(aStr: str) -> bool:
    try:
        float(aStr)
        return True
    except ValueError:
        return False
def is_bool(aStr: str) -> bool:
    return aStr in ["True", "False"]



def evaluateMathExpression(valuesForVariables: dict[str, float], arbol_de_filtro: ABBenPy) -> float:
    
    if is_real_real_operator(arbol_de_filtro.value):
        return mapStringOperatorToFunctionRealReal(
            evaluateMathExpression(valuesForVariables, arbol_de_filtro.izq),
            evaluateMathExpression(valuesForVariables, arbol_de_filtro.der),
            arbol_de_filtro.value)
    
    elif is_float(arbol_de_filtro.value):
        return float(arbol_de_filtro.value)
    else:
        # Es una variable
        return valuesForVariables[arbol_de_filtro.value]

def evaluateBoolExpression(valuesForVariables: dict[str, bool], arbol_de_filtro: ABBenPy) -> bool:

    if is_bool_bool_operator(arbol_de_filtro.value):
        return mapStringOperatorToFunctionBoolBool(
            evaluateBoolExpression(valuesForVariables, arbol_de_filtro.izq),
            evaluateBoolExpression(valuesForVariables, arbol_de_filtro.der),
            arbol_de_filtro.value)
    
    elif is_bool(arbol_de_filtro.value):
        return bool(arbol_de_filtro.value)
    else:
        # Es una variable
        return valuesForVariables[arbol_de_filtro.value]

def evaluateBinaryFilterTree(valuesForVariables: dict[str: typing.Union[float, bool]], arbol_de_filtro: ABBenPy) -> bool:
    # PRE: ABBenPy no es vacio

    if (arbol_de_filtro.esVacio):
        return True
    
    else:
        # Deal with Constants and Variables
        # The only Constants accepted are floats and bools 
        
        # The only place where non bool elements can appear is on leafs. Despues todo lo otro son bools, y por lo tanto solo AND u OR
        # Los operadores de las leafs pueden incluir los demas tmb (>, <, ==)

        # ---

        if is_real_bool_operator(arbol_de_filtro.value):
            numOnLeft: float = evaluateMathExpression(arbol_de_filtro.izq)
            numOnRight: float = evaluateMathExpression(arbol_de_filtro.der)

            return mapStringOperatorToFunctionRealBool(numOnLeft, numOnRight, arbol_de_filtro.value)
        
        elif is_bool_bool_operator(arbol_de_filtro.value):
            return evaluateBoolExpression(valuesForVariables, arbol_de_filtro)
    




if __name__ == "__main__":

    arbolGenerado = ABBenPy()
    miFiltro = "( ( ( ( Prop ) < ( 15 ) ) AND ( Booly ) ) OR ( ( Num ) == ( 5 ) ) ) AND ( ( OtherBool ) OR ( ( realy ) > ( 0 ) ) )"
    generate_ABB_from_filter_string(miFiltro.split(), arbolGenerado)

    arbolGenerado.imprimir_arbol_binario(0)

    miExpMatematica = "( ( x ) + ( 1 ) ) - ( ( 2 ) * ( y ) )"
    unArbolMat = ABBenPy()
    generate_ABB_from_filter_string(miExpMatematica.split(), unArbolMat)
    myvalsmat = {"x":4, "y":10}
    print("CUANTO DA " + miExpMatematica + " con " + str(myvalsmat))
    print(evaluateMathExpression(myvalsmat, unArbolMat))

    miExpBool = "( booly ) AND ( ( someBooly ) OR ( otropo ) )"
    misVarsBool = {"booly": False, "someBooly": False, "otropo": True}
    miArbolBool = ABBenPy()
    generate_ABB_from_filter_string(miExpBool.split(), miArbolBool)
    print(evaluateBoolExpression(misVarsBool, miArbolBool))


    misValoresTODO = {"Prop": 3, "Booly": False, "Num": 5, "OtherBool": False, "realy": -5}
    print(evaluateBinaryFilterTree(misValoresTODO, arbolGenerado))
    