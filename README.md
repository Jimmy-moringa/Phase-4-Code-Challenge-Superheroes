
# Superheroes API

This project is a Flask-based API for tracking superheroes and their powers. It allows users to retrieve and manage heroes, their powers, and the associations between them. The API supports full CRUD operations and follows RESTful conventions.

## Table of Contents
- [Setup](#setup)
- [Models](#models)
- [Validations](#validations)
- [Routes](#routes)
- [Testing with Postman](#testing-with-postman)
- [Future Improvements](#future-improvements)
- [License](#license)

## Setup

### Requirements
- Python 3.8+
- Flask
- SQLAlchemy
- Marshmallow (for serialization)
- Flask-Migrate (for handling database migrations)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/superheroes-api.git
   cd superheroes-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Seed the database (optional, if using seed data):
   ```bash
   python seed.py
   ```

6. Run the Flask server:
   ```bash
   flask run
   ```

## Models

- **Hero**: Represents a superhero with attributes such as name and super_name.
- **Power**: Represents a superpower with attributes like name and description.
- **HeroPower**: A join model representing the relationship between a hero and a power, with an additional attribute for `strength` (can be 'Strong', 'Weak', or 'Average').

## Validations
- **HeroPower**:
  - `strength` must be one of the following values: 'Strong', 'Weak', 'Average'.
  
- **Power**:
  - `description` must be present and at least 20 characters long.

## Routes

### Heroes

- **GET /heroes**  
  Returns a list of all heroes.
  ```json
  [
    {
      "id": 1,
      "name": "Kamala Khan",
      "super_name": "Ms. Marvel"
    },
    {
      "id": 2,
      "name": "Doreen Green",
      "super_name": "Squirrel Girl"
    }
  ]
  ```

- **GET /heroes/:id**  
  Returns a specific hero with associated powers.
  ```json
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel",
    "hero_powers": [
      {
        "hero_id": 1,
        "power": {
          "id": 2,
          "name": "flight",
          "description": "gives the wielder the ability to fly"
        },
        "strength": "Strong"
      }
    ]
  }
  ```

### Powers

- **GET /powers**  
  Returns a list of all powers.
  ```json
  [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    },
    {
      "id": 2,
      "name": "flight",
      "description": "gives the wielder the ability to fly"
    }
  ]
  ```

- **PATCH /powers/:id**  
  Updates an existing power's description.
  ```json
  {
    "id": 1,
    "name": "super strength",
    "description": "Updated Description"
  }
  ```

### Hero Powers

- **POST /hero_powers**  
  Assigns a power to a hero with a specific strength level.
  ```json
  {
    "id": 11,
    "hero_id": 3,
    "power_id": 1,
    "strength": "Average",
    "hero": {
      "id": 3,
      "name": "Gwen Stacy",
      "super_name": "Spider-Gwen"
    },
    "power": {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    }
  }
  ```

## Testing with Postman

1. Download and install [Postman](https://www.postman.com/downloads/).
2. Import the provided Postman collection to test all API endpoints.
3. Ensure that your API is running, and use the requests in the collection to verify that each route works as expected.

## Future Improvements
- Add authentication and authorization for managing heroes and powers.
- Implement pagination for large datasets.
- Improve error handling and add more detailed validation error messages.

## License
This project is licensed under the MIT License.
