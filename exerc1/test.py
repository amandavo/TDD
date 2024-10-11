import pytest
from app import Triangulo

# 1
def test_triangulo_escaleno_valido():
    t = Triangulo(3, 4, 5)
    assert t.tipo() == "Escaleno"

# 2
def test_triangulo_isosceles_valido():
    t = Triangulo(3, 3, 4)
    assert t.tipo() == "Isósceles"

# 3
def test_triangulo_equilatero_valido():
    t = Triangulo(5, 5, 5)
    assert t.tipo() == "Equilátero"

# 4
# 3 casos de teste (CTs)
def test_triangulos_isosceles_com_permutacao():
    assert Triangulo(3, 3, 4).tipo() == "Isósceles"
    assert Triangulo(3, 4, 3).tipo() == "Isósceles"
    assert Triangulo(4, 3, 3).tipo() == "Isósceles"

# 5
def test_valor_zero():
    assert Triangulo(0, 3, 4).tipo() == "Não é um triângulo"

# 6
def test_valor_negativo():
    assert Triangulo(-3, 4, 5).tipo() == "Não é um triângulo"

# 7
def test_soma_dois_lados_igual_terceiro():
    assert Triangulo(2, 2, 4).tipo() == "Não é um triângulo"

# 8
# o item acima, um CT para cada permutação de valores
def test_soma_dois_lados_igual_terceiro_com_permutacao():
    assert Triangulo(2, 4, 2).tipo() == "Não é um triângulo"
    assert Triangulo(4, 2, 2).tipo() == "Não é um triângulo"

# 9
def test_soma_dois_lados_menor_que_terceiro():
    assert Triangulo(1, 2, 6).tipo() == "Não é um triângulo"

# 10
def test_soma_dois_lados_menor_que_terceiro_com_permutacao():
    assert Triangulo(6, 1, 2).tipo() == "Não é um triângulo"
    assert Triangulo(2, 6, 1).tipo() == "Não é um triângulo"

# 11
def test_valores_iguais_zero():
    assert Triangulo(0, 0, 0).tipo() == "Não é um triângulo"
