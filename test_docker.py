import os
from decouple import config

# Read environment variable using python-decouple
test_var = config('TEST_VAR', default='Not Set')
db_name = config('DB_NAME', default='DB Not Set')

print(f"Hello from Docker! The value of TEST_VAR is: {test_var}")
print(f"Database name from env is: {db_name}")

# Check if psycopg2 is installed and can be imported
try:
    import psycopg2
    print("psycopg2 library imported successfully.")
except ImportError as e:
    print(f"Failed to import psycopg2: {e}")

print("Docker setup test completed.")
