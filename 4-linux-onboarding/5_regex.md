1. Primeiro, devemos instalar os pacotes necessários para treinar: sudo apt install wamerican

2. busque onde foi instalado:

find /usr -name *american*

3. copie o arquivo acima para uma pasta labs

4. Buscando todas as palavras que começam com computer: cat american-english | grep -E "^computer"

isso resulta diferente se usarmos: cat american-english | grep computer

5. palavras terminadas em computer:cat american-english | grep -E "computer$"

6. apenas computer: cat american-english | grep -E "^computer$"

* atalho: egrep "^computer&" american-english

7. buscar com primeira letra variando:

egrep "^.oop" american-english

8. primeira letra variando entre um conjunto:

egrep "^[abc]oop" american-english


