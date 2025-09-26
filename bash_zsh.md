whoami --> who is the user
pwd --> provide the path where I am // print working directory


ls --> list the files in the current directoy
ls -a --> list les fichiés cachés

cd --> change directory
 . --> repertoire courant
 .. --> parent directory
 cd Ø --> bring back in my personnal directory/home
 cd - --> bring back in the directory just before the command
 cd / --> provide an absolut path
 echo "hello word" --> print hello word
 echo $HOME --> print the variable HOME --> useful to know a directory

 sudo useradd "user" --> add a new user

 command --help --> get the different options of the command

 clear --> remove all previous commands


 vim
 1. i  : Mode insertion avant le curseur
2. I  : Mode insertion au début de la ligne
3. a  : Mode insertion après le curseur
4. A  : Mode insertion à la fin de la ligne
5. o  : Nouvelle ligne en dessous
6. O  : Nouvelle ligne au-dessus
7. Esc : Quitter le mode insertion
8. :w  : Sauvegarder
9. :q  : Quitter
10. :wq : Sauvegarder et quitter
10. :x : Sauvegarder et quitter
11. :q! : Quitter sans sauvegarder
12. dd  : Supprimer la ligne
13. yy  : Copier la ligne
14. p   : Coller après le curseur
15. u   : Annuler
16. Ctrl + r : Refaire
17. /   : Rechercher
18. n   : Prochaine occurrence
19. x   : Supprimer le caractère
20. :   : Mode commande

touch: creer un ou plusieurs fichiers si inexistant, change le timestamp
echo text > fichier: permet d'ecraser ce qu'il y a dans fichier et le remplacer par text
echo text >> fichier: permet d'ajouter text a fichier
cat fichier: permet de lire ce qu'il y a dans fichier
rm: remove
rm day{1,7}: supprimer les fichiers day1, day2, ..., day7
rm -i: permet d'avoir une confirmation si peur de supprimer un fichier
trash-cli: bibilothèque qui permet d'avoir un backup comme avec la corbeille (trash)
dans ~/.local/share/Trash

mkdir : make directory
--> mkdir Day{1..365}
--> mkdir -p folder/subforlder pour créer les deux dossiers d'un coup (-p nécessaire)
--> mkdir /folder : créer un dossier dans le repertoire racine

rmdir: remove empty directory
rm -r directory :supprimer directory et tout ce qu'il y a a l'interieur
rm -ri directory :supprimer directory et tout ce qu'il y a a l'interieur en demandant a chaque fois si on est d'accord

cp file path: copie file dans path
cp -r directory path: copie récursive du dossier complet dans path
mv file path: couper file dans path

commande1 && commande2 : permet de faire deux commandes d'un coup

ls -l: permet d'afficher avec:
lrwxrwxrwx   1 root root          7 avril 22  2024 bin -> usr/bin

-droits (directory, link, folder / groupe de trois lettres read, write & execute) pour utilisateur / groupe d'utilisateur / other)
-nombre d'item contenu a l'interieur
-utilisateur qui a les droit
-groupe d'utilisateur auquel appartient l'utilisateur
-taille (si flag = -lh)
-date du dernier changement
-dossier/fichier
--> ls -lt : affiche dans l'ordre le plus récent

who am i ?$(whoami) : permet d'executer une commande bash (tel que f"who am I ?:{me})

which bash : permet de savoir le path de bash
dans un script
#! /bin/bash : permet d'indiquer quel shell utiliser et ou le trouver
exemple de script:
#! /bin/bash

echo "Hello World"
echo "You are: $(whoami)"
now=$(date)
echo "Current time : $now"
echo "--------"

chmod +x file: ajoute x pour user, group & other
chmod -x file: supprime x pour user, group & other
chmod u+x: ajoute x uniquement pour user

./: dossier courant (./file correspond a faire bash file mais ne fonctionne pas pour python sans la commande python3 file.py)
../: dossier parent

ls /usr/bin/* : * permet de lister tout ce qui commence avant *

conda (de)activate : active conda 

obtenir la variable d'environnement:
echo "from os import environ" > envvar.py
echo "print(environ['HOME'])" >> envvar.py
python3 envvar.py
ou
export ENV="dev" : pour creer une variable d'environement 
--> très utile pour savoir si on est en preprod, prod, ...

pour connaitre les variables d'environement:
echo $PATH | tr ":" "\n"
export PATH="new_path":$PATH": permet d'ajouter un path dans PATH mais pas persistant d'une session a une autre
printenv: equivalent a echo $ (plus rapide)

bashrc: permet la customisation du terminal et est lancé à chaque nouvelle session
--> config admin: un sys-admin peut desactiver certains features du shell
--> accessibilite: customization du PATH et des varaibels d'environnement
--> efficience: création de fonctions et d'alias
--> customisation: modification du prompt, des couleurs, des sorties de commandes

exemple de fonction:
cdl () {
	cd $1 && ls -lh
}

mcd () {
	mdir $1 && cd $1
}

alias hist='history | grep' : history --> permet d'avoir l'historique de toutes les commandes tapées dans le terminal

alias gco ="git commit"
--> alias permet de faire un raccourci

ctr + z : interromp un process
--> fg permet de le continuer

htop : permet de lister les différents process
--> fleche pour naviguer
--> k pour selectionner le process
--> entrée pour selection l'action sur le process

pour mac os, Homebrew remplace apt-get

stdin: standard input stream (interface pour écrire des commandes)
stdout: standard output (stream par lequel les outputs des commandes arrivent sur le shell)
stderr: standard error (stream par lequel els erreurs des commandes arrivent sur le shell)

python3 2> log_file: permet de capturer l'error dans le fichier log (2>)

ping website: permet d'avoir le temps de connection au website (et donc savoir si on est connecté à internet)

zip zipladedans.zip testzipfolder/ : permet de zipper un fichier (attention il faut d'abord mentionner le fichier de destination)


man command: permet d'avoir le manuel
--> tldr: permet d'avoir les commandes les plus utiles
---> pour l'installer
sudo npm install -g tldr
reset (pour relancer)

apt search paint: permet de chercher s'il y a un pacjage proche de paint

sudo shotdown now