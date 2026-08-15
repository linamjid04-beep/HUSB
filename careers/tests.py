from django.contrib import admin
from django.test import TestCase
from django.urls import reverse

from .models import JobOffer


class CareersTests(TestCase):
    def setUp(self):
        self.active_offer = JobOffer.objects.create(
            title="Exemple de demonstration - Technicien fibre",
            slug="demo-technicien-fibre",
            location="Rabat",
            contract_type=JobOffer.CONTRACT_STAGE,
            short_description="Offre de demonstration pour valider l'affichage.",
            description="Description de demonstration.",
            missions="Mission de demonstration.",
            is_active=True,
        )
        self.inactive_offer = JobOffer.objects.create(
            title="Exemple de demonstration - Offre inactive",
            slug="demo-offre-inactive",
            location="Rabat",
            contract_type=JobOffer.CONTRACT_STAGE,
            short_description="Cette offre ne doit pas etre publique.",
            description="Description inactive.",
            is_active=False,
        )

    def test_active_offer_appears(self):
        response = self.client.get(reverse("careers:job_list"))
        self.assertContains(response, self.active_offer.title)

    def test_inactive_offer_does_not_appear(self):
        response = self.client.get(reverse("careers:job_list"))
        self.assertNotContains(response, self.inactive_offer.title)

    def test_active_offer_detail_is_accessible(self):
        response = self.client.get(self.active_offer.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.active_offer.title)
        self.assertContains(response, "Mission de demonstration.")

    def test_inactive_offer_detail_is_not_public(self):
        response = self.client.get(self.inactive_offer.get_absolute_url())
        self.assertEqual(response.status_code, 404)

    def test_job_offer_is_registered_in_admin(self):
        self.assertIn(JobOffer, admin.site._registry)
