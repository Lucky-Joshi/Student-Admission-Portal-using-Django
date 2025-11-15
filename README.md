# Modern Full-Stack Web Application

A beautiful, modern full-stack website built with Django backend and aesthetic frontend using Tailwind CSS, custom animations, and modern UI components.

## 🎨 Features

### Frontend

- **Modern UI/UX**: Clean, minimal design with glassmorphism effects
- **Smooth Animations**: Framer Motion-inspired animations and transitions
- **Fully Responsive**: Perfect on mobile, tablet, and desktop
- **Dark Mode**: Toggle between light and dark themes
- **Interactive Components**:
  - Animated navbar with hover effects
  - Hero section with floating elements
  - Feature cards with hover animations
  - Forms with floating labels
  - Toast notifications
  - Smooth scroll effects

### Backend (Django)

- **URL Routing**: Clean URL structure
- **Class-based & Function-based Views**
- **Django Templates**: Server-side rendering
- **Models**: Contact and Registration models with SQLite
- **Form Processing**: Server-side validation
- **Admin Panel**: Full CRUD operations
- **REST API**: Optional API endpoints with Django REST Framework

## 📁 Project Structure

```
project/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── app/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── urls.py
│       ├── serializers.py
│       ├── static/
│       │   ├── css/
│       │   │   └── style.css
│       │   └── js/
│       │       └── main.js
│       └── templates/
│           └── app/
│               ├── base.html
│               ├── index.html
│               ├── about.html
│               ├── contact.html
│               ├── form.html
│               ├── success.html
│               └── dashboard.html
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- uv (Python package manager)

### Step 1: Create Virtual Environment with uv

```bash
# Install uv if you haven't already
# Visit: https://github.com/astral-sh/uv

# Create virtual environment
cd backend
uv venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Step 2: Install Dependencies

```bash
uv pip install -r requirements.txt
```

### Step 3: Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 5: Run Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## 📱 Available Pages

- **Home** (`/`) - Landing page with hero section and features
- **About** (`/about/`) - About us page
- **Contact** (`/contact/`) - Contact form
- **Registration** (`/form/`) - Course registration form
- **Success** (`/success/`) - Success page after form submission
- **Dashboard** (`/dashboard/`) - Admin dashboard with stats
- **Admin Panel** (`/admin/`) - Django admin interface

## 🎨 Design Features

### Color Palette

- Primary: Purple (#7c3aed)
- Secondary: Blue (#2563eb)
- Accent: Pink (#ec4899)
- Background: Soft gradients (purple, blue, pink)

### Typography

- Font Family: Poppins (Google Fonts)
- Weights: 300, 400, 500, 600, 700

### UI Components

- **Glassmorphism Cards**: Frosted glass effect with backdrop blur
- **Floating Labels**: Modern form inputs with animated labels
- **Hover Effects**: Smooth transitions on all interactive elements
- **Toast Notifications**: Auto-dismissing success/error messages
- **Animated Bubbles**: Background animation on hero section
- **Responsive Navigation**: Mobile-friendly menu

## 🔧 Technologies Used

### Backend

- Django 5.0.1
- Django REST Framework 3.14.0
- SQLite Database

### Frontend

- HTML5
- CSS3 (Custom + Tailwind CSS CDN)
- JavaScript (ES6+)
- FontAwesome Icons
- Google Fonts (Poppins)

## 📝 Models

### Contact Model

- name (CharField)
- email (EmailField)
- subject (CharField)
- message (TextField)
- created_at (DateTimeField)

### Registration Model

- full_name (CharField)
- email (EmailField)
- phone (CharField)
- course (CharField with choices)
- experience (TextField)
- created_at (DateTimeField)

## 🎯 Key Features Explained

### Dark Mode

Toggle between light and dark themes. Preference is saved in localStorage.

### Form Validation

- Client-side validation with JavaScript
- Server-side validation with Django forms
- Real-time error feedback
- Floating label animations

### Animations

- Fade-in on scroll (Intersection Observer)
- Floating elements with CSS keyframes
- Smooth page transitions
- Counter animations on stats
- Parallax effects

### Responsive Design

- Mobile-first approach
- Breakpoints for tablet and desktop
- Collapsible mobile menu
- Touch-friendly interactions

## 🔐 Admin Access

Access the Django admin panel at `/admin/` to:

- View all contacts and registrations
- Manage database entries
- Export data
- User management

## 🌟 Best Practices Implemented

1. **Separation of Concerns**: Backend and frontend clearly separated
2. **DRY Principle**: Reusable components and base templates
3. **Security**: CSRF protection, form validation
4. **Performance**: Optimized animations, lazy loading
5. **Accessibility**: Semantic HTML, ARIA labels
6. **Code Quality**: Clean, commented code
7. **Responsive**: Mobile-first design approach

## 📦 Optional: REST API

The project includes Django REST Framework setup. To use the API:

1. Add API views in `app/views.py`
2. Create serializers in `app/serializers.py`
3. Configure API URLs in `app/urls.py`

Example API endpoint structure:

- `/api/contacts/` - List/Create contacts
- `/api/registrations/` - List/Create registrations

## 🐛 Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic
```

### Database Issues

```bash
python manage.py flush
python manage.py migrate
```

### Port Already in Use

```bash
python manage.py runserver 8080
```

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for your own purposes!

## 📧 Support

For issues or questions, please open an issue on the repository.

---

**Built with ❤️ using Django and Modern Web Technologies**
