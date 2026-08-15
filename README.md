# Groupe HUSB - Site institutionnel Django

Site institutionnel du Groupe HUSB pour presenter les activites telecoms et fibre optique au Maroc: bureau d'etudes, travaux, materiel professionnel, partenaire Sumitomo/Sumimoto, realisations, partenaires, recrutement, contact et devis.

Le projet est pret techniquement pour recevoir les contenus officiels. Aucune information commerciale, juridique ou technique non fournie par HUSB n'est inventee.

## Stack

- Python
- Django 6.0.7
- SQLite en local
- Django Admin
- HTML, CSS, JavaScript
- Pillow pour les images

## Structure

- `config/`: configuration Django, URLs racine, WSGI/ASGI.
- `core/`: pages institutionnelles, realisations, partenaires, sitemap, robots.
- `catalog/`: categories, produits et page partenaire.
- `careers/`: offres d'emploi.
- `inquiries/`: contact et devis.
- `templates/`: templates publics.
- `static/`: CSS et JavaScript.
- `docs/`: guides admin, technique, deploiement, sauvegarde et contenus manquants.

## Installation Windows

```powershell
cd C:\Users\1234\Documents\HUSB-SITE
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuration

Le projet fonctionne en local sans `.env`. Pour une configuration explicite, copier `.env.example` vers `.env` ou definir les variables dans l'environnement.

Variables importantes:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- `CONTACT_RECIPIENT_EMAIL`, `QUOTE_RECIPIENT_EMAIL`

## Base de donnees

```powershell
python manage.py migrate
python manage.py createsuperuser
```

## Donnees de demonstration

Optionnel en local:

```powershell
python manage.py seed_demo
```

Toutes les donnees creees portent la mention `DEMO`.

## Lancement

```powershell
python manage.py runserver
```

Ouvrir `http://127.0.0.1:8000/`.

## Administration

Ouvrir `http://127.0.0.1:8000/admin/`.

HUSB peut gerer:

- offres d'emploi;
- realisations;
- partenaires;
- categories produits;
- produits;
- demandes de contact;
- demandes de devis.

## Tests et validation

```powershell
python manage.py check
python manage.py makemigrations --check
python manage.py migrate
python manage.py test
python manage.py collectstatic --noinput
python manage.py check --deploy
```

## Production

Consulter:

- `docs/GUIDE_TECHNIQUE.md`
- `docs/DEPLOIEMENT_HOSTUPON.md`
- `docs/BACKUP_RESTORE.md`
- `docs/CONTENUS_MANQUANTS_HUSB.md`

Ne pas deployer sans vrais acces HostUpon, DNS, base de donnees et SMTP.
