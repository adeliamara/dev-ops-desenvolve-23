1. sudo mkdir /projetos

2. sudo chmod 770 /projetos

3. sudo chmod 774 /projetos

4. mudando dono de arquivo: sudo chown ricardo /projetos

5. mudando grupo e dono:

sudo chown riacardo:projeto /projetos


# Atenção: se vc quer que o usuario leia um arquivo, ele deve ter permissao x do diretorio.


# Permissão especial: serve para os arquivos de dentro de um diretorio recebeam as mesmas permissoes do diretorio pai

sudo chamod g+s

o que é essa permissao?

No contexto de permissões de arquivos no Linux, a permissão "s" se refere ao "bit setuid" ou "bit setgid", dependendo de onde é aplicado.

Quando a permissão "s" é definida em um arquivo, ela significa que o arquivo deve ser executado com as permissões do proprietário do arquivo. Isso é conhecido como "bit setuid" ou "suid". Isso pode ser útil, por exemplo, quando um arquivo precisa ser executado como root para acessar certos recursos, mas deve ser acessado por um usuário comum. Nesse caso, definir a permissão "s" no arquivo permitiria que ele fosse executado com as permissões de root, mas ainda pudesse ser acessado por usuários comuns.

Por outro lado, quando a permissão "s" é definida em um diretório, ela significa que os arquivos criados nesse diretório herdarão o grupo do diretório, em vez do grupo do usuário que os criou. Isso é conhecido como "bit setgid" ou "sgid". Isso pode ser útil em situações em que vários usuários precisam compartilhar acesso a um diretório, mas precisam garantir que os arquivos criados no diretório pertençam ao mesmo grupo.

Você pode ver a permissão "s" em arquivos e diretórios listados com um "s" em vez de "x" na posição do bit de permissão "x". Por exemplo, se um arquivo tiver a permissão "s" definida, sua listagem de permissões de arquivo seria algo como "-rwsr-xr-x". Se um diretório tiver a permissão "s" definida, sua listagem de permissões de diretório seria algo como "drwxrwsr-x"