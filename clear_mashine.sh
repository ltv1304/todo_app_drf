docker stop $(docker ps -a -q)
docker container prune 
docker network prune 
docker-compose up --build --remove-orphans
