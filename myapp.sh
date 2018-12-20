#!/bin/bash

ls -l 

NAME=$(docker ps -aqf "name=appy")

if [ -n "$NAME" ]; then

    docker stop appy && docker rm appy
fi

docker build --rm -t appy .

ID=$(docker images -q appy)

docker tag $ID localhost:5000/appy:3

docker run --name appy -d -p 3001:3000 localhost:5000/appy:3
docker login --username=masiddy --email=masiddymaanikyam@gmail.com -p 111d60014


docker tag $ID masiddy/appy:2
docker push masiddy/appy:2
