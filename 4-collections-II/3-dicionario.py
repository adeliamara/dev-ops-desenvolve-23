aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}


print(type(aparicoes))


print(aparicoes["Guilherme"])


# Falar que eu quero pegar a chave "xpto", se não estiver lá dentro a chave "xpto", devolva zero.
aparicoes.get("xpto", 0)


novo_dict = dict(guilherme = 2, paulo = 1)
print(novo_dict)


#ad elementos

novo_dict["Carlos"] = 1

del novo_dict["guilherme"]
print(novo_dict)


print("Guilherme" in novo_dict)



for elemento in aparicoes.values():
  print(elemento)
  
  
  
for chave, valor in aparicoes.items():
  print(chave, "=", valor)