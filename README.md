# Arsha - Django Corporate Web Application

A full-stack Django application converted from the modern **Arsha** Bootstrap template by [BootstrapMade](https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/).

This project demonstrates clean Django / Jinja templating practices, modular component organization, static files configuration, and backend models for inquiry and newsletter handling.

---

## 🌟 Recommended BootstrapMade Template

**Template Name:** [Arsha - Free Corporate Bootstrap HTML Template](https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/)

### Why Arsha is the Best Template to Work With:
1. **Modern Stack:** Built on Bootstrap 5.3 with clean vanilla JavaScript (no jQuery dependency), AOS animations, GLightbox, and Swiper.
2. **Complete Page Suite:** Includes not only the one-page corporate landing page, but also multi-page templates:
   - Homepage (`index.html`)
   - Starter Template (`starter-page.html`)
   - Service Details (`service-details.html`)
   - Portfolio Details (`portfolio-details.html`)
   - Blog Listing (`blog.html`)
   - Blog Article Detail (`blog-details.html`)
   - Custom 404 Error Page (`404.html`)
3. **Clean Architecture:** Well-organized CSS, modern typography (Jost, Open Sans, Poppins), and responsive layouts that convert cleanly into Django's template inheritance system.

---

## 📁 Project Architecture

```
STATIC/
├── arsha_project/           # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Static files & template settings configured
│   ├── urls.py              # Root URL routing + custom 404 handler
│   └── wsgi.py
├── website/                 # Dedicated Django app
│   ├── migrations/
│   ├── admin.py             # Admin models for Contact and Newsletter
│   ├── apps.py
│   ├── models.py            # ContactMessage & NewsletterSubscriber models
│   ├── urls.py              # App routing
│   └── views.py             # View controllers (Home, Blog, Services, etc.)
├── static/                  # Static assets (CSS, JS, Images, Vendors)
│   ├── css/
│   ├── img/
│   ├── js/
│   ├── scss/
│   └── vendor/
├── templates/               # Django / Jinja templates
│   ├── base.html            # Master base template with blocks
│   ├── index.html           # Extends base.html
│   ├── starter-page.html    # Extends base.html
│   ├── service-details.html # Extends base.html
│   ├── portfolio-details.html
│   ├── blog.html
│   ├── blog-details.html
│   ├── 404.html
│   └── includes/
│       ├── navbar.html      # Modular navigation component
│       └── footer.html      # Modular footer component with newsletter
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/makeromusa/arsha-django-template.git
cd arsha-django-template
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Panel)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🧩 Template Inheritance & Jinja/Django Features

All views extend `templates/base.html`:
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Arsha - Modern Corporate Bootstrap Template{% endblock %}
{% block body_class %}index-page{% endblock %}

{% block content %}
<!-- Page-specific sections -->
{% endblock %}
```

### Modular Components
- **Navbar:** Extracted into `templates/includes/navbar.html` and included with `{% include 'includes/navbar.html' %}`. Supports dynamic active states based on current route.
- **Footer:** Extracted into `templates/includes/footer.html` with working newsletter subscription form protected by `{% csrf_token %}`.

---

## 📄 Available Routes

| Route | Description |
|---|---|
| `/` | Landing page (Hero, About, Services, Portfolio, Pricing, Contact) |
| `/starter/` | Clean boilerplate starter page |
| `/services/details/` | Service details page |
| `/portfolio/details/` | Portfolio project showcase details |
| `/blog/` | Blog article archive |
| `/blog/details/` | Blog single post view |
| `/contact/` | Contact message submission endpoint (AJAX-ready) |
| `/newsletter/` | Newsletter subscription endpoint (AJAX-ready) |
| `/404/` | Custom styled 404 page |
| `/admin/` | Django Administration panel |

---

## ⚖️ Credits & License

- Original HTML Template: [Arsha by BootstrapMade](https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/)
- License: BootstrapMade Free License (attribution required)
- Django Conversion: Built for seamless deployment and extensibility.
