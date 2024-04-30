<b>WHAT IT DOES</b>
<br>
This is very simple app that works with a Django REST API, and has the following functionality:

<b> VIEWS </b>
- <b>/save_user</b>: Add a github user to our DataBase, if the user exist. (POST REQUEST)
- <b>/save_repo</b>: Add a backup of the repos names and links of an user already included in our DataBase, in another table. (POST REQUEST)
  
- <b>delete_user/username</b>: Delete an user from our Database (DELETE REQUEST)
- <b>delete_repo/username</b>: Delete the backup of the repos of an User (DELETE REQUEST)
  
- <b>user/username</b> Get the info of an user (GET REQUEST)
- <b>repos/username</b Get the repos of an user (GET REQUEST)

<b>HOW TO USE</b>

- Clone the repository
- Add a .env file with your own GITHUB_ACCESS_TOKEN, with this info --> GITHUB_ACCESS_TOKEN = "youraccesstoken"
- Create a virtual enviorment (python -m venv "myenvname") & activate it (source myenvname/bin/activate if you are working in linux/ios)
- Install the requirements.txt (pip install -r requirements.txt)
- move to the directory where manage.py is and execute--> python manage.py runserver
  
Here some examples:
1. Saving user in the DB
   ![saveUser](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/ec1dc103-c412-4ad0-8117-8434c8d2788b)

<br>
3. Saving user's repo backup in the DB
  ![saveRepos](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/375aa44c-4ec6-40a8-baa3-e00752b19a53)

<br>
3. Get an User's data
![getUser](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/43ddc764-1505-4095-8e22-8bbd01ccb650)

<br>
4. Get User's repos backup data
![getRepos](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/dfcda2e6-a89a-45ca-acf5-4e560c500fbf)

<br>
5. Delete an user from the DB
![deleteUser](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/ebec9bc9-9061-42bb-b2f5-01125505b633)

<br>
6. Delete an user's repo backup from the DB
![deleteRepos](https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/6c9eb705-8dde-40cb-9caa-4f050202f9d3)


<b>WHAT IT USES</b>
- SQL lite
- Django / Django Rest Framework
