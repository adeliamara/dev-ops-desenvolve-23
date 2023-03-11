# Como buscar arquivos?

1. Se não souber onde o arquivo esta localizado, posso usar o find. para isso, faço:
find (nomedodiretorioraiz) -name termobuscao

exemplo:
~~~
find / -name *.conf 
~~~

<strong>Muito diretorios exigem permissao de super usuario, isto é, boot</strong>

assim, devemos sar:

~~~
sudo find / -name *.conf 
~~~

3. para ver isso de forma paginada, faça: sudo find / -name *.conf | more


4. escolhendo a pronfudade da busca: sudo find / -maxdepth 2 -name *.conf


5. Como saber quais ultimos arquivos acessados?

~~~
find . -amin -5
~~~

O comando acima busca arquivos a partir do diretorio atual que foram modificados nos ultimos 5 min

-atime é poder dia. -amin é por dia

6. Localizando arquivos por tamanho:

~~~
sudo find / -size +160M
~~~

com o +, sao exatps 160M; sem o +, são exetatos 160

~~~
sudo find / -size 160M
~~~

