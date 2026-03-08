import pytest
from calculadora import sumar, restar, multiplicar, dividir

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])

def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado
with pytest.raises(TypeError):
    sumar("2", "3")

def test_restar():
    assert restar(5, 2) == 3
    assert restar(0, 1) == -1
    assert restar(-1, -1) == 0
with pytest.raises(TypeError):
    restar("5", "2")

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0
with pytest.raises(TypeError):
    multiplicar("2", "3")

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(-1, 1) == -1
    assert dividir(5, 2) == 2.5
with pytest.raises(TypeError):
    dividir("6", "3")
with pytest.raises(ZeroDivisionError):
    dividir(6, 0)