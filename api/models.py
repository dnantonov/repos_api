from django.db import models


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=250)
    node_id = models.CharField(max_length=250)

    def __str__(self):
        return f'user: {self.login}'


class Repo(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    private = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    html_url = models.URLField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'repository: {self.name}'
