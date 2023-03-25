Vamos voltar a fazer o teste do ping para o domínio do curso de redes da Alura.

`ping www.cursoderedesdaalura.com`

Nesta tradução entrará o nome www.cursoderedesdaalura.com para o endereço IP, em algum momento podemos ter problemas em cada um deles no processo de tradução. Para identificarmos em qual parte está o problema, usaremos uma ferramenta administrativa chamada nslookup e o nome do endereçamento IP que queremos descobrir. Veremos o exemplo, um teste com o site do Facebook.

`nslookup www.facebook.com`

No retorno veremos que os dois tipos de máquinas com identificação:


Vemos o primeiro com um formato maior e o segundo com um formato em que estamos mais acostumados.

Ele também nos diz que o endereçamento da máquina IP não é uma resposta autoritativa. Isto acontece porque na minha rede local, já acessamos previamente o site do Facebook e ficou armazenado no cache qual é o respectivo endereçamento da plataforma. O processo ficaria muito lento se tivéssemos que fazer a verificação na internet toda vez, por isso, a minha máquina local guarda na memória qual é o respectivo endereçamento do IP do Facebook. A resposta não é autoritativa porque ela não veio de quem realmente tem a propriedade de passar o registro. A resposta veio internamente da minha rede.

Teoricamente, nós poderíamos colocar no teste do ping qualquer nome. O que acontecerá, por exemplo se digitarmos no Terminal nslookup x?

`nslookup x`

Ele respondeu que não existe esse domínio, ou seja, não existe o registro nem na minha rede e nem na internet sobre um possível domínio que receba o nome x. O mesmo ocorrerá se fizermos um teste de conectividade com o ping.

`ping 1.1.1.1`

Veja que foi esgotado o tempo limite do pedido. Nós fizemos uma chamada para o endereçamento 1.1.1.1, mas não recebemos uma resposta.

