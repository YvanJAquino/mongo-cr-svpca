#! /bin/bash

# https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/

sudo apt upgrade &&
sudo apt install -y gnupg &&
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add - &&
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list && 
sudo apt update; 
sudo apt install -y mongodb-org