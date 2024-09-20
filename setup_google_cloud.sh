#!/bin/bash

#docker compose -f <docker-compose filename> logs --follow <service name>

sudo curl -sSL https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64 -o /var/lib/google/docker-compose
sudo chmod o+x /var/lib/google/docker-compose
mkdir -p ~/.docker/cli-plugins
ln -sf /var/lib/google/docker-compose   ~/.docker/cli-plugins/docker-compose

#docker compose -f docker-compose.unattended.yml up --build

#To delete all containers including its volumes use,

#docker rm -vf $(docker ps -aq)

#To delete all the images,

#docker rmi -f $(docker images -aq)

#Set timezone on Debian-based or RedHat-based distro
#timedatectl
#timedatectl list-timezones
#sudo timedatectl set-timezone America/New_York