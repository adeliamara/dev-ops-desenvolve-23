1. acesse

cd /var/log


2. para ver informaçoes/conjutno de logs:

dmesg

3. para ver os sda:

dmesg | grep sda


4. o kernnel vai registrando tudo que acontece. para verificar isso:

cat syslog

5. "CRON", ele é uma parte do sistema responsável por agendar as tarefas. então, para ver o cron:

cat syslog | grep -i cron


6. inforamções sobre autenticação:
cat auth.log

7. parar ver os acessos remotos que fizemos:  cat auth.log | grep -i ssh


8. para ver as novas entradas em tempo real

tail -f auth.log

9. por que ha tantos syslogs?

há rotação de logs, por exemplo, as frequencias. para ver qual é essa rotação:

cat /etc/logrotate.conf