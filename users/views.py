from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from .forms import LoginForm
from .models import Student,Subject,Mark
from django.db.models import Count,Sum,Avg,Max


def home(request):
    
    return render(request,'home.html')


def login_view(request):

    if request.method == 'POST':
        print(request)
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            
            return redirect('/home/')
        else: 
            messages.info(request,'invalid credentials')
            
            return redirect('login')
        
    else:
        form = LoginForm()
        return render(request,'login.html',{"form":form})


def logout_view(request):
    auth.logout(request)
    return render(request,'logout.html')


def result_view(request):
   
    user = request.user.is_authenticated
    
    if user :
        a = str(request.user)
        student = Student.objects.get(student_id=a)
        mark = Mark.objects.filter(student_id=student)        
        total = Mark.objects.filter(student_id=student).aggregate(Avg('marks'))
        
        context ={
                "student":student,
                "mark":mark,
                "total": total, 
                }         
        return render(request,'result.html',context)
    
    
    form = LoginForm()    
    return render(request,'login.html',{"form":form})

def topper_view(request):
    
    user = request.user.is_authenticated
        
    if user:
       student = Student.objects.all()
       lis=[]
       for stu in student:
           mark = Mark.objects.filter(student_id=stu).aggregate(Avg('marks'))
           a = (mark['marks__avg'],stu)
           lis.append(a)
       lis.sort(reverse=True)
       topper = lis[0][1]
       aggregate = lis[0][0]
       topper_mark = Mark.objects.filter(student_id=topper)
       
          
       context ={
                    "student":topper,
                    "topper" : topper_mark,
                    "aggregate" : aggregate                                             
                    }
             
       return render(request,'topper_page.html',context)
    
    
    form = LoginForm()    
    return render(request,'login.html',{"form":form})    
                




    