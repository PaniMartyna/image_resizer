# A simple REST API for resizing images.

### How to run:

1. clone the repository into a folder with virtual env
2. install all required packages
    `pip install -r requirements.txt`
3. connect to a database
4. migrate `python manage.py migrate`
5. create admin `python manage.py createsuperuser`
6. run the server `python manage.py runserver`
7. go to /admin and log in as admin
8. create new users and assign their subscription plans (automatically when a user is created, they get the Basic Plan)
9. as and admin you can crete new subscription plans

### endpoints:

| method    | endpoint              | description              |
|-----------|-----------------------|--------------------------|
| GET       | api/images/           | List all users' pictures |
| POST      | api/images            | Upload a picture         |
| GET       | api/images/{image_id} | Get image details        |
| PUT/PATCH | api/images/{image_id} | Change picture name      |
| DELETE    | api/images/{image_id} | Delete picture           |






