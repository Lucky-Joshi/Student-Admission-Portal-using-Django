from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Contact, Registration
from .forms import ContactForm, RegistrationForm

def index(request):
    """Homepage view"""
    return render(request, 'app/index.html')

def about(request):
    """About page view"""
    return render(request, 'app/about.html')

def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})

def registration_form(request):
    """Registration form page"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'app/form.html', {'form': form})

def success(request):
    """Success page after form submission"""
    return render(request, 'app/success.html')

class DashboardView(ListView):
    """Dashboard view showing all registrations"""
    model = Registration
    template_name = 'app/dashboard.html'
    context_object_name = 'registrations'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()[:5]
        context['total_registrations'] = Registration.objects.count()
        context['total_contacts'] = Contact.objects.count()
        return context
