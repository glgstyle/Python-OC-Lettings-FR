.. _database:

Accès à la base de données
---------------------------

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

================================
Structure de la base de données
================================

-----------
les tables
-----------
- location : nom des biens
- adresse : contient les adresses postales des propriétés
- profile : contient la préférence de pays de l'utilisateur

~~~~~~~~~~~~~~
1. Locations :
~~~~~~~~~~~~~~

- id : numéro incrémental automatisé, clé primaire
- titre : le nom du bien à louer, max caractères 255
- adresse : clé étrangère vers les adresses

~~~~~~~~~~~~~
2. Adresses :
~~~~~~~~~~~~~

- id : numéro incrémental automatisé, clé primaire
- numéro : numéro de rue, valeur max 9999
- rue : nom de la rue, 64 caractères max
- ville : Nom de la ville, 64 caractères max
- state : Code de l'état, 2 caractères max
- zip_code : valeur maximale 99999
- country_iso_code : Code ISO du pays, 3 caractères max

~~~~~~~~~~~~~
3. Profils :
~~~~~~~~~~~~~

- id : numéro incrémental automatisé, clé primaire
- user : clé étrangère vers la table de l'utilisateur
- favorite_city : la ville préférée de l'utilisateur, 64 caractères max