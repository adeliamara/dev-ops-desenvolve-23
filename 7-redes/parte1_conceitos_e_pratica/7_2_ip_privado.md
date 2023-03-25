Nos vimos três classes de IP que são utilizadas para o endereçamento nas máquinas: A, B e C. As classes D e E não são utilizadas para a atribuição em máquinas.

Dentro de cada um dos intervalos de IP, teremos faixas que são chamadas de privadas. Elas recebem esse nome, porque só podemos nos comunicar na rede local, não podendo ser utilizados na comunicação na internet.

Os endereços IP privados são usados para comunicação somente em minha rede local, de acordo com a especificação, eles não podem ser usados para comunicação na internet por exemplo.


* Na classe A, temos a faixa de endereço que começam com 10 não poderá se comunicar na internet.

* Na classe B, os endereço que serão privados começarão com 172.16 até 172.31.

* Os endereço privado na classe C começarão com 192.168.


Nós acabamos de ver que os IPs que começa com 192.168 estão dentro da faixa de privados. Então, como estamos conseguindo acessar a internet? O meu roteador irá traduzir o IP privado pelo IP público. Quando contratamos um serviço de empresas como a Vivo ou GVT, elas nos fornecem um número de IP público. Se fizermos uma pesquisa no site Meu IP, o IP que será identificado será outro.



O IP 189.18.129.152 será o número que a Vivo atribuiu. Observe que efetivamente o roteador fez a tradução do endereço que aparecia no Prompt para o que vemos no site. Isto é feito por meio do método NAT (Network Address Translation), em que é feita a tradução de um endereço privado para o público.


