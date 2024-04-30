
<h1>README</h1>

<h2>WHAT IT DOES</h2>

<p>This is a very simple app that interacts with a Django REST API, providing the following functionality:</p>

<ul>
        <li><b>/save_user</b>: Adds a GitHub user to our database if the user exists. (POST REQUEST)</li>
        <li><b>/save_repo</b>: Adds a backup of the repositories' names and links of a user already included in our database to another table. (POST REQUEST)</li>
        <li><b>/delete_user/username</b>: Deletes a user from our database (DELETE REQUEST)</li>
        <li><b>/delete_repo/username</b>: Deletes the backup of the repositories of a user (DELETE REQUEST)</li>
        <li><b>/user/username</b>: Gets the info of a user (GET REQUEST)</li>
        <li><b>/repos/username</b>: Gets the repositories of a user (GET REQUEST)</li>
    </ul>
<h2>HOW TO USE</h2>

<ol>
        <li>Clone the repository</li>
        <li>Add a .env file with your own GITHUB_ACCESS_TOKEN, with this info --> GITHUB_ACCESS_TOKEN = "youraccesstoken"</li>
        <li>Create a virtual environment (python -m venv "myenvname") & activate it (source myenvname/bin/activate if you are working in Linux/iOS)</li>
        <li>Install the requirements.txt (pip install -r requirements.txt)</li>
        <li>Move to the directory where manage.py is located and execute: python manage.py runserver</li>
    </ol>

<p>Here are some examples:</p>

<ol>
        <li>Saving a user in the DB<br>
            <img src="https://github.com/medinamaria90/bjumper_backend_test/assets/131414823/ec1dc103-c412-4ad0-8117-8434c8d2788b" alt="saveUser" class="example-img">
        </li>
        <li>Saving a user's repo backup in the DB<br>
            <img src="https://github.com/medinamaria90/Rest_API_django/assets/131414823/4c52d92c-9ee3-4380-8d33-809f8999e242" alt="saveRepos" class="example-img">
        </li>
        <li>Getting an User's data<br>
            <img src="https://github.com/medinamaria90/Rest_API_django/assets/131414823/4cfa70e2-c7c4-4cec-9fb6-3d01f0ccc19e" alt="getUser" class="example-img">
        </li>
        <li>Getting User's repos backup data<br>
            <img src="https://github.com/medinamaria90/Rest_API_django/assets/131414823/1cb05e61-d6ee-467d-9b62-91324156f7e4" alt="getRepos" class="example-img">
        </li>
        <li>Deleting a user from the DB<br>
            <img src="https://github.com/medinamaria90/Rest_API_django/assets/131414823/c0905af3-93de-4067-ac32-24b95e24846d" alt="deleteUser" class="example-img">
        </li>
        <li>Deleting a user's repo backup from the DB<br>
            <img src="https://github.com/medinamaria90/Rest_API_django/assets/131414823/9807a287-17e0-4c5b-8056-8f140401e91c" alt="deleteRepos" class="example-img">
        </li>
    </ol>

<h2>WHAT IT USES</h2>
<ul>
        <li>SQLite</li>
        <li>Django / Django Rest Framework</li>
</ul>




<b>WHAT IT USES</b>
- Django / Django Rest Framework
- SQL lite

