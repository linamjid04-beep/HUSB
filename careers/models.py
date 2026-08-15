from django.db import models
from django.urls import reverse
from django.utils import timezone


class JobOffer(models.Model):
    CONTRACT_CDI = "cdi"
    CONTRACT_CDD = "cdd"
    CONTRACT_STAGE = "stage"
    CONTRACT_FREELANCE = "freelance"
    CONTRACT_OTHER = "autre"

    CONTRACT_CHOICES = [
        (CONTRACT_CDI, "CDI"),
        (CONTRACT_CDD, "CDD"),
        (CONTRACT_STAGE, "Stage"),
        (CONTRACT_FREELANCE, "Freelance"),
        (CONTRACT_OTHER, "Autre"),
    ]

    title = models.CharField("intitule", max_length=180)
    slug = models.SlugField("slug", max_length=200, unique=True)
    location = models.CharField("localisation", max_length=120, default="Rabat, Maroc")
    contract_type = models.CharField(
        "type de contrat", max_length=20, choices=CONTRACT_CHOICES, default=CONTRACT_STAGE
    )
    short_description = models.TextField("resume court", max_length=500)
    description = models.TextField("description")
    missions = models.TextField("missions", blank=True)
    profile = models.TextField("profil recherche", blank=True)
    requirements = models.TextField("prerequis", blank=True)
    published_at = models.DateTimeField("date de publication", default=timezone.now)
    closing_date = models.DateField("date limite", blank=True, null=True)
    is_active = models.BooleanField("visible publiquement", default=False)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)

    class Meta:
        ordering = ["display_order", "-published_at", "title"]
        verbose_name = "offre d'emploi"
        verbose_name_plural = "offres d'emploi"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("careers:job_detail", kwargs={"slug": self.slug})
