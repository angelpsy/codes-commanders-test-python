# Django Application

## 1. Project Overview
This is a Django-based application designed to manage core business logic and provide APIs for various functionalities. It includes modular apps for API handling, status monitoring, and more.

## 2. Setup Instructions
### Prerequisites
- Python 3.10+
- Docker and Docker Compose (optional for containerized setup)

### Local Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements/dev.txt
   ```
3. Create a `.env` file in the root directory to store environment variables. An example can be found in `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with the following database connection details:
   ```
   DB_NAME=shop_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
   Replace `your_password` with the actual password for the PostgreSQL user.

4. Create a PostgreSQL database:
   ```bash
   psql -U postgres -c "CREATE DATABASE shop_db;"
   ```
   Replace `shop_db` with your desired database name if needed.

5. Apply migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```

6. Create a Django superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Docker Setup
1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
2. Access the application at `http://localhost:8000`.

## 3. Folder Structure
- **api/**: Contains the main API logic, including models, views, serializers, and tests.
- **core/**: Holds project-wide settings, configurations, and entry points.
- **status/**: Provides health monitoring and versioning utilities.
- **requirements/**: Contains dependency files for different environments:
  - `base.txt`: Common dependencies shared across all environments.
  - `dev.txt`: Additional dependencies for development (e.g., linters, testing tools).
  - `prod.txt`: Dependencies optimized for production.

## 4. API Example Usage
To retrieve a list of users, send a GET request to:
```
http://localhost:8000/api/users/
```
To create a new user, send a POST request with JSON payload to:
```
http://localhost:8000/api/users/
```
Example payload:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30
}
```

## 5. Testing
Run tests using:
```bash
pytest
```
To check test coverage:
```bash
pytest --cov=.
```

## 6. Deployment

### Production Deployment with Docker Compose
1. Build and start the production containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```
2. Access the application at `http://<your-server-ip>:8000`.

### Manual Production Deployment
1. Set up environment variables in `.env`.
2. Use the production settings:
   ```bash
   python manage.py runserver --settings=core.settings.prod
   ```

## 7. Commands

### Run the Development Server
```bash
python manage.py runserver
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create Migrations
```bash
python manage.py makemigrations
```

### Update Version

#### Set a Specific Version
```bash
python manage.py update_version --set 1.2.3
```

#### Increment Version
- Increment the major version:
```bash
python manage.py update_version --increment major
```
- Increment the minor version:
```bash
python manage.py update_version --increment minor
```
- Increment the patch version:
```bash
python manage.py update_version --increment patch
```

### Get Current Version

Retrieve the current version from the latest Git tag:
```bash
python manage.py get_version
```