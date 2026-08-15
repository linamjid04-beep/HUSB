from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("a-propos/", views.about, name="about"),
    path("nos-metiers/", views.services, name="services"),
    path("realisations/", views.projects, name="projects"),
    path("realisations/<slug:slug>/", views.project_detail, name="project_detail"),
    path("partenaires/", views.partners, name="partners"),
    path("mentions-legales/", views.legal_notice, name="legal_notice"),
    path("politique-confidentialite/", views.privacy_policy, name="privacy_policy"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
