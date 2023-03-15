1. usamos o ps:

ps -e

2. para entender melhor:

man ps

3. para ver os processos mais detalhadamente:

ps -ef

4. o pid é o processo do id. o ppid é o pai do processo.

5. semelhante ao gerencidador de procesos windoes:

ps aux

6. há um daemon rodando no servidor. normalmente chamado de daemon + d, por isso viauzliamos sshh.

7. o ps é uma foto, mas podemos ver isso de forma mais dinamica?

top


8. ordenando por ordem de cpu

apos entrar no top, aperte: P

consumo de memoria: M

por pid: N

9. para sair do top:
q




# Para praticar

1. instale o apache 2: sudo apt install apache2

2. apos instalar, verifique se esta ecutando: sudo service apache2 status


3. coloque o ip da maquina no google

4. use o top para ver os processo ativos. Dentro do top, digite L e o nome da string que procura, semelhante ao grep


5. Para visualizar os processo em andamento, vamos gerar uma carga no serviro. Crie um novo terminal e acesse a maquina

6. faça o seguinte comando:
~~~
while :; do curl -l http://192.168.100.5;done
~~~

## O que é o apache?
Apache2 é um servidor web de código aberto, o mais popular da Internet, que permite a entrega de conteúdo na web para navegadores da Internet. Ele é amplamente utilizado para hospedar sites e aplicativos da web em várias plataformas, incluindo Linux, Unix, Windows e MacOS.

Quando você digita o endereço IP da máquina no Google, é provável que o Apache2 seja exibido porque ele é o servidor da web padrão para muitas distribuições de Linux e outras plataformas. Quando o Apache2 está em execução, ele responde às solicitações dos navegadores da Internet e exibe conteúdo da web armazenado em diretórios específicos do sistema de arquivos. Por padrão, o Apache2 exibe uma página de boas-vindas quando nenhuma página específica é solicitada. Isso pode ser o que você está vendo ao digitar o endereço IP da máquina no Google.

# Matando processos


1. kill -l

para ver as opções  de subausdisponiveis

2. para matar o processo:
kill -9 piddoprocesso


3. para matar o processo com o termo podemos fazer

kill piddoprocesso

ou k

kill -15 piddoprocesso



# tipos de sianais no kill

O comando kill é usado para enviar sinais para processos em execução no sistema Linux. Existem vários sinais que podem ser enviados, mas os mais comuns são o sinal 15 (SIGTERM) e o sinal 9 (SIGKILL).

O sinal 15 (SIGTERM) é usado para solicitar que um processo encerre de forma amigável, permitindo que o processo execute algumas tarefas de limpeza antes de terminar sua execução. Quando o processo recebe o sinal SIGTERM, ele pode escolher como lidar com ele, mas geralmente ele inicia o processo de desligamento ordenado.

Por outro lado, o sinal 9 (SIGKILL) é usado para terminar imediatamente um processo sem dar a ele a chance de executar qualquer tarefa de limpeza. Quando o processo recebe o sinal SIGKILL, ele é encerrado imediatamente, sem fazer qualquer limpeza ou finalização.

Em geral, é recomendado enviar o sinal SIGTERM para um processo em primeiro lugar, permitindo que ele encerre de forma ordenada. Se o processo não responder ao sinal SIGTERM ou se houver uma necessidade urgente de encerrar o processo, pode-se usar o sinal SIGKILL para encerrá-lo imediatamente. No entanto, é importante lembrar que o sinal SIGKILL não permite que o processo faça qualquer limpeza ou finalização antes de ser encerrado, o que pode levar a problemas de integridade do sistema ou perda de dados.