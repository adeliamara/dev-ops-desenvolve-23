Nós tentamos fazer o teste de comunicação entre o Financeiro e o Marketing, mas ainda não tivemos sucesso.

Quando usamos o ping para uma máquina se comunicar com a outra, ele comparou o IP de destino 192.168.3.2 com o do Financeiro 191.168.3.1. Como a nossa máscara de rede é 255.255.255.0, ele perceberá que os quatro primeiros octetos dos IPs não são iguais. As máquinas estão em redes diferentes. Mas agora, o nosso computador não sabe para onde enviar a informação. Ele sabe que queremos acessar um dispositivo que não está na mesma rede. Então, precisaremos indicar para onde queremos que a informação seja enviada.

Diremos para o computador: "caso você precise se comunicar com um computador em uma rede diferente, você enviará para o roteador. Afinal, a função do roteador é conectar redes diferentes." O computador passará o problema para o roteador, que terá que encontrar uma forma de enviar a informação adiante.

Para isto, preencheremos um novo campo na "IP Configuration".


Traduzido para o português, Default Gateway significa portão padrão ou seja, trata-se do portão de saída da rede - que no nosso caso, será o roteador. Usaremos o endereço IP configurado em cada porto do roteador. Para descobrirmos o número, na linha de comando digitaremos o seguinte:

Router>enable
router#show ip interface briefCOPIAR CÓDIGO
O brief indicará que queremos um resumo das interfaces IPs que ele possui.

IPs configurados

Dois IPs foram configurados: 191.168.3.7 é a configuração do IP que fizemos na porta conectada com o laptop, enquanto o 192.168.3.5, é o IP configurado com a porta da outra máquina. Já sabemos qual número preencher no campo de Default Gateway.

Default Gateway 2

Agora, a informação consegue sair da rede. Vamos fazer um novo teste usando o ping. No "Command Prompt", digitaremos o seguinte:

PC>ping 192.168.3.2COPIAR CÓDIGO
Mas ainda não teremos sucesso. Lembraremos como o ping funciona: dentro dele, temos o protocolo ICMP - que funciona como um telefone e verificará se o outro computador está ativo, permitindo a comunicação entre os dois. A informação consegue sair do computador do Financeiro, mas o computador do Marketing não sabe como retornar a informação. Teremos que indicar para ele também qual será o portão de saída.

Default Gateway 3

Informamos para o computador do Marketing qual era o portão de saída.

Faremos um novo teste de conectividade, desta vez, os dois computadores foram configurados para enviarem as informações para o roteador. No terminal, digitaremos:

PC>ping 192.168.3.2COPIAR CÓDIGO
conexão estabelecida

A conexão foi estabelecida. Observe que quando fizemos os testes com os dois computadores diretamente, aparecia no retorno o TTL igual a 128 (agora, o valor é 127). Isto acontecia porque não tínhamos o roteador, que irá decrementar em uma unidade cada vez que os pacotes passarem por ele.

