from django.contrib import admin
from .models import GithubUser, GithubRepositories

# Register your models here.
admin.site.register(GithubUser)
admin.site.register(GithubRepositories)
