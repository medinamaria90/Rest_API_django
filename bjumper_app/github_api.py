# github_api.py
import requests

class GitHubAPI:
  def __init__(self, access_token):
    self.access_token = access_token
    self.base_url = "https://api.github.com"

  def get_user_info(self, username):
    url = f"{self.base_url}/users/{username}"
    headers = {"Authorization": f"Bearer {self.access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.json()
    else:
      print(f"Error: {response.status_code} - {response.text}")
      return None
  
  def get_user_repos(self, username):
    url = f"{self.base_url}/users/{username}/repos"
    headers = {"Authorization": f"Bearer {self.access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos_data = response.json()
        for repo in repos_data:
          print("one!")
        return repos_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
  


