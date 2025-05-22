🎯 Plan détaillé du projet : Système de Reconnaissance d’Objets IoT
✅ Difficulté totale estimée : 35 points
📌 Objectif final : Développer un système IoT capable de détecter et reconnaître des objets en temps réel avec une caméra connectée et un modèle IA.

📌 1. Préparation & Configuration de l’Environnement (6 points)
✅ Installation des outils de développement (Python, OpenCV, TensorFlow, Flask...)
✅ Mise en place de la structure du projet (Dossiers & fichiers)
✅ Vérification du matériel (Test caméra sur PC et Raspberry Pi)
✅ Création de la base de données (SQLite ou PostgreSQL)

🟢 Barème :
✔ Installation Python et dépendances (2 pts)
✔ Création de la structure des fichiers (2 pts)
✔ Vérification du bon fonctionnement de la caméra (2 pts)

📌 2. Capture d’Images en Temps Réel (6 points)
✅ Développement d’un script pour capturer des images avec OpenCV
✅ Mise en place d’une boucle pour la capture continue en temps réel
✅ Stockage des images capturées dans un dossier dédié
✅ Ajout d’une option pour activer/désactiver la caméra

🟢 Barème :
✔ Capture d’images avec OpenCV (3 pts)
✔ Enregistrement et gestion des fichiers images (2 pts)
✔ Interface simple pour activer/désactiver la caméra (1 pt)

📌 3. Détection et Reconnaissance des Objets (10 points)
✅ Chargement d’un modèle pré-entraîné pour la détection d’objets (YOLO, MobileNet, etc.)
✅ Analyse des images capturées pour identifier les objets
✅ Affichage des résultats de la reconnaissance en temps réel
✅ Possibilité d’ajouter un modèle d’apprentissage personnalisé

🟢 Barème :
✔ Chargement du modèle IA et test sur images (3 pts)
✔ Détection en temps réel sur le flux vidéo (3 pts)
✔ Stockage des résultats et statistiques des objets détectés (2 pts)
✔ Option d’entraîner un modèle personnalisé (2 pts)

📌 4. Communication IoT et Stockage des Données (6 points)
✅ Développement d’une API Flask/Django pour envoyer les données des objets détectés
✅ Connexion entre Raspberry Pi et le serveur via requêtes HTTP
✅ Stockage des résultats de détection dans une base de données
✅ Affichage de l’historique des détections avec date et heure

🟢 Barème :
✔ Développement de l’API pour récupérer les résultats (2 pts)
✔ Connexion entre Raspberry Pi et API (2 pts)
✔ Sauvegarde des images et données dans une base de données (2 pts)

📌 5. Interface Utilisateur (5 points)
✅ Développement d’une interface web (ou desktop) pour afficher les résultats
✅ Affichage en temps réel des objets détectés et leurs statistiques
✅ Mise en place d’un tableau avec historique des détections
✅ Interface ergonomique et facile d’utilisation

🟢 Barème :
✔ Interface affichant les résultats de reconnaissance (2 pts)
✔ Tableau des statistiques et historique (2 pts)
✔ Interface intuitive et accessible (1 pt)

📌 6. Intégration d’un Serveur Cloud pour Analyse (5 points)
✅ Déploiement de l’API sur un serveur distant (AWS, Heroku, DigitalOcean, etc.)
✅ Accès aux résultats de reconnaissance via une application mobile ou web
✅ Stockage cloud des images et des statistiques des détections

🟢 Barème :
✔ Hébergement et test de l’API sur un serveur cloud (3 pts)
✔ Accès aux résultats via une plateforme externe (2 pts)

📌 7. Améliorations et Optimisations (Facultatif - 3 points)
✅ Ajout d’un système d’alerte (ex: envoi d’un message en cas de détection spécifique)
✅ Optimisation du modèle IA pour une meilleure précision et rapidité
✅ Ajout d’un mode apprentissage pour affiner la reconnaissance

🟢 Barème :
✔ Notifications en cas de détection d’un objet spécifique (1 pt)
✔ Optimisation des performances IA (1 pt)
✔ Mode apprentissage pour améliorer la reconnaissance (1 pt)

