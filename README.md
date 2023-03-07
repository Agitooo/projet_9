# **Projet 9 python openclassrooms**

Application web LITReview réalisée avec Django

La version de **Python** à utiliser : _**3.10.5**_

# **ENVIRONNEMENT VIRTUEL**

Création de l'environnement virtuel :


Pour créer l'environnement virtuel il faut exécuter la commande suivante à la racine du projet :

    python -m venv env


Puis la commande suivante pour démarrer l'environnement :

-   sous Linux

    
    source env/bin/activate

-   sous Windows


    env/Scripts/activate.bat


Pour installer les packages spécifiés dans le fichier requirements.txt il faut exécuter la commande suivante :

    pip install -r requirements.txt

# **FLAKE8**

Le code suit les normes de codage de la PEP8, un rapport peut être généré via flake8 avec la commande :

    flake8

Le fichier de configuration est ".flake8" à la racine du projet


# **SCRIPT**

Il faut dans un premier temps, démarrer le serveur Django à l'aide de la commande suivante :

    python manage.py runserver

Pour accéder à l'interface, il faut ouvrir l'url ___http://127.0.0.1:8000/___ dans un navigateur.

## Django administration

Pour accéder à l'interface d'administration de Django, il faut aller sur l'url  ___http://127.0.0.1:8000/admin/___ 

### Avec le fichier db.sqlite fournis

Compte admin:

| *Identifiant* | *Mot de passe* |
|---------------|----------------|
| Agito_su      | PassW0rd!su    |

Comptes utilisateurs:

| *Identifiant* | *Mot de passe* |
|---------------|----------------|
| toto1         | Tata123!       |
| toto2         | Passw0rd!      |
| toto3         | Passw0rd!      |
| toto4         | Passw0rd!      |

### Sans le fichier db.sqlite fournis

Il faut dans un premier temps générer la base de données avec la commande :

    python manage.py makemigrations

Puis, appliquer la migration à l'aide de la commande :

    python manage.py migrate

Pour créer un compte dans la partie administration, il faut exécuter la commande suivante et suivre les instructions:

    python manage.py createsuperuser

La création des comptes utilisateurs se fait depuis l'interface web via **"S'inscrire"**

## Fonctionnalités du site web

 - Se connecter / S'inscrire / Se déconnecter
 - Voir ses tickets et critiques et ceux des utilisateurs suivis
 - Créer des tickets
 - Déposer des critiques sur un ticket existant ou non
 - Edition / Suppression de ses tickets / critiques
 - Gestions des abonnements : suivre ou ne plus suivre un utilisateur