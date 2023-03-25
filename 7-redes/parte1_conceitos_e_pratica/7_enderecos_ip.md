# Classes IP

Nós já discutimos que para uma máquina ser identificada, precisaremos do IP dela. Mas será que nós podemos criar qualquer valor em qualquer intervalo do endereço? Não podemos! Existe um órgão internacional que regulamenta os IPs colocando em classes que podem ser utilizadas.

## Classe A

 A classe A é a primeira que veremos.

~~~
Para um endereço IP estar dentro da classe A, deverá ter o primeiro octeto variando de 1-126 e a máscara de rede padrão deverá ser 255.0.0.0.
~~~


Sabemos que a máscara de rede irá separar o IP em "Rede" e "Host". Desta forma, o que for referente a 255 fará parte da rede, e o que for 0 pertencerá a parte das máquina

## Classe B

Para fazer parte da classe B, o endereço IP deve ter o seu primeiro octeto dentro dos valores 128-191 e a máscara padrão será 255.255.0.0. 

## Classe C

para fazer parte desta classe, o IP deve ter o primeiro octeto dentro do intervalo 192-223 e a máscara de rede padrão será 255.255.255.0.


## Classes D e E

Ela será caracterizada pelo primeiro octeto indo de 224-239. Mas ela é diferente das demais, por ser reservada para o uso de multicast (casos em que queremos fazer a comunicação somente com alguns dispositivos que estão na nossa rede). Ela não é atribuída para máquinas. Assim como a classe E, identificada pelo intervalo 240-255 no primeiro octeto.


as duas últimas classes não são usadas para serem endereçadas as máquinas. A classe D seria usada para multicast (termo usado quando queremos nos comunicar com somente algumas máquinas de nossa rede) e a classe E seria uma classe experimental. Portanto as classes de IP que podem ser endereçadas para máquinas seriam a classe A, B e C.

