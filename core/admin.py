from django.contrib import admin

from .models import Partner, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "client",
        "location",
        "mission_type",
        "is_published",
        "display_order",
        "completion_date",
        "updated_at",
    )
    list_filter = ("is_published", "mission_type", "completion_date", "created_at")
    search_fields = ("title", "client", "location", "mission_type", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_published", "display_order")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "completion_date"
    ordering = ("display_order", "-completion_date", "title")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "is_active", "display_order", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "website", "description")
    list_editable = ("is_active", "display_order")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("display_order", "name")
