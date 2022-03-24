from django.shortcuts import render,redirect
from .models import signup

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        address = request.POST['address']
        username = request.POST['username']
        pwd = request.POST['pwd']
        obj = signup(name=name, place=place, email=email, address=address, username=username, password=pwd)
        obj.save()
    return render(request,'register.html')

def login(request):
    msg=""
    if request.method=='POST':
        uname=request.POST['username']
        psw=request.POST['password']
        
        try:
            if uname=='alan':
                obj_exist=signup.objects.get(username=uname, password=psw)
                request.session['user']=obj_exist.signid
                return redirect("admin_home")
            else:
                obj_exist=signup.objects.get(username=uname, password=psw)
                request.session['user']=obj_exist.signid
                return redirect("employee_home")

        except signup.DoesNotExist:
            msg="Username or password incorrect"
    return render(request,'login.html',{'msg':msg,})

def admin(request):
    data=signup.objects.all()
    if request.method=='POST':
        id=request.POST['id']
        obj=signup.objects.filter(signid=id)
        obj.delete()
    return render(request,'admin.html',{'user':data})

def employee(request):
    obj=signup.objects.get(signid=request.session['user'])
    return render(request,"employee.html",{'user':obj,})

def update(request, id):
    obj = signup.objects.get(signid=id)
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        obj.name = name
        obj.email = email
        obj.password = pwd
        obj.save()
    return render(request,'update.html',{'user':obj})


def logout(request):
    return render(request,'index.html')