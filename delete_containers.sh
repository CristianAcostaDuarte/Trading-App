#!/bin/bash
sudo docker compose stop
sudo docker compose rm
sudo docker volume ls
var=$(sudo docker volume ls| awk '{if(NR == 2){print $2}}')
sudo docker volume rm $var
sudo rm -r data

#En caso de que Nginx moleste o diga que el puerto 80 este ocupado usar el comando
sudo lsof -nP | grep LISTEN

# En cAaso de que sea Nginx el servicio que este molestando entonces usamos
sudo systemctl stop nginx 
