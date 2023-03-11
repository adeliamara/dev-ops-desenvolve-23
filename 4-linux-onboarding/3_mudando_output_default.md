1. pega o conteudo de service que tem o termo ssh e redireciona para o arquivo listagem: grep ssh service > listagem.txt

se fizermos isso outra vez, o arquivo é sobrescrito

2. Para incluir um novo conteudo, decemos apendar: grep ssh service >> listagem.txt


3. redireciona o primeiro comando para o segundo: cat /etc/passwd | grep ricardo

# Ordenando


1. cat nomedoarquivo | sort

2. cat nomedoarquivo | sort > arquivoordenado.txt

