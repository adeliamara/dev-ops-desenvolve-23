from collections import defaultdict

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)


from collections import defaultdict

aparicoes2 = defaultdict(int)

#passando funcao int() que retorna 0

#definindo que os valores serao int. por padrão, se nao houve usa 0


for palavra in meu_texto.split():
  ate_agora = aparicoes2[palavra]
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)




aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)






class Conta:
    def __init__(self):
        print("Criando uma conta")
        
contas = defaultdict(Conta)

#sempre que chamamos algo que nao esta aqui, criamos uma nova
print(contas[15])


from collections import Counter
aparicoes = Counter(meu_texto.split())
print(aparicoes)

    
    
    