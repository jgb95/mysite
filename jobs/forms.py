from django import forms
from jobs import models

class PostNewJobForm(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = [
            'title',
            'job_description',
            'company'
        ]

    def __init__(self, *args, **kwargs):
        super(PostNewJobForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={
            'placeholder': 'Eg. Cashier'
        })
        self.fields['job_description'].widget = forms.Textarea(attrs={
            'placeholder': 'A brief description of the duties of the job',
            'class': 'materialize-textarea'
        })

