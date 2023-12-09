# DIPEAT FOOD PRIVATE LIMITED ASSIGNMENT

In this assignment, we have created **Django REST Framework** project that enables the User registeration and login using the **Token Authentication** system.

### Getting Started

1. Open the project directory:

```
cd dipear foods private limited
```

2. Create a new virtual environment:

```
# Let's first install the pipenv
pip install pipenv

#Now create the virtual environment
pipenv shell
```

3. Activate the environment:

```
# when called in the same directory as where virtual env is created,
# then it activates the virtual env
pipenv shell
```

4. Install the requirements:

```
pipenv install -r requirements.txt
```

5. Run Migrations:

```
py manage.py migrate
```

### Run the App

Start the server

```
py manage.py runserver
```

⚠ Then, the development server will be started at `http://127:8000/`

### Features

1. This project uses the **DRF** Token Authentication.
2. It has a `Forget Password` endpoint, from which user can reset their password.
3. It has a `User Profile` endpoint, from which user can make their profile and save it.
4. In this project the `Class based Views` are used.

All the API endpoints are tested.

### API Testing Vedio

To see how the api are tested open the vedio linked: [API Testing](https://github.com/Vikuuu/DRF-Token-Authentication/blob/main/API%20Tesiting.mp4)
