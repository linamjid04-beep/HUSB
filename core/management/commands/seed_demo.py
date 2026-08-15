from django.core.management.base import BaseCommand

from careers.models import JobOffer
from catalog.models import Product, ProductCategory
from core.models import Partner, Project


class Command(BaseCommand):
    help = "Cree des donnees locales de demonstration clairement identifiees."

    def handle(self, *args, **options):
        category, _ = ProductCategory.objects.get_or_create(
            slug="demo-soudeuses-fibre",
            defaults={
                "name": "DEMO - Soudeuses fibre",
                "description": "Categorie de demonstration a remplacer par une categorie officielle.",
                "is_active": True,
            },
        )
        Product.objects.get_or_create(
            slug="demo-produit-sans-reference-officielle",
            defaults={
                "name": "DEMO - Produit sans reference officielle",
                "brand": "DEMO",
                "category": category,
                "short_description": "Produit de demonstration sans prix ni caracteristique technique.",
                "is_active": True,
                "featured": True,
            },
        )
        Project.objects.get_or_create(
            slug="demo-realisation-a-remplacer",
            defaults={
                "title": "DEMO - Realisation a remplacer",
                "mission_type": "Demonstration",
                "short_description": "Reference fictive uniquement destinee a tester l'affichage local.",
                "is_published": True,
            },
        )
        Partner.objects.get_or_create(
            name="DEMO - Partenaire a remplacer",
            defaults={
                "description": "Partenaire fictif pour demonstration locale.",
                "is_active": True,
            },
        )
        JobOffer.objects.get_or_create(
            slug="demo-technicien-fibre",
            defaults={
                "title": "DEMO - Technicien fibre",
                "location": "Maroc",
                "short_description": "Offre fictive pour demonstration locale.",
                "description": "Description de demonstration.",
                "missions": "Missions de demonstration.",
                "profile": "Profil de demonstration.",
                "is_active": True,
            },
        )
        self.stdout.write(self.style.SUCCESS("Donnees de demonstration creees ou deja presentes."))
