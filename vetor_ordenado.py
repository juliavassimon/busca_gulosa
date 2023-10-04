from typing_extensions import Self
#busca gulosa
import numpy as np

class Vertice:

    #construtor
    #rotulo = nome das cidades
    def __init__(self, rotulo, distancia_objetivo):
        #criar atributo
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
    def adiciona_adjacente (self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        #fazer um for para pecorrer cada cidade e mostrar o nomes
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

#criar uma classe para representa a ligação
class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
#custo é a distancia da estrada, sem largura...
#classe que vai unir as duas
class grafo_completo:
    #criar as cidades
    arad = Vertice ('Arad',366 )
    zerind = Vertice ('Zerind', 374)
    oradea = Vertice('Oredea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)
#as ligações
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(sibiu, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

grafo = grafo_completo()
#mostra as cidades e distancias
#grafo.arad.mostra_adjacentes()
#grafo.bucharest.mostra_adjacentes()
class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    #mudança no tipo do dado
    self.valores = np.empty(self.capacidade, dtype=object)
#referencia para o verticie e comparação com a distancia para o objetivo
  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:
        print('Capacidade máxima atingida')
        return

    posicao = 0
    while posicao <= self.ultima_posicao:
        if self.valores[posicao].distancia_objetivo > vertice.distancia_objetivo:
            break
        posicao += 1

    for i in range(self.ultima_posicao, posicao - 1, -1):
        self.valores[i + 1] = self.valores[i]

    self.valores[posicao] = vertice
    self.ultima_posicao += 1

  def imprime(self):
   if self.ultima_posicao ==-1:
     print('O vetor está vazio')
   else:
     for i in range(self.ultima_posicao+1):
      print(i,' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo )

#o atributo distancia_objetivo será utilizado para fazer a inserção em ordem
#busca gulosa
vetor = VetorOrdenado(5)
vetor.insere(grafo_completo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.imprime()

print(vetor.valores[0].rotulo)

class Gulosa:
    def __init__(self, objetivo):
       self.objetivo = objetivo
       self.encontrado = False
       #o atual é ser o elemento que estamos processando agr. começa com arad e depois faz a ordenação 
    def buscar(self, atual):
        print("---------")
        print("Atual: {}".format(atual.rotulo))
        atual.visitado = True
        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True 
                    vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()
            
            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])   
#sempre vai pelo menor valor 
busca_gulosa = Gulosa(grafo.bucharest)#destino final
#é importante colocar por onde começar
busca_gulosa.buscar(grafo.arad) 