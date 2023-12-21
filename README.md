# Flask-React-SQLAlchemy-PostgreSQL
Simple App I created that uses Python, React, Flask-SQLAlchemy, and PostgreSQL.

The app allows the user to put their name and email in a PostgreSQL database. Their name/email must be unique. The app will allow the user to search if their name exists in the database. 

## Basic Structure of the Code 

PostgreSQL will host the data for the application. The database will have 1 table called "user." This table will have two columns, "username" and "email." Python will be the backend framwork that will allow to do CRUD and ORM operations on the database, allowing us to add and search into the database. The Specific Libraries we will be using in the python code are known as Flask and Flask-SQLAlchemy. Lastly, the frontend will consist of a React App, based in JavaScript, which will allow the user to input their data into the database.


## Backend 

### PostgreSQL

PostgreSQL, often referred to as Postgres, is an advanced, open-source relational database management system (RDBMS). It's known for its robustness, scalability, and support for advanced data types and SQL (Structured Query Language) standards. 

### Web Server Gateway Interface

The Web Server Gateway Interface (WSGI) is a specification in Python that describes a universal interface between web servers and web applications or frameworks. Its primary goal is to facilitate a standard way for web servers to communicate with web applications written in Python. 

### Jinja 

"Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document"

### CLI 

"Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box"

### ORM 
Before we continue, it would be beneficial to learn what ORM is. From wikipedia: "Object–relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between a relational database and the heap of an object-oriented programming language"


### Flask 

Flask is a lightweight web application framework for Python, designed to make it easy to develop the backend for web applications by providing tools, libraries, and technologies for creating web services.

Flask utilizes WSGI, Jinja, and CLI (see descriptions of these above).

You will notice that we will import two other things alongside with flask in the code: requests and jsonify 


### Flask-SQLAlchemy 

SQLAlchemy is a ORM tool. It allows us to interact with the backend database through python syntax and abstract away SQL commands. 

#### URI
You will notice that using Flask-SQLAlchemy, we have to specify something called a URI: 

A URI, or Uniform Resource Identifier, is a string of characters used to identify a resource on the internet or a network. It serves as a generic term for all types of names and addresses that refer to objects on the World Wide Web. A URI provides a simple and extensible means for identifying a resource, whether it's a webpage, a document, an image, or a service.

Specifically for our use case, the URI helps provide the information needed to talk to our PostgresSQL Database.

### CORS

Sometimes the requests get blocked. CORS helps bypass this.

## Frontend 

### React 

React is a Javascript based tool to develop the frontend for web applications

#### Hooks 
React Hooks are functions that let you "hook into" React state and lifecycle features from function components. React Hooks simplify the code, making it easier to use state and other React features without the complexity of classes. They enable better code reuse and composition, leading to cleaner and more intuitive code designs.

### Axios 

Axios is a promise-based HTTP client for making requests to external services.


