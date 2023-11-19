======================
Circle CI/CD Pipeline
======================

Lorsqu'une modification est effectuée sur le dépôt Github (après un commit),
 CircleCi lance quelques commandes :

1. **Pytest** : une liste de tests est lancée pour vérifier si le code
   est stable

* note : vous pouvez lancer cette commande manuellement, depuis le dossier 
  racine de l'application (où se trouve le fichier **manage.py**) et avec
  l'environnement virtuel activé

.. code-block:: console

    pytest --nomigrations --disable-warnings

2. **Flake8** : ce module teste si les conventions de la PEP8 sont respectées


* note : vous pouvez lancer cette commande manuellement, depuis le dossier
  racine de l'application (où se trouve le fichier **manage.py**)
  et avec l'environnement virtuel activé

.. code-block:: console

    flake8

3. Si ces 2 étapes sont claires, l'image est créée et transférée vers
   **Docker Hub**


* Notez que vous pouvez transférer manuellement l'image vers **Docker Hub**
  (l'image devrait déjà être créée dans Docker Desktop)

 Tout d'abord : taguer l'image

.. code-block:: console

     tag docker glgstyle/lettings-image glgstyle/lettings-image

Ensuite : déployer sur **Docker Hub**

.. code-block:: console

     docker push glgstyle/lettings-image

4. si l'image est bien poussée, **CircleCi** lance **Render** en important 
l'image


* remarque : vous pouvez déployer manuellement l'image **Docher Hub** en 
  accédant à l'URL du **deploy hook**

.. code-block:: console

    https://api.render.com/deploy/srv-clbpusd4lnec73dv717g?key=DZbtmdjTEQE

Après toutes ces étapes, le site Web sera accessible (**Render** lance 
automatiquement le service du serveur Web)
