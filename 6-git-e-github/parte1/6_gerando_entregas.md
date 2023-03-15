Temos um projeto finalizado, com todas as alterações necessárias no conteúdo entre tags <titulo>, todos os nomes da listagem de cursos estão corretos, já vimos como trabalhar em equipe, com repositórios remotos, branches independentes, corrigindo conflitos, alocando dados, atualizando branches, enfim, vimos bastante conteúdo.

Entretanto, no momento de finalizarmos, queremos verificar o que houve em cada commit, para garantir que nenhum bug foi adicionado no projeto, e entender o que de fato cada commit gerou no código. Como conferiremos as diferenças entre commits?

Logados como Vinicius, já entendemos que, se utilizarmos git log -p, conseguiremos ver o que foi alterado em código commit a commit. Existe um comando do Git, bem interessante e poderoso, que é o git diff, capaz de exibir estas diferenças. Ao tentarmos executá-lo, porém, nada é exibido.

Isso porque por enquanto não há nada alterado no nosso código, que não tenha sido salvo. Então, para entendermos as diferenças entre dois commits, precisaremos informar quais são, no caso, ea539b3 até (..) 6ca12ac. Por meio deste comando, visualizamos todas as alterações feitas, marcadas em cores diferentes.

Além disso, caso estejamos modificando algo, como acresentando um novo curso na listagem, no código, e queiramos verificar o que foi alterado, poderemos simplesmente usar o git diff, que nos mostra o que foi alterado e que ainda não foi adicionado para commit. Mas a partir do momento em que adicionamos o arquivo, este comando não nos mostra mais o que existe de diferente.

Traremos o arquivo de volta após git status com git reset HEAD index.html, e com git status conferiremos que ele está pronto para ser adicionado ao commit. Vamos desfazer as alterações com git checkout -- index.html. Desta forma, conseguimos começar a analisar com maior controle todas as alterações que foram adicionadas durante o desenvolvimento de um projeto.

Após termos visto as alterações e garantido que realmente não há bugs, de que forma poderemos gerar uma versão, por exemplo, 0.1? Como será possível definirmos isto com o Git? Vamos conversar sobre isso adiante.

# Tags e releases

Tendo finalizado o projeto de fato, queremos gerar uma versão, indicando ao Git que a partir do penúltimo commit — que acessaremos com git log -n 2 — seja cravada uma marcação, um checkpoint indicando que trata-se da versão 0.1, por exemplo. Em vários outros sistemas de controle de conteúdo, existe o conceito de tag, como quando você cria blogs e possui tags para marcar postagens que pertencem a categorias específicas.

No Git, é possível utilizar um conceito bastante similar, também denominado tag, capaz de marcar um ponto na aplicação que não pode ser modificado, fixo. Assim, após ser lançada, a versão 0.1 nunca deixará de ser a versão 0.1, e quaisquer alterações que forem feitas nela, serão incluídas na versão posterior.

Isso não quer dizer que faremos um código que não será mais editável, apenas que criaremos um marco para onde poderemos ir, e que terá um código correspondente àquele estado. E para criarmos uma tag, informaremos isto ao Git, com git tag -a, seguido do nome que damos a ela, v0.1.0, que poderia ser qualquer outro. Além disto, poderemos incluir uma mensagem. O comando completo ficaria, então: git tag -a v0.1.0 -m "Lançando a primeira versão (BETA) da aplicação de cursos".

Ao darmos "Enter", geramos uma tag, um marco na nossa aplicação. E se executarmos git tag, são exibidos todos estes marcos disponíveis, que no caso por enquanto se resume a apenas um. Já sabemos que é possível fazer push de master, ou de qualquer outra branch, como com git push local master e depois git push local v0.1.0 para enviarmos a tag ao servidor.

Para nos lembrarmos de um detalhe, vamos executar git remote -v. Estamos utilizando o GitHub, e temos um repositório local denominado origin, que faz menção a ele. Então, atualizaremos nosso código no GitHub com git push origin master. Também enviaremos a tag, com git push origin v0.1.0. Mas como será que visualizamos tags por meio do GitHub?

Atualizaremos a página do navegador, que nos informa que temos 17 commits, 1 branch (já que não enviamos as demais para lá), e 1 release, que é a versão pronta para ser lançada ou baixada por qualquer pessoa que queira utilizar em seu sistema. Poderemos ver a nossa mensagem, em qual commit a tag foi gerada, e baixar clicando no ícone com "zip".

A release poderá inclusive ser compartilhada com outras pessoas, por meio da URL correspondente, possibilitando o acompanhamento das releases do projeto. Esta é uma feature bem interessante do GitHub!

