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
