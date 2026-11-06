# Fahari Digital Solutions (Nairobi, Kenya)

A full-stack Django web application built for **Fahari Digital Solutions**, a software development agency in Nairobi, Kenya.

---

## Business Information

- **Company Name:** Fahari Digital Solutions
- **Meaning:** "Fahari" is Swahili for Pride and Excellence
- **Location:** Westlands Business Park, Waiyaki Way, Nairobi, Kenya
- **Phone:** +254 700 123 456
- **Email:** hello@faharidigital.co.ke

---

## Executive Leadership

| Name | Role | Responsibilities |
|---|---|---|
| **Asman Makero Musa** | **Founder & Chief Executive Officer (CEO)** | Project Architecture and Technical Direction |
| **Marylyne Mwazighe** | **Chief Operations Officer (COO)** | Client Operations and Project Schedules |
| **Caldrin Daisy Omondi** | **Lead UI/UX Designer** | Mobile and Web Interface Design |
| **Cynthia Mukami Murithi** | **Head of Digital Marketing** | Search Rankings and Online Advertising |
| **Druzler Chepngeno** | **Senior Backend Engineer** | APIs, Database Design, and M-Pesa Gateways |

---

## Project Structure

Templates are organized inside the application directory (`website/templates/`):

```
STATIC/
├── FahariDigital/           # Django Project Configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── website/                 # Django Application
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/           # App Templates (Flat layout)
│   │   ├── 404.html
│   │   ├── base.html
│   │   ├── blog-details.html
│   │   ├── blog.html
│   │   ├── index.html
│   │   ├── portfolio-details.html
│   │   ├── service-details.html
│   │   └── starter-page.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   ├── img/
│   ├── js/
│   └── vendor/
├── Fahari_Template_Source/  # Original HTML Template Assets
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/makeromusa/arsha-django-template.git
cd arsha-django-template
```

### 2. Activate Virtual Environment
```powershell
# Windows
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

---

## Features
- Clean Python and Django 6 architecture with template inheritance
- Modular navbar and footer components
- Contact message and newsletter subscription models with Django Admin support
- M-Pesa Daraja payment integration structure and practical documentation
- Fully responsive across mobile, tablet, and desktop viewports
