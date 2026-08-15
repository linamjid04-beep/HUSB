from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactRequestForm, QuoteRequestForm


def notify_team(subject, body, recipient):
    if not recipient:
        return
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [recipient],
        fail_silently=True,
    )


def contact(request):
    if request.method == "POST":
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            contact_request = form.save()
            notify_team(
                f"Nouveau contact HUSB: {contact_request.subject}",
                (
                    f"Nom: {contact_request.first_name} {contact_request.last_name}\n"
                    f"Entreprise: {contact_request.company or '-'}\n"
                    f"Email: {contact_request.email}\n"
                    f"Telephone: {contact_request.phone or '-'}\n\n"
                    f"{contact_request.message}"
                ),
                settings.CONTACT_RECIPIENT_EMAIL,
            )
            messages.success(request, "Votre demande de contact a bien ete enregistree.")
            return redirect("inquiries:contact_success")
        messages.error(request, "Merci de corriger les champs signales.")
    else:
        form = ContactRequestForm()
    return render(request, "inquiries/contact.html", {"form": form})


def contact_success(request):
    return render(request, "inquiries/contact_success.html")


def quote_request(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote_request_obj = form.save()
            notify_team(
                f"Nouvelle demande de devis HUSB: {quote_request_obj.company}",
                (
                    f"Contact: {quote_request_obj.first_name} {quote_request_obj.last_name}\n"
                    f"Entreprise: {quote_request_obj.company}\n"
                    f"Fonction: {quote_request_obj.job_title or '-'}\n"
                    f"Email: {quote_request_obj.email}\n"
                    f"Telephone: {quote_request_obj.phone}\n"
                    f"Ville: {quote_request_obj.city}\n"
                    f"Materiel: {quote_request_obj.product_interest}\n"
                    f"Quantite: {quote_request_obj.quantity or '-'}\n"
                    f"Formation souhaitee: {'oui' if quote_request_obj.training_required else 'non'}\n\n"
                    f"Usage:\n{quote_request_obj.usage_description}\n\n"
                    f"Message:\n{quote_request_obj.additional_message or '-'}"
                ),
                settings.QUOTE_RECIPIENT_EMAIL,
            )
            messages.success(request, "Votre demande de devis materiel a bien ete enregistree.")
            return redirect("inquiries:quote_success")
        messages.error(request, "Merci de corriger les champs signales.")
    else:
        form = QuoteRequestForm()
    return render(request, "inquiries/quote_request.html", {"form": form})


def quote_success(request):
    return render(request, "inquiries/quote_success.html")
