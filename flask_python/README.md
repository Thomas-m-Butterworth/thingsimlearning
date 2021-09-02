# Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

## What Am I Doing?
I will create a simple template which allows users to log in and out, and has those credentials stored. This template will become the base of any projects I make for *Social Distance Warriors*, *(No) Money in the Bank*, or any personal project that needs a home on web.

After I have achieved this in Flask. I will move on to the basics of **Django**.

## Packges to install
    pip install flask
    pip install flask-login
    pip install flask-sqlalchemy

## Creating Routes & Views
Standard routes are stored in *views.py*. These routes are the pages that can be accessed by the user (unless they are related in authentication (e.g a login page). In this case they are located in *auth.py*)

 ```from flask import``` 
 
 Blueprints allow us to organise and define our pages, allowing them to be defined and accessed from multiple files, rather than one master file. This is much better for organisation. It's essentially a sitemap. *views.py* and *auth.py* should have the same import structure to define the blueprint, but be named appropiately.

    ## views.py
    from flask import Blueprint

    views = Blueprint("views", __name__)  # Define the blueprint. Name of it is the argument.

    ## auth.py
    from flask import Blueprint

    auth = Blueprint("auth", __name__)  # Appropiately altered variable name.

Once views are established, they must be added to the \___init\___ file.

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

### auth.py
The home of authentication routes. (login pages etc.)

## Templates, Jinja, and Rendering HTML
HTML is kept in the templates folder. Jinja is the templating language used with Flask. This allows us to use python in our HTML, reducing the need for JS. This code is contained with a {% %} tag. e.g:
```<title>{% block title %}Home{% endblock %}</title>```
This inserts block that changes the title dependant on the child template.

**base.html** is the base template that every page is based on. Further templates will override and add into the base. e.g (from *home.html*)
```{%extends "base.html"%} {% block title %}NMitB Project Hub{% endblock %}```

The above code extends the template into home bage, the block action afterwards replaces the blocks with the same name.

### Variables
Jinja allows us to pass pythonic variables within a template, to output different results.