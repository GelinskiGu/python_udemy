class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False


p1 = Pessoa('Gustavo', 19)
p2 = Pessoa('João', 32)

p1.comer('batata')

#Teste