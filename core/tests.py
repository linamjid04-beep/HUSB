from django.contrib import admin
from django.test import TestCase
from django.urls import reverse

from .models import Partner, Project


class CorePageTests(TestCase):
    def test_public_pages_are_accessible(self):
        names = [
            "core:home",
            "core:about",
            "core:services",
            "core:projects",
            "core:partners",
            "core:legal_notice",
            "core:privacy_policy",
            "catalog:equipment",
            "catalog:sumitomo",
        ]

        for name in names:
            with self.subTest(name=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_home_links_global_stylesheet_and_metadata(self):
        response = self.client.get(reverse("core:home"))
        self.assertContains(response, "/static/css/style.css")
        self.assertContains(response, 'rel="canonical"')
        self.assertContains(response, 'property="og:title"')

    def test_project_publication_rules(self):
        published = Project.objects.create(
            title="Projet publie",
            slug="projet-publie",
            short_description="Reference validee.",
            is_published=True,
        )
        hidden = Project.objects.create(
            title="Projet masque",
            slug="projet-masque",
            short_description="Reference non publiee.",
            is_published=False,
        )

        list_response = self.client.get(reverse("core:projects"))
        self.assertContains(list_response, published.title)
        self.assertNotContains(list_response, hidden.title)
        self.assertEqual(self.client.get(published.get_absolute_url()).status_code, 200)
        self.assertEqual(self.client.get(hidden.get_absolute_url()).status_code, 404)

    def test_partner_active_rules(self):
        Partner.objects.create(name="Partenaire actif", is_active=True)
        Partner.objects.create(name="Partenaire inactif", is_active=False)
        response = self.client.get(reverse("core:partners"))
        self.assertContains(response, "Partenaire actif")
        self.assertNotContains(response, "Partenaire inactif")

    def test_robots_and_sitemap_are_accessible(self):
        robots = self.client.get(reverse("core:robots_txt"))
        self.assertEqual(robots.status_code, 200)
        self.assertContains(robots, "Disallow: /admin/")
        sitemap = self.client.get("/sitemap.xml")
        self.assertEqual(sitemap.status_code, 200)

    def test_custom_models_are_registered_in_admin(self):
        self.assertIn(Project, admin.site._registry)
        self.assertIn(Partner, admin.site._registry)
