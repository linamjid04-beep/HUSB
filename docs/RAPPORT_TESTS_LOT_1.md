# Rapport de tests lot 1

## Commandes executees
- `python manage.py check`
- `python manage.py findstatic css/style.css`
- `python manage.py findstatic core/css/style.css`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py test`
- `python manage.py collectstatic --noinput`
- Verification HTTP locale sur `http://127.0.0.1:8001/`
- Verification HTTP locale sur `http://127.0.0.1:8001/static/css/style.css`

## Resultats
- `check`: aucun probleme.
- `findstatic css/style.css`: fichier trouve dans `static/css/style.css`.
- `findstatic core/css/style.css`: aucun fichier trouve, conforme a la convention retenue.
- Migrations creees pour `careers` et `inquiries`.
- Migrations appliquees avec succes.
- Tests: 15 tests, tous en succes.
- `collectstatic`: 132 fichiers copies vers `staticfiles`.
- Serveur local: page d'accueil en HTTP 200.
- CSS local: `/static/css/style.css` en HTTP 200.
