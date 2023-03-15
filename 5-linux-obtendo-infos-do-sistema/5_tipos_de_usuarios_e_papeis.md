# O que é o sudo?
O comando sudo é usado no Linux e em outros sistemas operacionais baseados em Unix para permitir que usuários comuns executem comandos com privilégios de superusuário (root).

Geralmente, o sudo é configurado em sistemas Unix/Linux para permitir que usuários específicos ou grupos de usuários sejam autorizados a executar comandos com privilégios de superusuário. Esses usuários são conhecidos como "usuários sudo" e podem executar comandos com privilégios elevados, mas apenas quando autorizados e quando solicitados a inserir sua própria senha para autenticação.

Os usuários que não têm permissão para usar o sudo não podem executar comandos com privilégios de superusuário. Eles precisam autenticar com uma conta de usuário que tenha privilégios elevados para realizar tarefas administrativas ou usar o comando su (switch user) para trocar para uma conta de usuário com privilégios de superusuário.

Em resumo, o sudo pode ser usado por usuários que têm permissão para fazê-lo. As permissões são normalmente gerenciadas pelos administradores do sistema e, em geral, somente usuários confiáveis e experientes são autorizados a executar comandos

# Permissões

1. Por padrão, não devemos realizar tarefas com usuários privilegiados. Apenas tarefas especificos.

2. para verificar as permisscoes do sudo:

sudo cat /etc/sudoers

3. nem todos os usuarios tem permissoes de utilizar o sudo


4. para editar o sudo

sudo visudo

5. para visualizar quais grupos o usuario atual pertence:

groups

6. para verificar os grupos disponiveis:

cat /etc/group

7. para trocar de usuarios e ir para o root:
sudo su

8. para sair:
exit


# Diferença entre o root e os demais usuários

1. para mudar senha do usuario corrente:

passwd

2. para mudar senhas  no root, devemos fazer isso:

passwd nomedousuario

3. para visualizar infos dos usuarios (fora do root):

cat /etc/passwd | grep nomeousuario

4. e para ver as senhas?

sudo cat /etc/shadow
