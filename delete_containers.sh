#!/bin/bash
sudo docker compose stop
sudo docker compose rm
sudo docker volume ls
var=$(sudo docker volume ls| awk '{if(NR == 2){print $2}}')
sudo docker volume rm $var
sudo rm -r data
