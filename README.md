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
<img width="656" height="367" alt="Brower_example" src="https://github.com/user-attachments/assets/c151a3d8-1093-411a-a5fc-ce3cf4a415b8" />
<img width="530" height="395" alt="Success_Reporters" src="https://github.com/user-attachments/assets/50e03a74-d2dc-4e94-b79f-1b931000148f" />
<img width="539" height="409" alt="Bad_request_reporters" src="https://github.com/user-attachments/assets/a8ab1d5a-0664-4987-872b-22f5e0cbe6b4" />
<img width="538" height="461" alt="Success_issues" src="https://github.com/user-attachments/assets/829e7669-7236-4701-a3a5-8c2c461a4dab" />
<img width="538" height="350" alt="Failure_issues" src="https://github.com/user-attachments/assets/6f907f32-1572-43ab-b0c8-9394607bb9e9" />
<img width="536" height="344" alt="Get_Reporters" src="https://github.com/user-attachments/assets/796c0c10-f2d9-4019-9f95-2704ecf96a14" />
<img width="538" height="410" alt="Get_Issues" src="https://github.com/user-attachments/assets/a587a034-ea24-4cc8-9224-9ca543ee3ccd" />
<img width="534" height="396" alt="Get_Reporter_by_ID" src="https://github.com/user-attachments/assets/8a8d27ea-dc73-40f6-b722-861827a8b671" />
<img width="533" height="394" alt="Get_Issues_by_Status" src="https://github.com/user-attachments/assets/1d3594c2-9c29-4655-be04-33cd33849bfc" />
<img width="656" height="367" alt="Brower_example" src="https://github.com/user-attachments/assets/7183d11b-f0fb-4c8d-b56c-1d261221638a" />
<img width="533" height="394" alt="Get_Issues_by_Status" src="https://github.com/user-attachments/assets/e3865d4c-f77f-40b4-827a-56554b00666b" />
