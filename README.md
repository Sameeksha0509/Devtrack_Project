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
<img width="530" height="395" alt="Success_Reporters" src="https://github.com/user-attachments/assets/ad920b3e-7c91-48c8-a7a6-15dba056eae7" />
<img width="539" height="409" alt="Bad_request_reporters" src="https://github.com/user-attachments/assets/4777f4d9-807d-42f1-a47d-6b29cd8eaec6" />
<img width="538" height="461" alt="Success_issues" src="https://github.com/user-attachments/assets/ea4eb787-4d19-4aa3-9d49-3abb373f0aa7" />
<img width="538" height="350" alt="Failure_issues" src="https://github.com/user-attachments/assets/38191b43-6dcd-44e6-9c57-a9982e19967d" />
<img width="536" height="344" alt="Get_Reporters" src="https://github.com/user-attachments/assets/5ca3b9b7-aaa7-49cc-81da-f0b7834048df" />
<img width="538" height="410" alt="Get_Issues" src="https://github.com/user-attachments/assets/dd62ae39-90d6-47ce-b839-3e824d258ad7" />
<img width="534" height="396" alt="Get_Reporter_by_ID" src="https://github.com/user-attachments/assets/92973738-0068-4e94-a4c1-6a8fdf23122b" />
<img width="533" height="394" alt="Get_Issues_by_Status" src="https://github.com/user-attachments/assets/8f08266a-b232-4d1c-94c5-4226469286be" />
<img width="656" height="367" alt="Brower_example" src="https://github.com/user-attachments/assets/ce00edb7-39d6-4ec9-abee-a154723f58a3" />

