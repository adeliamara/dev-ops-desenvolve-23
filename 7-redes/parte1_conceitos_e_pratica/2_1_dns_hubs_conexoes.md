Falamos que existem diversos tamanhos de rede, agora, vamos começar com um projeto básico: uma rede que seria composta por dois computadores diretamente conectados. O computador usado na gravação do curso e um notebook conectado a ele por um cabo de rede azul será utilizado no curso. Comentamos que as máquinas na rede precisam de um endereço de identificação, chamado de IP. Mas nós sabemos que na rede, nós não podemos ter dois IPs iguais para máquinas diferentes. Cada computador precisa ter seu endereço de IP próprio - que não vem direto de fábrica. Existem duas formas de configurá-lo: uma máquina pode fornecer o endereço IP ou precisamos configurar manualmente. Como não temos uma máquina que faça isso, faremos isso manualmente usando o Windows. Nas explicações você verá como fazer isso no Linux e no Mac.

Vamos até no ícone de conectividade, depois em "configurações de rede", "Ethernet". Em seguida, clicaremos em "Ethernet", ao ser aberta uma nova janela, selecionaremos "Propriedades".


Será aberta uma nova janela, buscaremos pela opção "Protocolo IP Versão 4(TCP/IPv4)", depois em "Propriedades". Na nova janela, selecionaremos "Usar o seguinte endereço IP" e escreveremos o IP que ele deverá usar para fazer o teste.


Para finalizar, clicaremos em "OK" e fecharemos as janelas.

Para um dos computadores eu configurei o IP com o final 2 e o outro com o final 1.

Vamos testar a conectividade entre os dois computadores. Abriremos o Prompt de comando do Windows (ou o Terminal no Linux e no Mac), e digitaremos o ping e o IP da máquina ao lado da que estou usando.

`ping 192.168.3.1`

E a comunicação será estabelecida.

Foi enviada uma informação com 32 bytes e o laptop respondeu uma informação com os mesmo 32 bytes. Nós já havíamos falado que o tempo é referente ao envio das informações até a outra máquina e de retorno. O TTL é o tempo de vida útil do pacote, no caso, ele poderia passar por 128 máquinas antes de ser extinguido.

Se começarmos a analisar as estatísticas do ping, veremos que enviamos e recebemos quatro pacotes. Isto significa que a comunicação entre os dois computadores foi estabelecida com sucesso.

E será que existe uma forma de testarmos a conectividade da minha própria placa de rede? Talvez ela tenha algum problema de fábrica. A resposta é sim. Existe um endereçamento IP reservado para a parte interna da placa de rede, para fazer este teste de conectividade.

Vamos fazer um teste, ele será um endereçamento reservado que começará pelo 127.

`ping 127.0.0.1`

Este tipo de endereçamento chamamos de loopback, em que ele enviará a informação para ele mesmo para verificar se está tudo funcionando nesta transmissão interna.

No nosso teste, veremos que ela está funcionando adequadamente.


Mas como falei, o endereço é reservado e não podemos usá-lo para atribuir em outra placa de rede. Se retornarmos a configurações de rede, retornaremos a "Propriedade de Protocolo IP Versão 4 (TCP/IPv4)", onde acessamos anteriormente. Ao tentarmos modificar o IP para 127 receberemos uma mensagem de erro.

Ele nos informa que os endereços de IP que começam com 127 não são válidos, porque esta parte de número é reservada para testes de conectividade da placa de rede. Chegamos a um ponto importante aqui.

As traduções que estão sendo mostradas no terminal só possuem números. Vamos ver como é feita a tradução pelo servidor DNS, entre nome e endereçamento IP. Vamos fazer uma simulação no sistema operacional.

Abriremos o bloco de notas, com privilegio de administrador.


Você pode conferir como realizar o processo no Linux e no Mac clicando aqui aqui.

Vamos ver como fazer esta configuração. Percorreremos o seguinte caminho: Clicaremos em "C:"> "Windows" > System32 > drivers > etc. Então, mudarem o tipo de arquivos para "Todos os arquivos". Selecionaremos com o botão direito o "hosts", depois vamos em "Abrir com", será aberto um arquivo.



Observe que ocorre um mapeamento no meu sistema, entre o nome localhost e o IP 127.0.0.1. O localhost é o mesmo que usamos para programação Web. Vamos colocar outro nome para o endereçamento IP. Agora, tentaremos tentar encontrar o www.cursoderedesdaalura.com.
~~~
# localhost name resolution is handled within DNS itself.
#       127.0.0.1      localhost
#       ::1            localhost
         127.0.0.1      www.cursoderedesdaalura.com
~~~
Queremos que o nome seja traduzido para o endereço IP. Faremos o teste adiante.

`ping www.cursoderedesdaalura.com`


É esse processo de mapeamento que o DNS faz. Teremos as mesmas informações que tivemos nos testes anteriores, em que verificaremos que a conectividade foi estabelecida, obtivemos resposta, e temos quatro pacotes enviados e recebidos. Está tudo funcionando.


# Hands on

Vamos fazer agora a tradução do endereço IP de loopback para a url www.cursoderedesdaalura.com:

* Caso seja Windows: Abrir bloco de notas como administrador e abrir o arquivo hosts localizado em C:\Windows\System32\drivers\etc e insira na última linha o mapeamento 127.0.0.1 www.cursoderedesdaalura.com e teste o ping para essa url
* Caso seja Mac: Abrir o terminal e digitar: sudo vi /private/etc/hosts e posteriormente ir com a seta para baixo até ir numa linha em branco e realizar o mapeamento 127.0.0.1 www.cursoderedesdaalura.com pressione x, caso ele pergunte se deseja salvar diga que sim. Posteriormente teste o ping para essa url
* Caso seja Linux: Abrir o terminal e digitar: sudo vim /etc/hosts e posteriormente ir com a seta para baixo até ir numa linha em branco e realizar o mapeamento 127.0.0.1 www.cursoderedesdaalura.com pressione :wq para salvar e sair. Posteriormente teste o ping para essa url