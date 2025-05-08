# Django Application

## Commands

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

### Version Management
- The version is dynamically read from the latest Git tag.
- Updating the version creates or updates a Git tag locally.

### Run Tests
```bash
python manage.py test
```