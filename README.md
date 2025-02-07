#Projet maintenance applicative

Si vous avez des soucis lors de l'installation du projet, vous m'appelez
Mise en place du projet :
- Faite un clone du projet
- Faite un nouveau repository et me l'envoyer à l'adresse faivrem22@gmail.com avec <NOM> et <PRENOM>
##Lancement du projet 
- Build le docker compose (dans le dossier du projet dans un terminal : docker compose build)
- Lancer le docker compose (dans le dossier du projet dans un terminal : docker compose up)
Une fois que tout est fini :
- Aller dans le container python (en console : docker compose exec api sh)
  - Lancer le script python : init.py (python3 init.py)
- Le projet est lancé
Pour tester : 
Adresse angular :
http://localhost:4200/accueil
Adresse api :
http://127.0.0.1:5000/
