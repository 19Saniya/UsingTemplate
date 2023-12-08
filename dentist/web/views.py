from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView
from .models import Topbar, NavbarHeading, BannerText, AboutText, AboutFeature, ServiceHeading, Service

# from .forms import SignUpForm, LoginForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from django.urls import reverse_lazy

# Create your views here.


def home(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()
    banner = BannerText.objects.all()
    info = AboutText.objects.all()
    feature = AboutFeature.objects.all()
    service_heading = ServiceHeading.objects.all()
    service = Service.objects.all()
    # banner_img = HomeImg.objects.all()
    context = {
        'top': top,
        'navbar': navbar,
        'banner': banner,
        'info': info,
        'feature': feature,
        'service_heading': service_heading,
        'service': service,
        # 'banner_img': banner_img,
    }
    # if not request.user.is_staff:
    #     return redirect('login_page')

    return render(request, 'home.html', context)


def about(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()
    info = AboutText.objects.all()
    feature = AboutFeature.objects.all()

    return render(request, template_name='about.html',
                  context={'top': top, 'navbar': navbar, 'info': info, 'feature': feature})


def appointment(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    if request.method == "POST":
        appoint_name = request.POST['appoint_name']
        appoint_email = request.POST['appoint_email']
        appoint_date = request.POST['appoint_date']
        appoint_time = request.POST['appoint_time']
        appoint_department = request.POST['appoint_department']
        appoint_doctor = request.POST['appoint_doctor']

        return render(request, template_name='appointment.html', context={
            'appoint_name': appoint_name,
            'appoint_email': appoint_email,
            'appoint_date': appoint_date,
            'appoint_time': appoint_time,
            'appoint_department': appoint_department,
            'appoint_doctor': appoint_doctor,
            'top': top,
            'navbar': navbar,
        })

    else:

        return render(request, template_name='appointment.html', context={'top': top, 'navbar': navbar, })


def blog(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    return render(request, template_name='blog.html', context={'top': top, 'navbar': navbar, })


def contact(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']

        # send_mail(
        #     message_name, # subject
        #     message, # message
        #     [message_email],
        #     ['john2codemy.com', ],
        # )

        return render(request, template_name='contact.html',
                      context={'message_name': message_name, 'message_email': message_email,
                               'message_subject': message_subject, 'message': message, })

    else:
        return render(request, template_name='contact.html', context={'top': top, 'navbar': navbar, })


def detail(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    return render(request, template_name='detail.html', context={'top': top, 'navbar': navbar, })


def price(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    return render(request, template_name='price.html', context={'top': top, 'navbar': navbar, })


def search(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    return render(request, template_name='search.html', context={'top': top, 'navbar': navbar, })


def service(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()
    service_heading = ServiceHeading.objects.all()
    service = Service.objects.all()

    return render(request, template_name='service.html',
                  context={'top': top, 'navbar': navbar, 'service': service, 'service_heading': service_heading})


def team(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    return render(request, template_name='team.html', context={'top': top, 'navbar': navbar, })


def testimonial(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()

    return render(request, template_name='testimonial.html', context={'top': top, 'navbar': navbar, })


def register(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email exists! Try logging in')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login_page')
    else:
        pass
    return render(request, template_name='accounts/register.html', context={'top': top, 'navbar': navbar})

def login_page(request):
    top = Topbar.objects.all()
    navbar = NavbarHeading.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('appointment')
        else:
            messages.info(request, 'Invalid Credentials, try again!')
            return redirect('login_page')
    else:
        return render(request, template_name='accounts/login.html', context={'top': top, 'navbar': navbar})

def logout_user(request):
    auth.logout(request)
    return redirect('home')


# def login_page(request):
#     top = Topbar.objects.all()
#     navbar = NavbarHeading.objects.all()
#     # form = LoginForm
#     error = ""
#     usereml = request.POST.get('user_email')
#     pwd1 = request.POST.get('pwd1')
#
#     user = User.objects.create(
#         username=usereml,
#         password=pwd1,
#     )
#     try:
#         if user.is_staff:
#             login(request, user)
#             error = "no"
#         else:
#             error = "yes"
#     except:
#         error = "yes"
#     data = {'error': error}
#
#     return render(request, template_name='accounts/login.html', context={'top': top, 'navbar': navbar, 'data': data})



# def register
    # form = SignUpForm

    # if request.method == 'POST':
    #     # form = SignUpForm(request.POST)
    #     email = request.POST.get('email')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     u = request.POST.get('u')
    #     password1 = request.POST.get('password1')
    #
    #     user = User.objects.filter(username=u, first_name=first_name, last_name=last_name, email=email)
    #
    #     if user.exists():
    #         messages.info = (request, 'User Name already taken')
    #         return redirect('/register/')
    #
    #     user = User.objects.create()
    #
    #     user.set_password(password1)
    #     user.save()
    #
    #     messages.info =(request, 'Account created successfully!')
    #     return redirect('/register/')

    # Using Django Forms
    # if form.is_valid():
    #     form.save()
    #     # return redirect('login')
    # else:
    #     form = SignUpForm

    # context = {'form': form}
    # return render(request, template_name='accounts/register.html', context={'top': top, 'navbar': navbar})