# Fahari Digital Solutions — Nairobi, Kenya

A full-stack, production-grade Django web application crafted for **Fahari Digital Solutions**, Nairobi's premier digital engineering and software agency. 

Converted and heavily customized from BootstrapMade to feature 100% authentic Kenyan content, team leadership, localized pricing (KSh), M-Pesa integration architecture, and modern Jinja/Django template inheritance.

---

## 🇰🇪 Business Identity & Creative Kenyan Brand

- **Name:** **Fahari Digital Solutions** (*"Fahari"* — Swahili for Pride, Prestige, and Excellence)
- **Tagline:** Digital Solutions Built for Africa's Future
- **Headquarters:** Westlands Business Park, Waiyaki Way, Nairobi, Kenya
- **Contact:** `+254 700 123 456` | `hello@faharidigital.co.ke`

---

## 👥 Executive Leadership & Team

| Name | Role | Focus Area |
|---|---|---|
| **Asman Makero Musa** | **Founder & Chief Executive Officer (CEO)** | Vision, Strategy, and Technical Architecture |
| **Marylyne Mwazighe** | **Chief Operations Officer (COO)** | Client Operations, Delivery, and Agile Project Management |
| **Caldrin Daisy Omondi** | **Lead UI/UX & Product Designer** | User Experience, Design Systems, and Mobile-First Prototyping |
| **Cynthia Mukami Murithi** | **Head of Digital Marketing** | Growth Marketing, SEO, Social Strategy, and Brand Visibility |
| **Druzler Chepngeno** | **Senior Backend Engineer** | APIs, Cloud Infrastructure, Database Design, and M-Pesa Gateways |

---

## 📁 Project Structure (App-Centric Templates)

Organized following standard Django best practices (templates inside the application directory, identical to VS Code project layout):

```
STATIC/
├── arsha_project/           # Django Project Config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Static files & template settings
│   ├── urls.py              # Root URL routing + 404 handler
│   └── wsgi.py
├── website/                 # Core Django App
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/           # App Templates Folder
│   │   ├── includes/
│   │   │   ├── navbar.html  # Modular navigation with active link logic
│   │   │   └── footer.html  # Clean footer (no third-party branding)
│   │   ├── 404.html         # Custom styled 404 error page
│   │   ├── base.html        # Master Jinja/Django base template
│   │   ├── blog-details.html# M-Pesa Daraja guide by Asman Makero Musa
│   │   ├── blog.html        # Tech articles & insights
│   │   ├── index.html       # Fahari Digital landing page
│   │   ├── portfolio-details.html # PesaSmart case study
│   │   ├── service-details.html   # Web & mobile dev services
│   │   └── starter-page.html      # Boilerplate for new pages
│   ├── admin.py             # Admin panel for inquiries & subscribers
│   ├── apps.py
│   ├── models.py            # ContactMessage & NewsletterSubscriber
│   ├── urls.py              # App URLs namespace
│   └── views.py             # View controllers
├── static/                  # Static assets (CSS, JS, Images, Vendors)
│   ├── css/
│   │   └── main.css
│   ├── img/                 # Images & icons
│   ├── js/
│   │   └── main.js
│   └── vendor/              # Bootstrap, Swiper, GLightbox, AOS
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Quickstart Guide

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

Visit **http://127.0.0.1:8000/** in your browser.

---

## 🛠️ Customizations Done
- **Zero Placeholder / Latin Text:** Every single instance of *Lorem Ipsum* replaced with realistic Kenyan tech agency copy.
- **Removed Third-Party Branding:** All *“Designed by BootstrapMade”* and third-party markers removed.
- **Localized Content:** Pricing in Kenya Shillings (KSh), addresses in Westlands, Nairobi, Kenyan phone format (`+254`), and Daraja M-Pesa case studies.
- **Jinja / Django Templating:** Master `base.html` inheritance, modular `includes/navbar.html` and `includes/footer.html`, CSRF tokens, and dynamic routing.
- **Database Models:** Fully functional models for `ContactMessage` and `NewsletterSubscriber` with Django Admin integration.
