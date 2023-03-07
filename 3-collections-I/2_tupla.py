class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
        
    def deposita(self, valor):
        self.saldo += valor
        
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
    
conta_adelia = ContaCorrente(15)
print(conta_adelia)

conta_adelia.deposita(500)
print(conta_adelia)


conta_karla = ContaCorrente(22)
conta_karla.deposita(1000)
print(conta_karla)

contas = [conta_adelia, conta_karla, conta_adelia]
print(contas)


for conta in contas:
    print(conta)
    
#tupla é imutavel, mas lista é mutavel  
  
tupla = ('Adélia', 10, 20)

#mas note que ela faz uma referencia. Se nós mudarmos o objeto refeenciado, pode ocorrer
tupla2 = (conta_adelia, conta_karla)

#mas normalmente nao é usado assim, possivelmente importa