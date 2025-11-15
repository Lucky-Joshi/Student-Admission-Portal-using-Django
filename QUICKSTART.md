# 🚀 Quick Start Guide

## Automated Setup (Recommended)

### Windows

```bash
setup.bat
```

### macOS/Linux

```bash
chmod +x setup.sh
./setup.sh
```

## Manual Setup

### 1. Navigate to backend folder

```bash
cd backend
```

### 2. Create virtual environment

```bash
uv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Start development server

```bash
python manage.py runserver
```

### 8. Open browser

Visit: `http://127.0.0.1:8000/`

## 📱 Available URLs

- Home: `http://127.0.0.1:8000/`
- About: `http://127.0.0.1:8000/about/`
- Contact: `http://127.0.0.1:8000/contact/`
- Registration: `http://127.0.0.1:8000/form/`
- Dashboard: `http://127.0.0.1:8000/dashboard/`
- Admin: `http://127.0.0.1:8000/admin/`

## 🎨 Features to Try

1. **Dark Mode**: Click the moon/sun icon in the navbar
2. **Contact Form**: Fill out and submit the contact form
3. **Registration**: Register for a course
4. **Dashboard**: View all submissions
5. **Responsive**: Resize your browser or use mobile view
6. **Animations**: Scroll through pages to see smooth animations

## 🔧 Troubleshooting

### uv not found

Install uv first:

```bash
pip install uv
```

### Port already in use

Use a different port:

```bash
python manage.py runserver 8080
```

### Static files not loading

Collect static files:

```bash
python manage.py collectstatic
```

## 📝 Next Steps

1. Customize colors in `static/css/style.css`
2. Add your own content in templates
3. Modify models in `app/models.py`
4. Add more views in `app/views.py`
5. Create custom forms in `app/forms.py`

Enjoy building! 🎉
