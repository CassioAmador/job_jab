from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    doc_id = models.CharField(max_length=255)
    employer_name = models.CharField(max_length=255)
    date_posted = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = "jobs"

    def __str__(self):
        return self.name
