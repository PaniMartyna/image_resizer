# A simple REST API for resizing images.

### How to run:

1. fork and clone the repository into a folder with virtual env
2. fill-in .env-default.txt and save as .env
3. install all required packages
    `pip install -r requirements.txt`
4. connect to a database
5. migrate `python manage.py migrate`
6. create admin `python manage.py createsuperuser`
7. run the server `python manage.py runserver`
8. go to /admin and log in as admin
9. create new users and assign their subscription plans (automatically when a user is created, they get the Basic Plan)
10. as and admin (using Django Admin) you can create new subscription plans

### endpoints:

| method    | endpoint              | description              |
|-----------|-----------------------|--------------------------|
| GET       | api/images/           | List all users' pictures |
| POST      | api/images            | Upload a picture         |
| GET       | api/images/{image_id} | Get image details        |
| PUT/PATCH | api/images/{image_id} | Change picture name      |
| DELETE    | api/images/{image_id} | Delete picture           |






