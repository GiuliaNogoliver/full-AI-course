import numpy as np

class VetorOrdenado:
    # construtor, recebe esses 2 carametros
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # Funcao para imprimir
    def imprime(self):
        # ele ta verificando se esta na ultima posicao
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            # for para percorrer cada uma das posicoes
            for i in range(self.ultima_posicao +1):
                print(i, '_', self.valores[i])

    # Funcao de inserir o numero no vetor
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade maxima atingida')
            return

        # Procura a posicao para fazer a insercao
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        # Insere
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

vetor = VetorOrdenado(10)
vetor.imprime()

vetor.insere(6)
vetor.insere(4)
vetor.insere(5)
vetor.insere(8)
vetor.insere(9)
vetor.insere(3)
vetor.insere(1)
vetor.insere(7)

vetor.imprime()

