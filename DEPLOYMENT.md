# 🚀 Deployment Guide

## Production Checklist

### 1. Security Settings

Update `backend/project/settings.py`:

```python
# Change DEBUG to False
DEBUG = False

# Set allowed hosts
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Generate new SECRET_KEY
# Use: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = 'your-new-secret-key-here'

# HTTPS settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

### 2. Database Configuration

For PostgreSQL (recommended for production):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Install PostgreSQL adapter:

```bash
uv pip install psycopg2-binary
```

### 3. Static Files

```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Collect static files
python manage.py collectstatic
```

### 4. Environment Variables

Create `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

Install python-decouple:

```bash
uv pip install python-decouple
```

Update settings.py:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
```

## Deployment Options

### Option 1: Traditional VPS (DigitalOcean, Linode, AWS EC2)

#### Step 1: Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx postgresql -y

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Step 2: Clone Project

```bash
git clone your-repo-url
cd your-project
```

#### Step 3: Setup Virtual Environment

```bash
cd backend
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv pip install gunicorn psycopg2-binary
```

#### Step 4: Configure PostgreSQL

```bash
sudo -u postgres psql
CREATE DATABASE yourdb;
CREATE USER youruser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE yourdb TO youruser;
\q
```

#### Step 5: Run Migrations

```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

#### Step 6: Configure Gunicorn

Create `gunicorn_config.py`:

```python
bind = "127.0.0.1:8000"
workers = 3
```

Create systemd service `/etc/systemd/system/django.service`:

```ini
[Unit]
Description=Django Application
After=network.target

[Service]
User=your-user
Group=www-data
WorkingDirectory=/path/to/backend
Environment="PATH=/path/to/backend/.venv/bin"
ExecStart=/path/to/backend/.venv/bin/gunicorn --config gunicorn_config.py project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:

```bash
sudo systemctl start django
sudo systemctl enable django
```

#### Step 7: Configure Nginx

Create `/etc/nginx/sites-available/django`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /path/to/backend;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 8: SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Option 2: Heroku

#### Step 1: Install Heroku CLI

```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 2: Create Heroku App

```bash
heroku login
heroku create your-app-name
```

#### Step 3: Add Files

Create `Procfile`:

```
web: gunicorn project.wsgi --chdir backend
```

Create `runtime.txt`:

```
python-3.13.7
```

Update `requirements.txt`:

```bash
cd backend
uv pip freeze > requirements.txt
```

Add to requirements.txt:

```
gunicorn
dj-database-url
whitenoise
```

#### Step 4: Update Settings

```python
# settings.py
import dj_database_url

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Step 5: Deploy

```bash
git init
git add .
git commit -m "Initial commit"
heroku git:remote -a your-app-name
git push heroku main
heroku run python backend/manage.py migrate
heroku run python backend/manage.py createsuperuser
```

### Option 3: PythonAnywhere

#### Step 1: Create Account

Visit: https://www.pythonanywhere.com

#### Step 2: Upload Code

Use Git or upload files via dashboard

#### Step 3: Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
cd backend
pip install -r requirements.txt
```

#### Step 4: Configure Web App

- Go to Web tab
- Add new web app
- Choose Manual configuration
- Set Python version
- Set source code directory
- Set working directory

#### Step 5: Configure WSGI

Edit WSGI configuration file:

```python
import os
import sys

path = '/home/yourusername/your-project/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Step 6: Static Files

```bash
python manage.py collectstatic
```

Configure static files in web app settings:

- URL: /static/
- Directory: /home/yourusername/your-project/backend/staticfiles

### Option 4: Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Create `docker-compose.yml`:

```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: djangodb
      POSTGRES_USER: djangouser
      POSTGRES_PASSWORD: djangopass
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: gunicorn project.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://djangouser:djangopass@db:5432/djangodb

volumes:
  postgres_data:
```

Deploy:

```bash
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## Post-Deployment

### 1. Test Everything

- [ ] Homepage loads
- [ ] All pages accessible
- [ ] Forms submit correctly
- [ ] Admin panel works
- [ ] Static files load
- [ ] HTTPS works
- [ ] Mobile responsive

### 2. Setup Monitoring

- [ ] Error tracking (Sentry)
- [ ] Uptime monitoring
- [ ] Performance monitoring
- [ ] Log aggregation

### 3. Backup Strategy

- [ ] Database backups
- [ ] Media files backup
- [ ] Code repository backup
- [ ] Automated backup schedule

### 4. Email Configuration

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### 5. Performance Optimization

- [ ] Enable caching
- [ ] Optimize database queries
- [ ] Compress static files
- [ ] Use CDN for static files
- [ ] Enable gzip compression

## Maintenance

### Regular Tasks

```bash
# Update dependencies
uv pip install --upgrade -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Clear cache
python manage.py clear_cache

# Backup database
python manage.py dumpdata > backup.json
```

### Monitoring Commands

```bash
# Check logs
sudo journalctl -u django -f

# Check Nginx logs
sudo tail -f /var/log/nginx/error.log

# Check disk space
df -h

# Check memory
free -m
```

## Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic --clear
sudo systemctl restart nginx
```

### Database Connection Error

```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Check connection
psql -U youruser -d yourdb -h localhost
```

### 502 Bad Gateway

```bash
# Check Gunicorn
sudo systemctl status django
sudo systemctl restart django
```

### Permission Errors

```bash
sudo chown -R www-data:www-data /path/to/project
sudo chmod -R 755 /path/to/project
```

## Security Best Practices

1. **Never commit secrets** - Use environment variables
2. **Keep dependencies updated** - Regular security patches
3. **Use HTTPS** - Always encrypt traffic
4. **Regular backups** - Automated and tested
5. **Monitor logs** - Watch for suspicious activity
6. **Rate limiting** - Prevent abuse
7. **Strong passwords** - Enforce password policies
8. **Two-factor auth** - For admin accounts

## Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Let's Encrypt](https://letsencrypt.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

**Your app is now ready for production! 🚀**
