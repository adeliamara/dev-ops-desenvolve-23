# Filtrando conteudos

1. mostrando conteudo de um arquivo: cat nomedoarquivo

* tail mostra as ultimas linhas do arquivo
* head mostra as primeiras linhas do arquivos

2. Localizando um texto no conteudo do arquivo: grep palavrabuscada arquivo


3. buscar ignorando o o lower case e upper case: grep -i http services


4. buscar qual arquivo tem o ocntuedo: grep -l nomebuscao

5. buscar qual arquivo nao tem o ocntuedo: grep -L nomebuscao

6. buscar quais arquivos dentor de um diretorio tem o conteudo: grep -i -r nome buscado *

7. Observe queo seguinte comando mostra o nome do arquivo: grep -i -rl nome buscado *

# Como formatar o output?

1. coloca o output paginado: more nomedoarquivo

2. coloca o output paginado e permite navegar: less nomedoarquivo

