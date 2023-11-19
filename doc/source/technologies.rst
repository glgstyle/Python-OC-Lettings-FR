.. _technologies:

Technologies
=======================


  - Python v3.x+
  - Django
  - SQLite 
  - Circle CI
  - Docker
  - Sentry


-----------------------
Applications utilisées
-----------------------

- L'image de l'application est créée et stockée sur **Docker Hub**.
- Le reporting est centralisé sur **Sentry**. Toutes les erreurs
  (page web incorrecte, requête erronée sur la base de données ou base de 
  données indisponible) sont envoyées vers cette application.
- Pour déployer l'application, j'ai utilisé le service Paas de **Render**.
- Pour gérer des étapes entières du Piple CI/CD, j'ai utilisé 
  l'application **CircleCi**.

---------------------------------
Langage de programmation utilisé
---------------------------------

- Cette application est codée avec Python
- Pour le pipeline CI/CD, nous utilisons le langage **YAML**.
  Ce langage décrit le flux d'emploi. Le fichier se trouve dans le 
  dossier **.circleci**, nommé **config.yml**
- Pour la conteneurisation, chaque étape est décrite dans le fichier
  **Dockerfile** (situé dans le dossier racine de l'application)