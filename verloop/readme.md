# Documentation:

- Uses Django 2.2.2

## Question ID: 0d91dac2a3b14cde91a29326cb12dd06

## Instructions to run:

- Must have python3 and pip installed
- navigate to folder with requirements.txt and execute 'pip install requirements.txt'
- navigate to folder with manage.py
- execute 'python3 manage.py makemigrations'
- execute 'python3 manage.py migrate'
- execute 'python3 manage.py runserver'
- visit http://127.0.0.1:8000/repos on your browser

## Structure:

- views.py in api folder inside verloopapp folder contains the view/logic
- urls.py takes care of routing

## Feature:

- Tested using Postman
- POST request format:

{
"org": "github-organization-id"
}

- Example:

{
"org":"31602251"
}

- Response:

{
"results": [
{"name":"rick", "stars": 100},
{"name":"morty", "stars": 98},
{"name":"jerry", "stars":2},
]
}
