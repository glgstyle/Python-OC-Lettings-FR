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


.. _windows:

Windows
-----------------------

Utilisation de PowerShell, comme ci-dessus sauf :

1. Pour activer l'environnement virtuel

.. code-block:: console

   .\venv\Scripts\Activate.ps1

2. Remplacer ``which <my-command>`` par ``(Get-Command <my-command>).Path``
