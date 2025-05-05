FROM python:3.10-slim

WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copying and installing Python dependencies
COPY requirements/base.txt requirements/base.txt
COPY requirements/dev.txt requirements/dev.txt
COPY requirements/prod.txt requirements/prod.txt

# Installing dependencies from dev.txt by default,
# can be overridden in production via REQUIREMENTS_FILE
ARG REQUIREMENTS_FILE=requirements/dev.txt
RUN pip install --no-cache-dir -r ${REQUIREMENTS_FILE}

# Copying project files
COPY . .

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]