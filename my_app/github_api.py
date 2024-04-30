# github_api.py
import requests
from .models import GithubUser, GithubRepositories

class GitHubAPI:
  def __init__(self, access_token):
    self.access_token = access_token
    self.base_url = "https://api.github.com"

  def get_user_info(self, username):
    url = f"{self.base_url}/users/{username}"
    headers = {"Authorization": f"Bearer {self.access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      user_info = response.json()
      print("I got the info!!")
      print(user_info)
      return GithubUser(
            username=user_info["login"],
            github_url=user_info["html_url"],
            avatar_url=user_info["avatar_url"],
            public_repos=user_info["public_repos"],
        )
    else:
      print(f"Error: {response.status_code} - {response.text}")
      return None
  
  def get_user_repos(self, username):
    url = f"{self.base_url}/users/{username}/repos"
    headers = {"Authorization": f"Bearer {self.access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos_data = response.json()
        users_repos = []
        for repo in repos_data:
          user_object, created = GithubRepositories.objects.get_or_create (
            repo_user=username,
            name=repo["name"],
            repo_link=repo["url"]
          )
          users_repos.append(user_object)
        return users_repos
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False
     
      

        
  


