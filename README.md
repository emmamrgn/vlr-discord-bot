# vlr-discord-bot

## Description
Ce projet est un bot Discord pour Valorant qui permet d'afficher le rang d'un joueur en utilisant des commandes simples. Le bot utilise l'API de tracker.gg pour récupérer les informations de rang des joueurs.

## Prérequis
- Python 3.8 ou supérieur
- Bibliothèques Python : `aiohttp`, `discord.py`

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/vlr-discord-bot.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd vlr-discord-bot
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Créez un fichier `token_file.py` et ajoutez votre token Discord et l'ID du canal de log :
   ```python
   TOKEN = 'votre-token-discord'
   CHANNEL_LOG_ID = votre_id_de_canal_log
   ```

## Utilisation
Lancez le bot avec la commande suivante :
```bash
python main.py
```

## Commandes
- `+aide` : Affiche le message d'aide avec la liste des commandes disponibles.
- `+ping` : Vérifie la latence du bot.
- `+rank username#tag` : Affiche le rang Valorant d'un joueur.


## Auteur/Développeur
Ce projet a été développé par [jiaxi](https://github.com/emmamrgn).

