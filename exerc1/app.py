class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def condicao(self):
        # somando 2 lados é maior que o 3°?
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def tipo(self):
        if not self.condicao():
            return "Não é um triângulo"
        
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"
