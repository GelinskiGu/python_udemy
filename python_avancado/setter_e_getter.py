class Caneta:
    def __init__(self, cor, cor_tampa):
       # self.cor_tinta = cor
       # Private
        self._cor = cor  # Atributos com _ não devem ser usados fora da classe
        self._cor_tampa = cor_tampa
        
    @property  # Método que se comporta como atributo
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')


caneta.cor = 'Rosa'  # Rosa vai como argumento no setter da classe
