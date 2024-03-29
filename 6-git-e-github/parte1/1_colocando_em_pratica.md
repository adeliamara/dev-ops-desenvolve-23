Chegou a hora de você pôr em prática o que foi visto na aula. Para isso, execute os passos listados abaixo.

1) No terminal (ou Git Bash, no Windows) navegue até a pasta recém criada (utilize o comando cd para navegar entre pastas);

2) Execute o comando `git add index.html` para marcar o arquivo para ser salvo (commitado);

3) Execute `git status` e confira que o arquivo agora mudou de estado e está pronto para ser salvo (commitado);

4) Após adicionar, execute o comando `git commit -m "Criando arquivo index.html com lista de cursos"`. Sinta-se à vontade para alterar a mensagem de commit, se desejar;

5) Altere o arquivo index.html. Adicione o acento em "Integração Continua", por exemplo;

6) Adicione o arquivo para ser salvo, com `git add .`;

7) Execute o comando `git commit -m "Acento adicionado no curso de Integração Contínua"`. Sinta-se à vontade para alterar a mensagem de commit, se desejar;

8) Execute o comando `git log` e analise a sua saída. Execute também `git log --oneline`, `git log -p` e outras alternativas que quiser testar;

9) Crie um arquivo vazio com o nome que quiser, por exemplo, `ide-config`;

10) Crie o arquivo `.gitignore` e adicione uma linha com o nome do arquivo recém-criado (ide-config, no exemplo acima);

11) Execute git status e verifique que o arquivo ide-config não está na lista para ser adicionado;

12) Adicione (com `git add .gitignore`) e realize o commit (com `git commit -m "Adicionando .gitignore`") o arquivo .gitignore.