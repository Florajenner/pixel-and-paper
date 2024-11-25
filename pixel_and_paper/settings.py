import os
if os.path.exists("env.py"):
    import env
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

CSRF_TRUSTED_ORIGINS = [
    'https://*.codeinstitute-ide.net',
    'https://*.herokuapp.com',
    'https://pixel-and-paper.herokuapp.com',
    'https://*.gitpod.io',
]

ALLOWED_HOSTS = [
    'pixel-and-paper.herokuapp.com',
    '.herokuapp.com',
    'localhost',
    '127.0.0.1',
    '8000-florajenner-pixelandpap-xrmzfff1cqb.ws.codeinstitute-ide.net',
    '*'
]

# Rest of your settings remain the same...
[Your existing INSTALLED_APPS, MIDDLEWARE, etc.]

# Update the DEBUG setting to properly handle production
DEBUG = False if os.environ.get("DEVELOPMENT") != "True" else True

# For better security, remove the wildcard (*) from ALLOWED_HOSTS in production
if not DEBUG:
    ALLOWED_HOSTS = [
        'pixel-and-paper.herokuapp.com',
        '.herokuapp.com',
    ]