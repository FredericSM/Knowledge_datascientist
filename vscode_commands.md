ctrl + shift + P --> interpreteur
alt + shift + clic --> multicurseur

black --> permet de formater le code selon le PEP 8
pip install black
black python_file.py

pylint --> permet de detecter les erreurs de format
# pylint: disable=missing-module-docstring
--> permet d'éviter l'erreur s'il considère que c'est un package alors que ce n'est pas le cas
isort --> permet de formater automatiquement certaines erreur de pylint