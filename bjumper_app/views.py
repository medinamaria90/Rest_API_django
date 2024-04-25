from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db import IntegrityError  # Import IntegrityError
import json
from .github_api import GitHubAPI
from .models import GithubUser, GithubRepositories
from .serializer import GetSerializer, UserSerializer, GetRepoSerializer
import os

access_token = os.getenv('GITHUB_ACCESS_TOKEN')


def user_found_msj(user):
    return (f"User {user.username} has been found and saved in the DB")


def look_for_user_in_github(username):
    github_object = GitHubAPI(access_token)
    user_info = github_object.get_user_info(username)
    print(user_info)
    if user_info:
        return GithubUser(
            username=user_info["login"],
            github_url=user_info["html_url"],
            avatar_url=user_info["avatar_url"],
            public_repos=user_info["public_repos"],
        )


def look_for_repos_in_github(username):
    github_object = GitHubAPI(access_token)
    user_repos = github_object.get_user_repos(username)
    try:
      for repo in user_repos:
        user_object, created = GithubRepositories.objects.get_or_create(
            repo_user=username,
            name=repo["name"],
            repo_link=repo["url"]
        )
        user_object.save()
      return True
    except Exception as e:
        print(f"Error updating user record: {e}")
        return False
    return (False)


@api_view(['GET'])
def getData(request):
    username = request.query_params.get('username')
    if not username:
        return Response({'error': 'Missing username in query parameters'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = GithubUser.objects.get(username=username)
        user_serializer = GetSerializer(user)
        return Response(user_serializer.data)
    except GithubUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def getReposData(request):
    username = request.query_params.get('username')
    print(f"Username received: {username}")  # Log the received username
    if not username:
        return Response({'error': 'Missing username in query parameters'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        repos = GithubRepositories.objects.filter(repo_user=username).all()
        print(repos.count())
        repo_serializer = GetRepoSerializer(repos, many=True)  # Set many=True to serialize multiple objects
        return Response(repo_serializer.data)
    except Exception as e:
        return Response({'error': f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def postData(request):
    post_type = request.data.get('post_type')
    username = request.data.get('username')
    if not username or not post_type:
        return Response({'error': 'Missing username or post_type in request data'}, status=status.HTTP_400_BAD_REQUEST)
    if post_type == 'saveUser':
        user = look_for_user_in_github(username)
        if user:
            try:
                user_object, created = GithubUser.objects.get_or_create(
                    username=user.username,
                    defaults={
                        'github_url': user.github_url,
                        'avatar_url': user.avatar_url,
                        'public_repos': user.public_repos,
                    }
                )
                if not created:
                    return Response({'error': 'User already exists in the database'}, status=status.HTTP_409_CONFLICT)
                json_data = json.dumps(user_found_msj(user))
                return Response(json_data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if 'username' in str(e):
                    return Response({'error': 'Username already exists. Please choose a different one.'}, status=status.HTTP_409_CONFLICT)
                else:
                    return Response({'error': f"There was an unexpected database error: {e}"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as excp:
                return Response({'error': f"An unexpected error occurred: {excp}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    elif post_type == 'deleteUser':
        try:
            user_count = GithubUser.objects.filter(username=username).count()
            if user_count == 0:
                return Response({'error': 'User not found in the database'}, status=status.HTTP_404_NOT_FOUND)
            GithubUser.objects.filter(username=username).delete()
            return Response({'message': f"User with username '{username}' deleted successfully, (if there was something to delete.)."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"An error occurred while deleting the user: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif post_type == 'saveRepos':
        try:
            user_count = GithubUser.objects.filter(username=username).count()
            if user_count == 0:
                return Response({'error': 'User not found in the database'}, status=status.HTTP_404_NOT_FOUND)
            user_repos = look_for_repos_in_github(username)
            print("got the repos!")
            if user_repos == True:
                return Response({'message': f"Repos saved in the DB."}, status=status.HTTP_200_OK)
            if user_repos == False:
                return Response({'error': f"An error occurred saving the data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': f"An error occurred saving the data: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif post_type == 'deleteRepos':
        try:
            user_count = GithubUser.objects.filter(username=username).count()
            if user_count == 0:
                return Response({'error': 'User not found in the database'}, status=status.HTTP_404_NOT_FOUND)
            GithubRepositories.objects.filter(repo_user=username).delete()
            return Response({'message': f"Repos has been deleted from DB, (if there was something to delete)."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f"An error occurred saving the data: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user = look_for_user_in_github(username)
        if user:
            try:
                user_object, created = GithubUser.objects.get_or_create(
                    username=user.username,
                    defaults={
                        'github_url': user.github_url,
                        'avatar_url': user.avatar_url,
                        'public_repos': user.public_repos,
                    }
                )
                if not created:
                    return Response({'error': 'User already exists in the database'}, status=status.HTTP_409_CONFLICT)
                json_data = json.dumps(user_found_msj(user))
                return Response(json_data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if 'username' in str(e):
                    return Response({'error': 'Username already exists. Please choose a different one.'}, status=status.HTTP_409_CONFLICT)
                else:
                    return Response({'error': f"There was an unexpected database error: {e}"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as excp:
                return Response({'error': f"An unexpected error occurred: {excp}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({'error': 'Invalid post type'}, status=status.HTTP_400_BAD_REQUEST)

