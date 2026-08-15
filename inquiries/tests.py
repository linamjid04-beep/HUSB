from django.test import TestCase
from django.urls import reverse

from .forms import ContactRequestForm, QuoteRequestForm
from .models import ContactRequest, QuoteRequest


class ContactRequestTests(TestCase):
    def valid_payload(self):
        return {
            "first_name": "Sara",
            "last_name": "Amrani",
            "company": "Entreprise test",
            "email": "sara@example.com",
            "phone": "0600000000",
            "subject": "Demande d'information",
            "message": "Bonjour, ceci est un test.",
            "consent": "on",
            "website": "",
        }

    def test_valid_contact_form_is_saved(self):
        response = self.client.post(reverse("inquiries:contact"), self.valid_payload())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactRequest.objects.count(), 1)

    def test_contact_honeypot_blocks_spam(self):
        payload = self.valid_payload()
        payload["website"] = "https://spam.example"
        response = self.client.post(reverse("inquiries:contact"), payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactRequest.objects.count(), 0)

    def test_invalid_contact_form_is_refused(self):
        payload = self.valid_payload()
        payload["email"] = "adresse-invalide"
        form = ContactRequestForm(data=payload)
        self.assertFalse(form.is_valid())

    def test_contact_consent_is_required(self):
        payload = self.valid_payload()
        payload.pop("consent")
        form = ContactRequestForm(data=payload)
        self.assertFalse(form.is_valid())
        self.assertIn("consent", form.errors)


class QuoteRequestTests(TestCase):
    def valid_payload(self):
        return {
            "first_name": "Yassine",
            "last_name": "Idrissi",
            "company": "Fibre Test",
            "job_title": "Technicien",
            "email": "yassine@example.com",
            "phone": "0611111111",
            "city": "Rabat",
            "product_interest": "Soudeuse fibre optique",
            "quantity": "1",
            "usage_description": "Besoin de demonstration pour devis.",
            "training_required": "on",
            "additional_message": "Message complementaire.",
            "consent": "on",
            "website": "",
        }

    def test_valid_quote_form_is_saved(self):
        response = self.client.post(reverse("inquiries:quote_request"), self.valid_payload())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(QuoteRequest.objects.count(), 1)
        self.assertEqual(QuoteRequest.objects.first().status, QuoteRequest.STATUS_NEW)

    def test_quote_quantity_validation(self):
        payload = self.valid_payload()
        payload["quantity"] = "0"
        form = QuoteRequestForm(data=payload)
        self.assertFalse(form.is_valid())
        self.assertIn("quantity", form.errors)

    def test_quote_form_is_distinct_from_contact(self):
        self.assertNotEqual(set(ContactRequestForm.Meta.fields), set(QuoteRequestForm.Meta.fields))

    def test_quote_consent_is_required(self):
        payload = self.valid_payload()
        payload.pop("consent")
        form = QuoteRequestForm(data=payload)
        self.assertFalse(form.is_valid())
        self.assertIn("consent", form.errors)
