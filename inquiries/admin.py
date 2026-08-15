from django.contrib import admin

from .models import ContactRequest, QuoteRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("subject", "first_name", "last_name", "email", "company", "created_at", "is_processed")
    list_filter = ("is_processed", "created_at")
    search_fields = ("first_name", "last_name", "company", "email", "subject", "message")
    list_editable = ("is_processed",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = (
        "product_interest",
        "company",
        "city",
        "email",
        "phone",
        "status",
        "created_at",
    )
    list_filter = ("status", "training_required", "created_at", "city")
    search_fields = (
        "first_name",
        "last_name",
        "company",
        "email",
        "city",
        "product_interest",
        "usage_description",
    )
    list_editable = ("status",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
