#!/bin/bash

echo "========================================"
echo "Modern Full-Stack Web App Setup"
echo "========================================"
echo ""

cd backend

echo "Creating virtual environment with uv..."
uv venv
echo ""

echo "Activating virtual environment..."
source .venv/bin/activate
echo ""

echo "Installing dependencies..."
uv pip install -r requirements.txt
echo ""

echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate
echo ""

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To create a superuser, run:"
echo "  python manage.py createsuperuser"
echo ""
echo "To start the development server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/"
echo "========================================"
