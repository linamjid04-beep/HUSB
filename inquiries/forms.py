from django import forms

from .models import ContactRequest, QuoteRequest


class HoneypotMixin(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "website":
                continue
            field.widget.attrs.setdefault("autocomplete", "on")
            if field.required:
                field.widget.attrs["required"] = "required"

    def clean_website(self):
        value = self.cleaned_data.get("website")
        if value:
            raise forms.ValidationError("Le formulaire n'a pas pu etre valide.")
        return value


class ContactRequestForm(HoneypotMixin):
    consent = forms.BooleanField(
        required=True,
        label="J'accepte que HUSB utilise ces informations pour repondre a ma demande.",
    )

    class Meta:
        model = ContactRequest
        fields = [
            "first_name",
            "last_name",
            "company",
            "email",
            "phone",
            "subject",
            "message",
            "consent",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 6}),
        }


class QuoteRequestForm(HoneypotMixin):
    consent = forms.BooleanField(
        required=True,
        label="J'accepte que HUSB utilise ces informations pour traiter ma demande de devis.",
    )

    class Meta:
        model = QuoteRequest
        fields = [
            "first_name",
            "last_name",
            "company",
            "job_title",
            "email",
            "phone",
            "city",
            "product_interest",
            "quantity",
            "usage_description",
            "training_required",
            "additional_message",
            "consent",
        ]
        widgets = {
            "usage_description": forms.Textarea(attrs={"rows": 5}),
            "additional_message": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity is not None and quantity < 1:
            raise forms.ValidationError("La quantite doit etre superieure a zero.")
        return quantity
