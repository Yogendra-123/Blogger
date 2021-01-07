from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import customUser,Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

def index(request):
    return render (request,'home.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fullname = fname + ' ' + lname
        user = customUser(name = fullname,email=email,password=password)
        user.save()
        messages.success(request,"Your Account Created Successfully")
        return redirect('login')
    return  render(request,"register.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = customUser.objects.get(email=email)
            if user.password == password:
                request.session['email']=user.email
                request.session['name']=user.name
                print(user.email)
                return redirect('profile')
            else:
                messages.error(request,"Incorrect Password!")
                return redirect('login')
        except customUser.DoesNotExist:
            message = messages.error(request, "Email Does Not Exist!")
            return redirect('login')
    return render(request,'login.html')


def profile(request):
    email = request.session.get('email')
    user = customUser.objects.get(email=email)
    blogPosts = user.blog_set.all()
    if request.session.get('email'):
        time = datetime.now() - timedelta(days=15)
        blogs = Blog.objects.all()
        name = request.session.get('name')
        recent_blogs = Blog.objects.filter(created_at__gt=time)
        return render(request,'profile.html',{'blogPosts':blogPosts,'blogs':blogs,'recent_blogs':recent_blogs,'name':name})
    return redirect('login')
def logout(request):
    request.session.flush()
    messages.success(request,"You are Logged Out!")
    return redirect('login')

def post_create(request):
    email = request.session.get('email')
    user = customUser.objects.get(email=email)
    name = user.name
    if request.method == 'POST':
        title = request.POST.get('title')
        short_desc = request.POST.get('short_desc')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Blog(title=title,short_desc=short_desc,desc=description,image=image,author=user).save()
        messages.success(request,"Post Created Successfully.")
        return redirect('post_create')

    return render(request,'create_post.html',{'name':name})