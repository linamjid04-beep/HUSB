# Audit initial

## Etat actuel
- Projet Django local existant avec les applications `core`, `careers`, `inquiries` et `catalog`.
- Page d'accueil existante dans `templates/core/home.html`.
- Base SQLite locale presente.
- Aucun depot Git detecte dans `C:\Users\1234\Documents\HUSB-SITE`.

## Erreurs trouvees
- L'URL `/static/core/css/style.css` retourne 404 car le projet utilise un fichier global `static/css/style.css`.
- `python manage.py findstatic css/style.css` trouve bien `static/css/style.css`.
- `python manage.py findstatic core/css/style.css` ne trouve rien, ce qui est normal avec la convention globale retenue.
- Les dossiers `js` et `images` avaient ete crees sous `static/css/`, ce qui melangeait l'organisation des assets.

## Fichiers concernes
- `config/settings.py`
- `config/urls.py`
- `templates/core/home.html`
- `static/css/style.css`
- `core/views.py`
- `core/urls.py`
- les fichiers `apps.py` des quatre applications

## Corrections prevues
- Conserver une convention unique: `static/css/`, `static/js/`, `static/images/`.
- Utiliser `{% static 'css/style.css' %}` dans le layout global.
- Ajouter `templates/base.html` et les includes communs.
- Ajouter les URLs publiques par application.
- Ajouter les modeles administrables pour recrutement, contact et devis.

## Elements deja fonctionnels
- `python manage.py check` passait avant modifications.
- Le template chargeait deja la bonne reference `css/style.css`.
- `STATICFILES_DIRS` pointait vers le dossier `static`.

## Risques techniques
- Les contenus officiels HUSB, partenaires, produits et realisations ne sont pas encore disponibles.
- Le site reste en configuration locale et ne doit pas etre deploye tel quel.
- SMTP, donnees legales, SEO final et production sont hors lot.

## Perimetre retenu
- Socle demonstrable: pages publiques, design responsive, admin Django, offres d'emploi, contact, devis materiel, pages materiel et partenaire provisoire, tests et documentation.
