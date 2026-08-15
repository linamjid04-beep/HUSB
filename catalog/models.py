from django.core.validators import FileExtensionValidator
from django.db import models

from core.models import validate_image_size


def validate_document_size(file):
    max_size = 8 * 1024 * 1024
    if file.size > max_size:
        from django.core.exceptions import ValidationError

        raise ValidationError("Le document ne doit pas depasser 8 Mo.")


class ProductCategory(models.Model):
    name = models.CharField("nom", max_length=150)
    slug = models.SlugField("slug", max_length=170, unique=True)
    description = models.TextField("description", blank=True)
    is_active = models.BooleanField("active", default=True)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "categorie produit"
        verbose_name_plural = "categories produits"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("nom", max_length=180)
    slug = models.SlugField("slug", max_length=200, unique=True)
    brand = models.CharField("marque", max_length=140, blank=True)
    category = models.ForeignKey(
        ProductCategory,
        verbose_name="categorie",
        related_name="products",
        on_delete=models.PROTECT,
    )
    short_description = models.TextField("resume court", max_length=500)
    description = models.TextField("description", blank=True)
    image = models.ImageField(
        "image",
        upload_to="products/",
        blank=True,
        validators=[
            FileExtensionValidator(["jpg", "jpeg", "png", "webp"]),
            validate_image_size,
        ],
    )
    technical_document = models.FileField(
        "document technique",
        upload_to="products/documents/",
        blank=True,
        validators=[
            FileExtensionValidator(["pdf"]),
            validate_document_size,
        ],
    )
    is_active = models.BooleanField("actif", default=False)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    featured = models.BooleanField("mis en avant", default=False)
    created_at = models.DateTimeField("cree le", auto_now_add=True)
    updated_at = models.DateTimeField("modifie le", auto_now=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "produit"
        verbose_name_plural = "produits"

    def __str__(self):
        return self.name
