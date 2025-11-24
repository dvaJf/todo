from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm,UserCreationForm1
from django.shortcuts import redirect
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout
from django.views import View

def index(request):

    tasks = Task.objects.all()
    return render(request,'main/main.html', {'title':'главная','task':tasks,'now':now() + timedelta(days=1)})
def reg(request):
    return render(request,'main/reg.html')
def sigin(request):
    return render(request,'main/sigin.html')

def task(request):
    error=""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/main')
        else:
            print(form.errors)
            error = "форма не верная"
    form = TaskForm()
    
    context={
        'form':form,
        'error':error
    }
    return render(request,'main/task.html',context)

def profile(request):
    return render(request,'main/profile.html')

def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user=user)
            return redirect('/main')
        return redirect('/sigin')

def user_logout(request):
    logout(request)
    return redirect('/sigin')

class Register(View):
    template_name = 'reg.html'
    def get(self,request):
        context = {
            'form': UserCreationForm1()
        }
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = UserCreationForm1(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user=user)
            return redirect('/main')
        return redirect('/reg')