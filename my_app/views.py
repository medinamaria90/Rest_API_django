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
from dotenv import load_dotenv
import os

# Add your own access token
load_dotenv()
access_token = os.getenv("GITHUB_ACCESS_TOKEN")
github_object = GitHubAPI(access_token)

# This is the view/API for gettin the username info


@api_view(['GET'])
def get_user(request, username):
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
def get_repos(request, username):
    if not username:
        return Response({'error': 'Missing username in query parameters'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        repos = GithubRepositories.objects.filter(repo_user=username).all()
        repo_serializer = GetRepoSerializer(repos, many=True)
        return Response(repo_serializer.data)
    except Exception as e:
        return Response({'error': f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def save_user(request):
    username = request.data.get('username')
    if not username:
        return Response({'error': 'Missing username'}, status=status.HTTP_400_BAD_REQUEST)
    user = GithubUser.objects.filter(username=username)
    if user:
        print(user)
        return Response({'error': 'User already exists in the database'}, status=status.HTTP_409_CONFLICT)
    user = github_object.get_user_info(username)
    if user:
        try:
            print("Going to save user (and break the code)")
            user.save()
            json_data = json.dumps(
                f"User {user.username} has been found and saved in the DB")
            return Response(json_data, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'There was an unexpected database error'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'User not found in GitHub'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save_repos(request):
    username = request.data.get('username')
    if not username:
        return Response({'error': 'Missing username'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = GithubUser.objects.filter(username=username)
        if user == False:
            return Response({'error': 'User not found in the database'}, status=status.HTTP_404_NOT_FOUND)
        user_repos = github_object.get_user_repos(username)
        print(user_repos)
        if user_repos:
            try:
                for repo in user_repos:
                    repo.save()
            except:
                return Response({'message': f"Error saving data."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': f"Repos saved in the DB."}, status=status.HTTP_200_OK)
        else:
            return Response({'error': f"No repos for this user"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'error': f"An error occurred saving the data: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_user(request, username):
    if not username:
        return Response({'error': 'Missing username'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_count = GithubUser.objects.filter(username=username).count()
        if user_count == 0:
            return Response({'error': 'User not found in the database'}, status=status.HTTP_404_NOT_FOUND)
        GithubUser.objects.filter(username=username).delete()
        return Response({'message': f"User with username '{username}' deleted successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f"An error occurred while deleting the user: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_repos(request, username):
    try:
        user_count = GithubUser.objects.filter(username=username).count()
        if user_count == 0:
            return Response({'error': 'Usuario no encontrado en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
        GithubRepositories.objects.filter(repo_user=username).delete()
        return Response({'message': 'Los repositorios han sido eliminados de la base de datos.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Se produjo un error al eliminar los datos: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
