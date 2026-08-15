# Deploiement HostUpon

Nom de domaine prevu: `husb-groupe.com`

## Informations necessaires

- Acces HostUpon.
- Acces DNS du domaine.
- Version Python disponible.
- Type de base de donnees disponible: MySQL ou PostgreSQL.
- Identifiants base de donnees.
- Identifiants SMTP.
- Adresse email destinataire contact et devis.

## Preparation

1. Creer l'application Python sur HostUpon.
2. Televerser le code sans `.env`, sans `db.sqlite3` de developpement et sans medias de test.
3. Installer les dependances:

```bash
pip install -r requirements.txt
```

4. Definir les variables d'environnement:

```bash
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=husb-groupe.com,www.husb-groupe.com
CSRF_TRUSTED_ORIGINS=https://husb-groupe.com,https://www.husb-groupe.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## Base de donnees

Configurer `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` selon HostUpon.

Migrer:

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Static et media

```bash
python manage.py collectstatic --noinput
```

Configurer le serveur pour exposer `/static/` depuis `staticfiles/` et `/media/` depuis `media/`.

## WSGI

Pointer l'application HostUpon vers `config.wsgi:application`. Verifier que le dossier du projet est dans le `PYTHONPATH`.

## SSL et domaine

1. Pointer `husb-groupe.com` et `www.husb-groupe.com` vers HostUpon.
2. Activer SSL.
3. Activer les variables HTTPS seulement apres validation du certificat.

## Email

Renseigner:

- `DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS`
- `DEFAULT_FROM_EMAIL`
- `CONTACT_RECIPIENT_EMAIL`
- `QUOTE_RECIPIENT_EMAIL`

## Verification finale

- Accueil, metiers, materiel, Sumitomo, realisations, partenaires, recrutement, contact, devis.
- `/admin/`
- `/sitemap.xml`
- `/robots.txt`
- Envoi contact et devis.
- Upload image/PDF depuis admin.

Aucun deploiement externe n'a ete effectue depuis cette codebase car les acces HostUpon, DNS, base et SMTP ne sont pas disponibles ici.
