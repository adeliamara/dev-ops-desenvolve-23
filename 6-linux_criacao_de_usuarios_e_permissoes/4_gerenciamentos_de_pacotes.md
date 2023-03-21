1. `sudo apt install apache2` e podemos usar tambem `sudo apt-get apache2`

### Qual a diferença?

Tanto o comando "sudo apt install" quanto o "sudo apt-get install" são utilizados para instalar pacotes de software no sistema operacional baseado em Debian. Ambos os comandos instalam os pacotes necessários, suas dependências e quaisquer outros arquivos necessários para o funcionamento correto do software.

No entanto, há uma diferença sutil entre os dois comandos. O "apt" é um gerenciador de pacotes mais moderno e avançado que foi introduzido no Ubuntu 16.04, enquanto o "apt-get" é um gerenciador de pacotes mais antigo e básico que está presente em versões anteriores do Ubuntu e outras distribuições baseadas em Debian.

O "apt" é uma interface de linha de comando mais amigável e possui recursos adicionais, como a capacidade de exibir informações detalhadas sobre os pacotes, realizar pesquisas avançadas e atualizar a lista de pacotes automaticamente. Ele também usa uma saída mais fácil de ler e interpretar.

Por outro lado, o "apt-get" é uma ferramenta mais básica que é usada para tarefas básicas, como instalar pacotes, remover pacotes e atualizar a lista de pacotes. Ele é um pouco menos amigável para o usuário em comparação com o "apt".

Em resumo, o "apt" é uma ferramenta mais avançada e moderna para gerenciamento de pacotes que oferece recursos adicionais, enquanto o "apt-get" é uma ferramenta mais antiga e básica que é útil para tarefas simples. No entanto, ambos podem ser usados para instalar pacotes de software no sistema operacional baseado em Debian.



2.  `sudo apt update`
precismoas


O comando "sudo apt update" é utilizado em sistemas operacionais baseados em Debian (como Ubuntu, Linux Mint, etc.) para atualizar a lista de pacotes disponíveis nos repositórios de software.

Quando você executa o comando "sudo apt update", o sistema operacional consulta os repositórios de software para verificar se existem atualizações ou novos pacotes disponíveis desde a última atualização. Em seguida, o sistema atualiza a lista de pacotes disponíveis localmente no seu sistema operacional.

Isso é importante porque, se você tentar instalar um novo software ou atualizar um software existente sem antes atualizar a lista de pacotes, o sistema operacional pode não encontrar as versões mais recentes do software que você está tentando instalar.

Em resumo, executar "sudo apt update" é um passo importante antes de instalar qualquer software ou atualizar o sistema, pois garante que você tenha acesso às versões mais recentes dos pacotes disponíveis.


3. `apt search apache2`: mostra tudo que está instalando no sistema


O comando "apt search" é utilizado para pesquisar pacotes de software disponíveis nos repositórios de software do sistema operacional baseado em Debian.

Ao executar o comando "apt search", o sistema operacional consulta a lista de pacotes disponíveis e retorna uma lista de pacotes que correspondem à palavra-chave fornecida como argumento para o comando.

Por exemplo, se você executar o comando "apt search editor de texto", o sistema operacional retornará uma lista de pacotes de software relacionados a editores de texto. A saída incluirá o nome do pacote, uma breve descrição e outras informações relevantes.

O comando "apt search" é útil para encontrar pacotes de software específicos quando você não sabe o nome exato do pacote. Ele também pode ser útil para descobrir novos pacotes que você pode não ter conhecido anteriormente.

Uma vez que você tenha encontrado o pacote que deseja instalar usando o comando "apt search", você pode usar o comando "apt install" ou "apt-get install" para instalar o pacote no seu sistema operacional.

Faça `apt help` em caso de duvidas.
# atencao:

1 – se você está usando uma distribuição baseada em head head, ou seja, o Fedora, que comentamos no início do curso, como você faria isso? Dentro do Fedora, do head head, nós não usamos o apt ou o apt-get, nós usamos a ferramenta yum. yum install e o nome do pacote.

[04:55] No head head, já fica a dica, não seria “apache2”, seria, por exemplo, yum install httpd, é a forma mais tradicional, isso vem do head head. httpd, o dimon do HTTP, que é, na verdade, o servidor do HTTP. Mas isso, também, em duas, três consultas no Google, você identifica de forma rápida qual é o nome do pacote.


6. Vamos dar um `apt show apache2`. Ele vai trazer o detalhamento, versão, quem é o mantenedor, quais são as dependências


7. `sudo apt autoremove apache2`: remove todos o apache2 e  pacotes dependentes do apache. No entanto, tenha cuidado ao usar esse comando, pois ele pode remover pacotes importantes que são necessários para o funcionamento adequado do sistema. Sempre verifique cuidadosamente a lista de pacotes que serão removidos antes de confirmar a ação.

8. `apt list --updradable`: lista de sofwares que precisam ser atualizadas

9. `suo apt list`: O comando "sudo apt list" lista todos os pacotes disponíveis para instalação no sistema operacional. Ele mostra uma lista de pacotes ordenada alfabeticamente com seus nomes, versões, descrições e informações sobre o repositório de onde eles são provenientes.

Você também pode especificar um nome de pacote para listar apenas as informações sobre esse pacote específico, como sua versão atual, dependências, repositório, entre outras informações. Por exemplo, "sudo apt list apache2" listaria informações apenas sobre o pacote Apache2.