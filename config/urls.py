from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core.sitemaps import ProjectSitemap, StaticViewSitemap

admin.site.site_header = "Administration HUSB"
admin.site.site_title = "Administration HUSB"
admin.site.index_title = "Administration HUSB"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": {"static": StaticViewSitemap, "projects": ProjectSitemap}}, name="django.contrib.sitemaps.views.sitemap"),
    path("recrutement/", include("careers.urls")),
    path("contact/", include("inquiries.urls")),
    path("materiel-professionnel/", include("catalog.urls")),
    path("", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
