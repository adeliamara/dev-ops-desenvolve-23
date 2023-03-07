#Listas são uma sequencia de acesso aleatorio
idades = [39, 30, 27, 18]

#tipo da collection
print(type(idades))

#tamanho da collection
print(len(idades))

#listas sao mutaveis
idades.append(15)
idades.remove(39) 
#quando um elemento se repete, o remove remove apenas o primeiro elemento

#se o elemento nao existe, o remove dá um erro. Por isso, reomenda-se utilizar o algoritmo abaixo:
if 28 in idades:
    idades.remove(28)

#remover todos os elementos
idades.clear()

#checar se um elemento esta em uma lista
print(15 in idades)

#adicionar elementos em posicoes diferentes insert(posicao, elemento)
idades.insert(0,20)

#adicionar mais de um elemento de uma vez em yma lista
idades.extend([27,19])

#iterando sobre listas
idades_no_ano_que_vem = []
idades_no_ano_que_vem.append(idades + 1)
idades_no_ano_que_vem = [(idade + 1) for idade in idades]

#filter
idades_filtradas = [(idade) for idade in idades if idade > 21]

####### ser mutável é bom? ##########

#Listas sao passadas por referencia


def faz_processamento_de_visualizacao(lista = []):
    print(len(lista))
    lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()


#como boa pratica, faça:
def faz_processamento_de_visualizacao(lista = None):
    if(lista == None):
        lista = list()
    print(len(lista))
    lista.append(13)
    
    
    
    
    


