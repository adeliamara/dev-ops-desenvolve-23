# Administrando usuários e grupos

O usuário que estamos utilizando foi criado automaticamente na hora que instalamos o sistema. Ao acessar a home e digitarmos `ls` conseguimos ver todos os usuários 

1. Adicionar novo usuário: `sudo useradd novousuario` ou `sudo adduser novousuario`

* Quando criamos um usuário é craido por default um grupo com o nome do usuário, este é o grupo primário. O usuario poderá ser colocado em grupo `suplementares`. Além disso, ele também popula o diretorio do usuário. Copia os carvios do `/etc/skel`.


## Quando usar useradd e quando usar adduser?

Tanto o `useradd` quanto o `adduser` são comandos usados no Linux para criar novos usuários, no entanto, existem algumas diferenças sutis entre os dois.

O comando useradd é mais primitivo e requer mais opções para criar um usuário. É necessário especificar manualmente todas as informações do usuário, como nome de login, UID, diretório inicial, grupo primário, entre outros.

Por outro lado, o comando `adduser` é uma interface mais amigável que simplifica o processo de criação de usuário. Ele possui um script que interage com o usuário e faz perguntas para preencher as informações necessárias. Além disso, o adduser oferece mais recursos, como a possibilidade de criar automaticamente um diretório inicial e um diretório compartilhado com permissões de grupo.

Em resumo, se você é um usuário iniciante ou deseja criar usuários de forma mais fácil e com mais recursos, é recomendável usar o adduser. Por outro lado, se você precisa de mais controle e personalização ao criar usuários, o useradd pode ser a melhor opção.

Observe que useradd não cria o usuário. Criou apenas um ponteiro para esse usuario. Para ver isso, digite

`cat /etc/passwd | grep nomeusuario`


O /etc/passwd corresponde ao banco de dados de usuários LOCAIS do sistema.

## O que são os numeros que aparecem na frente do usuário? 

São o Uid. Se fosse grupo, seria o gid.Números do UID abaixo de 1000 são usuários do sistema

## Onde ficam as senhas dos usuários? 

As “senhas” dos usuários ficam registradas em:

`/etc/shadow`

o /etc/shadow armazena o hash das senhas. Nenhum sistema moderno deve fazer o armazenamento de senhas.


2. Como ver os grupos de um usuario?

groups nomedousuario

3. Como logar em outro s usuarios?

`su - nomeuser`

4. como adicionar o usuario a um novo grupo?

`sudo groupadd nomedogrupo`

### Para ver os grupos existentes: `cat /etc/group`

4. como adicionar o usuario a um grupo suplementares?

`sudo usermod -aG nomedogrupo nomedousuario`

*** se o g for minusculo, estaremos mudando o grupo primario do usuario *** cuidado!!


5. Remover usuario: `sudo userdel nomedousuario`

6. remover grupo: `sudo groupdel nomedogrupo`






