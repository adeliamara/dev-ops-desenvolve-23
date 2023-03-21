1. `sudo lshw -c disk`: verificar os discos existentes na maquina e se o discto instalado está sendo instalando


2. `sudo fdisk -l`: para ver as partições


3. `sudo fdisk /dev/sdb`: apontando a ferramenta fdisck para o dispositvo
command: p


# Instalando filesystem

É como formatar o disco.


1. `sudo fdisk -l`

2. `sudo mkfs -t ext4 /dev/sdb1`: a ferramenta mkfs aponta para o tipo de filesystem e para a partição


4. mount: mostra os dispositovs motnados

5. vamos agora montar o disco.precisamos escolher o ponto de montagem (diretorio). Monte preferencialmente no `/media/`:
sudo mkdir disk2

sudo mount /dev/sdb1 /media/disk2

5. se reiniciarmos a mquina, o disco nao sera montado. precisamos fzazer isso automaticamente sempre que ligarmos: 

6. `sudo vi /etc/fstab`

mas antes pegue o uuid do dis


co: `sudo blkid`

7. agora faço o passo 6

coloque a linha UUID="4aaaf0a7-d33c-402f-854d-05dabb3168f4 /media/disk2 ext4 defaults 0 2 nesse padeõa

8. sudo mount -a: é o que o sistema faz por baixo dos panos quando reinicia

9. podemos usar o systemd e systemcl para gerenciar



