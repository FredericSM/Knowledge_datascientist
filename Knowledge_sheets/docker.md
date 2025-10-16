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
  <img width="501" height="255" alt="image1" src="https://github.com/user-attachments/assets/e1229c29-1342-4bbc-ab45-bace5cde464d" />
  <img width="501" height="255" alt="image" src="https://github.com/user-attachments/assets/aa872732-b12d-4c14-9eca-e5ecf9397ece" />

