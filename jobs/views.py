from django.shortcuts import render, reverse
from jobs.models import Job
from jobs import forms
from django.http import HttpResponseRedirect


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


def post_new_job(request):
    if request.method == 'POST':
        form = forms.PostNewJobForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('thanks/' + str(instance.pk) + '/')
    else:
        form = forms.PostNewJobForm()
    context = {
        'form': form
    }
    return render(request, 'jobs/postnewjob.html', context)


def thanks(request, id):
    job = Job.objects.get(id=id)
    context = {
        'job': job
    }
    return render(request, 'jobs/thanks.html', context)