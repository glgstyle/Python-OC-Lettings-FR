.. _installation:

Installation du projet 
=======================



Pré-requis 
-----------

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).


Installation
-------------

Pour installer Orange County Lettings, veuillez suivre les instructions suivantes:

1. Créer un répertoire pour le projet et se placer à l'intérieur

.. code-block:: console

   mkdir in
   cd /path/to/put/project/in

2. Cloner le repository

.. code-block:: console

   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

3. Créer l'environnement virtuel

.. code-block:: console

   cd /path/to/Python-OC-Lettings-FR
   python -m venv venv

Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu

.. code-block:: console

   apt-get install python3-venv

4. Activer l'environnement, puis vérifier que python exécute l'interpréteur Python dans l'environnement virtuel

.. code-block:: console

   source venv/bin/activate
   which python

5. Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure

.. code-block:: console

   python --version

6. Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel

.. code-block:: console

   which pip

Pour désactiver l'environnement

.. code-block:: console

   deactivate

7. Créer un fichier .env à la racine du projet

.. code-block:: console
   mkdir .env

8. Copier le contenu du fichier.env_sample et le coller dans le fichier .env 

.. code-block:: console


.. _utilisation_du_site:

Utilisation du site en local
-----------------------------

1. Aller dans le répertoire contenant le projet

.. code-block:: console

   cd /path/to/Python-OC-Lettings-FR

2. Activer l'environnement

.. code-block:: console

   source venv/bin/activate

3. Installer les packages

.. code-block:: console

   pip install --requirement requirements.txt`

4. Démarrer le serveur

.. code-block:: console

   python manage.py runserver

5. Aller à l'adresse suivante dans un navigateur

.. code-block:: console
   
   http://localhost:8000

6. Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations)


.. _linting:

Recherche d'erreurs (linting)
------------------------------

1. Aller dans le répertoire contenant le projet

.. code-block:: console

   cd /path/to/Python-OC-Lettings-FR

2. Activer l'environnement

.. code-block:: console

   source venv/bin/activate

3. Chercher les erreurs et violations des conventions et normes PEP8

.. code-block:: console

   flake8

4. Générer un rapport html pour plus de lisibilité sur les erreurs

.. code-block:: console

   flake8 --format=html --htmldir=flake-report

5. Ouvrir dans un navigateur l'index.html qui se trouve dans le dossier flake-report 


.. _unit_tests:

Tests unitaires
----------------

1. Aller dans le répertoire contenant le projet

.. code-block:: console

   cd /path/to/Python-OC-Lettings-FR

2. Activer l'environnement

.. code-block:: console

   source venv/bin/activate

3. Lancer les tests

.. code-block:: console
   
   pytest


.. _coverage_tests:

Tests de couverture
--------------------

Générer un rapport html des tests

.. code-block:: console

   coverage html --skip-covered


.. _database:

Base de données
----------------

1. Aller dans le répertoire contenant le projet

.. code-block:: console

   cd /path/to/Python-OC-Lettings-FR

2. Activer l'environnement

.. code-block:: console

   source venv/bin/activate

3. Ouvrir une session shell 

.. code-block:: console

   sqlite3

4. Se connecter à la base de données

.. code-block:: console

   .open oc-lettings-site.sqlite3

5. Afficher les tables dans la base de données

.. code-block:: console
   
   .tables

6. Afficher les colonnes dans le tableau des profils

.. code-block:: console
   pragma table_info(Python-OC-Lettings-FR_profile);

7. Lancer une requête sur la table des profils

.. code-block:: console

   select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';

8. Quitter

.. code-block:: console

   .quit


.. _admin_panel:

Panel d'administration
-----------------------

1. Ouvrir le navigateur et aller à l'adresse suivante

.. code-block:: console

   http://localhost:8000/admin

2. Connectez-vous avec l'utilisateur ``admin``, et le mot de passe ``Abc1234!``


.. _windows:

Windows
-----------------------

Utilisation de PowerShell, comme ci-dessus sauf :

1. Pour activer l'environnement virtuel

.. code-block:: console

   .\venv\Scripts\Activate.ps1

2. Remplacer ``which <my-command>`` par ``(Get-Command <my-command>).Path``
