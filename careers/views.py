from django.shortcuts import get_object_or_404, render

from .models import JobOffer


def job_list(request):
    offers = JobOffer.objects.filter(is_active=True)
    return render(request, "careers/job_list.html", {"offers": offers})


def job_detail(request, slug):
    offer = get_object_or_404(JobOffer, slug=slug, is_active=True)
    return render(request, "careers/job_detail.html", {"offer": offer})
