class Funcionario:
    def __init__(self, nome, email, salariobase, cargo):
        self.nome = nome
        self.email = email
        self.salariobase = salariobase
        self.cargo = cargo

    def calculadora_salario(self):
        if self.cargo == "DESENVOLVEDOR":
            if self.salariobase >= 3000:
                return self.salariobase * 0.8
            else:
                return self.salariobase * 0.9
        elif self.cargo == "DBA" or self.cargo == "TESTADOR":
            if self.salariobase >= 2000:
                return self.salariobase * 0.75
            else:
                return self.salariobase * 0.85
        elif self.cargo == "GERENTE":
            if self.salariobase >= 5000:
                return self.salariobase * 0.7
            else:
                return self.salariobase * 0.8
        else:
            raise TypeError("Cargo não identificado!")