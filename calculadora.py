

def sumar(a: int, b: int) -> int:
    """
    Suma dos números enteros.
    Parametros:
    a (int): El primer número a sumar.
    b (int): El segundo número a sumar.
    Retorna:
    int: La suma de a y b.
    Ejemplo de uso:
    >>> sumar(2, 3)
    5
    """
    if type(a) != int or type(b) != int:
        raise TypeError("Los argumentos deben ser enteros")
    return a + b

def restar(a: int, b: int) -> int:
    """
    Resta dos números enteros.
    Parametros:
    a (int): El primer número a restar.
    b (int): El segundo número a restar.
    Retorna:
    int: La resta de a y b.
    Ejemplo de uso:
    >>> restar(5, 3)
    2
    """
    if type(a) != int or type(b) != int:
        raise TypeError("Los argumentos deben ser enteros")
    return a - b

def multiplicar(a: int, b: int) -> int:
    if type(a) != int or type(b) != int:
        raise TypeError("Los argumentos deben ser enteros")
    return a * b

def dividir(a: int, b: int) -> float:
    if type(a) != int or type(b) != int:
        raise TypeError("Los argumentos deben ser enteros")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


