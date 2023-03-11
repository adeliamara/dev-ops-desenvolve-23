# Comandos Linux


ip addr -> mostra ip

# controlando maquina remotamente

1. Abre terminal e digita seguinte comando

~~~ 
ssh nickname@ip
~~~

2. Coloque a senha da maquina que esta sendo acessada

3. apt é para gerenciamento de pacote. acessa o repositorio. sudo coloca permissoes de admin

~~~ 
sudo apt update
~~~

4. Se não houvesse ssh instalado, faça
~~~ 
sudo apt instal openssh-server
~~~

5. Como saber o ip na maquina linux?

~~~ 
ifconfig
~~~

* obs: precisa ter o net-tools. para isso faça 
~~~
sudo apt install net-tools
~~~

<strong> Tive um erro aqui na etapa 1</strong>

<br> Resolve assim: O erro "'ssh' não é reconhecido como um comando interno ou externo, ou programa operável ou arquivo em lotes" geralmente indica que o comando SSH não está instalado ou não está configurado corretamente no seu sistema operacional.

O SSH (Secure Shell) é um protocolo de rede criptografado que permite a conexão segura a um servidor remoto. Se você estiver tentando executar o comando SSH em um prompt de comando ou terminal e receber essa mensagem de erro, pode ser necessário instalar o cliente SSH em seu sistema operacional ou adicionar o caminho para o executável SSH às suas variáveis de ambiente.

Se você estiver usando o Windows, uma opção é instalar o cliente OpenSSH, que pode ser baixado no site oficial do projeto OpenSSH. Após a instalação, adicione o caminho para o executável SSH à sua variável de ambiente PATH. Para fazer isso, siga estas etapas:

Abra o Painel de Controle e selecione "Sistema e Segurança" > "Sistema".
Clique em "Configurações avançadas do sistema".
Na guia "Avançado", clique em "Variáveis de Ambiente".
Em "Variáveis do Sistema", selecione a variável "Path" e clique em "Editar".
Adicione o caminho para o diretório contendo o executável SSH (por exemplo, C:\Program Files\OpenSSH\bin) ao final do valor da variável "Path".
Clique em "OK" para fechar todas as janelas de configurações.
Depois de adicionar o caminho do executável SSH às suas variáveis de ambiente, tente executar o comando SSH novamente no prompt de comando ou terminal.


Para instalar o cliente OpenSSH em um sistema operacional baseado em Windows, siga as instruções abaixo:

Baixe o pacote de instalação mais recente do cliente OpenSSH para Windows a partir do seguinte repositório: https://github.com/PowerShell/Win32-OpenSSH/releases.

Extraia o conteúdo do arquivo zip baixado para uma pasta de sua escolha.

Abra o Prompt de Comando ou o PowerShell como Administrador. Você pode fazer isso clicando com o botão direito do mouse no ícone do Prompt de Comando ou do PowerShell e selecionando "Executar como administrador".

Navegue até o diretório onde você extraiu o pacote de instalação usando o comando "cd". Por exemplo, se você extraiu o pacote na pasta Downloads, digite o seguinte comando no Prompt de Comando ou PowerShell:

bash
~~~
cd C:\Users\<seu nome de usuário>\Downloads\Win32-OpenSSH
~~~
Substitua "<seu nome de usuário>" pelo nome de usuário do seu computador.

Execute o script de instalação usando o seguinte comando:
~~~
install-sshd.ps1
~~~
Siga as instruções na tela para concluir a instalação do cliente OpenSSH.

Adicione o diretório contendo o executável SSH às suas variáveis de ambiente. Para fazer isso, abra o Painel de Controle e vá para Sistema > Configurações avançadas do sistema > Variáveis de ambiente. Em "Variáveis do sistema", encontre a variável "Path" e clique em "Editar". Adicione o caminho para o diretório onde o executável SSH está localizado (geralmente C:\Program Files\OpenSSH\bin) e clique em "OK".

Depois de instalar o cliente OpenSSH, você pode testá-lo digitando "ssh" no Prompt de Comando ou PowerShell. Se o comando for reconhecido, o cliente OpenSSH foi instalado corretamente e está pronto para uso.