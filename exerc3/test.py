import pytest
from app import Funcionario

def test_invalid_cargo():
    with pytest.raises(TypeError) as excinfo:
        emp = Funcionario("Amanda", "amanda@gmail.com", 3000, "CARGO_INVALIDO")
        emp.calculadora_salario()
    assert str(excinfo.value) == "Cargo não identificado!"

def test_unspecified_cargo():
    with pytest.raises(TypeError) as excinfo:
        emp = Funcionario("Amanda", "amanda@gmail.com", 3000, "")
        emp.calculadora_salario()
    assert str(excinfo.value) == "Cargo não identificado!"

def test_desenv_limite_salario():
    emp = Funcionario("Amanda", "amanda@gmail.com", 3000, "DESENVOLVEDOR")
    assert emp.calculadora_salario() == 2400

def test_dba_limite_salario():
    emp = Funcionario("Amanda", "amanda@gmail.com", 2000, "DBA")
    assert emp.calculadora_salario() == 1500

def test_testador_limite_salario():
    emp = Funcionario("Amanda", "amanda@gmail.com", 2000, "TESTADOR")
    assert emp.calculadora_salario() == 1500

def test_gerente_limite_salario():
    emp = Funcionario("Amanda", "amanda@gmail.com", 5000, "GERENTE")
    assert emp.calculadora_salario() == 3500

def test_desenv_salario_minimo():
    emp = Funcionario("Amanda", "amanda@gmail.com", 1000, "DESENVOLVEDOR")
    assert emp.calculadora_salario() == 900

def test_dba_salario_minimo():
    emp = Funcionario("Amanda", "amanda@gmail.com", 1000, "DBA")
    assert emp.calculadora_salario() == 850

def test_testador_salario_minimo():
    emp = Funcionario("Amanda", "amanda@gmail.com", 1000, "TESTADOR")
    assert emp.calculadora_salario() == 850

def test_gerente_salario_minimo():
    emp = Funcionario("Amanda", "amanda@gmail.com", 1000, "GERENTE")
    assert emp.calculadora_salario() == 800