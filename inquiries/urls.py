from django.urls import path

from . import views

app_name = "inquiries"

urlpatterns = [
    path("", views.contact, name="contact"),
    path("confirmation/", views.contact_success, name="contact_success"),
    path("devis-materiel/", views.quote_request, name="quote_request"),
    path("devis-materiel/confirmation/", views.quote_success, name="quote_success"),
]
