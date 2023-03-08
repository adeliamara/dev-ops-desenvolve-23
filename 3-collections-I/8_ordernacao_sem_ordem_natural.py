
class ContaSalarioTeste:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalarioTeste:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalarioTeste(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalarioTeste(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalarioTeste(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
  print(conta)

#print(sorted(contas))

#print(conta_do_guilherme < conta_da_daniela)

def extrai_saldo(conta):
  return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
  print(conta)

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)

print(conta_do_guilherme < conta_da_daniela)

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def __lt__(self, outro):
    return self._saldo < outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme < conta_da_daniela)

print(conta_do_guilherme > conta_da_daniela)

for conta in sorted(contas):
  print(conta)

for conta in sorted(contas,reverse=True):
  print(conta)


for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)