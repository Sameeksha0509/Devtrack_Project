# DevTrack

A Django project for tracking engineering issues.

## Setup

1. Ensure Python and Django are installed.
2. Navigate to the project directory: `cd devtrack`
3. Run the development server: `python manage.py runserver`

## API Endpoints

### Reporters
- **POST /api/reporters/**: Create a new reporter. Body: `{"id": 1, "name": "John Doe", "email": "john@example.com", "team": "backend"}`
- **GET /api/reporters/**: Get all reporters.
- **GET /api/reporters/?id=1**: Get a specific reporter by ID.

### Issues
- **POST /api/issues/**: Create a new issue. Body: `{"id": 1, "title": "Bug title", "description": "Description", "status": "open", "priority": "critical", "reporter_id": 1}`
- **GET /api/issues/**: Get all issues.
- **GET /api/issues/?id=1**: Get a specific issue by ID.
- **GET /api/issues/?status=open**: Get issues filtered by status.

## Design Decision

I chose to store data in JSON files instead of a database for simplicity and to avoid database setup, making the project easy to run without additional dependencies. This allows quick prototyping and testing in Postman.


