from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


def validate_image_size(file):
    max_size = 3 * 1024 * 1024
    if file.size > max_size:
        from django.core.exceptions import ValidationError

        raise ValidationError("L'image ne doit pas depasser 3 Mo.")


class Project(models.Model):
    title = models.CharField("titre", max_length=180)
    slug = models.SlugField("slug", max_length=200, unique=True)
    client = models.CharField("client", max_length=160, blank=True)
    location = models.CharField("localisation", max_length=140, blank=True)
    mission_type = models.CharField("type de mission", max_length=140, blank=True)
    short_description = models.TextField("resume court", max_length=500)
    description = models.TextField("description", blank=True)
    image = models.ImageField(
        "image",
        upload_to="projects/",
        blank=True,
        validators=[
            FileExtensionValidator(["jpg", "jpeg", "png", "webp"]),
            validate_image_size,
        ],
    )
    completion_date = models.DateField("date de realisation", blank=True, null=True)
    is_published = models.BooleanField("publie", default=False)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)

    class Meta:
        ordering = ["display_order", "-completion_date", "title"]
        verbose_name = "realisation"
        verbose_name_plural = "realisations"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:project_detail", kwargs={"slug": self.slug})


class Partner(models.Model):
    name = models.CharField("nom", max_length=160)
    logo = models.ImageField(
        "logo",
        upload_to="partners/",
        blank=True,
        validators=[
            FileExtensionValidator(["jpg", "jpeg", "png", "webp", "svg"]),
            validate_image_size,
        ],
    )
    website = models.URLField("site web", blank=True)
    description = models.TextField("description", blank=True)
    is_active = models.BooleanField("actif", default=False)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "partenaire"
        verbose_name_plural = "partenaires"

    def __str__(self):
        return self.name
