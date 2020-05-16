from django.db import models 
from django.utils import timezone
from datetime import datetime


class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('date started', default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    open_date = models.DateTimeField('date opened', default=datetime.now, blank=True)

    def __str__(self):
        if self.complete:
            return "Closed bug (project " + self.project.name
        else:
            return "Open bug (project " + self.project.name


class Worknote(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    date = models.DateTimeField('date', default=datetime.now, blank=True)

    def __str__(self):
        return self.description
