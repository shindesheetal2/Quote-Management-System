# Quote Management System (QMS)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Configuration](#configuration)


## Installation
To run the Quote Management System project locally, follow these steps:

1. Clone the repository:

   git clone https://github.com/shindesheetal2/Quote-Management-System.git
   cd QMS

2. Create a virtual environment:

    python -m venv env
    source env/bin/activate   # For Linux/Mac
    env\Scripts\activate      # For Windows

    pip install -r requirements.txt

3. Install dependencies:

    pip install -r requirements.txt

4. Apply migrations to create the SQLite database:

    python manage.py migrate

5. Run the development server:
     
    python manage.py runserver

6. Access the admin page of Quote Management System in your web browser at http://127.0.0.1:8000/admin

7. Perform CRUD (Create, Read, Update, Delete) operations on quotes using Postman:
    - Install Postman.
    - Start the Django development server if it's not already running.
    - Use Postman to send requests to the API endpoints and verify their functionality.
    - Access postman collection file provided with project, `QMS.postman_collection.json`


## Usage
To use the Quote Management System, follow these steps:

1. Use API client Postman to interact with the Quote Management System's API endpoints.
2. User can perform the following operations on quotes directly without authentication:
   - View a list of all quotes.
   - Retrieve a specific quote by its ID.
3. Create a valid JWT token to access protected endpoints (see [Authentication](#authentication) section for details).
4. User can perform the following operations on quotes after JWT Authentication:
    - Create a new quote.
    - Update an existing quote.
    - Delete a quote.

## API Endpoints
The Quote Management System provides the following API endpoints:

- `/api/listQuotes/`: GET - Retrieve a list of all quotes.
- `/api/getSingleQuote/<int:pk>`: GET - Retrieve a specific quote by its ID.
- `/api/createQuote/`: POST - Create a new quote.
- `/api/updateQuote/<int:pk>`: PUT/PATCH - Update an existing quote by its ID.
- `/api/deleteQuote/<int:pk>`: DELETE - Delete a quote by its ID.

## Authentication
The Quote Management System uses token-based authentication provided by Django REST Framework's JWT authentication. To authenticate and access protected endpoints, follow these steps:

1. Obtain a JWT token by sending a POST request to the token endpoint (`/api/token/`) with valid user credentials (username and password).
    User will get pair of access token and refresh token

    In postman POST request,  body(in form-data) section provide username and password
    sample username = "test_user" , password = "user_123"

2. Aceess protected endpoints by providing Access token
    
   In postman, headers section provide 
   key as `Authorization` and value as Bearer ObtainedAccessToken 

3. The token expires after a certain period (default is set to 1 minutes), so ensure you refresh the token using the token refresh endpoint (`/api/token/refresh/`) before it expires.

    In postman POST request, body(in form-data) section provide 
    key as `refresh` and value as refresh ObtainedRefreshToken 

    Use this new access token for protected endpoints


## Configuration

The Quote Management System project can be configured using the following settings:

1. **Django Settings**: The project's settings are defined in the `QMS/settings.py` file. This includes configuration opModify this file to customize the behavior of the Django project.

2. **Database Configuration**: The project is configured to use SQLite as the database backend. Database schema and records can be accessed from `QMS.sqlite3`

3. **Authentication**: Token-based authentication using JWT is implemented in the project.



    
