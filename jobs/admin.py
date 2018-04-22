from django.contrib import admin

from jobs.models import Company, Job, User

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(User)
