from rest_framework import serializers
from .models import GithubUser, GithubRepositories

class GetSerializer(serializers.ModelSerializer):
	class Meta:
		model=GithubUser
		fields='__all__'
  
class GetRepoSerializer(serializers.ModelSerializer):
	class Meta:
		model=GithubRepositories
		fields='__all__'
  
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubUser
        fields = ('username', 'github_url', 'public_repos_links')  # Only username & URL needed for backup