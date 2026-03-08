import pytest
from busqueda import busqueda_binaria_recursiva
from ordenamiento import ordenamiento_rapido

@pytest.mark.parametrize("arr, elemento, esperado", [
    ([5, 10, 20, 30, 50], 30, 3),
    ([5, 10, 20, 30, 50], 25, -1),
    ([5, 10, 20, 30, 50], 50, 4)
])

def test_busqueda_binaria_recursiva(arr, elemento, esperado):
    assert busqueda_binaria_recursiva(arr, elemento) == esperado
with pytest.raises(TypeError):
    busqueda_binaria_recursiva([5, 10, 20, 30, 50], "30")
with pytest.raises(TypeError):
    busqueda_binaria_recursiva("no_lista", 30)

@pytest.mark.parametrize("arr, esperado", [
    ([5, 10, 20, 30, 50, 90, 80, 40, 70, 60], [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]),
    ([3, 1, 4, 1, 5, 9, 26, 12, 49, 52, 23, 2], [1, 1, 2, 3, 4, 5, 9, 12, 23, 26, 49, 52]),
    ([10, 9, 8, 7, 6, 3, 4, 3, 9, 3, 12, 3], [3, 3, 3, 3, 4, 6, 7, 8, 9, 9, 10, 12])
])

def test_ordenamiento_rapido(arr, esperado):
    assert ordenamiento_rapido(arr) == esperado
with pytest.raises(TypeError):
    ordenamiento_rapido([5, "10", 20])