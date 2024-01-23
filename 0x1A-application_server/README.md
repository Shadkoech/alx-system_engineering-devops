# 0x1A. Application server

This project is on further confirguring my server web-01. Initially Nginx was already installed as a web-server in order to serve static files. This folder entails the step by step process of installing an application server to serve dynamic content. 

## Task 0: Set up development with Python

This task is an exercise in setting up the development environment that will be used for testing and debugging code well before deploying it to production
Requirements:
* Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
* Install the net-tools package on your server: sudo apt install -y net-tools
* Git clone your AirBnB_clone_v2 on your web-01 server.
* Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
* Your Flask application object must be named app (This will allow us to run and check your code).



## Task 1: Set up production with Gunicorn

Setting up the production environment with Gunicorn on web-01, port 5000. Gunicorn is installed together with other libraries needed by the application. Flask application object will serve as a WSGI entry point into your application
Requirements:
* Install Gunicorn and any other libraries required by your application.
* The Flask application object should be called app.
* You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
* In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.
