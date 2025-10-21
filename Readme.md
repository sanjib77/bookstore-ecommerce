# 📚 Online Bookstore — E-commerce Platform

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![License: SANJIB](https://img.shields.io/badge/License-SANJIB-yellow.svg)](./LICENSE)

A full-featured online bookstore built with Django and PostgreSQL, prepared for AWS deployment. This repo contains a learning-focused, production-capable example with user and admin features.

Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [Database Setup](#database-setup)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features
Customer
- Browse, search, and filter books (title, author, ISBN, category)
- Book detail pages, cover images, reviews and ratings
- Persistent shopping cart, checkout, order history
- Authentication, user profiles, saved addresses

Admin
- Django admin dashboard
- Inventory and category management
- Order processing and status updates
- Sales tracking and bulk operations

## Tech Stack
Backend: Django 4.2, Python 3.11+  
Database: PostgreSQL 15  
Frontend: Django templates, Bootstrap 5.3, Vanilla JS  
Deployment: Gunicorn, Nginx, WhiteNoise  
Cloud: AWS (EC2, VPC, Security Groups, Route53 optional)

## Prerequisites
Install:
- Python 3.11+
- PostgreSQL 15+
- pip
- Git

Verify:
```bash
python --version
pip --version
psql --version
git --version
```

## Quickstart (development)
Clone and set up a virtual environment:

```bash
git clone https://github.com/yourusername/bookstore.git
cd bookstore
python -m venv .venv
# Activate virtualenv:
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # or: copy .env.example .env (Windows)
# Edit .env with your config (see Environment Variables below)
```

Apply migrations, create a superuser, and run the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Database Setup (PostgreSQL)
Run these SQL commands in psql or a DB client (replace password and names as needed):

```sql
CREATE DATABASE bookstore_db;
CREATE USER bookstore_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE bookstore_db TO bookstore_user;
```

In production, configure appropriate roles, network access, and backups.

## Environment Variables
See .env.example. Typical variables:
- SECRET_KEY
- DEBUG (True/False)
- DATABASE_URL or DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
- ALLOWED_HOSTS
- AWS / S3 credentials (if using cloud storage)

Generate a SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Project Structure
```
bookstore_project/
├── bookstore_config/    # Project settings
├── books/               # Book catalog app
├── accounts/            # User management
├── cart/                # Shopping cart
├── orders/              # Order processing
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS)
└── media/               # User uploads
```

## Deployment
Production stack suggestions:
- Gunicorn as WSGI server
- Nginx as reverse proxy and static file handler
- WhiteNoise for simple static file serving
- PostgreSQL managed DB (RDS) or separate EC2 instance
- Use environment variables and secrets manager for credentials

See DEPLOYMENT.md for detailed AWS deployment steps (VPC, EC2, Elastic IP, NAT Gateway, Route53).

## Contributing
Contributions welcome. Please:
- Fork the repo
- Create a feature branch
- Submit PRs with descriptive titles and tests where applicable

Add issues and link to relevant discussions. See CONTRIBUTING.md (if present) for full guidelines.

## Tests
If tests are included, run:
```bash
python manage.py test
```

## License
This project is open source project made for personal practice! 

## Author
Sanjib Chakraborty — Initial work

## Acknowledgments
Django documentation, Bootstrap, and AWS resources.

(Replace placeholders such as repository URL, DB credentials, and author details before publishing.)
