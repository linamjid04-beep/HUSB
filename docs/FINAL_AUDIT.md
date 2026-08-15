# Audit final avant corrections

Date: 15 aout 2026

## Etat initial constate

Le projet est une application Django organisee autour de quatre apps: `core`, `careers`, `catalog` et `inquiries`. Les pages publiques principales existent, les formulaires contact/devis sont separes, le recrutement dispose deja d'un modele administrable, et le design responsive de base est en place.

## Points fonctionnels

- Django demarre sur une structure simple et lisible.
- `JobOffer` est administrable et filtre les offres inactives cote public.
- Les demandes de contact et de devis sont persistees.
- Les formulaires utilisent CSRF, validation serveur et honeypot.
- Les pages 404 et 500 existent.
- Les assets statiques sont centralises dans `static/`.

## Manques et risques identifies

- Realisations et partenaires non administrables.
- Catalogue materiel non administrable.
- Page Sumitomo seulement statique, avec nom a centraliser.
- Pas de pages legales publiques.
- SEO incomplet: pas de sitemap, robots, canonical ni Open Graph robuste.
- Configuration production incomplete: `DEBUG` force a `True`, variables email limitees, securite HTTPS/cookies non pilotee par environnement.
- Uploads non modelises pour images/documents et validations absentes.
- Admin perfectible pour un usage back-office complet.
- Tests insuffisants pour les nouveaux parcours attendus.
- Documentation finale, deploiement, sauvegarde et contenus manquants a produire.
- Pas de depot Git initialise dans ce dossier; impossible d'inspecter un historique ou de preparer un commit.

## Contraintes de contenu

Aucune information commerciale, juridique, technique ou historique non fournie par HUSB ne doit etre inventee. Les contenus officiels absents doivent rester centralises, administrables lorsque pertinent, ou documentes comme informations a fournir.

## Strategie de correction

- Ajouter les modeles dynamiques manquants sans supprimer les apps existantes.
- Remplacer les placeholders publics par des etats vides propres.
- Centraliser les libelles sensibles dans une configuration Python claire.
- Renforcer `settings.py` via variables d'environnement sans casser le local.
- Completer templates, CSS, JS, admin, migrations et tests.
- Produire la documentation finale demandee.
