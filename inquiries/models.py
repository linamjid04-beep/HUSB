from django.db import models


class ContactRequest(models.Model):
    first_name = models.CharField("prenom", max_length=100)
    last_name = models.CharField("nom", max_length=100)
    company = models.CharField("entreprise", max_length=160, blank=True)
    email = models.EmailField("email")
    phone = models.CharField("telephone", max_length=40, blank=True)
    subject = models.CharField("sujet", max_length=180)
    message = models.TextField("message")
    consent = models.BooleanField("consentement")
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)
    is_processed = models.BooleanField("traitee", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "demande de contact"
        verbose_name_plural = "demandes de contact"

    def __str__(self):
        return f"{self.subject} - {self.first_name} {self.last_name}"


class QuoteRequest(models.Model):
    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_DONE = "done"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = [
        (STATUS_NEW, "Nouveau"),
        (STATUS_IN_PROGRESS, "En cours"),
        (STATUS_DONE, "Traite"),
        (STATUS_ARCHIVED, "Archive"),
    ]

    first_name = models.CharField("prenom", max_length=100)
    last_name = models.CharField("nom", max_length=100)
    company = models.CharField("entreprise", max_length=160)
    job_title = models.CharField("fonction", max_length=120, blank=True)
    email = models.EmailField("email")
    phone = models.CharField("telephone", max_length=40)
    city = models.CharField("ville", max_length=120)
    product_interest = models.CharField("materiel souhaite", max_length=180)
    quantity = models.PositiveIntegerField("quantite", blank=True, null=True)
    usage_description = models.TextField("usage prevu")
    training_required = models.BooleanField("formation souhaitee", default=False)
    additional_message = models.TextField("message complementaire", blank=True)
    consent = models.BooleanField("consentement")
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)
    status = models.CharField(
        "statut", max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "demande de devis materiel"
        verbose_name_plural = "demandes de devis materiel"

    def __str__(self):
        return f"Devis {self.product_interest} - {self.company}"
