from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return [
            "core:home",
            "core:about",
            "core:services",
            "catalog:equipment",
            "catalog:sumitomo",
            "core:projects",
            "core:partners",
            "careers:job_list",
            "inquiries:contact",
            "inquiries:quote_request",
            "core:legal_notice",
            "core:privacy_policy",
        ]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return Project.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
