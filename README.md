# Backend-in-FastAPI

A simple CRUD backend application built with FastAPI, SQLAlchemy, and Pydantic.

## Features

- Create, Read, Update, Delete (CRUD) operations for users
- RESTful API endpoints
- SQLAlchemy ORM integration
- Pydantic schema validation

## Project Structure

```
.
├── main.py
├── requirements.txt
├── .gitignore
├── database/
│   └── connection.py
├── models/
│   └── user.py
├── routes/
│   └── user.py
├── schemas/
│   └── user.py
└── services/
    └── user.py
```

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/Bhanu-Sharma-7/Backend-in-FastAPI.git
   cd Backend-in-FastAPI
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the root directory.
   - Add your database URL:
     ```
     DATABASE_URL=postgresql://user:password@localhost/dbname
     ```

5. **Run the application**
   ```sh
   uvicorn main:app --reload
   ```

6. **API Documentation**
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

## Endpoints

- `POST /user` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `PUT /users/{user_id}` - Update user by ID
- `DELETE /users/{user_id}` - Delete user by ID
