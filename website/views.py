from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage, NewsletterSubscriber


def home(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def service_details(request):
    return render(request, 'service-details.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            return HttpResponse("OK")
        return HttpResponse("Please fill in all required fields.", status=400)
    return HttpResponse("Invalid request method.", status=405)


def newsletter_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            return HttpResponse("OK")
        return HttpResponse("Please provide a valid email.", status=400)
    return HttpResponse("Invalid request method.", status=405)


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
