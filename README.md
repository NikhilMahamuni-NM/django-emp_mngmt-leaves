# django-emp_mngmt-leaves
Django App for Leaves Applications

## Table of contents
* [General info](#Info)
* [Modules](#Modules)
* [Running the Project](#Setup)

## Info
This App is about Applying leaves by the employees which is managed by the manager while the admin keeps track of all the processes. 
	
## Modules
This Django application  is created with:
* Python
* Django
* Django Modules

## Setup
To run this App, first install the required modules by running the following command
```
$ pip install -r requirements.txt
```
After the Setting up the environment, it’s time to configure the Django app. Now run the following commands:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
After the migrations, create the super user for the webapp using the following command:
```
$ python manage.py createsuperuser
```
Fill the required details and then the superuser will be created for our webapp.
Now it’s time to run our web app. Run the following command.
```
$ python manage.py runserver
```
Now go to the browser and enter http://127.0.0.1:8000/ in the url tab.

Now login in using the username and password entered during creating superuser(admin).
![Login Page](/Screenshots/login-page.png)
Following is the admin page for our webapp.
As admin, add the employees and the managers using the links given in the Admin Dashboard.
![Admin Page](/Screenshots/admin-dashboard.png)
Now you can logout of admin and login as Employee and manager using the credentials created by admin.
When logged in as Employee, you can apply for leave and check the status of leave application.
![Employee Dashboard](/Screenshots/emp-dashboard.png)
And when logged in as Manager, you can apply for leave, check the status of leave application and also approve the leaves of employees.
![Manager Dashboard](/Screenshots/mngr-dashboard.png)
When logged in as Admin, you can check the leave applications of all employees and managers and check their status, and can also make changes done by the manager or directly approve the leaves of the employees and manager.
