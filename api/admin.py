from django.contrib import admin

from api.models import Repo, Owner

admin.site.register(Repo)
admin.site.register(Owner)
