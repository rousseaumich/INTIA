### Prérequis

- Assurez-vous d'avoir Python installé sur votre système.
- Créez un environnement virtuel pour isoler les dépendances de votre projet.

### Installation depuis le dossier .rar

- Décompressez le fichier .rar contenant l'application Django REST Framework dans un répertoire de votre choix.
- Activez votre environnement virtuel.
- Déplacez-vous dans le répertoire du projet décompressé 
- Installez les dépendances du projet en utilisant pip 


#### Configuration de la base de données

- Ouvrez le fichier settings.py du projet.
- Configurez les paramètres de connexion à la base de données (moteur, nom, utilisateur, mot de passe).
- Sauvegardez le fichier de configuration.

#### Création des tables de la base de données

- Effectuez les migrations initiales pour créer les tables de base de données 

"python manage.py makemigrations suivie de python manage.py migrate"

#### Lancement du serveur de développement
  
  "python manage.py runserver"

#### Étapes supplémentaires

- Créez un superutilisateur pour accéder à l'interface d'administration

"python manage.py createsuperuser"
