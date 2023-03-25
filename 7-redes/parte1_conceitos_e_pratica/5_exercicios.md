# O que é o arp?


O ARP é o protocolo utilizado para fazer o mapeamento entre o endereço IP e o endereço MAC de um dispositivo. Isso é necessário porque o MAC encontra-se um nível abaixo do IP e eu preciso dele para poder transmitir as informações.

Em redes de computadores, temos protocolos que possuem hierarquias diferentes. Para poder chegar até o IP que está na camada 3, eu preciso passar pelo MAC que está na camada 2, pense como se fosse escalar uma pirâmide, não dá pra chegar ao topo sem passar pelo meio dela!

# Qual é a principal diferença entre os Hubs e os Switches?


O Hub não consegue aprender onde um equipamento está localizado, o Switch sim
Os hubs não conseguem aprender o endereço MAC das máquinas, já os Switches possuem essa função.


# Qual é uma forma de ataque usada para conseguir informações passadas no Switch destinadas a outro usuário?

Colocar vários endereços MAC falsos para “lotar” a memória do Switch e fazer com que ele atue como um Hub



Métodos usados por usuários maliciosos seria de inserir vários endereços MAC falsos para “lotar” a memória do Switch, uma vez que a memória esteja cheia, o Switch não vai conseguir definir quem está onde e ele passa a atuar como um Hub.

Podemos configurar a porta do Switch para aceitar um número máximo de endereços MAC, ao ultrapassar esse limite a porta é desligada e o ataque não teria sucesso.