grafo = {}
grafo["voce"] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []

from collections import deque

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def search(grafo, inicio):
    fila_de_pesquisa = deque(grafo[inicio]) 
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()

        if not pessoa in verificadas: 
            if pessoa_e_vendedor(pessoa):
                print (f"{pessoa} é um vendedor")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
 

   
    return False

search(grafo, 'voce')
