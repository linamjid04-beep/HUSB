# Decisions techniques

- Convention static globale retenue: `static/css/style.css`, `static/js/main.js`, `static/images/`.
- Toutes les pages publiques heritent de `templates/base.html`.
- Les applications gardent leurs responsabilites: `core` pour pages institutionnelles, `careers` pour recrutement, `inquiries` pour contact/devis, `catalog` pour materiel.
- Le formulaire de devis materiel est un modele distinct du contact general.
- La page partenaire utilise une constante `PARTNER_DISPLAY_NAME` dans `catalog/views.py` pour corriger rapidement le nom Sumitomo/Sumimoto.
- Django Admin suffit pour le lot; aucun dashboard specifique n'est cree.
- E-mail configure en console backend pour le developpement local.
- Les secrets sont preparables via variables d'environnement et documentes dans `.env.example`.
