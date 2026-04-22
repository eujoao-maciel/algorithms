voted = {}

def verifica_eleitor(nome):
    if voted.get(nome): 
        print ("Mande embora")

    else:
        voted[nome] = True
        print ("Deixe votar.")


for nome in range(0, 5):
    nome = input("Digite o seu nome: ")
    verifica_eleitor(nome)
    
print (voted)





