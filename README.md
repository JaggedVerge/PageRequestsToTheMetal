# PageRequestsToTheMetal
This repository is the source code that goes with the page request down to the metal article.
Using this will let you follow along with the article.

The original article can be found here: http://www.jaggedverge.com/2017/11/how-a-web-page-request-makes-it-down-to-the-metal/

## Installation
The code requires all the python dependencies in `requirements.txt` to be installed in order to run.

## Running the server
This project uses the django development server.
For this to work we need to have a port opened through the VM if we are using Vagrant.
To do this use `python manage.py runserver 0.0.0.0:8000` to specify the right port to run the server on.
