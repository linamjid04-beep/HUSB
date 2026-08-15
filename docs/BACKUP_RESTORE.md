# Sauvegarde et restauration

## A sauvegarder

- Base de donnees de production.
- Dossier `media/`.
- Variables d'environnement, conservees dans un coffre ou gestionnaire securise.
- Code source versionne.

## Frequence recommandee

- Base de donnees: quotidienne.
- Medias: quotidienne ou apres ajout important.
- Conservation: au moins 7 jours glissants et une sauvegarde mensuelle, a valider par HUSB.

## SQLite local

Sauvegarde:

```powershell
Copy-Item .\db.sqlite3 .\backups\db-YYYY-MM-DD.sqlite3
Copy-Item .\media .\backups\media-YYYY-MM-DD -Recurse
```

Restauration:

```powershell
Copy-Item .\backups\db-YYYY-MM-DD.sqlite3 .\db.sqlite3
Copy-Item .\backups\media-YYYY-MM-DD .\media -Recurse
python manage.py check
```

## Production

Utiliser l'outil de sauvegarde HostUpon ou un export base selon MySQL/PostgreSQL. Tester la restauration sur un environnement separe avant toute operation sur production.

## Points de vigilance

- Ne pas stocker les sauvegardes publiques dans le dossier web.
- Chiffrer les sauvegardes contenant des donnees personnelles.
- Documenter la date, l'auteur et le resultat de chaque restauration.
