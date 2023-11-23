from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=50, help_text='The name of the candidate')
    website = models.URLField(help_text='The candidate\'s website')
    email = models.EmailField(help_text='The candidate\'s email address')

    def __str__(self):
        return self.name