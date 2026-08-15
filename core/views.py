from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Product

from .models import Partner, Project
from .site_config import CONTACT, CONTENT_STATUS, LEGAL


def home(request):
    context = {
        "featured_products": Product.objects.filter(is_active=True, featured=True).select_related("category")[:3],
        "projects": Project.objects.filter(is_published=True)[:3],
        "partners": Partner.objects.filter(is_active=True)[:6],
        "key_figures_enabled": CONTENT_STATUS["key_figures_enabled"],
        "meta_description": "Groupe HUSB presente ses activites telecoms et fibre optique: bureau d'etudes, travaux, materiel professionnel et recrutement.",
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html", {"meta_description": "Presentation institutionnelle du Groupe HUSB, specialise dans les telecoms et la fibre optique au Maroc."})


def services(request):
    return render(request, "core/services.html", {"meta_description": "Les metiers HUSB: bureau d'etudes fibre optique, travaux telecoms et materiel professionnel."})


def projects(request):
    projects_qs = Project.objects.filter(is_published=True)
    return render(request, "core/projects.html", {"projects": projects_qs})


def project_detail(request, slug):
    project = get_object_or_404(Project.objects.filter(is_published=True), slug=slug)
    return render(request, "core/project_detail.html", {"project": project})


def partners(request):
    partners_qs = Partner.objects.filter(is_active=True)
    return render(request, "core/partners.html", {"partners": partners_qs})


def legal_notice(request):
    items = [(label, value) for label, value in [
        ("Raison sociale", LEGAL["company_name"]),
        ("Forme juridique", LEGAL["legal_form"]),
        ("Capital", LEGAL["capital"]),
        ("Siege social", LEGAL["head_office"]),
        ("RC", LEGAL["rc"]),
        ("IF", LEGAL["if"]),
        ("ICE", LEGAL["ice"]),
        ("Directeur de publication", LEGAL["publication_director"]),
        ("Contact", LEGAL["contact_email"]),
        ("Hebergeur", LEGAL["hosting_provider"]),
    ] if value]
    return render(request, "core/legal_notice.html", {"legal_items": items})


def privacy_policy(request):
    return render(request, "core/privacy_policy.html")


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Sitemap: https://husb-groupe.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def contact_context(request):
    return {"contact_config": CONTACT}
