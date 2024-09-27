
# Inventory Management System

This is an Inventory Management System built using Django and Django Rest Framework. The project provides endpoints to manage items and user authentication using JWT tokens.

## Features

- User registration and authentication using JWT.
- Create, Retrieve, Update, and Delete operations on inventory items.
- Caching of retrieved items for faster access.

## Installation

### Prerequisites
- Python 3.8 or above
- pipenv for managing virtual environments

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/inventory_management.git
   cd inventory_management
   ```

2. **Install the dependencies using pipenv:**
   If pipenv is not installed, you can install it by running:
   ```bash
   pip install pipenv
   ```

   Then, install the project dependencies:
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

4. **Create a `.env` file in the project root directory** and add the following environment variables:

   ```bash
   # .env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Set up the database:**
   If using PostgreSQL, ensure that your PostgreSQL service is running and a database is created. Update the database configuration in your `.env` file.

   Run the following commands to migrate the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```


6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

### API Endpoints

#### 1. User Registration
- **POST** `/api/register/`
```bash
curl --silent --location --request POST 'http://127.0.0.1:8000/api/register/' --header 'Content-Type: application/json' --data '{"username":"name","password":"password"}'
  ```
- Response: 
  ```json
  {
      "status": "User created"
  }
  ```

#### 2. user login 
- **POST** `/api/login/`
```bash
curl --silent --location --request POST 'http://127.0.0.1:8000/api/login/' --header 'Content-Type: application/json' --data '{"username":"name","password":"password"}'
```

response:
```json
{
    "refresh": "refresh key",
    "access": "access key"
}
```


#### 3. Item Create
- **POST** `/items/`
- Requires authentication (JWT token).    example: 'Authorization: Bearer +{access}
```bash
curl --silent --location --request POST 'http://127.0.0.1:8000/api/items/' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDI2NjE1LCJpYXQiOjE3Mjc0MjMwMTUsImp0aSI6IjFhZDA0Yjk5NDllNDRjNTRhMmMzZDczNDkzYzZlYTAwIiwidXNlcl9pZCI6MX0.BxjhT9LPQkEGfmn08-6hMCrb7b-ZlZJ6bCQOMrgpxOg' --header 'Content-Type: application/json' --data '{"name":"bat","price":"160"}'
```

#### 4. Item Retrieve
- **GET** `/items/{item_id}/`
- Requires authentication (JWT token).   example: 'Authorization: Bearer +{access}

```bash
curl --silent --location --request GET 'http://127.0.0.1:8000/api/items/1' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDI2NjE1LCJpYXQiOjE3Mjc0MjMwMTUsImp0aSI6IjFhZDA0Yjk5NDllNDRjNTRhMmMzZDczNDkzYzZlYTAwIiwidXNlcl9pZCI6MX0.BxjhT9LPQkEGfmn08-6hMCrb7b-ZlZJ6bCQOMrgpxOg' --header 'Content-Type: application/json'
```

#### 5. Item Update
- **PUT** `/items/{item_id}/`
- Requires authentication (JWT token).   example: 'Authorization: Bearer +{access}
```bash
curl --silent --location --request PUT 'http://127.0.0.1:8000/api/items/1/' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDI2NjE1LCJpYXQiOjE3Mjc0MjMwMTUsImp0aSI6IjFhZDA0Yjk5NDllNDRjNTRhMmMzZDczNDkzYzZlYTAwIiwidXNlcl9pZCI6MX0.BxjhT9LPQkEGfmn08-6hMCrb7b-ZlZJ6bCQOMrgpxOg' --header 'Content-Type: application/json' --data '{"name":"bat","price":"120"}'
  ```

#### 6. Item Delete
- **DELETE** `/items/{item_id}/`
- Requires authentication (JWT token).   example: 'Authorization: Bearer +{access}

```bash
curl --silent --location --request DELETE 'http://127.0.0.1:8000/api/items/1/' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDI2NjE1LCJpYXQiOjE3Mjc0MjMwMTUsImp0aSI6IjFhZDA0Yjk5NDllNDRjNTRhMmMzZDczNDkzYzZlYTAwIiwidXNlcl9pZCI6MX0.BxjhT9LPQkEGfmn08-6hMCrb7b-ZlZJ6bCQOMrgpxOg' --header 'Content-Type: application/json'
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
