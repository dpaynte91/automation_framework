from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    rest_url = models.CharField(max_length=2048)


# Each Credential is associated with a Project
class Credentials(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=200)
    client_secret = models.CharField(max_length=200)
