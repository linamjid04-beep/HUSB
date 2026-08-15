from django.test import TestCase
from django.urls import reverse

from .models import Product, ProductCategory


class CatalogTests(TestCase):
    def test_equipment_page_is_accessible(self):
        response = self.client.get(reverse("catalog:equipment"))
        self.assertEqual(response.status_code, 200)

    def test_partner_page_marks_content_as_pending(self):
        response = self.client.get(reverse("catalog:sumitomo"))
        self.assertContains(response, "Orthographe a confirmer")

    def test_only_active_products_are_public(self):
        category = ProductCategory.objects.create(name="Soudeuses", slug="soudeuses")
        active = Product.objects.create(
            name="Produit actif demo",
            slug="produit-actif-demo",
            category=category,
            short_description="Produit de demonstration.",
            is_active=True,
        )
        inactive = Product.objects.create(
            name="Produit inactif demo",
            slug="produit-inactif-demo",
            category=category,
            short_description="Produit masque.",
            is_active=False,
        )
        response = self.client.get(reverse("catalog:equipment"))
        self.assertContains(response, active.name)
        self.assertNotContains(response, inactive.name)
