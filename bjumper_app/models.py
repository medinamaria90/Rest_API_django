from django.db import models


class GithubUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    github_url = models.CharField(max_length=255, unique=True)
    avatar_url = models.CharField(max_length=255, unique=True, default="")
    public_repos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
      
class GithubRepositories(models.Model):
    repo_user = models.CharField(max_length=255, unique=False)
    name = models.CharField(max_length=255)
    repo_link= models.CharField(max_length=255, unique=True, default="")
    
    def __str__(self):
        return self.repo_user