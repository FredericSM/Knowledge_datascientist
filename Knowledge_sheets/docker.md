docker
docker commands [...options]
docker commande sous-command [...options]
Usage:	docker container ls [OPTIONS]

List containers

Aliases:
  ls, ps, list

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all
                        states) (default -1)
  -l, --latest          Show the latest created container (includes all
                        states)
      --no-trunc        Don't truncate output
  -q, --quiet           Only display numeric IDs
  -s, --size            Display total file sizes

  docker container ls / docker ps

  docker container ls -a / docker ps -a
  docker images (ls)

  docker container rm NOM_OU_ID

  docker container rm -f redis1 redis2 redis3
  docker container prune
  docker image rm NOM_OU_ID
  docker run --name redis -d redis
  docker system prune
  docker run -it alpine

  docker container attach 0db4
  docker container -ai 0db4
  docker container stop stupefied_blackwell
  docker container kill 7d99

  docker container rename CONTENEUR NOUVEAU_NOM
  docker container pause test
  docker container exec test mkdir /app

  docker container cp ./fromhost.txt test:/app (dossier d'origine dossier de destination)

  docker container top test
  docker container diff test (A: nouveau, C:modifié)

  docker system prune

  ARG env(=default_value)
  docker build --build-arg env=prod
  ENV CLE1="Une valeur1"
  ENV CLE2="Une valeur2"
  LABEL version="2.3.1"
  LABEL auteur="jean@gmail.com"
  docker image inspect

  docker container commit --help (créé une image depuis un container, peu utilisé)
  docker image history container_name
  docker image tag container_name:tag_name container_name:new_tag

  docker container (-f) logs container_id/name

  repertoire: contient toutes les versions d'une image

  docker image pull/push <username>/<repertoire>:[tag]

  docker login
  docker build -t name/folder destination_folder

  docker logout
  sudo apt install pass
  gpg2 --gen-key
  wget https://github.com/docker/docker-credential-helpers/releases/download/v0.6.3/docker-credential-pass-v0.6.3-amd64.tar.gz && tar -xf docker-credential-pass-v0.6.3-amd64.tar.gz && chmod +x docker-credential-pass && sudo mv docker-credential-pass /usr/local/bin/
  pass init "VOTRE NOM
  nano ~/.docker/config.json
  {
    "credsStore": "pass"
  }
  docker login

  docker image save -o mesimages.tar image1 image2
  docker image load < mesimages.tar

  docker container export -o moncontainer.tar container_id
  docker image import moncontainer.tar image_name
  --> perd les layers de l'image

  Mise en place du Dockerfile
  Dans le Dockerfile nous mettons pour le moment :
  
  FROM node:alpine
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD [ "node", "/app/app.js" ]
  EXPOSE 80

  docker run -it -p 80:80 test

  ctrl + R: match avec ce qui a déjà été fait
  pour optimiser le rebuilt, ne pas hésiter à copier les dépendances avant le reste quite à faire deux fois copy
  .dockerignore

  hello.txt
  */hello.txt
  **/hello.txt
  hel*
  *.csv

  docker run -d -p 80:70 myapp
  docker exec -it conainer_id sh
  docker attach container_id

  docker container stats container_id

  probleme de persistence: volumes, bind mounts & tmpfs
  <img width="501" height="255" alt="image" src="https://github.com/user-attachments/assets/aa872732-b12d-4c14-9eca-e5ecf9397ece" />

  docker container run -it --name alpine1 --mount type=bind,source="$(pwd)",target=/data alpine sh
  --> très utile pour le mode développement
  adaptation car ca ecrase les fichiers:
  Pour commencer créons un dossier src et déplaçons y le fichier app.js.
  FROM node:alpine
  WORKDIR /app
  COPY ./package.json .
  RUN npm install
  COPY . .
  CMD ["node", "--watch", "src/app.js"]
  docker run -p 80:80 --mount type=bind,source="$(pwd)/src",target=/app/src myapp
  comprendre pourquoi ca supprime les fichiers et pourquoi src permet d'éviter le problème

  docker volume create
  docker volume inspect ID_NOM

  docker container run -d --name mongodb mongo
  docker container logs mongodb
  docker container exec -it mongodb mongosh
  docker container run -d --name mongodb --mount source=mydb,target=/data/db mongo
  MongoDB compass
  docker container run -d --name mongodb --mount source=mydb,target=/data/db -p 27017:27017 mongo

  docker run --name tmp --mount type=tmpfs,target=/data -it alpine sh

  driver bridge/ host / overlay
  docker network inspect
  ping 172.17.0.3
  docker container run  --name alpine2 --link alpine1 -it alpine sh
  ping alpine2

  docker network create mynet
  docker container run --network mynet --name alpine1 -d alpine ping google.fr
  docker network inspect bridge
  docker exec -it alpine1 ping alpine2
  reseau bridge par default ne doit pas etre utilisé mais un nouveau doit etre créé pour une meilleur isolation et une réoslution dns automatique entre les conteneurs


  docker compose
  difference avec CLI et docker daemon, docker engine, docker desktop
  docker compose version

  docker compose up
  docker compose run myalpine
  docker compose down
  docker compose down -v
  docker compose run SERVICE (pas de problème de port ?)

  services:
myalpine:
  image: alpine
  command: ls / entrypoint: ls
  docker compose ps

  services:
  a:
    image: alpine
    command: ['ls']
  b:
    build:
      context: ./backend
      dockerfile: Dockerfile
      args:
        - FOLDER=test
      labels:
        - email=jean@gmail.com


ports:
  - "80:80"
  - "8080:3000/udp"
services:
a:
  image: alpine
  command: ['ls']
b:
  build:
    context: ./backend
    dockerfile: Dockerfile
    args:
      - FOLDER=test
    labels:
      - email=jean@gmail.com
  volumes:
    - type: bind
      source: ./data
      target: /app/data
volumes anonymes
services:
a:
  image: alpine
  command: ['ls']
b:
  build:
    context: ./backend
    dockerfile: Dockerfile
    args:
      - FOLDER=test
    labels:
      - email=jean@gmail.com
  volumes:
    - type: bind
      source: ./data
      target: /app/data
    - type: volume
      target: /app/data2
volumes déjà nommés:
volumes:
  data3:
volumes nommées déjà créés: 
volumes:
  data3:
    external: true

variables d'environnement
backend:
  image: "node-app:${NODE_APP_VERSION}"

backend:
  environment:
    - NODE_APP_VERSION=2.2.3

Utiliser un fichier externe avec env_file et .env
NODE_APP_VERSION=2.2.3
NODE_ENV=dev
DEBUG=1

backend:
  env_file:
    - config/env.dev

COMPOSE_PROJECT_NAME=monprojet

Définir la valeur des variables d'environnement avec Docker CLI
docker compose run -e USER=paul up
docker compose run -e USER up

L'ordre de priorité
1 - Le fichier docker-compose.yml.

2 - Les variables d'environnement de votre shell.

3 - Le fichier des variables d'environnement défini, par exemple .env.dev.

4 - Le fichier Dockerfile (si vous avez défini des valeurs dans des instructions ENV).

S'il ne trouve pas la valeur de la variable à tous ces endroits, et dans cet ordre, la variable sera non définie.

Création d'un réseau par défaut
services:
  api:
    image: node
  db:
    image: mongo:7

Utiliser des alias avec --link
services:
  api:
    image: node
  db:
    image: mongo:7
    links:
      - 'db:database'
      - 'db:mongo'
      
Créer d'autres réseaux
services:
  proxy:
    image: nginx
    networks:
      - frontend
  app:
    image: nginx
    networks:
      - frontend
      - backend
  api:
    image: node
    networks:
      - backend
  db:
    image: mongo:7
    networks:
      - backend
networks:
  frontend:
  backend:

Changer le nom du réseau par défaut
services:
  api:
    image: node
  db:
    image: mongo:7
networks:
  default:
    name: monreseau

services:
  proxy:
    image: nginx
    networks:
      - frontend
  app:
    image: nginx
    networks:
      - frontend
      - backend
  api:
    image: node
    networks:
      - backend
  db:
    image: mongo:7
    networks:
      - backend
networks:
  frontend:
    name: frontend
  backend:
    name: backend
