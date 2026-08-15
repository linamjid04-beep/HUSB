# Guide administrateur HUSB

## Connexion

1. Ouvrir `/admin/`.
2. Se connecter avec un compte administrateur cree par `python manage.py createsuperuser`.
3. Ne jamais partager le mot de passe administrateur.

## Offres d'emploi

- Aller dans **Offres d'emploi**.
- Creer une offre avec titre, slug, lieu, contrat, resume, description, missions, profil et prerequis.
- Activer **visible publiquement** pour publier.
- Desactiver ce champ pour retirer l'offre du site sans la supprimer.

## Realisations

- Aller dans **Realisations**.
- Ajouter titre, resume, mission, client, lieu, image et date si disponibles.
- Cocher **publie** uniquement pour les references validees.
- Utiliser **ordre d'affichage** pour organiser la liste.

## Partenaires

- Aller dans **Partenaires**.
- Ajouter nom, logo, site web et description si autorises.
- Cocher **actif** pour publier.

## Catalogue materiel

- Creer d'abord les **categories produits**.
- Creer ensuite les **produits** avec nom, marque, categorie, resume, image et document PDF optionnel.
- Cocher **actif** pour publier; cocher **mis en avant** pour l'accueil.
- Ne publier aucun prix ou detail technique non valide.

## Contacts et devis

- Les demandes de contact arrivent dans **Demandes de contact**.
- Les devis materiel arrivent dans **Demandes de devis materiel**.
- Mettre a jour le statut: nouveau, en cours, traite ou archive.
- Ne pas exporter inutilement les donnees personnelles.

## Medias

- Images acceptees: jpg, jpeg, png, webp; svg uniquement pour logos partenaires.
- Documents produits: PDF.
- Eviter les fichiers lourds; les validations bloquent les images de plus de 3 Mo et PDF de plus de 8 Mo.

## Bonnes pratiques

- Publier seulement les contenus valides par HUSB.
- Utiliser les donnees demo uniquement en local.
- Se deconnecter apres usage, surtout sur un ordinateur partage.
