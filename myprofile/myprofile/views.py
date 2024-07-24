from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
import json



from django.contrib.auth import authenticate

def index(request):

    return render(request, 'profile/index.html')

def home(request):
    
    persons = Person.objects.filter(customer=request.user)
    educations = Education.objects.filter(customer=request.user)
    languages = Language.objects.filter(customer=request.user)
    profiles = Profile.objects.filter(customer=request.user)
    experiences = Experience.objects.filter(customer=request.user)
    skills = Skills.objects.filter(customer=request.user)
    interests = Interest.objects.filter(customer=request.user)

        
    context = {
        'persons':persons,
        'educations':educations,
        'languages':languages, 
        'profiles':profiles,
        'experiences':experiences,
        'skills':skills,
        'interests':interests,
        }
    return render(request, 'profile/home.html', context)


def login_user(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'profile/login.html', {})
    

def logout_user(request):
    logout(request)
    return redirect('index')

def signup_user(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
 
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        print(uname,email,pass1,pass2)
        return redirect('login')

    return render(request, 'profile/signup.html', {} )


def save_personal(request):
    customer = request.user
   
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        image_path = None
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            image_path = default_storage.save(f'media/{image.name}', ContentFile(image.read()))
        person = Person.objects.create(
            customer=customer,
            name=request.POST.get('name'),
            level=request.POST.get('level'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            website=request.POST.get('website'),
            location=request.POST.get('location'),
            image=image_path
        )

  
    return JsonResponse(data={'msg':'OK'}, status=200)

    
      
def save_skill_box(request):
    customer = request.user
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])

        for item in data:
            skills = Skills.objects.create(
                customer=customer,
                skill=item.get('skill'),
                value=item.get('skill_level'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_education_box(request):
    customer = request.user

    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])
        
        for item in data:
            education = Education.objects.create(
                customer=customer,
                year=item.get('year'),
                qualification=item.get('qualification'),
                universityname=item.get('universityname')
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_language_box(request):
    customer = request.user
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])
        
        for item in data:
            language = Language.objects.create(
                customer=customer,
                language=item.get('language'),
                value=item.get('level'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_profile_box(request):
    customer = request.user
    if request.method == 'POST':
        print(request.POST)
        
        profile = Profile.objects.create(
            customer=customer,
            about=request.POST.get('about'),
        )

    return JsonResponse(data={'msg':'OK'}, status=200)



def save_experience_box(request):
    customer = request.user
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])

        for item in data:
            experience = Experience.objects.create(
                customer=customer,
                year_company=item.get('year_company'),
                company_name=item.get('company_name'),
                job=item.get('job'),
                about_job=item.get('about_job'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)


def save_interest_box(request):
    customer = request.user
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('data')
        data = json.loads(data)
        print(data[0])
         
        for item in data:
            interest = Interest.objects.create(
                customer=customer,
                interests=item.get('interests'),
            )

    return JsonResponse(data={'msg':'OK'}, status=200)



def add(request):

    if request.method == "POST":
        personform = PersonForm(request.POST, request.FILES)
        print(' --- ', request.FILES)
        educateform = EducationForm(request.POST)
        languageform = LanguageForm(request.POST)
        profileform = ProfileForm(request.POST)
        experienceform = ExperienceForm(request.POST)
        skillform = SkillsForm(request.POST)
        interestform = InterestForm(request.POST)
        
        if personform.is_valid() and educateform.is_valid() and languageform.is_valid() and profileform.is_valid() and experienceform.is_valid() and skillform.is_valid() and interestform.is_valid():
            personform.save()
            print(' -- ',personform.files)
            educateform.save()
            languageform.save()
            profileform.save()
            experienceform.save()
            skillform.save()
            interestform.save()

            return redirect('home')
    else:
        personform = PersonForm()
        educateform = EducationForm()
        languageform = LanguageForm()
        profileform = ProfileForm()
        experienceform = ExperienceForm()
        skillform = SkillsForm()
        interestform = InterestForm()

    
    personform = PersonForm
    educateform = EducationForm
    languageform = LanguageForm
    profileform = ProfileForm
    experienceform = ExperienceForm
    skillform = SkillsForm
    interestform = InterestForm
        
    return render(request, 'profile/add1.html', {
                                        'personform':personform, 
                                        'educateform':educateform,
                                        'languageform':languageform, 
                                        'profileform':profileform, 
                                        'experienceform':experienceform, 
                                        'skillform':skillform, 
                                        'interestform':interestform
                                        })

