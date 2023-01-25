from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import user_data,imgdata
from django.contrib import messages,auth
from django.db.models import Q

# Create your views here.

    
def admin_panel(request):
    if request.user.is_authenticated:
        context = {
            'users': user_data.objects.all(),
            'nums': user_data.objects.all().count()
        }
        return render(request, 'admin_panel.html',context)
    else:
        return render(request,'login.html')
    
def home(request):
    if 'username' in request.session:
        context = {
            'datas': imgdata.objects.all(),
            'showbtn': request.user.is_superuser
        }
        return render(request,'home.html', context)
    return render(request,'login.html')
    

def login_p(request):
    if 'username' in request.session:
        if request.user.is_authenticated:
            context = {
                'users': user_data.objects.all(),
                'nums': user_data.objects.all().count()
            }
            return render(request, 'admin_panel.html',context)
        else:
            context = {
                'datas': imgdata.objects.all()
            }
            return render(request, 'home.html',context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            request.session['username'] = username
            context = {
                'users': user_data.objects.all(),
                'nums': user_data.objects.all().count()
            }
            return render(request,'admin_panel.html',context)
        else:
            if user_data.objects.filter(
                username = request.POST['username'], password = request.POST['password']
            ).exists():
                request.session['username'] = request.POST['username']
                context = {
                    'datas': imgdata.objects.all()
                }
                return render(request, 'home.html',context)
            
            else:
                messages.info(request, "Invalid Credentials...!")
                return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def signup(request):
    if 'username' in request.session:
        if request.user.is_authenticated:
            context = {
                'users': user_data.objects.all(),
                'nums': user_data.objects.all().count()
            }
            return render(request, 'admin_panel.html',context)
        else:
            context = {
                'datas': imgdata.objects.all()
            }
            return render(request, 'home.html',context)
    elif request.method == 'POST':
        if user_data.objects.filter(
            email = request.POST['email'], username = request.POST['username']
        ).exists():
            messages.error(request, "email or username already exist...!")
            return render(request, 'signup.html')
        
        elif request.POST['password'] != request.POST['pass1']:
            messages.error(request, "2 Passwords Must be Match...!")
            return render(request, 'signup.html')        
        
        else:
            values = user_data(
                firstname = request.POST['firstname'], 
                lastname = request.POST['lastname'], 
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['password']
            )
            values.save()
            return redirect('login_p')
    return render(request,'signup.html')

def add_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if user_data.objects.filter(
                email = request.POST['email']
            ).exists():
                messages.error(request, "This Email already exist...!")
                return render(request, 'add_user.html')
        
            elif request.POST['password'] != request.POST['pass1']:
                messages.error(request, "2 Passwords Must be Match...!")
                return render(request, 'add_user.html')        
        
            else:
                values = user_data(
                    firstname = request.POST['firstname'], 
                    lastname = request.POST['lastname'], 
                    username = request.POST['username'],
                    email = request.POST['email'],
                    password = request.POST['password']
                )
                values.save()
                context = {
                    'users':user_data.objects.all(),
                    'nums': user_data.objects.all().count()
                }
                return render(request, 'admin_panel.html',context)
        else:
            return render(request,'add_user.html')
    else:
        return render(request,'login.html')

    
def delete_user(request,id):
    if request.user.is_authenticated:
        view_data = user_data.objects.get(id=id)
        view_data.delete()
        return redirect('admin_panel')
    else:
        return render(request,'login.html')

# def update_user_form(request,id):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             ex1 = user_data.objects.filter(id=id).update(
#                 firstname = request.POST['firstname'],
#                 lastname = request.POST['lastname'],
#                 username = request.POST['username'],
#                 email = request.POST['email'],
#                 password = request.POST['password']
#             )
#             context = {
#                 'users' : user_data.objects.all(),
#                 'nums': user_data.objects.all().count()
#             }
#             return render(request, 'admin_panel.html', context)
#         else:
#             return render(request,'edit_user.html')
#     return render(request,'login.html')
    
def update_user(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ex1 = user_data.objects.filter(id=id).update(
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['password']
            )
            return redirect('admin_panel')
        else:
            context = {
            'users': user_data.objects.get(id=id)
            }
            return render(request,'edit_user.html',context)
    return render(request,'login.html')
    

def search_data(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST['searched']

            multiple_query = Q(Q(username__icontains=searched) | Q(email__icontains=searched))
            users = user_data.objects.filter(multiple_query)
        
            context = {
                'users': users,
                'nums': users.count()
            }

        return render(request, 'admin_panel.html', context)
    else:
        return render(request,'login.html')

def upload(request):
    if request.method == 'POST':
        img_data = request.FILES['img_data']
        desc = request.POST['desc']
        new_user = imgdata(img_data=img_data, desc=desc)
        new_user.save()
        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html')


def logout_p(request):
    if 'username' in request.session:
        request.session.flush()
        logout(request)
        return redirect('login_p')
