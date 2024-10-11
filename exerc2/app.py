import re

class Person:
    def __init__(self, name, age, emails):
        self.name = name
        self.age = age
        self.emails = emails

    def isValidToInclude(self):
        errors = []

        if len(self.name.split()) < 2:
            errors.append("O nome deve ser composto por ao menos 2 partes")
        elif not self.name.replace(" ", "").isalpha():
            errors.append("O nome deve ser composto apenas de letras")

        if not 1 <= self.age <= 200:
            errors.append("A idade deve estar no intervalo entre 1 e 200")

        if not self.emails:
            errors.append("Pessoa deve ter pelo menos um email associado")
        else:
            for email in self.emails:
                if not email.validateEmail():
                    errors.append("Formato de email inválido! Siga esse padrão: ___@___.__")

        return errors

class Email:
    def __init__(self, address):
        self.address = address

    def validateEmail(self):
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.address) is not None