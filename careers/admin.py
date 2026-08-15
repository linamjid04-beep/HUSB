from django.contrib import admin

from .models import JobOffer


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "contract_type",
        "is_active",
        "display_order",
        "published_at",
        "updated_at",
    )
    list_filter = ("is_active", "contract_type", "published_at")
    search_fields = ("title", "location", "short_description", "description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_active", "display_order")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "published_at"
    ordering = ("display_order", "-published_at")
