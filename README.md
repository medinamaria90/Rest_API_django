<b>WHAT IT DOES</b>
This is very simple app that works with a Django REST API, and has the following functionality:

- Add a github user to our DataBase (if the user exist) --> localhost/post/ ---> {"username":"medinamaria90", "post_type":"saveUser"}
- Delete an user from our Database --> localhost/post/ --> {"username":"medinamaria90", "post_type":"deleteUser"}
- Add a copy of the repos names and links of an user already included in our DataBase, in other table (Only works if the user has been added before). localhost/post/ --> {"username":"medinamaria90", "post_type":"saveRepos"}
- Delete the copy of the repos of an User --> localhost/post/ --> {"username":"medinamaria90", "post_type":"deleteRepos"}
- Get the info of an user --> localhost/?username=medinamaria90
- Get the repos of an user--> localhost/repos/?username=medinamaria90

<b>HOW TO USE</b>

- Clone the repository
- Create a virtual enviorment (python -m venv "myenvname") & activate it (source myenvname/bin/activate if you are working in linux/ios)
- Install the requirements.txt (pip install -r requirements.txt)
- add a .env file with your own GITHUB_ACCESS_TOKEN, or add it directly to the variable in views.py (not recomended)
- move to the directory where manage.py is and execute--> python manage.py runserver

- --> To test POSTS (changes in our database) go to the localhost/post
- --> To test the GETS, first make some posts, and then, try localhost/?username=medinamaria90 or localhost/repos/?username=medinamaria90
  
Here some examples:
1. How to save a new user to the DB
![post_save_user](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/ae5c918e-edce-4676-84e7-1fb67a88a362)
<br>
2. How to save an existing user repos data in the DB
![post_save_repo](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/2d44e6fd-fa97-4ea1-a77c-b8f2592c8014)
<br>
3. How to get an user's data (our DB)
![get_user](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/4f6d8ab7-e46d-4f35-9fac-8756272f6854)
<br>
4. How to get an user's repos data (our DB)
![get_repos_user](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/832aed9b-b3ef-4d4f-921e-43aaa54d5c92)


<b>WHAT IT USES</b>
- SQL lite
- Django / Django Rest Framework
