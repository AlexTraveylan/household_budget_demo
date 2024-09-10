# API de Gestion de Budget

Une API robuste pour la gestion de budget personnel, construite avec Django et django-ninja.

## Fonctionnalités

- Gestion des utilisateurs et authentification
- Enregistrement et suivi des transactions

## Prérequis

- Python 3.8+
- Django 3.2+
- django-ninja

## Environnement

Copiez le fichier `.env.exemple` en `.env` et remplissez les variables d'environnement.

## Installation

1. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez les variables d'environnement dans un fichier `.env` à la racine du projet.

4. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

## Utilisation

Accédez à l'interface API à l'adresse `http://localhost:8000/api/docs` pour explorer et tester les endpoints disponibles.

## Contribution

Les contributions sont les bienvenues ! Veuillez consulter le fichier CONTRIBUTING.md pour les directives.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
