from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .helpers import send_forgot_password_mail
import uuid
from django.contrib import messages
# Create your views here.
def IndexPage(request):
    return render(request,'index.html')
@login_required(login_url='login')
def HomePage(request):
    # username=request.user
    laundry=Laundry.objects.all()
    lp=Price.objects.all()
    # pending=Laundry.objects.filter(status='PENDING').count()
    # accepted=Laundry.objects.filter(status='ACCEPTED').count()
    # rejected=Laundry.objects.filter(status='REJECTED').count()
    # completed=Laundry.objects.filter(status='COMPLETED').count()
    context={
        'laundry':laundry,
        'lp':lp,
    }
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        pick_date=request.POST.get('date')
        pick_time=request.POST.get('time')
        quantity=request.POST.get('quantity')
        wear_type=request.POST.get('wear_type')
        loundery_type=request.POST.get('loundry_type')
        data=Laundry(name=name,email=email,phone=phone,address=address,pick_date=pick_date,pick_time=pick_time,quantity=quantity,wear_type=wear_type,loundery_type=loundery_type)
        data.save()
        send_mail(
                    'Laundry Service Request🙂',
                    f'NAME :- {name}\n, Your laundry service order for wear type-{wear_type} and laundrytype-{loundery_type} has been placed successfully.Thank you. 🙂🙂',
                    'avksmlavk@gmail.com',
                    [email],
                    fail_silently=False,
                )
        return render(request,'home.html',{"nam":name,"wear":wear_type,"laundry":loundery_type})
    return render (request,'home.html',context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

def StatusPage(request,id):
    track=Status.objects.filter(id=id)
    print(track)
    context={
        'track':track,
    }
    return render (request,'status.html',context)

def ChangePassword(request):
    if request.method=='POST':
        old_pass=request.POST.get('old_pass')
        new_pass=request.POST.get('new_pass')
        confirm_pass=request.POST.get('confirm_pass')
        if new_pass!=confirm_pass:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            user=request.user
            user.set_password(new_pass)
            user.save()
            return redirect('login')
    return render (request,'changepass.html')


def ResetPassword(request,token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forgot_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/reset_password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/reset_password/{token}/')            
            user_obj = User.objects.get(id = user_id)
            # user_obj = request.user
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
        return render(request , 'reset-password.html' , context)
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)

def ForgotPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('forgot_password')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            # profile_obj= Profile.objects.get(user = user_obj)
            # profile_obj.forgot_password_token = token
            # profile_obj.save()
            send_forgot_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('forgot_password')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')

def Contact(request):
    return render(request, 'contact.html')
def About(request):
    return render(request, 'about.html')