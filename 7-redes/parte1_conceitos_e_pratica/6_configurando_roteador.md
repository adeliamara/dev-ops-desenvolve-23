Vamos começar a configuração do roteador. 

Faremos uma análise da imagem. Provavelmente, o roteador que temos nas nossas casas é bastante parecido ao da imagem. Nos dispositivos domésticos, geralmente, encontramos essas portas amarelas que são o Switch. Para economizar espaço, ele traz os Switch embutido.

![roteador](/imgs/rot1.png)

O equipamentos da Cisco, que aparecem no Packet Tracer são focados para empresa. Por isso, ocorre a segmentação entre Switch, que conectara vários usuários, e o Roteador para mandar os usuários para uma outra rede. Ocorre uma separação nos equipamentos de empresa.

Por isso, só teremos duas portas no roteador do projeto.


Para realizarmos a configuração dos equipamentos da Cisco, precisaremos utilizar um cabo especial: cabo console. Ele terá o seguinte formato:


![roteador](/imgs/rot2.png)



É um cabo azul, em que uma das pontas terá o conector plástico (RJ45) e na outra, terá o conector que recebe o nome de Rs232, referente a uma porta serial (que transmitirá os bits um por vez).

A conexão real será feita com o RJ45 sendo conectado na porta de console do roteador e o Rs232 será conectado na porta do computador. No entanto, a maioria dos computadores fabricados atualmente não possuem está porta serial, elas foram substituídas pelo USB. Isto significa que precisaremos usar um adaptador para realizar a configuração do equipamento.

E que programa será usado para utilizar o equipamento da Cisco? Existem programas que chamamos de Terminal, o mais famoso deles se chama `PuTTY` e é bastante utilizado.


O PuTTY é muito útil quando queremos acessar remotamente um equipamento. Isto significa que podemos acessar um equipamento em outra cidade e configurá-lo. Se tiver alguém na outra localidade que permita o acesso à distância, não precisaremos nos deslocar para realizar a configuração. Por isso, ele é bastante utilizado, além de ter um interface gráfica que não é tão cansativa.

Agora, voltaremos para o nosso projeto e realizaremos a configuração.

Adicionaremos um novo computador, selecionando o ícone no meu do canto inferior esquerdo. Depois, selecionaremos um cabo para conectar a nova máquina. Após clicarmos no menu do raio, vamos escolher o segundo cabo da listagem.


Em seguida, daremos um clique no ícone do computador e selecionaremos a porta RS232, a porta serial. Conectaremos com roteador e selecionaremos "Console".


Isto o que é feito na prática: precisamos utilizar o cabo e o programa para acessar o equipamento. Mas a equipe da Cisco facilitou o nosso trabalho, em vez de precisarmos conectar os equipamentos nos projetos, podemos clicar no ícone "Router" e ir até a aba "CLI" (Command Line Interface), em que poderemos configurar o equipamento.


Mas precisaríamos fazer a conexão via computador na prática. Para isto, clicaremos no computador, depois, seguiremos até a aba "Desktop" e selecionaremos o Terminal.


No Terminal, ele perguntará como queremos conectar com o roteador. Nós deixaremos as velocidades padrões. Receberemos as mesmas informações. A partir de agora, faremos as configurações clicando diretamente no roteador. Mas é possível realizar a ação ao clicarmos no computador.

Lembre-se: podemos fazer a configuração dando um clique duplo no roteador apenas no Packet Tracer. Na prática, precisaremos fazer a configuração real por meio do computador.

Como trabalharemos diretamente no roteador, vamos apagar o computador.

É possível configurar a tela do CLI, caso você queira que ela esteja como é mostrado no curso. Basta seguir o seguinte caminho: Options -> Preferences -> Font. Serão abertas algumas opções, em que é possível determinar o tamanho e a cor da fonte, além da cor de fundo da tela.


Na aba CLI é possível realizar a configuração do equipamento da Cisco. Nosso objetivo é estabelecer a conexão entre o setor Financeiro e o Marketing, que estão em redes diferentes no projeto.

O Financeiro terá o IP 191.168.3.1, enquanto o Marketing terá o IP 192.168.3.2. Nós iremos estabelecer a comunicação entre eles.

A porta do roteador aparecerá com a cor vermelha, porque elas são desabilitadas por padrão.


Então, a primeira coisa que faremos é habilitar as portas. Na parte de configuração eles perguntam se queremos um diálogo (Contiune with configuration dialog?). Ele será feito passo a passo, e pode ser demorado. Como nós queremos uma configuração simples, responderemos "não".


A tela começará a aparecer no primeiro modo de operação. O Router> indicará o que chamamos de modo usuário. Quem acessá-lo, só poderá fazer algumas configurações básicas da plataforma. Ele não poderá configurar nada efetivamente, por uma questão de segurança.

Para sabermos quais configurações são possíveis de serem realizadas no modo usuário, digitaremos o ?:
~~~
Router>?
~~~
O comando ? poderá ser utilizado em qualquer terminal da Cisco. Podemos usá-lo com outros comandos, como enable por exemplo.
~~~
Router>enable ?
~~~
E ele retornará tudo que ainda pode ser feito com o enable. O sinal de interrogação ? nos auxilia durante toda a etapa da escrita do código.


Comentamos sobre o modo usuário. O que teremos que fazer se quisermos aumentar o usuário para realizarmos a configuração? Para isto digitaremos enable apenas.
~~~
Router>enable
Router#
~~~
Depois do Router, ele deixará de ser seguido pelo símbolo > e passará a usar a #, que indica o modo privilegiado. Ainda não poderemos configurar o equipamento, mas se usarmos novamente a ?, ele nos retornará uma lista de visualizações do que chamamos de reparo de problemas.


Assim conseguimos verificar possíveis problemas do equipamento. Observe que no fim da tela aparece o More indicando que a lista ainda possui mais itens. Para ver as demais, podemos clicar em "Enter" (para vermos uma de cada vez) ou pressionar a barra de espaço e todas serão mostradas de uma vez.

Já que estamos no modo privilégio, entraremos na aba de configuração. Digitaremos configure terminal.
~~~
Router#configure terminal
~~~
Observe que agora o modo de operação mudou para configurarmos o computador.

~~~
Router config
~~~
Podemos visualizar o config. Em seguida, começaremos a habilitar as portas. Habilitaremos a porta "FastEthernet 0/0". Escreveremos isso na aba CLI:
~~~
Router(config)#interface fastEthernet 0/0
~~~
Ao escrever um número mínimo de caracteres, como fast por exemplo, ele completará automaticamente fastEthernet. Quando pressionarmos "Enter", ele já subirá o privilégio:
~~~
Router(config-if)#
~~~
gora, nós estamos configurando a interface. Nós iremos habilitá-la adicionando no shutdown.
~~~
Router(config-if)#no shutdown
~~~
A porta será habilitada.


E uma das luzes do computador já ficará verde.


Vamos sair da configuração desta porta digitando:
~~~
Router(config-if)#exit
~~~
E começaremos a habilitar a porta fastEthernet 0/1:

~~~
Router(config)#interface fastEthernet 0/1
Router(config)#no shutdown
~~~


Agora, as duas portas estão configuradas.


Precisaremos ainda configurar o endereçamento IP que cada uma das portas receberá, para podermos fazer está transição da rede do Financeiro para a rede do Marketing. Para isto, digitaremos o ip ? na aba CLI:
~~~
Router(config-if)#ip ?
~~~

Usamos a ? para recebermos auxilio no processo.


Vemos quais opções ele permite. Em seguida, digitaremos address ?.


Ele nos informa que devemos configurar um IP estático ou a configuração DHCP - em que uma máquina nos entregará os IPs. Como nós não temos a máquina, iremos adicionar o estático manualmente. O IP do Marketing é 192.168.3.2, mas para o roteador, iremos configurar um IP que terá o último octeto com o valor diferente: 192.168.3.5. Mas os dois estarão na mesma rede. Se digitarmos o ? novamente, ele dirá que falta informar a máscara de rede relacionada ao IP. Por isso, adicionaremos 255.255.255.0.
~~~
Router(config-if)#ip address 192.168.3.5 255.255.255.0
~~~


A configuração do IP dessa rede já foi estabelecida. Vamos fazer um teste de conectividade.

Apertaremos o "control+Z" para sair da aba de configuração da internet FastEthernet 0/1 e depois, digitaremos ping.

~~~
Router#ping 192.168.3.2
~~~

configurando ip das portas 5

A requisição teve sucesso, de cinco pacotes enviados, quatro retornaram. Isto significa que conseguimos nos comunicar com o computador da rede de Marketing.

Faremos o mesmo processo de configuração para o computador do Financeiro.

Entraremos na configuração do Terminal.


~~~
Router#configure Terminal
~~~


Digitaremos interface fa0/0.


~~~
Router(config)#interface fa0/0
~~~

Depois, adicionaremos ip address e o endereçamento IP deve estar na rede do Financeiro. Seguiremos a máscara de rede, e o IP terá apenas o último octeto diferente: 191.168.3.7.
~~~
Router(config-if) address 191.168.3.7 ?
~~~
Com o ? descobrimos o que falta preencher.


Ele pediu para adicionarmos a máscara de subnet, como fizemos anteriormente.


~~~
Router(config-if) ip address 191.168.3.7 255.255.255.0
~~~

Usaremos o comando "Control+Z" para voltarmos ao modo inicial. E logo, testaremos a conectividade usando o ping.
~~~
Router#ping 191.168.3.1
~~~

O roteador consegue pingar o computador tanto da rede do Marketing como a do Financeiro. Isto significa que os dois computadores podem se comunicar diretamente. Vamos testar. Clicaremos no computador do Financeiro, na janela que será aberta, vamos na aba "Desktop" e depois, em "Command Prompt". Na linha de comando, adicionaremos o ping.

~~~
PC>ping 192.168.3.2
~~~

No entanto, ninguém respondeu a nossa requisição. Vamos continuar a configuração e entender o porquê de isso acontecer.

