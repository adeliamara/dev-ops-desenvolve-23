1. script é uma sequencia de comandos. Podemos usar scripts de backup no linux


2. Variaveis do ssitema: o que são?

~~~
env
~~~

o comando acima mostra as variavies de sistema.

~~~
echo $HOME
~~~

ver o conteudo das variaveis de sistema

3. criando script:

~~~
vi backup.sh
~~~

insira no arquivo:

~~~  configuramos o shell que vamos utilizar, escolhemooos o bash
#!/bin/bash

echo "digite o diretorio de backup:"
read diretorio_bkp

cp -rv $diretorio_bkp ~/backup
echo ""
echo "Backup concluido!"
~~~

4. na linha de comando do linux, crie diretorio backup:
mkdir backup



5. permissoes:
chmod u+x nomearquivo -> usuaio tem permissao de executar

6. executando script
./backup.sh


7. criando uma variavel de ambiente para o script. va ao diretorio raiz e faça:

mkdir bin

cp labs/scripts/backup.sh .

AGORA, podemos rodar o backu de qaulquer direotrio








