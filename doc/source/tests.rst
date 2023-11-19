.. _linting:

======
Tests
======
------------------------------
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

----------------
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

--------------------
Tests de couverture
--------------------

Générer un rapport html des tests

.. code-block:: console

   coverage html --skip-covered
