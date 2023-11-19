## Site web d'Orange County Lettings

# <h1 align="center">Orange County Lettings</h1>
</br>
<p align="center">
    <img src="https://user.oc-static.com/upload/2023/07/20/1689880374259_Orange%20County%20Lettings%20Ad.png" 
            alt="le logo d'Orange County Lettings" 
            width="250" 
            height="auto"/>
</p>


## Développement local


### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).


### macOS / Linux


#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`


#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`
- Créer un fichier .env à la racine du projet
- Copier le contenu du fichier.env_sample et le coller dans le fichier .env  


#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).


#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`
- for flake8 html report `flake8 --format=html --htmldir=flake-report`


#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`


#### Tests de couverture

Pour générer un rapport html des tests :

- ```coverage html --skip-covered```


#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter


#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`


### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

Les données concernant les variables d'environnement se situent dans le 
fichier.env préalablement crée lors de la création de l'environnement virtuel.

le fichier .env doit contenir au minimum le contenu similaire aux lignes
suivantes en mode local par exemple:
SECRET_KEY='fp$9^59[3]sriajg$_%]=5trot9g!1qa@ew(o-1#@=&4%=hp4


### Pré-requis :

- compte/acces Github
- compte/acces CircleCi
- Compte/acces DockerHub
- Compte/Acces Render
- Compte/Acces Sentry


### Description du fonctionnement du Pipeline CircleCi:

  <u>Modification sur n'importe qu'elle branche :</u> 

   - 2 premiers jobs s'exécutent, le pytest et flake8

  <u>Modification sur la branche master :</u>

  une série d'étapes appelée workflows démarre:

  - 'run_tests_and_build_docker' du Pipeline (du dépôt) Python-OC-Lettings-FR.

  Elle est décomposé en différents 'jobs':

  - lance les tests avec pytest
  - contrôle le linting PEP8 avec Flake8
  - build-push-docker :
      se met à jour (le build) seulement si on modifie la branche master à la condition que les tests soient valides, va créer une image docker et l'uploader sur le docker hub.
  - deploy-from-dockerhub-to-render :
      va lancer le build de l'application sur render via gitHub à la condition que le build-push-docker soit ok


#### CircleCi :
Paramétrage nécessaire :

Création des variables d'environnement au niveau du projet :

Dans Projets:
Cliquez sur Project Settings (Les 3 petits points)
Cliquez sur Environment Variables
Cliquez sur Add Environment Variables

Nom des Variables |	Description |	Valeurs à renseigner
| :--------------- |:---------------| :-----|
DEBUG | Debug Mode | False
DOCKER_HUB_USER_ID | User Docker Hub | glgstyle
DOCKER_HUB_PASSWORD |	Dockerhub password | 1321654654654651231654
DEPLOY_HOOK |	 Render Token | 1321654654654651231654
DOCKER_IMAGE_NAME | Name of Docker Image | glgstyle/lettings-image
DOCKER_IMAGE_VERSION | Version of Docker Image | 1.0.0
SECRET_KEY | DJANGO SECRET_KEY | fp$9^593hs98ajg$_%=5trot9g!1qa@ew(o-1#@=&4%


#### Github :

Github Repository permet de faire le versionning de notre projet/application.


#### Docker Hub :

Docker-Hub glgstyle Repository permet de stocker en ligne l'image docker de
 notre application.

La commande unique pour récupération de l'application en local et son
 démarrage immédiat est :

  `docker pull glgstyle/lettings-image`

glgstyle est le compte du Hub Docker, lettings-image est le nom de l'image


#### Render :

Render permet d'heberger notre application. 
Info pour que l'application fonctionne, il faut définir plusieurs variables.
C'est le workflows CircleCI qui s'en charge. Les variables sont :

Nom des Variables |	Description |	Valeurs à renseigner
| :--------------- |:---------------| :-----|
DEBUG | Debug Mode | False
PORT | Port Number | 8000
SECRET_KEY | DJANGO SECRET_KEY | fp$9^593hs98ajg$_%=5trot9g!1qa@ew(o-1#@=&4%
SECRET_KEY_SENTRY | Sentry secret key | $_%=5trot9g!1qa@ew(o-1#@


#### Sentry :

Sentry permet de faire le monitoring de l'application.

Elle permet également de détecter des éventuels bug/issues.

Mais il faut pour cela intégrer le sentry-sdk et la variable dans settings.py.


### Technologies

  - Python v3.x+
  - Django
  - SQLite 
  - Circle CI
  - Docker
  - Sentry

### Read The Docs

Pour ajouter du contenu à la documentation, après avoir créé les fichiers rst, 
générer les fichiers html avec la commande suivante :

  `doc\make.bat html`


### Contribuer au project

Oc Lettings n'est pas un projet open source. Veuillez nous contacter pour contribuer avec vos propres fonctionnalités.


### Auteur

    Gwénaëlle
