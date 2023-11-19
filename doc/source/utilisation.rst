.. _utilisation:

=============================
Utilisation du site en local
=============================

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

.. _usage:
======
Usage
======

La page principale du site contient 2 boutons : Profils et Locations.

Profils contient une liste de profils sur lesquels vous pouvez cliquer
pour accéder à leurs détails. Par exemple, vous pouvez voir l'emplacement
préféré du profil.

Lettings contient une liste de locations. Lorsque vous cliquez dessus,
vous pouvez voir les détails.

Depuis les locations et les profils, il y a 2 boutons pour revenir à la page 
d'accueil ou à la page précédente.

