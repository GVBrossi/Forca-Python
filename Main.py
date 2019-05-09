import random


# Tabuleiro e seus estados
class Tabuleiro():

    def __init__(self):
        print("Jogo Criado")

    def erro0(self):
        print(" ------")
        print(" |    |")
        print(" |")
        print(" |")
        print(" |")
        print("---")

    def erro1(self):
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |")
        print(" |")
        print("---")

    def erro2(self):
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |")
        print("---")

    def erro3(self):
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |   /")
        print("---")

    def erro4(self):
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |   / \\")
        print("---")

    def erro5(self):
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |   /|")
        print(" |   / \\")
        print("---")

    def erro6(self):
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   / \\")
        print("---")


# Leitura do arquivo de palavras
class Palavra():

    palavras = []

    def __init__(self):

        with open("Palavras.txt", "r") as arquivo:
            palavrasLocais = arquivo.read()
            self.palavras = palavrasLocais.split()

    def retornaPalavra(self):
        return random.choice(self.palavras)


# Classe de erros
class Erros():

    erros = 0

    def __init__(self):
        print("Erros iniciados")

    def getErros(self):
        return self.erros

    def adicionaErro(self):
        self.erros += 1
        return self.erros


# método responsavel por codificar a palavra escolhida
def trocaLetra(L):
    return "_"


# Criação dos objetos e variaveis
tabuleiro = Tabuleiro()
palavraEscolhida = Palavra().retornaPalavra()
palavraCodificada = list(map(trocaLetra, palavraEscolhida))
erro = Erros()

# metodo para verificação de acerto de letra
def comparaLetraPalavra(letra):

    letraEscolhida = letra
    for i in palavraEscolhida:
        if letraEscolhida == i:
            print("Acertou")
            acertos =+ 1
            print(acertos)
            return erro.getErros()
    erro.adicionaErro()
    return print("ERROU " + str(erro.getErros()))


def mostraPalavra(palavra, letra):
    palavras = list(palavra)
    index = 0
    print(palavras)
    for l in palavras:
        if letra == l:
            palavraCodificada[index] = letra
        index += 1


# loop one a lógica do jogo funciona
print("Bem Vindo ao Jogo da Forca")
while erro.getErros() < 7:
    if erro.getErros() == 0:
        tabuleiro.erro0()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraCodificada))
        letra = str(input("Escolha uma letra: "))
        comparaLetraPalavra(letra)
        mostraPalavra(palavraEscolhida, letra)
    elif erro.getErros() == 1:
        tabuleiro.erro1()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraCodificada))
        letra = str(input("Escolha uma letra: "))
        comparaLetraPalavra(letra)
        mostraPalavra(palavraEscolhida, letra)
    elif erro.getErros() == 2:
        tabuleiro.erro2()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraCodificada))
        letra = str(input("Escolha uma letra: "))
        comparaLetraPalavra(letra)
        mostraPalavra(palavraEscolhida, letra)
    elif erro.getErros() == 3:
        tabuleiro.erro3()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraCodificada))
        letra = str(input("Escolha uma letra: "))
        comparaLetraPalavra(letra)
        mostraPalavra(palavraEscolhida, letra)
    elif erro.getErros() == 4:
        tabuleiro.erro4()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraCodificada))
        letra = str(input("Escolha uma letra: "))
        comparaLetraPalavra(letra)
        mostraPalavra(palavraEscolhida, letra)
    elif erro.getErros() == 5:
        tabuleiro.erro5()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraCodificada))
        letra = str(input("Escolha uma letra: "))
        comparaLetraPalavra(letra)
        mostraPalavra(palavraEscolhida, letra)
    elif erro.getErros() == 6:
        tabuleiro.erro6()
        print("Você errou: " + str(erro.getErros()) + " vezes. de um total de: 6")
        print("A Palavra é: " + str(palavraEscolhida))
        print("Voce Perdeu.")
        break