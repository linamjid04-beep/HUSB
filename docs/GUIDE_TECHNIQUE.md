# Guide technique

## Architecture

- `config`: configuration Django, URLs racine, WSGI/ASGI.
- `core`: pages institutionnelles, realisations, partenaires, sitemap, robots.
- `catalog`: categories et produits materiel, page partenaire Sumitomo/Sumimoto.
- `careers`: offres d'emploi.
- `inquiries`: contact general et demande de devis materiel.
- `templates`: templates HTML.
- `static`: CSS et JavaScript.
- `media`: uploads locaux, ignore par Git.

## Installation

```powershell
cd C:\Users\1234\Documents\HUSB-SITE
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Environnement

Copier `.env.example` vers `.env` si l'hebergeur ou le shell charge ce fichier. Le projet lit les variables directement depuis l'environnement.

Variables principales: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `DB_*`, `EMAIL_*`, `CONTACT_RECIPIENT_EMAIL`, `QUOTE_RECIPIENT_EMAIL`.

## Base de donnees

SQLite convient au local. En production, configurer `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

Pour MySQL HostUpon, utiliser le backend Django MySQL et installer le connecteur adapte selon l'environnement disponible. Pour PostgreSQL, utiliser `django.db.backends.postgresql` avec `psycopg`.

## Static et media

```powershell
python manage.py collectstatic --noinput
```

Servir `staticfiles/` comme fichiers statiques et conserver `media/` en ecriture pour les uploads.

## Email

En local, le backend console suffit. En production, renseigner SMTP via variables d'environnement et definir les destinataires contact/devis.

## Tests et validation

```powershell
python manage.py check
python manage.py makemigrations --check
python manage.py migrate
python manage.py test
python manage.py collectstatic --noinput
python manage.py check --deploy
```

## Maintenance

- Sauvegarder base et medias.
- Mettre a jour les dependances dans un environnement de test avant production.
- Verifier regulierement les demandes stockees et purger selon la politique validee par HUSB.
