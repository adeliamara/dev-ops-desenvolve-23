1. inforamçoes do sistema

ip addr

2. CONSEGUIR IP

hostname -I

3. ip route

4. dns

cat /etc/resolv.conf

5. cat /etc/hosts

trabalhe preferencialmente com dns em detrimento do hosts

# Informações de memoria 


1. sudo lshw | more

2. memoria do sistema

cd /proc

cat meminfo

3. outra alternativa:

cd /proc

free

o free acessa dados do memifo


# Informações de memoria

cd /proc

cat cpuinfo

1. vendo os processo

cat cpuinfo | grep processo

2. contanto linhas que contem apalvra processor 

cat cpuinfo | grep processor | wc

# Discos

1. cd /dev

2. ls -l | grep sda

conseguimos ver as particoes do primeiro disco

podem aparecer o hda, mas normalmente eh sda

4. df - h

mostra onde esta o /boot


# Infomações do sistema

cd /var

cd log









