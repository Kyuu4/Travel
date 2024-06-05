from django.shortcuts import render
from django.template.loader import get_template
from .models import Customer, Course
from django.http import HttpResponseRedirect
from .forms import ContactForm, UserRegistrationForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    #відображення курсів на головній сторінці
    return render(request, 'index.html', {'courses': Course.objects.all()[:3]})

def courses(request):
    return render(request, 'courses.html', {'courses': Course.objects.all()})

def course(request, id):
    return render(request, 'course.html', {'course': Course.objects.get(id=id)})

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    customer = Customer()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'],form.cleaned_data['email'], form.cleaned_data['text'], form.cleaned_data['phone'])
            customer.name = request.POST.get('name')
            customer.email = request.POST.get('email')
            customer.phone = request.POST.get('phone')
            customer.message = request.POST.get('text')
            customer.save()
            return HttpResponseRedirect("/contact-us/")
    return render(request, 'contact-us.html', {"form": ContactForm()})

def send_message(name, email, message, phone):
    text_send = get_template('message.html')
    html = get_template('message.html')
    context = {'name' : name, 'email' : email, 'message' : message, 'phone' : phone}
    subject = 'Повідомлення із сайту'
    from_email = 'support@kodim.ua'
    text_content = text_send.render(context)
    html_context = text_send.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['kodim.pervomaisk@gmail.com'])
    msg.attach_alternative(html_context, 'text/html')
    msg.send()

#class LoginUser(DataMixin, LoginView):
class LoginUser(LoginView):
    from_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return context
        
def profile(request):
    return render(request, 'registration/profile.html')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': UserRegistrationForm})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form':form})