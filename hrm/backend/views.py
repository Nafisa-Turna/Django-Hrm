from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
# Create your views here.
# start coustom login  logout method
# def backendLogin(request):
#         if request.method == 'POST':
#                 username=request.POST.get('username')
#                 password=request.POST.get('pwd')
#                 user=authenticate(username=username, password=password)
              
#                 if user is not None:
#                         login(request, user)
#                         messages.success(request,'Welcome')
#                         return HttpResponseRedirect(reverse('dashboard'))
#                 else:
#                         messages.error(request,'Sorry Invalid User')
#                         return HttpResponseRedirect(reverse('login'))
#         else:
#                 if request.user.is_authenticated:
#                         messages.warning(request,'Welcome Back')
#                         return HttpResponseRedirect(reverse('backend'))

#                 return render(request,'backend/login.html') 
# def backendLoginout(request):
#         logout(request)  
#         return HttpResponseRedirect(reverse('login'))    
#  end login logout method   

# start home view method           
# @login_required  
def HomeView(request):
        if request.method =='GET':
                return render(request,'backend/index.html')
# end home view method
def branch(request):
        return render(request,'backend/branch.html')
def department(request):
        return render(request,'backend/department.html')

def designation(request):
        return render(request,'backend/designation.html')

def employee(request):
        return render(request,'backend/employee.html')
def addemployee(request):
        return render(request,'backend/createemployee.html')