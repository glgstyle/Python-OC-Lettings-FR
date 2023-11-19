============================
Interfaces de programmation
============================

---------------
Docker Desktop
---------------

Lorsque vous construisez une image de votre projet, le fichier est stocké
localement. Vous pouvez y accéder avec l'interface **Docker Desktop**.

Depuis cette interface vous pouvez démarrer votre application en cliquant sur 
le "bouton play"


Lorsqu'une image est en cours d'exécution, un "conteneur" est créé. Vous pouvez
ensuite arrêter l'application


---------
CircleCi
---------

Depuis le site CircleCi, vous pouvez accéder au tableau de bord 
(il faut être connecté). Ici vous pouvez voir toutes les étapes du pipeline.
En cas d'échec, vous pouvez voir quelle étape arrête le pipeline.

cas d'échec :

La mention failed apparait en rouge.

cas fonctionnel :

La mention Success apparait en vert.

L'un des grands avantages de **CircleCi** est que vous pouvez stocker 
des données sensibles (comme l'utilisateur et le mot de passe pour accéder 
à Docker, Render...). De cette façon, dans **config.yml**, vous pouvez utiliser
une variable stockée dans CircleCi qui garantit que les données ne seront pas
vues. Vous pouvez accéder via aux **paramètres du projet**.


-------
Render
-------

`Render <https://render.com/>`_ est un serveur "Paas" utilisé pour déployer 
une application à partir du référentiel **Git** ou de l'image **Docker Hub**. 
Lorsque le **deploy hook** est accédé, **Render** téléchargez l'image depuis 
**Docker Hub** et lancez le service Web.


Vous pouvez arrêter le service Web à partir du menu de configuration
