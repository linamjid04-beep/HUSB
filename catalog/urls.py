from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.equipment, name="equipment"),
    path("sumitomo/", views.sumitomo_partner, name="sumitomo"),
]
