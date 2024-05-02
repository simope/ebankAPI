# eBank API project

Work in progress.

I started this project to learn and practice with FastAPI and PostgreSQL. The plan is to have an API that accesses a DB with information about currency transactions between users and users themselves.

### API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /users | List the users present in the DB |
| POST | /users | Create a new user |
| GET | /users/id | Find user with a specific id |
| DELETE | /users/id | Delete user with a specific id |
| POST | /transfer | Create a new transfer |


## Testing
Open the terminal, change directory to the root of the project and launch the tests with:

    pytest -v