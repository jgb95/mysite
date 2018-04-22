from django.shortcuts import render
from jobs.models import Job


def index(request):
    jobs = Job.objects.all()[:10]
    context = {
        'title': 'Job Listings',
        'jobs': jobs
    }
    return render(request, 'jobs/index.html', context)


def details(request, id):
    job = Job.objects.get(id=id)
    context = {
        'job': job
    }
    return render(request, 'jobs/details.html', context)
