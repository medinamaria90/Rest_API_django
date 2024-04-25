This is app that works with a Django REST API that helps doing the following things:
- Add a github user to our DataBase (if the user exist) --> localhost/post/ ---> {"username":"medinamaria90", "post_type":"saveUser"}
- Delete an user from our Database --> localhost/post/ --> {"username":"medinamaria90", "post_type":"deleteUser"}
- Add a copy of the repos names and links of an user already included in our DataBase, in other table (Only works if the user has been added before). localhost/post/ --> {"username":"medinamaria90", "post_type":"saveRepos"}
- Delete the copy of the repos of an User --> localhost/post/ --> {"username":"medinamaria90", "post_type":"deleteRepos"}
- Get the info of an user --> localhost/?username=medinamaria90
- Get the repos of an user--> localhost/repos/?username=medinamaria90

HOW TO USE

- Clone the repository
- Install the requirements.txt (pip install -r requirements.txt)
- add a .env file with your own GITHUB_ACCESS_TOKEN, or add it directly to the variable in views.py (not recomended)
- move to the directory where manage.py is --> python manage.py runserver

- --> To test POSTS (changes in our database) go to the localhost/post
- --> To test the GETS, first make some posts, and then, try localhost/?username=medinamaria90 or localhost/repos/?username=medinamaria90
